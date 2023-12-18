from odoo import api, models


class ResCompany(models.Model):

    _inherit = 'res.company'

    @api.model
    def _init_demo_retail(self):

        #Archivamos la compañía chicago
        company = self.env.ref('stock.res_company_1')
        company.write({'active':False})

