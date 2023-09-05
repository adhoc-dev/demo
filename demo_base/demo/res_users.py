from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    @api.model
    def _init_demo(self):
        # creamos usuarios igual a admin pero restringimos compañías
        if not self.search([('login', '=', 'admin_ar')]):
            user = self.env.ref('base.user_admin').copy({
                'name': 'Valentino',
                'email': 'valentino@fabricademuebles.com',
                'login': 'admin_ar',
                'password': 'admin_ar',
                'active': True,
                'lang': 'es_AR',
            })
            user.write({
                'company_ids': [
                    (3, self.env.ref('l10n_ar.company_mono').id, 0),
                    (3, self.env.ref('l10n_ar.company_exento').id, 0),
                    (3, self.env.ref('l10n_uy_account.company_uy').id, 0),
                    (3, self.env.ref('l10n_cl.demo_company_cl').id, 0)],
                'company_id': self.env.ref('l10n_ar.company_ri').id
            })
            user.action_create_employee()
        if not self.search([('login', '=', 'admin_uy')]):
            user = self.env.ref('base.user_admin').copy({
                'name': 'Valentino',
                'login': 'admin_uy',
                'password': 'admin_uy',
                'active': True,
                'lang': 'es_UY',
            })
            user.write({
                'company_ids': [
                    (3, self.env.ref('l10n_ar.company_mono').id, 0),
                    (3, self.env.ref('l10n_ar.company_exento').id, 0),
                    (3, self.env.ref('l10n_ar.company_ri').id, 0),
                    (3, self.env.ref('l10n_cl.demo_company_cl').id, 0)],
                'company_id': self.env.ref('l10n_uy_account.company_uy').id
            })
            user.action_create_employee()
        if not self.search([('login', '=', 'admin_cl')]):
            user = self.env.ref('base.user_admin').copy({
                'name': 'Valentino',
                'login': 'admin_cl',
                'password': 'admin_cl',
                'active': True,
                'lang': 'es_CL',
            })
            user.write({
                'company_ids': [
                    (3, self.env.ref('l10n_ar.company_mono').id, 0),
                    (3, self.env.ref('l10n_ar.company_exento').id, 0),
                    (3, self.env.ref('l10n_ar.company_ri').id, 0),
                    (3, self.env.ref('l10n_uy_account.company_uy').id, 0)],
                'company_id': self.env.ref('l10n_cl.demo_company_cl').id
            })
            user.action_create_employee()
        if not self.search([('login', '=', 'admin_us')]):
            user = self.env.ref('base.user_admin').copy({
                'name': 'Valentino',
                'login': 'admin_us',
                'password': 'admin_us',
                'active': True,
            })
            user.write({
                'company_ids': [
                    (3, self.env.ref('l10n_ar.company_mono').id, 0),
                    (3, self.env.ref('l10n_ar.company_exento').id, 0),
                    (3, self.env.ref('l10n_ar.company_ri').id, 0),
                    (3, self.env.ref('l10n_uy_account.company_uy').id, 0),
                    (3, self.env.ref('l10n_cl.demo_company_cl').id, 0)],
                'company_id': self.env.ref('base.main_company').id
            })
            user.action_create_employee()
