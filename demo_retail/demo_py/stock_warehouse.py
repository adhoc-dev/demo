from odoo import api, models


class Warehouse(models.Model):

    _inherit = 'stock.warehouse'

    @api.model
    def _init_demo_retail(self):
        warehouses = self.search([])
        for warehouse in warehouses:
            existing_warehouse = self.search([
                ('name', '=', warehouse.company_id.name),
                ('company_id', '=', warehouse.company_id.id)
            ])
            if not existing_warehouse:
                warehouse.name = warehouse.company_id.name
