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

    # @api.model
    # def create(self, vals_list):
    #     records = super(SPHCYLMatrix, self).create(vals_list)
    #
    #     # Fetch all unique SPH and CYL values from imported records
    #     sph_values = list(set(r.sph for r in records))
    #     cyl_values = list(set(r.cyl for r in records))
    #
    #     # Find matching products in one query
    #     products = self.env["product.product"].search([
    #         ("spherical_value", "in", sph_values),
    #         ("cylindrical_value", "in", cyl_values),
    #     ])
    #
    #     product_map = {(p.spherical_value, p.cylindrical_value): p.id for p in products}
    #
    #     for record in records:
    #         product_id = product_map.get((record.sph, record.cyl))
    #         if product_id:
    #             record.product_id = product_id
    #
    #     return records



