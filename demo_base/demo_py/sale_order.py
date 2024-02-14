from odoo import api, models, fields
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.model
    def _init_demo_base(self):
        # cl
        cl_c = self.env.ref('l10n_cl.demo_company_cl')
        # uy
        uy_c = self.env.ref('l10n_uy_account.company_uy')
        # ar (ri, muebleria)
        ar_c = self.env.ref('l10n_ar.company_ri')
        # TODO falta en us replicar la parte de facturar los 3 casos
        # us (main_company)
        us_c = self.env.ref('base.main_company')
        for company in ar_c + uy_c + cl_c:
            # setamos validity days de las companias a 100 por si está instalado sale_order_validity
            # ya que en ese caso da error porque estamos duplicando ventas viejas (que está bueno queden con fecha
            # vieja) y dan error al validar. De alguna manera hacemos lo mismo que hicimos en sale_order_validity
            # con demo data (pero para el resto de las cias)
            company.quotation_validity_days = 100
            new_sale_website_id = False
            new_sale_website_id = self.env['website'].search([('company_id', '=', company.id)], limit=1).id
            for sale in self.env['sale.order'].search([('company_id', '=', us_c.id)]):
                new_sale = sale.with_company(company).copy()
                vals = {'company_id': company.id, 'partner_id': sale.partner_id._get_company_partner(company).id}
                if sale.website_id:
                    vals['website_id'] = new_sale_website_id
                new_sale.write(vals)
                new_sale._compute_pricelist_id()
                if sale.state == 'sale':
                    new_sale.action_confirm()
                elif sale.state == 'sent':
                    new_sale.action_quotation_send()

            # por compañía buscamos una orden de venta que esté en to invoice (para no renegar con la entrega) y:
            # a) la duplicamos y generamos un caso de venta facturada con factura con pago vencido
            # b) la duplicamos y generamos un caso de venta facturada y cobrada (lo vamos a implementar en 17)
            # c) la duplicamos y generamos un caso de venta facturada y todavía no vencida
            sale = self.env['sale.order'].search([
                # buscamos para este producto ya que las ventas demo que tienen este producto solo tienen una linea a facturar
                # y eso nos permite pasar facilmente venta a estado "facturado"
                ('order_line.product_id', '=', self.env.ref('product.product_product_16').id),
                ('company_id', '=', company.id), ('invoice_status', '=', 'to invoice')], limit=1)
            today = fields.Date.today()
            yesterday = today - relativedelta(days=1)
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
            invoices.action_post()

            # caso b
            sale_b = sale.copy()
            sale_b.write({'date_order': yesterday})
            sale_b.action_confirm()
            invoices = sale_b._create_invoices(final=True)
            invoices.action_post()
            # TODO implementar pago en 17

            # caso c
            sale_c = sale.copy()
            sale_c.write({'date_order': yesterday})
            sale_c.action_confirm()
            invoices = sale_c._create_invoices(final=True)
            invoices.write({'invoice_date_due': next_month})
            invoices.action_post()
