from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'sale.order'

    @api.model
    def _init_demo(self):
        # cl
        cl_c = self.env.ref('l10n_cl.demo_company_cl')
        # uy
        uy_c = self.env.ref('l10n_uy_account.company_uy')
        # ar (ri, muebleria)
        ar_c = self.env.ref('l10n_ar.company_ri')
        # us (main_company)
        us_c = self.env.ref('base.main_company')
        for company in ar_c + uy_c + cl_c:
            for sale in self.env['sale.order'].search([('company_id', '=', us_c.id)]):
                new_sale = sale.copy(default={'company_id': company.id})
                # TODO verificar si toma bien los impuestos
                if sale.state == 'done':
                    new_sale.action_confirm()
                elif sale.state == 'sent':
                    new_sale.action_sent()
