from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    @api.model
    def _init_demo_data(self):
        # creamos usuario igual a admin pero sacando permiso a grupos de configuracion
        if not self.search([('login', '=', 'demo_admin')]):
            user = self.env.ref('base.user_admin').copy({
                'name': 'Demo Admin User',
                'email': 'demo@yourcompany.example.com',
                'login': 'demo_admin',
                'password': 'demo_admin',
                'active': True,
            })
            user.write({
                'groups_id': [
                    (3, self.env.ref('base.group_erp_manager').id, 0),
                    (3, self.env.ref('base.group_system').id, 0)]})

        # groups to add
        for group_xml_id in [
                'base.group_multi_currency', 'base.group_multi_company', 'analytic.group_analytic_accounting',
                'product.group_discount_per_so_line']:
            group = self.env.ref(group_xml_id, False)
            if not group:
                continue
            self.env.ref('base.group_user').write({'implied_ids': [(4, group.id)]})
