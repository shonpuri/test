from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    spherical_value = fields.Float(string="Spherical Value", store=True)
    cylindrical_value = fields.Float(string="Cylindrical Value", store=True)
    manufacturing_ok = fields.Boolean(string="Manufacturing")


class ProductProduct(models.Model):
    _inherit = 'product.product'

    spherical_value = fields.Float(string="Spherical Value", store=True)
    cylindrical_value = fields.Float(string="Cylindrical Value", store=True)
    manufacturing_ok = fields.Boolean(string="Manufacturing")

    # @api.depends('product_tmpl_id.spherical_value')
    # def _compute_spherical_value(self):
    #     for record in self:
    #         if record.product_tmpl_id:
    #             record.spherical_value = record.product_tmpl_id.spherical_value
    #
    # @api.depends('product_tmpl_id.cylindrical_value')
    # def _compute_cylindrical_value(self):
    #     for record in self:
    #         if record.product_tmpl_id:
    #             record.cylindrical_value = record.product_tmpl_id.cylindrical_value

