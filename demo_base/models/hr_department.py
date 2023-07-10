from odoo import api, models


class Department(models.Model):

    _inherit = 'hr.department'

    @api.model
    def _delete_company(self):
        self.search([]).write({'company_id': False})
