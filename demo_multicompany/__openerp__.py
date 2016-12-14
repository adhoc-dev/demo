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
    'version': '9.0.1.0.0',
    'category': 'Tools',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        # 'account_accountant',
        # 'l10n_ar_afipws_fe',
        # 'account_multicompany_usability',
        # 'account_multic_fix',
        # 'account_debt_management',
        # 'account_move_helper',
        # 'account_no_translation',
        # 'base_currency_inverse_rate',
        # 'account_clean_cancelled_invoice_number',
        # 'account_invoice_change_currency',
        # 'account_invoice_commercial',
        # 'account_invoice_company_search',
        # 'account_invoice_journal_group',
        # # 'account_invoice_operation',
        # 'account_invoice_prices_update',
        # 'account_invoice_tax_wizard',
        # 'l10n_ar_aeroo_einvoice',
        # 'l10n_ar_aeroo_purchase',
        # 'l10n_ar_aeroo_sale',
        # 'l10n_ar_aeroo_stock',
        # 'l10n_ar_aeroo_payment_group',
        # 'l10n_ar_currency_update',
        # 'l10n_ar_padron_afip',
        # 'l10n_ar_bank',
        # 'product_catalog_aeroo_report_public_categ',
        # 'product_no_translation',
        # 'product_price_currency',
        # 'product_pricelist',
        # 'product_price_taxes_included',
        # 'product_replenishment_cost_rule',
        # 'product_sale_price_by_margin',
        # 'product_template_search_by_barcode',
        # 'product_website_categ_search',
        # 'purchase_quotation_products',
        # 'sale_exception_credit_limit',
        # 'sale_exception_partner_state',
        # 'sale_exception_price_security',
        # 'sale_quotation_products',
        # 'purchase_discount',
        # 'stock_inventory_preparation_filter',
        # 'base_state_active',
        # 'project_description',
        # 'project_duplicate_fix',
        # 'project_kanban_open_project',
        # # 'sale_order_type_user_default',
        # 'sale_procurement_date_confirm',
        # 'hr_attendance',
        'base_technical_features',
        'account_transfer_unreconcile',

        # MODULOS NUEVOS QUE REEMPLAZAN A VIEJOS
        'l10n_ar_bank',
        'l10n_ar_aeroo_payment_group',
        'sale_contract_lines_sequence',
        'sale_contract_prices_update',
        'product_template_search_by_barcode',
        'sale_exception',
        'disable_odoo_online',
        'hr_appraisal',
        'account_financial_report_qweb',
        'account_tax_balance',
        # odoo enterprise modules
        'account_contract_dashboard',
        'hr_holidays_gantt',
        'mass_mailing_themes',
        'website_contract',
        'website_form_editor',
        'account_payment_fix',
        'purchase_contract',

        # MODULOS INSTALADOS EN ADHOC
        'account_accountant',
        # 'support_branding_adhoc', DEPRECIADO PARA ENTEPRISE
        'web_support_client',
        'web_support_client_issue',
        'web_support_server_issue',
        'stock',
        # 'admin_useful_groups', DEPRECIADO
        # 'auth_admin_passkey', NO MIGRADO
        # 'auth_server_admin_passwd_passkey', DEPRECIADO
        'mail',
        # 'account_voucher', DEPRECIADO
        'project',
        'note',
        'survey',
        # 'account_invoice_tax_auto_update', DEPRECIADO
        # 'account_move_line_no_filter', DEPRECIADO
        'account_statement_aeroo_report',
        # 'account_statement_disable_invoice_import', DEPRECIADO
        # 'account_statement_move_import', DEPRECIADO
        # 'hr_sign_in_out_task', DEPRECIADO
        'l10n_ar_aeroo_base',
        'l10n_ar_aeroo_einvoice',
        'l10n_ar_aeroo_invoice',
        'l10n_ar_aeroo_purchase',
        'l10n_ar_aeroo_sale',
        'l10n_ar_aeroo_stock',
        # 'l10n_ar_aeroo_voucher', DEPRECIADO
        'l10n_ar_afipws',
        # 'l10n_ar_bank_cbu', DEPRECIADO
        # 'l10n_ar_hide_receipts', DEPRECIADO
        # 'l10n_ar_invoice', DEPRECIADO
        # 'l10n_ar_invoice_sale', DEPRECIADO
        # 'portal_fix', DEPRECIADO
        # 'portal_partner_fix', DEPRECIADO
        'project_issue_closure_restrictions',
        'project_issue_create_task_defaults',
        'project_issue_order',
        'project_issue_solutions',
        'project_task_issues',
        'project_task_portal_unfollow',
        'report_extended',
        'sale',
        'stock_picking_labels',
        'stock_picking_list',
        'website_talkus',
        'web_support_server',
        'purchase',
        'hr',
        'hr_timesheet',
        # 'hr_timesheet_project', DEPRECIADO
        'hr_recruitment',
        'hr_expense',
        # 'hr_evaluation', RENOMBRADO a hr_appraisal
        'account',
        # 'account_chart', DEPRECIADo
        # 'account_financial_report_webkit', RENOMBRADO a _qweb
        # 'account_financial_report_webkit_xls', DEPRECIADO
        # 'account_general_ledger_fix', DEPRECIADO
        # 'account_journal_book', NO MIGRADo
        # 'account_journal_payment_subtype', DEPRECIADO
        # 'account_move_voucher', NO MIGRADO
        # 'account_onchange_fix', DEPRECIADO
        # 'account_voucher_account_fix', DEPRECIADO
        # 'account_voucher_fix', DEPRECIADO
        # 'account_voucher_payline', DEPRECIADO
        # 'account_voucher_withholding', DEPRECIADO
        'adhoc_modules_server',
        'analytic',
        # 'attachment_edit', NO MIGRADO
        'base_action_rule',
        # 'base_name_search_improved', NO MIGRADO
        'base_setup',
        # 'base_vat', DEPRECIADO
        # 'bi_view_editor', DEPRECIADO
        'board',
        'calendar',
        # 'contract_show_invoice', DEPRECIADO
        # 'cron_run_manually', DEPRECIADO
        'database_cleanup',
        'decimal_precision',
        'delivery',
        # 'disable_openerp_online', RENOMBRADO
        'document',
        # 'document_url',
        # 'edi', DEPRECIADO
        'google_account',
        'google_calendar',
        'google_drive',
        'google_spreadsheet',
        'hr_attendance',
        'hr_contract',
        # 'hr_timesheet_invoice', DEPRECIADO
        # 'knowledge', DEPRECIADO
        # 'l10n_ar_base_vat', DEPRECIADO
        'l10n_ar_padron_afip',
        'mail_tracking',
        'mass_editing',
        'mass_mailing',
        # 'mass_mailing_keep_archives', DEPRECIADO
        # 'partner_search_by_ref', DEPRECIADO
        # 'partner_search_by_vat', DEPRECIADO
        'payment_todopago',
        'procurement_jit',
        'product',
        'project_issue_sheet',
        'purchase_discount',
        # 'purchase_line_defaults', DEPRECIADO
        'report_aeroo',
        'report_webkit',
        # 'report_xls', DEPRECIADO por report_xlsx
        'resource',
        # 'sale_exceptions', RENOMBRADo
        # 'sale_pricelist_discount', DEPRECIADO
        'sale_service',
        # 'sale_usability_extension', DEPRECIADO
        'stock_inventory_preparation_filter',
        'stock_usability',
        # 'support_branding', DEPRECIADO PARA ENTEPRISE
        # 'warning_box', DEPRECIADO
        # 'web_advanced_search_wildcard', NO MIGRADO
        # 'web_advanced_search_x2x', NO MIGRADO
        # 'web_clean_navbar', DEPRECIADO
        'web_export_view',
        # 'web_ir_actions_act_window_message', DEPRECIADO
        # 'web_kanban_sparkline', DEPRECIADO
        # 'web_recipients_uncheck', NO MIGRADO
        # 'web_search_with_and', NO MIGRADO
        'web_sheet_full_width',
        # 'web_shortcuts', DEPRECIADO
        'website',
        # 'website_mail_snippet_table_edit', DEPRECIADO
        'website_partner',
        'web_widget_color',
        'web_widget_many2many_tags_multi_selection',
        # 'web_widget_one2many_tags', NO MIGRADO
        'web_widget_x2many_2d_matrix',
        'infrastructure_contract',
        'infrastructure_issue',
        'infrastructure_mass_mailing',
        # 'infrastructure_product', DEPRECIADO
        # 'ir_export_extended_ept', DEPRECIADO
        # 'adhoc_base_account', DEPRECIADO
        # 'adhoc_base_product', DEPRECIADO
        # 'adhoc_base_project', DEPRECIADO
        # 'adhoc_base_purchase', DEPRECIADO
        # 'adhoc_base_sale', DEPRECIADO
        # 'adhoc_base_setup', DEPRECIADO
        # 'adhoc_base_stock', DEPRECIADO
        # 'adhoc_base_website', DEPRECIADO
        # 'hr_timesheet_task', BAJA PRIORIDAD
        'infrastructure',
        # 'project_adhoc_personalization', NO MIGRADO
        # 'timesheet_task', DEPRECIADO
        # 'web_cleditor_ept', DEPRECIADO
        # 'website_favicon', NO MIGRADOwebsite_favicon
        'account_clean_cancelled_invoice_number',
        'account_invoice_commercial',
        # 'account_invoice_journal_filter', DEPRECIADO
        'account_reconciliation_menu',
        # 'account_transfer', DEPRECIADO
        'base_currency_inverse_rate',
        'base_state_active',
        'product_price_taxes_included',
        'sale_quotation_products',
        'account_debt_management',
        'account_invoice_company_search',
        'account_invoice_tax_wizard',
        'account_journal_active',
        # 'account_journal_sequence', DEPRECIADO
        'account_move_helper',
        'account_multicompany_usability',
        'account_no_translation',
        'adhoc_modules',
        'product_no_translation',
        # 'account_analytic_purchase_contract', RENOMBRADO
        'account_check',
        'product_catalog_aeroo_report',
        'project_category',
        'project_description',
        'project_duplicate_fix',
        'project_kanban_open_project',
        # 'purchase_prices_update', DEPRECIADO
        'sale_prices_update',
        'sale_procurement_date_confirm',
        'stock_voucher',
        # 'account_allow_code_change', DEPRECIADO
        'account_cancel',
        # 'account_followup', DEPRECIADO
        # 'report_custom_filename', NO MIGRADO
        # 'web_action_close_wizard_view_reload', DEPRECIADO
        'l10n_ar_afipws_fe',
        # 'auth_brute_force', NO MIGRADO
        'mis_builder',
        # 'web_graph_sort', NO MIGRADO
        # 'web_pdf_preview', DEPRECIADO
        'project_issue',
        # 'account_analytic_analysis_mods', DEPRECIADO
        'hr_timesheet_balance',
        'product_search_supplier_code',
        'project_closure_restrictions',
        # 'project_task_desc_html', DEPRECIADO
        # 'project_task_order', DEPRECIADO
        'sale_contract_restrict_domain',
        'sale_require_contract',
        # 'stock_picking_locations', DEPRECIADO
        # 'account_invoice_pricelist_discount', DEPRECIADO
        'account_invoice_prices_update',
        # 'contacts', DEPRECIADO
        'product_supplier_search',
        # 'product_template_search_by_ean13', RENOMBRADO
        # 'web_favicon', NO MIGRADO
        # 'web_widget_float_formula', DEPRECIADO PARA ENTERPRISE
        # 'account_contract_lines_sequence', RENOMBRADO
        # 'account_contract_prices_update', RENOMBRADO
        'partner_social_fields',
        # 'stock_multic_fix', DEPRECIADO
        'hr_holidays',
        # 'account_analytic_project', DEPRECIADO
        'account_multic_fix',
        # 'account_voucher_multic_fix', DEPRECIADO
        # 'attachment_preview', NO MIGRADO
        'auth_oauth',
        'auth_signup_verify_email',
        # 'contract_discount', DEPRECIADO
        # 'contract_multic_fix', DEPRECIADO
        'purchase_multic_fix',
        # 'sale_multic_fix', DEPRECIADO
        # 'web_dashboard_tile', NO MIGRADO
        'web_easy_switch_company',
        'website_blog',
        'website_crm',
        'website_twitter',
        # 'web_switch_company_warning', DEPRECIADO
        'account_invoice_operation',
        'product_computed_list_price',
        # 'product_pack', NO LO DEBERIAMOS USAR MAS
        'product_price_currency',
        'project_stage',
        'project_task_activity',
        # 'project_task_delegate', DEPRECIADo
        'sale_contract_editable',
        # 'sale_multiple_invoice', DEPRECIADO
        'sale_require_ref',
        # 'account_analytic_analysis', DEPRECIADO
        'account_analytic_default',
        # 'account_voucher_double_validation', DEPRECIADO
        # 'purchase_double_validation', DEPRECIADO
        # 'account_tax_settlement', NO MIGRADO
        'hr_timesheet_sheet',
        'marketing',
        # 'mass_mailing_statistic_extra', NO MIGRADO
        # 'mis_builder_demo', DEPRECIADO
        'website_doc',
        'website_issue',
        'crm',
        # 'account_contract_recurring_total', DEPRECIADO
        'project_issue_fix',
        # 'warning', DEPRECIADO

    ],
    'data': [
        'config_data.xml',
        'users_data.xml',
        # last load lang (so user is already created)
        'load_es_lang.yml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
