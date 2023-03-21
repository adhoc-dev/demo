from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    @api.model
    def _init_demo_admin(self):
        # creamos usuario igual a admin pero restringimos compañías
        if not self.search([('login', '=', 'admin_ar')]):
            user = self.env.ref('base.user_admin').copy({
                'name': 'Valentino',
                'email': 'valentino@fabricademueblessa.com',
                'login': 'admin_ar',
                'password': 'admin_ar',
                'active': True,
            })
            user.write({
                'company_ids': [
                    (3, self.env.ref('l10n_ar.company_mono').id, 0),
                    (3, self.env.ref('l10n_ar.company_exento').id, 0)],
                'company_id': self.env.ref('l10n_ar.company_ri').id
            })
