from odoo import models


class Module(models.Model):
    _inherit = "ir.module.module"

    def _button_immediate_function(self, function):
        if self._context.get('force_mode_edit_false'):
            return
        return super()._button_immediate_function(function)
