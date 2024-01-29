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
    'name': 'Demo Base',
    'version': "16.0.1.2.0",
    'category': 'Tools',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        # Módulos que se instalan mediante productos en nube, si vendemos estos productos se auto instalan estos módulos.
        # como por ahora runbot ni las bases demo, implementan esta logica de auto instalar en funcion de productos,
        # hicimos una análisis manual de que “productos” que consideramos ”base” (los queremos en todas las demo) y
        # agregamos como dependencia el modulo que instalaría dicho producto.

        # Finanzas / Consolidación:
        'account_consolidation',
        # Finanzas / Contabilidad avanzada:
        'account_accountant',
        'saas_client_account',
        # 'account_reports_multicurrency', solicitado por comercial
        # Finanzas / Facturacion y Pagos:
        'account',
        'account_invoice_tax',
        # General / Aprobaciones:
        'approvals',
        # General / Documentos:
        'documents',
        # General / Reportería / BI / ninja / Hoja de cálculo:
        'ks_dashboard_ninja',
        # Localizaciones / Loc Argentina:
        'l10n_ar_account_withholding',
        'l10n_ar_bank',
        'l10n_ar_edi_ux',
        # Localizaciones / Loc Chile:
        # 'l10n_cl_counties', ver
        'l10n_cl',
        # Localizaciones / Loc USA:
        'l10n_us',
        # Localizaciones / Loc Urugaya:
        'l10n_uy_edi',
        # Localizaciones / Loc España:
        'l10n_es',
        # Localizaciones / Loc Perú:
        'l10n_pe',
        # RRHH / Asistencias:
        'hr_attendance',
        # RRHH / Ausencias:
        'hr_holidays',
        # RRHH / Gastos:
        'hr_expense',
        # RRHH/ Selección de personal:
        'hr_recruitment',
        # Sitio web / E-commerce:
        'website_sale',
        # Sitio web / Encuestas:
        'survey',
        # Sitio web / Sitio web:
        'website',
        # Sitio web / Social Marketing:
        'social',
        # Supply Chain / Compras:
        'purchase',
        # Ventas / CRM:
        'crm',
        # Ventas / Ventas:
        'sale_management',

        # A este listado sumamos los módulos que comercial nos pide agregar y que no se auto instalarían por productos.
        # Si eventualmente implementamos logica de instalacion mediante productos la sección de arriba deberia poder borrarse.
        'base_exception',
        'l10n_ar_demo',
        'loyalty',
        'mass_mailing',
        'payment_demo',
        'product_internal_code',
        'product_planned_price',
        'product_price_taxes_included',
        'sale_margin',
        'sale_quotation_builder',
        'sale_ux',

        # modulos que se auto instalan porque lo tenemos forzado en adhoc modules
        # esto en realidad queremos ver de sincornizarlo de alguna manera con nuestra base para que sea mas dinamico
        # y ademas sincroncie info de modulo que desactivamos auto instalacion

        'auth_password_policy',
        'web_search_with_and',
        'base_user_show_email',
        'base_ux',
        'database_cleanup',
        'web_advanced_search',
        'mail_tracking',
        'partner_contact_access_link',
        'sale_ux',
        'payment_multic_ux',
        # 'account_balance_import', lo comento porque me da error al instalr
        'product_price_taxes_included',
        'sale_quotation_products',
        'l10n_ar_sale',
        'product_ux',
        'account_invoice_tax',
        'account_multicompany_ux',
        'purchase_ux',
        'purchase_quotation_products',

        # estos falta revisar y mandar a alguno de los verticales

        # 'delivery_ux',
        # 'stock_picking_sale_order_link',
        # 'stock_picking_invoice_link',
        # 'l10n_ar_stock',
        # 'stock_ux',
        # 'sale_exception_print',
        # 'purchase_global_discount',
        # 'sale_exceptions_ignore_approve',
        # 'website_sale_multic_ux',
        # 'website_sale_ux',
        # 'l10n_ar_website_sale_ux',
        # 'project_ux',
        # 'website_sale_exception',
        # 'hr_timesheet_ux',
        # 'sale_timesheet_ux',
        # 'helpdesk_ux',
        # 'sale_temporal_ux',
        # 'website_sale_product_pack',
        # 'sale_subscription_ux',
        # 'spreadsheet_dashboard_spreadsheet_edition_ux',
        # 'repair_multicompany_ux',
        # 'hr_timesheet_attendance_ux',
        # 'maintenance_ux',
        # 'helpdesk_timesheet_ux',
        # 'mail_activity_board_ux',
        # 'account_consolidation_ux',
        # 'sale_stock_analytic',
        # 'stock_request_ux',
        # 'sale_order_lot_selection_ux',
        # 'stock_picking_batch_extended',
        # 'product_order_noname',
        # 'sale_stock_renting_ux',

    ],
    'data': [
    ],
    'demo': [
        'demo/companies_demo.xml',
        'demo/payment_provider_demo.xml',
        'demo/res_users_demo.xml',
        'demo/res_groups_demo.xml',
        'demo/website_demo.xml',
        'demo/init_demo_py.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
