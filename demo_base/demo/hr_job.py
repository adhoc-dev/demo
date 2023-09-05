from odoo import api, models


class HrJob(models.Model):

    _inherit = 'hr.job'

    @api.model
    def _delete_company(self):
        self.search([]).write({'company_id': False})
