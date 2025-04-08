from odoo import models, fields, api
from odoo.addons.test_import_export.models.models_export_impex import selection_fn


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    spherical_value = fields.Float(string="Spherical Value", store=True)
    cylindrical_value = fields.Float(string="Cylindrical Value", store=True)
    manufacturing_ok = fields.Boolean(string="Manufacturing")
    size = fields.Char(string="Size")
    coating_type = fields.Selection(
        selection='_get_type_selection',
        string='Coating Type',
        tracking=True)

    coating = fields.Selection(
        selection='_get_coating_selection',
        string='Coating',
        tracking=True)

    def _get_type_selection(self):
        return [
            ('hard_coat', 'Hard Coat'),
            ('hard_multi_coat', 'Hard Multi Coat'),
        ]
    def _get_coating_selection(self):
        return [
            ('green', 'Green'),
            ('white', 'White'),
            ('photogrey_green', 'Photogrey Green Block Green'),
            ('photogrey_blue', 'Photogrey Blue Block Blue'),
            ('photogrey', 'Photogrey'),
            ('blue_block_blue', 'Blue Block Blue'),
            ('blue_block_green', 'Blue Block Green'),
        ]


class ProductProduct(models.Model):
    _inherit = 'product.product'

    spherical_value = fields.Float(string="Spherical Value", store=True)
    cylindrical_value = fields.Float(string="Cylindrical Value", store=True)
    manufacturing_ok = fields.Boolean(string="Manufacturing")
    size = fields.Char(string="Size")
    coating_type = fields.Selection(
        selection='_get_type_selection',
        string='Coating Type',
        tracking=True)

    coating = fields.Selection(
        selection='_get_coating_selection',
        string='Coating',
        tracking=True)

    def _get_type_selection(self):
        return [
            ('hard_coat', 'Hard Coat'),
            ('hard_multi_coat', 'Hard Multi Coat'),
        ]
    def _get_coating_selection(self):
        return [
            ('green', 'Green'),
            ('white', 'White'),
            ('photogrey_green', 'Photogrey Green Block Green'),
            ('photogrey_blue', 'Photogrey Blue Block Blue'),
            ('photogrey', 'Photogrey'),
            ('blue_block_blue', 'Blue Block Blue'),
            ('blue_block_green', 'Blue Block Green'),
        ]

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

