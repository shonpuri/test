from odoo import models, fields, api


class SPHCYLMatrix(models.Model):
    _name = "sph.cyl.matrix"
    _description = "SPH CYL Matrix"
    _order = "sph asc"

    product_id = fields.Many2one("product.template", string="Product")
    sph = fields.Float(string="SPH", required=True)
    cyl = fields.Float(string="CYL", required=True)
    value = fields.Integer(string="Quantity")

    def import_sph_cyl_matrix(self):
        pass




