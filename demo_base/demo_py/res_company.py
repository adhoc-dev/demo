from odoo import api, models


class ResCompany(models.Model):

    _inherit = 'res.company'

    @api.model
    def _init_demo_base(self):

        #Archivamos la compañía monotributista
        company = self.env.ref('l10n_ar.company_mono')
        company.write({'active':False})
        #le cambiamos el nombre a algunas companias
        self.env.ref('l10n_uy_account.company_uy').write({'name':'Muebleria UY'})
        self.env.ref('l10n_cl.demo_company_cl').write({'name':'Muebleria CL'})
        self.env.ref('base.main_company').write({'name':'Muebleria US'})
        self.env.ref('l10n_pe.demo_company_pe').write({'name':'Muebleria PE'})
        self.env.ref('l10n_es.demo_company_es').write({'name':'Muebleria ES'})
        # self.env.ref('l10n_ar.company_ri').write({'name':'Muebleria ARG'})

