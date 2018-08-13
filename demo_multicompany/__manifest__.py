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
    'name': 'Demo of Multicompany Environment',
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'board',
        'l10n_ar_demo',
        # 'l10n_ar_account_tax_settlement',
        # 'l10n_ar_account_reports',
        'account_reports_followup',
        'account_accountant',
        'l10n_ar_afipws_fe',
        # 'account_multicompany_usability',
        # 'account_multic_fix',
        'account_debt_management',
        'account_move_helper',
        # todavía no definimos usarlo y de hecho no está disponible
        # 'currency_rate_inverted',
        'account_clean_cancelled_invoice_number',
        'account_ux',
        'portal_ux',
        # 'account_statement_move_import',
        'l10n_ar_aeroo_einvoice',
        'l10n_ar_aeroo_purchase',
        'l10n_ar_aeroo_sale',
        # 'l10n_ar_aeroo_stock',
        'l10n_ar_aeroo_payment_group',
        # 'l10n_ar_currency_update',
        'l10n_ar_bank',
        # 'product_catalog_aeroo_report_public_categ',
        # 'product_price_currency',
        'product_pricelist',
        # 'product_price_taxes_included',
        'product_replenishment_cost',
        'purchase_quotation_products',
        # 'sale_quotation_products',
        'purchase_discount',
        'project_description',
        # 'sale_procurement_date_confirm',
        'helpdesk_solutions',
        # 'stock_picking_labels',
        # 'stock_picking_list',
        # 'l10n_ar_account_vat_ledger',
        'account_transfer_unreconcile',
        'purchase_subscription',
        # 'payment_todopago',
        # 'stock_ux',
        # 'purchase_ux',
        'sale_ux',
        'product_ux',
        'sale_subscription_ux',
        'sale_timesheet_ux',
        # 'sale_prices_update',
        # 'sale_contract_restrict_domain',
        # 'product_supplier_search',
        # 'purchase_multic_fix',

        # oca
        'mail_tracking',
        'auth_signup_verify_email',
        'mass_editing',
        # 'web_export_view',
        'web_widget_many2many_tags_multi_selection',

        # odoo modules
        'hr_attendance',
        'purchase',
        'survey',

        # odoo enterprise modules
        'website_quote_subscription',
        'sale_subscription_dashboard',
        'website_helpdesk_form',
        'website_sale_coupon',
        'hr_holidays_gantt',
        'mass_mailing_themes',
        'website_form_editor',
        'hr_recruitment',
        'hr_expense',
        'hr_contract',
        'website_partner',
        'website_blog',
        'website_crm',
        'website_twitter',
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
