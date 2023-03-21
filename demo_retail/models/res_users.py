from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    @api.model
    def _update_demo_admin(self):
        # demo_admin groups
        user = self.search([('login', '=', 'admin_ar')])
        group = self.env.ref('stock.group_stock_multi_warehouses', False)
        if group:
            user.write({'groups_id': [(4, group.id)]})

