##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Demo Full',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'demo_simple',

        # adhoc modules
        'ks_dashboard_ninja',
        # 'sale_order_type_ux',
        'sale_delivery_ux',
        'product_replenishment_cost',
        'product_currency',
        'l10n_ar_currency_update',
        'account_statement_move_import',
        'website_sale_ux',
        'purchase_discount',
        'helpdesk_solutions',
        'stock_picking_labels',
        'project_forecast_ux',
        # 'product_pricelist',

        # odoo modules
        'survey',
        'board',

        # odoo enterprise modules
        'sale_subscription_dashboard',
        'website_helpdesk_form',
        'website_sale_coupon',
        'hr_holidays_gantt',
        'mass_mailing_themes',
        'hr_recruitment',
        'hr_expense',
        'hr_contract',
        'website_partner',
        'website_blog',
        'website_crm',
        'website_twitter',
        'website_sale',
    ],
    'data': [
    ],
    'demo': [
        'config_data.xml',
        'users_data.xml',
        # last load lang (so user is already created) (we disable it to make it
        # faster and also because on rancher, already on es ar)
        # 'load_es_lang.yml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
