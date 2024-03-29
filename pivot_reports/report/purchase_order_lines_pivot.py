from odoo import tools
from odoo import api, fields, models


class SaleReport(models.Model):
    _name = "purchase.order.lines.report"
    _description = "Recibidas Versus Compradas"
    _auto = False
    _rec_name = 'name'
    #_order = 'requested_date desc'

    name = fields.Char(
        readonly=True,
        string="Referencia del pedido"
    )
    origin = fields.Char(
        readonly=True,
        string="Documento Origen"
    )
    id_line = fields.Integer(
        readonly=True,
        string="ID"
    )
    default_code = fields.Char(
        readonly=True,
        string="Prod. Referencia interna"
    )
    date_order = fields.Date(
        readonly=True,
        string="Fecha de Pedido"
    )
    date_planned = fields.Date(
        readonly=True,
        string="Fecha Prevista"
    )
    contact_name = fields.Char(
        readonly=True,
        string="proveedor"
    )
    description = fields.Char(
        readonly=True,
        string="Producto descripción"
    )
    product_qty = fields.Integer(
        readonly=True,
        string="Cant. Pedida"
    )
    qty_received = fields.Integer(
        readonly=True,
        string="Ctdad recibida"
    )
    uom = fields.Char(
        readonly=True,
        string="UdM"
    )
    currency = fields.Char(
        readonly=True,
        string="Moneda"
    )
    price_unit = fields.Float(
        readonly=True,
        string="Precio Unitario"
    )

    price_unit_ars = fields.Float(
        readonly=True,
        string="Precio unitario en pesos"
    )
    price_unit_usd = fields.Float(
        readonly=True,
        string="Precio unitario en dolares"
    )
    price_unit_eur = fields.Float(
        readonly=True,
        string="Precio unitario en euros"
    )

    price_subtotal = fields.Float(
        readonly=True,
        string="Subtotal"
    )
    price_total = fields.Float(
        readonly=True,
        string="Total"
    )
    create_date = fields.Date(
        readonly=True,
        string="Creado el"
    )
    write_date = fields.Date(
        readonly=True,
        string="Modificado el"
    )
    write_usr = fields.Char(
        readonly=True,
        string="Modificado por"
    )
    warehouse = fields.Char(
        readonly=True,
        string="Almacen"
    )
    income_cost_usd = fields.Float(
        readonly=True,
        string="Costo recibido USD"
    )
    income_cost_eur = fields.Float(
        readonly=True,
        string="Costo recibido EUR"
    )
    income_cost_ars = fields.Float(
        readonly=True,
        string="Costo recibido ARS"
    )

    def _select(self):
        select_str = """
            SELECT  pol.id,
                    po.name,
                    po.origin,
                    pol.id as id_line,
                    pt.default_code,
                    po.date_order::timestamp::date,
                    po.date_planned::timestamp::date,
                    rp.name
                        as contact_name,
                    pol.name
                        as description,
                    pol.product_qty,
                    pol.qty_received,
                    rp2.name
                        as warehouse,
                    pu.name
                        as uom,
                    rc.name
                        as currency,
                    pol.price_unit,

                    (CASE WHEN rc.name = 'ARS'
                        THEN pol.price_unit * pol.qty_received
                        ELSE NULL
                     END)
                        as income_cost_ars,

                    (CASE WHEN rc.name = 'USD'
                        THEN pol.price_unit * pol.qty_received
                        ELSE NULL
                     END)
                        as income_cost_usd,

                    (CASE WHEN rc.name = 'EUR'
                        THEN pol.price_unit * pol.qty_received
                        ELSE NULL
                     END)
                        as income_cost_eur,

                    (CASE WHEN rc.name = 'ARS'
                        THEN pol.price_unit
                        ELSE NULL
                     END)
                        as price_unit_ars,

                    (CASE WHEN rc.name = 'USD'
                        THEN pol.price_unit
                        ELSE NULL
                     END)
                        as price_unit_usd,

                    (CASE WHEN rc.name = 'EUR'
                        THEN pol.price_unit
                        ELSE NULL
                     END)
                        as price_unit_eur,

                    pol.price_subtotal,
                    pol.price_total,
                    pol.create_date::timestamp::date,
                    pol.write_date::timestamp::date,
                    rp1.name as write_usr
        """
        return select_str

    def _from(self):
        from_str = """
            purchase_order po

            JOIN purchase_order_line pol
            ON pol.order_id = po.id

            JOIN res_partner rp
            ON pol.partner_id = rp.id

            JOIN product_uom pu
            ON pol.product_uom = pu.id

            JOIN res_currency rc
            ON pol.currency_id = rc.id

            JOIN res_users ru
            ON pol.write_uid = ru.id

            JOIN res_partner rp1
            ON ru.partner_id = rp1.id

            JOIN product_product pp
            ON pol.product_id = pp.id

            JOIN product_template pt
            ON pp.product_tmpl_id = pt.id

            JOIN stock_picking_type spt
            ON po.picking_type_id = spt.id

            JOIN stock_warehouse sw
            ON spt.warehouse_id = sw.id

            JOIN res_partner rp2
            ON sw.partner_id = rp2.id

        """
        return from_str

    def _group_by(self):
        group_by_str = ""
        return group_by_str

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s FROM %s %s )
            """ % (self._table, self._select(), self._from(), self._group_by())
        )
