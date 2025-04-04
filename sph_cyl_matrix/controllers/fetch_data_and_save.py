from odoo import http
from odoo.http import request


class SPHCYLMatrixController(http.Controller):



    @staticmethod
    def sort_with_zero_first(values):
        values = sorted(set(values))
        if 0.0 in values:
            values.remove(0.0)
            return [0.0] + values
        return values

    @http.route('/sph_cyl_matrix', type='http', auth='user', website=True)
    def sph_cyl_matrix_view(self, **kwargs):
        records = request.env['sph.cyl.matrix'].sudo().search([])

        sph_values = self.sort_with_zero_first(records.mapped('sph') + [0.0])
        cyl_values = self.sort_with_zero_first(records.mapped('cyl') + [0.0])

        values_dict = {
            (rec.sph, rec.cyl): rec.value for rec in records
        }

        return request.render('sph_cyl_matrix.sph_cyl_matrix_table', {
            'sph_values': sph_values,
            'cyl_values': cyl_values,
            'values_dict': values_dict
        })

    @http.route('/update_sph_cyl_matrix', type='json', auth='user')
    def update_sph_cyl_matrix(self, sph, cyl, value):
        record = request.env['sph.cyl.matrix'].sudo().search([
            ('sph', '=', sph),
            ('cyl', '=', cyl)
        ], limit=1)

        if record:
            record.sudo().write({'value': int(value)})
        else:
            request.env['sph.cyl.matrix'].sudo().create({
                'sph': sph,
                'cyl': cyl,
                'value': int(value)
            })

        return {'success': True}
