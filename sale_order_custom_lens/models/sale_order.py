from odoo import models, fields, api

class SaleOrderLineExtension(models.Model):
    _name = 'sale.order.lens.line'
    _description = 'Sale Order Lens Line'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    sph_value = fields.Many2one('lens.sph.value', string='SPH Value')
    cyl_value = fields.Many2one('lens.cyl.value', string='CYL Value')
    quantity = fields.Integer(string='Quantity', default=0)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    lens_line_ids = fields.One2many('sale.order.lens.line', 'sale_order_id', string='Lens Lines')

    def action_open_lens_combinations(self):
        sph_values = self.env['lens.sph.value'].search([])
        cyl_values = self.env['lens.cyl.value'].search([])

        lens_lines = []
        for sph in sph_values:
            for cyl in cyl_values:
                lens_lines.append({
                    'sale_order_id': self.id,
                    'sph_value': sph.id,
                    'cyl_value': cyl.id,
                    'quantity': 0,
                })

        self.write({'lens_line_ids': [(0, 0, line) for line in lens_lines]})

        return {
            'type': 'ir.actions.act_window',
            'name': 'Lens Combinations',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'res_id': self.id,
            'target': 'new'
        }
