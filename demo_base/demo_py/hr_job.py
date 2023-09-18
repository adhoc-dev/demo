from odoo import api, models


class HrJob(models.Model):

    _inherit = 'hr.job'

    @api.model
    def _init_demo_base(self):
        self.search([]).write({'company_id': False})
