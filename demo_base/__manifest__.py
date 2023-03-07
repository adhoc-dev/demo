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
        # modulos que se instalarian mediante productos. Para obtener este listado
        # filtrar en adhoc products por "Modules Auto Installed está establecida" y 
        # agregar los "modules auto install" de los productos que se desee
        # Finanzas / Consolidación: account_consolidation
        # Finanzas / Contabilidad avanzada: account_accountant, saas_client_account
        # Finanzas / Facturacion y Pagos: account, account_invoice_tax
        # General / Aprobaciones: approvals
        # General / Documentos: documents
        # General / Reportería / BI / ninja / Hoja de cálculo: ks_dashboard_ninja
        # Localizaciones / Loc Argentina: l10n_ar_account_withholding, l10n_ar_bank, l10n_ar_edi_ux
        # Localizaciones / Loc Chile: l10n_cl_counties, l10n_cl
        # Localizaciones / Loc USA: l10n_us
        # Localizaciones / Loc Urugaya: l10n_uy_edi
        # Sitio web / E-commerce: website_sale
        # Supply Chain / Compras: purchase
        # Ventas / CRM: crm
        # Ventas / Ventas: sale_management
        'account_consolidation',
        'account_accountant',
        'saas_client_account',
        'account',
        'account_invoice_tax',
        'approvals',
        'documents',
        'ks_dashboard_ninja',
        'l10n_ar_account_withholding, l10n_ar_bank',
        'l10n_ar_edi_ux',
        'l10n_cl_counties',
        'l10n_cl',
        'l10n_us',
        'l10n_uy_edi',
        'website_sale',
        'purchase',
        'crm',
        'sale_management',
        # módulos adicionales que se suelen utilizar
        'product_internal_code',
    ],
    'data': [
    ],
    'demo': [
        'users_data.xml',
    ],
    'test': [
    ],
    'installable': False,
    'auto_install': False,
    'application': False,
}
