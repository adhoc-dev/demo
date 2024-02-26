
from odoo import models
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):

    _inherit = 'res.partner'

    def _get_company_partner(self, company):
        self.ensure_one()
        # mark demo con "k"
        # hr.res_partner_demo_private_address
        mapping = {
            'AR': {
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
                'base.res_partner_1': 'l10n_ar.res_partner_foreign',
                # Joel Willis mappeamos a Gritti
                'base.partner_demo_portal': 'l10n_ar.res_partner_gritti_agrimensura',
            },
            'UY': {
                # Ready Mat a Foreign Inc
                'base.res_partner_4': 'l10n_uy_account.res_partner_foreign',
                # Deco Addict mappeamos a Consumidor final uruguayo
                'base.res_partner_2': 'l10n_uy_account.partner_cfu',
                # Gemmini Furniture mappeamos a IEB
                'base.res_partner_3': 'l10n_uy_account.demo_partner_4',
                # Lumber Inc mappeamos a Meli
                'base.res_partner_18': 'l10n_uy_account.demo_partner_5',
                # Azure mappeamos a Cerro Castor
                'base.res_partner_12': 'l10n_uy_account.demo_partner_6',
                # Wood Corner mappeamos a Foreign Inc
                'base.res_partner_1': 'l10n_uy_account.res_partner_foreign',
                # Joel Willis mappeamos a Consumidor final uruguayo
                'base.partner_demo_portal': 'l10n_uy_account.partner_cfu',
            },
            'CL': {
                # Ready Mat a ready Mat (seria el foreign de chile que no esta creado, por ahora lo mapeamos a si mismo)
                'base.res_partner_4': 'base.res_partner_4',
                # Deco Addict mappeamos a Blanco Martin
                'base.res_partner_2': 'l10n_cl.res_partner_bmya',
                # Gemmini Furniture mappeamos a Blanco Martin
                'base.res_partner_3': 'l10n_cl.res_partner_bmya',
                # Lumber Inc mappeamos a Meli
                'base.res_partner_18': 'l10n_cl.res_partner_teksa',
                # Azure mappeamos a Cerro Castor
                'base.res_partner_12': 'l10n_uy_account.demo_partner_6',
                # Ready Mat a ready Mat (seria el foreign de chile que no esta creado)
                'base.res_partner_1': 'l10n_cl.res_partner_teksa',
                # Joel Willis mappeamos a Consumidor final uruguayo
                'base.partner_demo_portal': 'l10n_cl.res_partner_bmya',
            },
            'ES': {
                #Por ahora mapeamos todos asi mismos para que no de los Warning
                # Ready Mat a ready Mat
                'base.res_partner_4': 'base.res_partner_4',
                # Deco Addict mappeamos a Deco Addict
                'base.res_partner_2': 'base.res_partner_2',
                # Gemmini Furniture mappeamos a Gemmini Furniture
                'base.res_partner_3': 'base.res_partner_3',
                # Lumber Inc mappeamos a Lumber
                'base.res_partner_18': 'base.res_partner_18',
                # Azure mappeamos a Azure
                'base.res_partner_12': 'base.res_partner_12',
                # Ready Mat a ready Mat 
                'base.res_partner_1': 'base.res_partner_1',
                # Joel Willis mappeamos a Joel Willis
                'base.partner_demo_portal': 'base.partner_demo_portal',
            },
            'PE': {
                #Por ahora mapeamos todos asi mismos para que no de los Warning
                # Ready Mat a ready Mat
                'base.res_partner_4': 'base.res_partner_4',
                # Deco Addict mappeamos a Deco Addict
                'base.res_partner_2': 'base.res_partner_2',
                # Gemmini Furniture mappeamos a Gemmini Furniture
                'base.res_partner_3': 'base.res_partner_3',
                # Lumber Inc mappeamos a Lumber
                'base.res_partner_18': 'base.res_partner_18',
                # Azure mappeamos a Azure
                'base.res_partner_12': 'base.res_partner_12',
                # Ready Mat a ready Mat 
                'base.res_partner_1': 'base.res_partner_1',
                # Joel Willis mappeamos a Joel Willis
                'base.partner_demo_portal': 'base.partner_demo_portal',
            },
        }
        return self._get_partner(mapping.get(company.country_id.code, {}))

    def _get_partner(self, mapping):
        self.ensure_one()
        external_id = self.get_external_id()
        if not external_id:
            _logger.warning('No hay external id para partner %s', self.name)
            return self
        xmlid = mapping.get(list(external_id.values())[0])
        if not xmlid:
            _logger.info('No se encontró external id en mapping para partner %s', self.name)
            return self
        new_partner = self.env.ref(xmlid)
        if not new_partner:
            _logger.warning('No encontramos partner para %s', external_id)
            return self

        return new_partner
