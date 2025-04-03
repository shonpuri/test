from odoo import models, fields

class SphValue(models.Model):
    _name = 'lens.sph.value'
    _description = 'SPH Value'

    name = fields.Float(string="SPH Value", required=True)

class CylValue(models.Model):
    _name = 'lens.cyl.value'
    _description = 'CYL Value'

    name = fields.Float(string="CYL Value", required=True)
