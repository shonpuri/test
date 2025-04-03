# ?? 2025-2026 Momentum91 (https://www.momentum91.com)
# @@Momentum91
{
    'name': 'SPH-CYL Matrix Viewer',
    'version': '1.0',
    'summary': 'Visualize SPH-CYL matrix data',
    'category': 'Tools',
    'author': 'Momentum91',
    'website': 'https://www.momentum91.com/',
    'depends': ['web','base','stock','sale','product_extended'],
    'data': [
        'security/ir.model.access.csv',
        'views/matrix_views.xml',
        'wizard/view_upload_excel.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
