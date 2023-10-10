from odoo import api, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    @api.model
    def _init_demo_base(self):
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('sale_ux.update_prices_automatically', 'True')
