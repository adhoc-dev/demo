from odoo import api, models


class Website(models.Model):
    _inherit = "website"

    @api.model
    def _init_demo_retail(self):
        parameters = {
            'selected_features': [1, 8, 13],
            'industry_id': 1467,
            'selected_palette': "default-8",
            # MUY IMPORTANTE que el tema esté instalado (y tmb otros features que se quiere)
            'theme_name': "theme_loftspace",
            'website_purpose': "sell_more",
            'website_type': "online_store",
        }
        self._load_websites(parameters)
