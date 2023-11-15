from odoo import api, models


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
        # us (main_company)
        us_c = self.env.ref('base.main_company')
        for company in ar_c + uy_c + cl_c:
            new_sale_website_id = False
            new_sale_website_id = self.env['website'].search([('company_id', '=', company.id)], limit=1).id
            for sale in self.env['sale.order'].search([('company_id', '=', us_c.id)]):
                new_sale = sale.with_company(company).copy()
                vals = {'company_id': company.id}
                if sale.website_id:
                    vals['website_id'] = new_sale_website_id
                new_sale.write(vals)
                if sale.state == 'sale':
                    new_sale.action_confirm()
                elif sale.state == 'sent':
                    new_sale.action_quotation_send()
