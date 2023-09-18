from odoo import api, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    @api.model
    def _init_demo_retail(self):
        for view in (
                self.env.ref('stock.stock_location_view_tree2_editable', raise_if_not_found=False),
                self.env.ref('stock.stock_location_view_form_editable', raise_if_not_found=False),
                ):
            if view:
                view.active = False
