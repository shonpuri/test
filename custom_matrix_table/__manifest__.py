# ?? 2025-2026 Momentum91 (https://www.momentum91.com)
# @@Momentum91
{
    'name': 'Matrix Management & Viewer',
    'version': '1.0',
    'summary': 'Visualize SPH-CYL matrix data and management',
    'category': 'Tools',
    'author': 'Momentum91',
    'website': 'https://www.momentum91.com/',
    'depends': ['web', 'base', 'stock', 'sale', 'product_extended'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_menu.xml',
        'views/matrix_views.xml',
        'views/main_view_model.xml',
        'wizard/view_upload_excel.xml',

    ],
    'images': ['sph_cyl_matrix/static/icon.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'custom_matrix_table/static/src/components/**/*.xml',
            'custom_matrix_table/static/src/components/**/*.js',
        ],
    },

}
