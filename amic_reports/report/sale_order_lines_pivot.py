from odoo import tools
from odoo import api, fields, models


class SaleReport(models.Model):
    _name = "sale.order.lines.report"
    _description = "Sales Orders Lines Report"
    _auto = False
    _rec_name = 'name'
    _order = 'requested_date desc'

    name = fields.Char(
        readonly=True,
        string="Pedido"
    )
    requested_date = fields.Date(
        readonly=True,
        string="Fecha Solicitada"
    )
    partner_name = fields.Char(
        readonly=True,
        string="Cliente"
    )
    state = fields.Char(
        readonly=True,
        string="Estado del pedido"
    )
    default_code = fields.Char(
        readonly=True,
        string="Prod. Referencia interna"
    )
    product_name = fields.Char(
        readonly=True,
        string="Prod. Nombre"
    )
    sol_name = fields.Char(
        readonly=True,
        string="Prod. Referencia y nombre"
    )
    quantity = fields.Float(
        readonly=True,
        string="Cantidad Vendida"
    )
    delivered = fields.Float(
        readonly=True,
        string="Cantidad Entregada"
    )
    price_unit = fields.Float(
        readonly=True,
        string="Precio por unidad"
    )
    currency = fields.Char(
        readonly=True,
        string="Moneda"
    )
    uom = fields.Char(
        readonly=True,
        string="UdM nombre"
    )
    uom_factor = fields.Float(
        readonly=True,
        string="UdM Relación"
    )
    create_date = fields.Date(
        readonly=True,
        string="Fecha de creación"
    )
    create_user = fields.Char(
        readonly=True,
        string="Creado por"
    )

    # Campos calculados
    programmed_units_qty = fields.Integer(
        readonly=True,
        string="Cantidad de Unidades Programadas",
    )
    pending_units_qty = fields.Integer(
        readonly=True,
        string="Cantidad de Unidades Pendientes de Entrega",
    )
    dispatched_qty = fields.Integer(
        readonly=True,
        string="Cantidad de Unidades Despachadas",
    )
    invoiced_usd = fields.Monetary(
        readonly=True,
        string="Facturación USD",
        currency_field='usd_currency_id'
    )
    invoiced_ars = fields.Monetary(
        readonly=True,
        string="Facturación ARS",
        currency_field='ars_currency_id'
    )
    usd_currency_id = fields.Many2one(
        'res.currency',
        readonly=True,
    )
    ars_currency_id = fields.Many2one(
        'res.currency',
        readonly=True,
    )
    def _select(self):
        select_str = """
            SELECT  sol.id,
                    so.name,
                    so.requested_date::timestamp::date,
                    rp.name as partner_name,
                    sol.state,
                    pp.default_code,
                    pt.name as product_name,
                    sol.name
                        as sol_name,
                    sol.product_uom_qty
                        as quantity,
                    sol.qty_delivered
                        as delivered,
                    sol.price_unit,
                    rc.name
                        as currency,
                    pu.name
                        as uom,
                    1/pu.factor
                        as uom_factor,
                    sol.create_date::timestamp::date,
                    rp1.name
                        as create_user,
                    3 as usd_currency_id,
                    20 as ars_currency_id,
                    (CASE WHEN rc.name = 'ARS'
                          THEN sol.product_uom_qty * sol.price_unit / pu.factor
                          ELSE NULL
                     END)
                        as invoiced_ars,
                    (CASE WHEN rc.name = 'USD'
                          THEN sol.product_uom_qty * sol.price_unit / pu.factor
                          ELSE NULL
                     END)
                        as invoiced_usd,

                    sol.qty_delivered / pu.factor
                        as dispatched_qty,

                    (sol.product_uom_qty - sol.qty_delivered) / pu.factor
                        as pending_units_qty,

                    sol.product_uom_qty / pu.factor
                        as programmed_units_qty
        """
        return select_str

    def _from(self):
        from_str = """
            sale_order_line sol

            JOIN sale_order so
            ON sol.order_id = so.id

            JOIN res_partner rp
            ON sol.order_partner_id = rp.id

            JOIN product_product pp
            ON sol.product_id = pp.id

            JOIN product_template pt
            ON pp.product_tmpl_id = pt.id

            JOIN res_currency rc
            ON sol.currency_id = rc.id

            JOIN product_uom pu
            ON sol.product_uom = pu.id

            JOIN res_users ru
            ON sol.create_uid = ru.id

            JOIN res_partner rp1
            ON ru.partner_id = rp1.id
        """
        return from_str

    def _group_by(self):
        group_by_str = ""
        return group_by_str

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            FROM %s
            %s )
            """ % (self._table, self._select(), self._from(), self._group_by())
        )
