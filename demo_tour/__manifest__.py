{
    'name': 'Demo Tour',
    "version": "16.0.1.0.0",
    'category': 'Sales/Sales',
    'description': 'Integration Tests using Odoo Tours',
    'depends': [
        'sale_management',
    ],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'demo_tour/static/src/js/tours/sale.js',
            'demo_tour/static/src/js/tours/multicompany.js',
        ],
    },
    'license': 'LGPL-3',
}
