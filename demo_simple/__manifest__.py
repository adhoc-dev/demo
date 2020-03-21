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
    'name': 'Demo Simple',
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
        'l10n_ar_demo',
        # 'l10n_ar_stock',
        # 'l10n_ar_account_tax_settlement',
        # 'l10n_ar_account_reports',
        'account_accountant',
        # 'account_multic_fix',
        # 'account_debt_management',
        'base_currency_inverse_rate',
        # 'l10n_ar_aeroo_purchase',
        # 'l10n_ar_aeroo_sale',
        # 'l10n_ar_aeroo_stock',
        # 'l10n_ar_aeroo_payment_group',
        'l10n_ar_bank',
        # 'product_catalog_aeroo_report_public_categ',
        # 'product_price_taxes_included',
        'purchase_quotation_products',
        'sale_quotation_products',
        # 'project_description',
        # 'l10n_ar_website_sale',
        'account_transfer_unreconcile',
        'purchase_subscription',
        # 'payment_todopago',
        'account_accountant_ux',
        'account_ux',
        'base_ux',
        'helpdesk_timesheet_ux',
        'hr_timesheet_ux',
        'helpdesk_ux',
        # 'hr_timesheet_attendance_ux',
        # 'stock_ux',
        'purchase_ux',
        'project_ux',
        # 'sale_stock_ux',
        'sale_ux',
        'product_ux',
        'sale_subscription_ux',
        # 'account_multicompany_ux',
        'sale_timesheet_ux',
        # 'purchase_multic_fix',
        # 'sale_stock_multic_fix',
        'web_decimal_numpad_dot',
        # 'mail_internal',

        # oca
        # 'stock_picking_invoice_link',
        'mail_tracking',
        'mass_editing',
        # 'web_advanced_search',
        # 'web_search_with_and',
        # 'stock_no_negative',

        # odoo modules
        'stock',
        'hr_attendance',
        'purchase',
        'project',
    ],
    'data': [
    ],
    'demo': [
        'users_data.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
