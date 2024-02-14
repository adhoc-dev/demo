from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    @api.model
    def _init_demo_base(self):
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('sale_ux.update_prices_automatically', 'True')
        set_param('analytic.group_analytic_accounting', 'True')
        set_param('product.product_pricelist_setting', 'advanced')
        set_param('stock.group_stock_adv_location', 'True')
        # cl
        cl_c = self.env.ref('l10n_cl.demo_company_cl')
        # uy
        uy_c = self.env.ref('l10n_uy_account.company_uy')
        # ar (ri, muebleria)
        ar_c = self.env.ref('l10n_ar.company_ri')
        # us (main_company)
        us_c = self.env.ref('base.main_company')

        for company in ar_c + uy_c + cl_c + us_c:
            wizard = self.with_company(company).create({})
            wizard._inverse_sale_tax_ids()
            wizard._inverse_purchase_tax_ids()
