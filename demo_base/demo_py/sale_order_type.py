from odoo import api, models


class SaleOrderTypology(models.Model):

    _inherit = 'sale.order.type'

    @api.model
    def _init_demo_base(self):
        us_c = self.env.ref('base.main_company')
        for rec in self:
            if rec.company_id == us_c:
                rec.company_id = False
