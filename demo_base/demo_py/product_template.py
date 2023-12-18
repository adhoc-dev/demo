from odoo import api, models

class ProductTemplate(models.Model):

    _inherit = 'product.template'

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
        products = self.env['product.template'].with_company(us_c).search([('standard_price', '!=', 0.0)])
        for company in ar_c + uy_c + cl_c:
            for product in products:
                product.with_company(company).standard_price = product.standard_price





