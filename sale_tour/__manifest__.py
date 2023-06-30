{
    'name': 'Sales',
    "version": "16.0.1.0.0",
    'category': 'Sales/Sales',
    'summary': 'Sales tour',
    'description': 'This module contains sales tour',
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
            'sale_tour/static/src/js/tours/sale.js',
        ],
    },
    'license': 'LGPL-3',
}
