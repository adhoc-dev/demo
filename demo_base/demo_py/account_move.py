import logging
from odoo import api, models, fields
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.model
    def _init_demo_base(self):
        # cl
        cl_c = self.env.ref('l10n_cl.demo_company_cl')
        # uy
        uy_c = self.env.ref('l10n_uy_account.company_uy')
        # ar (ri, muebleria)
        ar_c = self.env.ref('l10n_ar.company_ri')
        # us (main_company)
        us_c = self.env.ref('base.main_company')

        for company in ar_c + uy_c + cl_c: 

            # por compañía buscamos una orden de venta que esté en to invoice (para no renegar con la entrega) y:
            # a) la duplicamos y generamos un caso de venta facturada con factura con pago vencido
            # b) la duplicamos y generamos un caso de venta facturada y cobrada (lo vamos a implementar en 17)
            # c) la duplicamos y generamos un caso de venta facturada y todavía no vencida
            sale = self.env['sale.order'].search([('company_id', '=', company.id), ('invoice_status', '=', 'to invoice')], limit=1)
            today = fields.Date.today()
            yesterday = today - timedelta(days=1)
            next_month = today + relativedelta(months=1)
            
            if not sale:
                _logger.warning('No encontramos ordenas de venta a facturar en compañía %s', company.name)
                continue

            # caso a
            sale_a = sale.copy()
            sale_a.write({'date_order': yesterday})
            sale_a.action_confirm()
            invoices = sale_a._create_invoices(final=True)
            invoices.write({'invoice_date': yesterday, 'invoice_date_due': yesterday})

            if not invoices.l10n_latam_document_type_id:
                if company == ar_c:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_ar.dc_fce_a_f')})
                elif company == uy_c:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_uy_account.dc_inv')})
                else:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_cl.dc_a_f_dte')})

            invoices.action_post()

            # caso b
            sale_b = sale.copy()
            sale_b.write({'date_order': yesterday})
            sale_b.action_confirm()
            invoices = sale_b._create_invoices(final=True)

            if not invoices.l10n_latam_document_type_id:
                if company == ar_c:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_ar.dc_fce_a_f')})
                elif company == uy_c:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_uy_account.dc_inv')})
                else:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_cl.dc_a_f_dte')})

            invoices.action_post()
            # TODO implementar pago en 17

            # caso c
            sale_c = sale.copy()
            sale_c.write({'date_order': yesterday})
            sale_c.action_confirm()
            invoices = sale_c._create_invoices(final=True)
            invoices.write({'invoice_date_due': next_month})

            if not invoices.l10n_latam_document_type_id:
                if company == ar_c:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_ar.dc_fce_a_f')})
                elif company == uy_c:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_uy_account.dc_inv')})
                else:
                    invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_cl.dc_a_f_dte')})

            invoices.action_post()
            # TODO implementar pago en 17


    
    
# OPCIONES PARA SACAR EL IMPUESTO DEL PRODUCTO
    # for line in sale_a.order_line:    
    #     if len(line.product_id.taxes_id) >1:
    #         # taxes = line.product_id.taxes_id
    #         line.product_id.write({'taxes_id':line.product_id.taxes_id[0]})
    #         #es necesario que vuelva a poner el impuesto que saque?   
    
    # for line in invoices.invoice_line_ids:
    #     if len(line.tax_ids.filtered(lambda x: x.tax_group_id.name == 'IVA')) > 1:
    #     # Eliminar impuestos adicionales
    #     taxes_to_remove = line.tax_ids.filtered(lambda x: x.tax_group_id.name == 'IVA')[1:]
    #     line.tax_ids -= taxes_to_remove

    # for line in invoices.invoice_line_ids:
    #     if len(line.product_id.taxes_id) >1:
    #         # taxes = line.product_id.taxes_id
    #         line.product_id.write({'taxes_id':line.product_id.taxes_id[0]})
    #         #es necesario que vuelva a poner el impuesto que saque?

# def document_type(self, invoices, company):
#     if not invoices.l10n_latam_document_type_id:
#         if company == ar_c:
#             invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_ar.dc_fce_a_f')})
#         elif company == uy_c:
#             # for linea in sale_a.order_lines:
#             #      if linea.
#             invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_uy_account.dc_inv')})
#         else:
#             invoices.write({'l10n_latam_document_type_id': self.env.ref('l10n_cl.dc_a_f_dte')})
