from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    upload_batch = fields.Char('Upload Batch No :', readonly=True, copy=False, )
