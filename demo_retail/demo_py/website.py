from odoo import api, fields, models, tools, http, release, registry


class Website(models.Model):
    _inherit = "website"


    @api.model
    def _init_demo_retail(self):
        # cl
        cl_c = self.env.ref('l10n_cl.demo_company_cl')
        # uy
        uy_c = self.env.ref('l10n_uy_account.company_uy')
        # ar (ri, muebleria)
        ar_c = self.env.ref('l10n_ar.company_ri')
        import pdb; pdb.set_trace;
        for company in ar_c + uy_c + cl_c:
            website = self.env['website'].search([('company_id','=',company.id)],limit=1)
            kwargs = {
                'selected_features': [1, 8, 13],
                'industry_id': 1467,
                'selected_palette': "default-8",
                'theme_name': "theme_loftspace",
                'website_purpose': "sell_more",
                'website_type': "online_store",
                'context': {
                    'allowed_company_ids':[company.id],
                    'lang': website.language_ids[:1],
                    'tz': 'America/Buenos_Aires',
                    'uid': 2
                    }
                }
            if website:
                website.configurator_apply(**kwargs)
