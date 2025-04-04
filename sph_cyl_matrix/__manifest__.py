# ?? 2025-2026 Momentum91 (https://www.momentum91.com)
# @@Momentum91
{
    'name': 'Lens Matrix Management & Viewer',
    'version': '1.0',
    'summary': 'Visualize SPH-CYL matrix data and management',
    'category': 'Tools',
    'author': 'Momentum91',
    'website': 'https://www.momentum91.com/',
    'depends': ['web', 'base', 'stock', 'sale', 'product_extended'],
    'data': [
        'security/ir.model.access.csv',
        'views/matrix_views.xml',
        'views/matrix_view_template.xml',
        'wizard/view_upload_excel.xml',
    ],
    'images': ['static/icon.jpg'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            # 'sph_cyl_matrix/static/src/js/open_import_wizard.js',
            # 'sph_cyl_matrix/static/src/js/dashboard.xml',
            # 'sph_cyl_matrix/static/src/js/matrix_table_cell.js',
        ],
    },
}
