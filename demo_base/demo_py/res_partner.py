from odoo import api, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    def _get_ar_partner(self):
        self.ensure_one()
        mapping = {
            # wood corner a adhoc SA
            'base.res_partner_1': 'l10n_ar.adhoc',
            # wood corner a adhoc SA
            'base.res_partner_1': 'l10n_ar.adhoc',
        }
        return self._get_partner(mapping)

    def _get_partner(self, mapping):
        self.ensure_one()
        external_id = self.get_external_id
        if not external_id:
            logger.warning('No hay external id para partner %s')
            return self
        new_partner = self.env.ref(mapping.get(self.get_external_id))
        if not new_partner:
            logger.warning('No encontramos partner para  %s')
            return self
        return new_partner
