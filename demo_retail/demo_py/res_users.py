from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    @api.model
    def _init_demo_retail(self):
        # demo_admin groups
        admin_ar = self.search([('login', '=', 'admin_ar')])
        admin_uy = self.search([('login', '=', 'admin_uy')])
        admin_cl = self.search([('login', '=', 'admin_cl')])
        admin_us = self.search([('login', '=', 'admin_us')])
        group = self.env.ref('stock.group_stock_multi_warehouses', False)
        if group:
            admin_ar.write({'groups_id': [(4, group.id)]})
            admin_uy.write({'groups_id': [(4, group.id)]})
            admin_cl.write({'groups_id': [(4, group.id)]})
            admin_us.write({'groups_id': [(4, group.id)]})

