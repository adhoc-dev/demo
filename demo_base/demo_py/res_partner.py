
from odoo import models
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):

    _inherit = 'res.partner'

    def _get_ar_partner(self):
        self.ensure_one()
        mapping = {
            # Ready Mat a Expresso
            'base.res_partner_4': 'l10n_ar.res_partner_expresso',
            # Deco Addict mappeamos a Gritti
            'base.res_partner_2': 'l10n_ar.res_partner_gritti_agrimensura',
            # Gemmini Furniture mappeamos a Adhoc SA
            'base.res_partner_3': 'l10n_ar.res_partner_adhoc',
            # Lumber Inc mappeamos a Concejo municipal
            'base.res_partner_18': 'l10n_ar.res_partner_cmr',
            # Azure mappeamos a Cerro Castor
            'base.res_partner_12': 'l10n_ar.res_partner_cerrocastor',
            # Wood Corner mappeamos a Foreign Inc
            'base.res_partner_1': 'l10n_ar.res_partner_foreign'
        }
        return self._get_partner(mapping)

    def _get_partner(self, mapping):
        self.ensure_one()
        external_id = self.get_external_id()
        if not external_id:
            _logger.warning('No hay external id para partner %s', self.name)
            return self
        xmlid = mapping.get(list(external_id.values())[0])
        if not xmlid:
            _logger.warning('No se encontró external id en mapping para partner %s', self.name)
            return self
        new_partner = self.env.ref(xmlid)
        if not new_partner:
            _logger.warning('No encontramos partner para %s', external_id)
            return self

        return new_partner

