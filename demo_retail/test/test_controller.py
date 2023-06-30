# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestSaleSignature(HttpCase):

    def test_01_portal_sale_signature_tour(self):
        self.start_tour("/web", 'retail_tour.sale', login="admin")
