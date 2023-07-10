from odoo import api, models


class Applicant(models.Model):

    _inherit = 'hr.applicant'

    @api.model
    def _delete_company(self):
        self.search([]).write({'company_id': False})
