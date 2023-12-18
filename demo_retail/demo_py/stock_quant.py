from odoo import api, models


class StockQuant(models.Model):

    _inherit = 'stock.quant'

    @api.model
    def _init_demo_retail(self):
        """ En este metodo tratamos de duplicar todos los quants que odoo genera para dar de alta inventario en este
        archivo https://github.com/odoo/odoo/blob/16.0/addons/stock/data/stock_demo.xml#L32-L128
        Duplicamos esos quants y los mandamos a la location de stock de cada almacen.
        Eventualmente podemos ver de en vez de hacerlo así duplicar la data xml cambiando el warehouse/location
        """
        # cl
        cl_c = self.env.ref('l10n_cl.demo_company_cl')
        # uy
        uy_c = self.env.ref('l10n_uy_account.company_uy')
        # ar (ri, muebleria)
        ar_c = self.env.ref('l10n_ar.company_ri')
        # us (main_company)
        us_c = self.env.ref('base.main_company')

        # Obtener la ubicación de stock principal del almacén predeterminado (warehouse0)
        main_warehouse_stock_location = self.env.ref('stock.warehouse0').lot_stock_id.id
        for company in ar_c + uy_c + cl_c:
            new_warehouse_stock_location = self.env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1).lot_stock_id
            if not new_warehouse_stock_location:
                continue
            for quant in self.env['stock.quant'].search([('location_id', '=', main_warehouse_stock_location)]):
                new_defaults = {}
                if quant.lot_id:
                    new_defaults['lot_id'] = quant.lot_id.copy({'company_id':company.id, 'name': quant.lot_id.name+'1'}).id
                new = quant.with_company(company).copy(new_defaults)
                vals = {'location_id': new_warehouse_stock_location.id}
                new.write(vals)
                new.action_apply_inventory()

