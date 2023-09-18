from odoo import api, models


class Warehouse(models.Model):

    _inherit = 'stock.warehouse'

    @api.model
    def _init_demo_retail(self):
        warehouse = self.search([('name', '=', '(AR) Responsable Inscripto')])
        if warehouse:
            warehouse.write({'name': 'Muebleria SRL'})
