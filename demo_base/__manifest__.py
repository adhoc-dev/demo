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
    'name': 'Demo Data',
    'version': "15.0.1.0.0",
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
                # 'l10n_cl_counties',
                # 'l10n_cl',
            # Localizaciones / Loc USA:
                # 'l10n_us',
            # Localizaciones / Loc Urugaya:
                # 'l10n_uy_edi',
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

        # A este listado sumamos sumamos los módulos que comercial nos pide agregar y que no se auto instalarían por productos.
        # Si eventualmente implementamos logica de instalacion mediante productos la sección de arriba deberia poder borrarse.
        'mass_mailing',
        'product_internal_code',
        'product_planned_price',
        'sale_coupon',
        'sale_margin',
        'sale_quotation_builder',
    ],
    'data': [
    ],
    'demo': [
        'companies_data.xml',
        'users_data.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
