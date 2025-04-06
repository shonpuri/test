from odoo import models, fields, api
from odoo.odoo.api import readonly


class SPHCYLMatrix(models.Model):
    _name = "sph.cyl.matrix"
    _description = "SPH CYL Matrix"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "sph asc"

    # main fields
    product_id = fields.Many2one("product.template", string="Product", tracking=True)
    sph = fields.Float(string="SPH", required=True,tracking=True)
    cyl = fields.Float(string="CYL", required=True, tracking=True)
    value = fields.Integer(string="Quantity", tracking=True)

    # Extra fields
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', tracking=True)
    is_approved = fields.Boolean(string="Approved" ,tracking=True)
    approved_by = fields.Many2one('res.users', string='Approved By',tracking=True)
    date = fields.Date(string="Date",tracking=True)

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
        records = self.sudo().search([])

        sph_values = self.sort_with_zero_first(records.mapped('sph') + [0])
        cyl_values = self.sort_with_zero_first(records.mapped('cyl') + [0])

        values_dict = {
            f"{rec.sph},{rec.cyl}": rec.value for rec in records
        }

        return {
            'sph_values': sph_values,
            'cyl_values': cyl_values,
            'values_dict': values_dict,
        }