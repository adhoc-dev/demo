from odoo import models, api


class BaseLanguageInstall(models.TransientModel):

    _inherit = "base.language.install"

    @api.model
    def _install_lenguages(self):
        lang_ids = self.env['res.lang'].with_context(active_test=False).search([('code', 'in', ['es_AR', 'es_UY', 'es_CL'])]).ids
        installer = self.env['base.language.install'].create({'lang_ids': [(6, 0, lang_ids)]})
        installer.lang_install()
