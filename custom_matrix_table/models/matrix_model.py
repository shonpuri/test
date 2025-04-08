from odoo import models, fields, api
import uuid

from odoo.exceptions import UserError


class SPHCYLMatrix(models.Model):
    _name = "sph.cyl.matrix"
    _description = "SPH CYL Matrix"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "sph asc"

    # main fields
    upload_batch = fields.Char('Batch Code', readonly=True, copy=False, )
    product_id = fields.Many2one("product.template", string="Product", tracking=True)
    sph = fields.Float(string="SPH", required=True,tracking=True)
    cyl = fields.Float(string="CYL", required=True, tracking=True)
    value = fields.Integer(string="Quantity", tracking=True)
    partner_id = fields.Many2one("res.partner", string="Customer", tracking=True)
    date = fields.Date(string="Date", tracking=True)
    customer_ref = fields.Char(string="Customer PO/Ref", tracking=True)

    # Extra fields
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', tracking=True)
    is_approved = fields.Boolean(string="Approved" ,tracking=True)
    approved_by = fields.Many2one('res.users', string='Approved By',tracking=True)
    approved_date = fields.Date(string="Approved Date",tracking=True)

    def import_sph_cyl_matrix(self):
        pass

    @staticmethod
    def sort_with_zero_first(values):
        """Sort with 0.0 first, then descending negatives"""
        values = list(set(values))
        values.sort(key=lambda x: (x != 0, x))  # sort numerically
        return values

    @api.model
    def get_matrix_data(self):
        records = self.sudo().search([
            # ('upload_batch', '=', upload_batch_no),
            ('is_approved', '=', False),
            ('sale_order_id', '=', False)
        ])
        if not records:
            return {
                'partner_id': False,
                'partner_name': '',
                'date': False,
                'customer_ref': '',
                'upload_batch': '',
                'sph_values': [],
                'cyl_values': [],
                'values_dict': {},
            }

        partner_id = records[0].partner_id.id
        upload_batch = records[0].upload_batch
        partner_name = records[0].partner_id.name
        date = records[0].date.strftime('%d/%m/%Y') if records[0].date else ''
        customer_ref = records[0].customer_ref
        sph_values = self.sort_with_zero_first(records.mapped('sph') + [0])
        cyl_values = self.sort_with_zero_first(records.mapped('cyl') + [0])

        values_dict = {
            f"{rec.sph},{rec.cyl}": rec.value for rec in records
        }
        return {
            'partner_id': partner_id,
            'partner_name': partner_name,
            'date': date,
            'upload_batch': upload_batch,
            'customer_ref': customer_ref,
            'sph_values': sph_values,
            'cyl_values': cyl_values,
            'values_dict': values_dict,
        }
    @api.model
    def update_matrix_cell(self, sph, cyl, value):
        # Update the corresponding record
        record = self.search([('sph', '=', sph), ('cyl', '=', cyl)], limit=1)
        if record:
            record.value = value
        else:
            self.create({'sph': sph, 'cyl': cyl, 'value': value})

    @api.model
    def mark_approved(self, upload_batch):
        records = self.search([('upload_batch', '=', upload_batch)])
        if not records:
            raise UserError("No records found for the provided upload batch.")

        records.write({
            'is_approved': True,
            'approved_by': self.env.user.id,
            'approved_date': fields.Date.today()
        })

        records_with_value = records.filtered(lambda r: r.value > 0)

        if not records_with_value:
            return True

        first = records_with_value[0]
        sale_order = self.env['sale.order'].create({
            'partner_id': first.partner_id.id,
            'date_order': first.date,
            'origin': "Excel Import" + ' - ' + first.upload_batch ,
            'client_order_ref': first.customer_ref,
            'upload_batch': first.upload_batch,
            'company_id': first.company_id.id,
            'user_id': self.env.user.id,  # Directly assign during create
        })

        for record in records_with_value:
            self.env['sale.order.line'].create({
                'product_id': record.product_id.id,
                'product_uom_qty': record.value,
                'product_uom': record.product_id.uom_id.id,
                'order_id': sale_order.id,
            })

        # Optional: link the SO back to each record
        records.write({'sale_order_id': sale_order.id})

        return sale_order.id  # Optional for debugging/traceability




