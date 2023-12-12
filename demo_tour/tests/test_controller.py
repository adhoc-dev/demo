# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestSaleSignature(HttpCase):

    def test_01_portal_sale_signature_tour(self):
        self.start_tour("/web", 'demo_tour.sale', login="admin")

    def test_02_multicompany(self):
        self.start_tour("/web", 'demo_tour.multicompany', login="admin")

    def test_03_ganancias(self):
        self.start_tour("/web", 'demo_tour.ganancias', login="admin")
