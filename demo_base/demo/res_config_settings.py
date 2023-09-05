from odoo import api, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    @api.model
    def _init_demo(self):
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('sale_ux.update_prices_automatically', 'True')

    def _inverse_sale_tax_ids(self):
        super()._inverse_sale_tax_ids()
        # TODO ver con team localizaciones si sumamos esto en saas_client_account para que quede para todo el mundo
        # buscamos productos de esta compañia o sin compañía que no tengan ningun impuesto de esta compañía y
        # le configuramos este impuesto por defecto
        for rec in self:
            taxes = rec.sale_tax_ids.filtered(lambda tax: tax.company_id == rec.company_id)
            if taxes:
                self.env['product.template'].search([
                    ('company_id', 'in', [False, rec.company_id.id]),
                    ('taxes_id.company_id', '=', rec.company_id.id)]).write({'taxes_id': [(4, taxes[0].id)]})

    def _inverse_purchase_tax_ids(self):
        super()._inverse_purchase_tax_ids()
        # TODO ver con team localizaciones si sumamos esto en saas_client_account para que quede para todo el mundo
        # buscamos productos de esta compañia o sin compañía que no tengan ningun impuesto de esta compañía y
        # le configuramos este impuesto por defecto
        for rec in self:
            taxes = rec.purchase_tax_ids.filtered(lambda tax: tax.company_id == rec.company_id)
            if taxes:
                self.env['product.template'].search([
                    ('company_id', 'in', [False, rec.company_id.id]),
                    ('supplier_taxes_id.company_id', '=', rec.company_id.id)]).write({'supplier_taxes_id': [(4, taxes[0].id)]})
