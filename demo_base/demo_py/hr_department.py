from odoo import api, models


class Department(models.Model):

    _inherit = 'hr.department'

    @api.model
    def _init_demo_base(self):
        self.search([]).write({'company_id': False})
