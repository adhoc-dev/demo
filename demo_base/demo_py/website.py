from odoo import api, models


class Website(models.Model):
    _inherit = "website"

    @api.model
    def _init_demo_base(self):
        # por pedido de producto dejar todos los domain de los sitios web vacios
        for website in self.env['website'].search([('domain', '!=', False)]):
            website.write({'domain': False})

    @api.model
    def _load_websites(self, parameters):
        # lo hacemos en cada demo para que el look and feel sea según el tipo de vertical
        # cl
        cl_c = self.env.ref('l10n_cl.demo_company_cl')
        # uy
        uy_c = self.env.ref('l10n_uy_account.company_uy')
        # ar (ri, muebleria)
        ar_c = self.env.ref('l10n_ar.company_ri')
        for company in ar_c + uy_c + cl_c:
            # solo lo hacemos si no hay theme para que si ya se corrió por otro vertical no se vuelva a correr
            website = self.env['website'].search([('theme_id', '=', False), ('company_id', '=', company.id)],limit=1)
            if not website:
                continue
            # aca dejamos algunos valores por defecto pero pueden ser modificados por el parameters que se mande
            kwargs = {
                'selected_features': [1, 8, 13],
                'industry_id': 1467,
                'selected_palette': "default-8",
                # TODO chequear antes tema instalado y si no mandar a instalar?
                # MUY IMPORTANTE que el tema esté instalado (y tmb otros features que se quiere)
                'theme_name': "theme_loftspace",
                'website_purpose': "sell_more",
                'website_type': "online_store",
                'context': {
                    'allowed_company_ids':[company.id],
                    'lang': 'es_AR',
                    'tz': 'America/Buenos_Aires',
                    'uid': 2
                    }
                }
            kwargs.update(parameters)
            website.with_context(website_id=website.id, force_mode_edit_false=True).configurator_apply(**kwargs)

    def button_go_website(self, path='/', mode_edit=False):
        if mode_edit and self._context.get('force_mode_edit_false'):
            mode_edit = False
        return super().button_go_website(path=path, mode_edit=mode_edit)
