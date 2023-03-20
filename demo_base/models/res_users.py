from odoo import api, models


class ResUsers(models.Model):

    _inherit = 'res.users'

    @api.model
    def _init_demo_data(self):
        # groups by settings
        for group_xml_id in [
                # 'account.group_show_line_subtotals_tax_excluded',
                'crm.group_use_lead',
                'product.group_discount_per_so_line',
                'product.group_product_pricelist',
                'product.group_product_variant',
                'sale.group_delivery_invoice_address',]:
            group = self.env.ref(group_xml_id, False)
            if group:
                self.env.ref('base.group_user').write({'implied_ids': [(4, group.id)]})

        for group_xml_id in [
                # 'account.group_show_line_subtotals_tax_included'
                'purchase.group_send_reminder',]:
            group = self.env.ref(group_xml_id, False)
            if group:
                self.env.ref('base.group_user').write({'implied_ids': [(3, group.id)]})

        # creamos usuario igual a admin pero con compañías determinadas
        if not self.search([('login', '=', 'demo_admin')]):
            user = self.env.ref('base.user_admin').copy({
                'name': 'Valentino',
                'email': 'valentino@fabricademueblessa.com',
                'login': 'demo_admin',
                'password': 'demo_admin',
                'active': True,
            })
            user.write({
                'company_ids': [
                    (3, self.env.ref('l10n_ar.company_ri').id, 0),
                    (3, self.env.ref('l10n_ar.company_mono').id, 0),
                    (3, self.env.ref('l10n_ar.company_exento').id, 0)],
                'company_id': self.env.ref('demo_base.company_muebleria_sa').id
            })
            for group_xml_id in [
                'analytic.group_analytic_tags',
                'product.group_sale_pricelist',
                'saas_client_adhoc.group_hidden_resources',
                'uom.group_uom']:
                group = self.env.ref(group_xml_id, False)
                if group:
                    user.write({'groups_id': [(4, group.id)]})

