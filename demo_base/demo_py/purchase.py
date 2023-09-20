from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'purchase.order'

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
            for purchase in self.env['purchase.order'].search([('company_id', '=', us_c.id)]):
                new_purchase = purchase.copy(default={'company_id': company.id})
                new_purchase._compute_tax_id()
                # TODO verificar si toma bien los impuestos
                if purchase.state == 'purchase':
                    new_purchase.button_confirm()
                elif purchase.state == 'sent':
                    new_purchase.action_rfq_send()
