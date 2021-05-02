from odoo import tools
from odoo import api, fields, models


class SaleReport(models.Model):
    _name = "sale.order.lines.report"
    _description = "Sales Orders Lines Report"
    _auto = False
    _rec_name = 'name'
    _order = 'requested_date desc'

    name = fields.Char(readonly=True)
    requested_date = fields.Date(readonly=True)
    partner_name = fields.Char(readonly=True)
    state = fields.Char(readonly=True)
    default_code = fields.Char(readonly=True)
    product_name = fields.Char(readonly=True)
    sol_name = fields.Char(readonly=True)
    quantity = fields.Float(readonly=True)
    delivered = fields.Float(readonly=True)
    price_unit = fields.Float(readonly=True)
    currency = fields.Char(readonly=True)
    uom = fields.Char(readonly=True)
    uom_factor = fields.Float(readonly=True)
    uom_factor_inv = fields.Float(readonly=True, compute="_compute_uom_factor_inv")
    create_date = fields.Date(readonly=True)

    def _compute_uom_factor_inv(self):
        for rec in self:
            rec.uom_factor_inv = 1/rec.uom_factor if rec.uom_factor != 0 else 0

    def _select(self):
        select_str = """
            SELECT  sol.id,
                    so.name,
                    so.requested_date,
                    rp.name as partner_name,
                    sol.state,
                    pp.default_code,
                    pt.name as product_name,
                    sol.name as sol_name,
                    sol.product_uom_qty as quantity,
                    sol.qty_delivered as delivered,
                    sol.price_unit,
                    rc.name as currency,
                    pu.name as uom,
                    pu.factor as uom_factor,
                    sol.create_date
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
