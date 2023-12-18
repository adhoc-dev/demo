from odoo import models, api


class BaseLanguageInstall(models.TransientModel):

    _inherit = "base.language.install"

    @api.model
    def _init_demo_base(self):
        lang_ids = self.env['res.lang'].with_context(active_test=False).search([('code', 'in', ['es_AR', 'es_UY', 'es_CL'])]).ids
        installer = self.env['base.language.install'].create({'lang_ids': [(6, 0, lang_ids)]})
        installer.lang_install()
        # por ahora seteamos idioma por defecto es_AR para todas las compañías.
        # Luego podriamos cambiar y hacer que los por defecto sean distintos para cada cia
        self.env['ir.default'].set('res.partner', 'lang', 'es_AR')
        self.env['res.partner'].with_context(active_test=False).search([]).write({'lang': 'es_AR'})
