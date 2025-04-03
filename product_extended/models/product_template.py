from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    spherical_value = fields.Float(string="Spherical Value")
    cylindrical_value = fields.Float(string="Cylindrical Value")
    manufacturing_ok = fields.Boolean(string="Manufacturing")

    # @api.depends('product_variant_ids.spherical_value')
    # def _compute_spherical_value(self):
    #     for record in self:
    #         if record.product_variant_ids:
    #             record.spherical_value = record.product_variant_ids[0].spherical_value
    #
    # @api.depends('product_variant_ids.cylindrical_value')
    # def _compute_cylindrical_value(self):
    #     for record in self:
    #         if record.product_variant_ids:
    #             record.cylindrical_value = record.product_variant_ids[0].cylindrical_value



class ProductProduct(models.Model):
    _inherit = 'product.product'

    spherical_value = fields.Float(string="Spherical Value")
    cylindrical_value = fields.Float(string="Cylindrical Value")
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

