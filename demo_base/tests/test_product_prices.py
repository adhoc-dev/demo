from datetime import datetime
import time

from odoo.tests import tagged
from odoo.fields import Command, first
from odoo.tools import float_compare

from odoo.addons.product.tests.common import ProductCommon



class TestProductPrices(ProductCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product.write({
            'taxes_id': cls.env['account.tax'].search([('type_tax_use', '=', 'sale'), ('company_id', '=', cls.env.company.id)]),
        })

        cls.pricelist_pricelist = cls.env['product.pricelist'].create({
            'name': 'Pricelist based on pricelist',
            'item_ids': [
                Command.create({
                    'compute_price': 'formula',
                    'base': 'pricelist',  # based on pricelist
                    'base_pricelist_id': cls.pricelist.id,
                    'price_discount': -100,
                    'price_surcharge': 10,
                    'product_id': cls.product.id,
                    'applied_on': '0_product_variant',
                }),
            ],
        })

    def test_product_price(self):
        product_price = self.pricelist._get_product_price(self.product, 1.0)
        product_price_with_taxes = self.product.taxes_id \
            .filtered(lambda x, company=self.env.company: x.company_id == company) \
            .compute_all(product_price, product=self.product)['total_included']

        self.assertEqual(
            self.pricelist.with_context({'taxes_included':True})._get_product_price(self.product, 1.0),
            product_price_with_taxes
        )
        self.assertEqual(
            self.product.taxed_lst_price,
            product_price_with_taxes
        )

        product_price = self.pricelist_pricelist._get_product_price(self.product, 1.0)
        product_price_with_taxes = self.product.taxes_id \
            .filtered(lambda x, company=self.env.company: x.company_id == company) \
            .compute_all(product_price, product=self.product)['total_included']

        self.assertEqual(
            self.pricelist_pricelist.with_context({'taxes_included':True})._get_product_price(self.product, 1.0),
            product_price_with_taxes
        )
        self.assertEqual(
            self.product.taxed_lst_price,
            product_price_with_taxes
        )
