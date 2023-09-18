from odoo import api, models


class Applicant(models.Model):

    _inherit = 'hr.applicant'

    @api.model
    def _init_demo_base(self):
        self.search([]).write({'company_id': False})
