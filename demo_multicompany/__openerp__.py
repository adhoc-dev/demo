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
        'account_accountant',
        'l10n_ar_afipws_fe',
        'account_multicompany_usability',
        'account_multic_fix',
        'account_debt_management',
        'account_move_helper',
        'account_no_translation',
        'base_currency_inverse_rate',
        'account_clean_cancelled_invoice_number',
        'account_invoice_change_currency',
        'account_invoice_commercial',
        'account_invoice_company_search',
        'account_invoice_journal_group',
        # 'account_invoice_operation',
        'account_invoice_prices_update',
        'account_invoice_tax_wizard',
        'l10n_ar_aeroo_einvoice',
        'l10n_ar_aeroo_purchase',
        'l10n_ar_aeroo_sale',
        'l10n_ar_aeroo_stock',
        'l10n_ar_aeroo_payment_group',
        'l10n_ar_currency_update',
        'l10n_ar_padron_afip',
        'l10n_ar_bank',
        'product_catalog_aeroo_report_public_categ',
        'product_no_translation',
        'product_price_currency',
        'product_pricelist',
        'product_price_taxes_included',
        'product_replenishment_cost_rule',
        'product_sale_price_by_margin',
        'product_template_search_by_barcode',
        'product_website_categ_search',
        'purchase_quotation_products',
        'sale_exception_credit_limit',
        'sale_exception_partner_state',
        'sale_exception_price_security',
        'sale_quotation_products',
        'purchase_discount',
        'stock_inventory_preparation_filter',
        'base_state_active',
        'project_description',
        'project_duplicate_fix',
        'project_kanban_open_project',
        # 'sale_order_type_user_default',
        'sale_procurement_date_confirm',
        'base_technical_features',
    ],
    'data': [
        'load_es_lang.yml',
        'config_data.xml',
        'users_data.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
