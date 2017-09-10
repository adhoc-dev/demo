# -*- coding: utf-8 -*-
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
    'version': '10.0.1.0.0',
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
        'purchase',
        'account_check',
        'account_payment_group',
        'marketing_campaign',
        # 'l10n_ar_account_reports',
        # 'l10n_ar_afipws_fe',
        # 'account_multic_fix',
        # 'account_multicompany_usability',
        # 'account_move_helper',
        # 'account_debt_management',
        # 'account_clean_cancelled_invoice_number',
        # 'base_currency_inverse_rate',
        # 'account_invoice_change_currency',
        # 'account_invoice_commercial',
        # 'account_invoice_company_search',
        # 'account_invoice_journal_group',
        # 'adhoc_account_planner',
        # 'account_usability',
        # 'account_statement_move_import',
        # 'account_invoice_prices_update',
        # 'account_invoice_tax_wizard',
        # 'l10n_ar_aeroo_einvoice',
        # 'l10n_ar_aeroo_purchase',
        # 'l10n_ar_aeroo_sale',
        # 'l10n_ar_aeroo_stock',
        # 'l10n_ar_aeroo_payment_group',
        # 'l10n_ar_currency_update',
        # 'product_catalog_aeroo_report_public_categ',
        # 'product_price_currency',
        # 'product_pricelist',
        # 'product_price_taxes_included',
        # 'product_replenishment_cost_rule',
        # 'product_sale_price_by_margin',
        # 'product_template_search_by_barcode',
        # 'product_website_categ_search',
        # 'purchase_quotation_products',
        # 'sale_quotation_products',
        # 'purchase_discount',
        # 'stock_inventory_preparation_filter',
        # 'base_state_active',
        # 'project_description',
        # 'project_duplicate_fix',
        # 'project_kanban_open_project',
        # 'sale_procurement_date_confirm',
        # 'account_transfer_unreconcile',
        # 'l10n_ar_account_vat_ledger',
        # 'purchase_contract',
        # 'project_issue_solutions',
        # 'stock_picking_labels',
        # 'stock_picking_list',
        # 'payment_todopago',
        # 'stock_usability',
        # 'purchase_usability',
        # 'sale_usability',
        # 'account_reconciliation_menu',
        # 'adhoc_modules',
        # 'project_category',
        # 'sale_prices_update',
        # 'product_search_supplier_code',
        # 'project_closure_restrictions',
        # 'sale_contract_restrict_domain',
        # 'product_supplier_search',
        # 'auth_signup_verify_email',
        # 'purchase_multic_fix',
        # 'web_easy_switch_company',
        # 'project_issue_fix',
        'l10n_ar_bank',
        'website_portal_followup',
        'account_reports_followup',
        'account_accountant',
        'hr_attendance',
        'base_technical_features',
        'hr_appraisal',
        'account_contract_dashboard',
        'hr_holidays_gantt',
        'mass_mailing_themes',
        'website_contract',
        'website_form_editor',
        'hr_recruitment',
        'hr_expense',
        'hr_contract',
        'mail_tracking',
        'mass_editing',
        'web_export_view',
        'web_sheet_full_width',
        'project_issue_sheet',
        'website_partner',
        'web_widget_many2many_tags_multi_selection',
        'hr_holidays',
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
        'account_data.yml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
