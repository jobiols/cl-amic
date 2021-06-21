from odoo import tools
from odoo import api, fields, models


class MrpWorkorderReport(models.Model):
    _name = "mrp.workorder.report"
    _description = "Volumen y Kilogramos Cortados PIVOT"
    _auto = False
    _rec_name = 'ot'

    ot = fields.Char(
        readonly=True,
        string="Orden de Trabajo"
    )
    wo = fields.Char(
        readonly=True,
        string="Orden de Producción"
    )
    operation = fields.Char(
        readonly=True,
        string="Operación"
    )
    workcenter = fields.Char(
        readonly=True,
        string="Centro de Producción"
    )
    product = fields.Char(
        readonly=True,
        string="Producto"
    )
    product_uom = fields.Char(
        readonly=True,
        string="Unidad de Medida"
    )
    date_planned_start = fields.Char(
        readonly=True,
        string="Fecha de comienzo programada"
    )
    date_planned_finished = fields.Char(
        readonly=True,
        string="Fecha de Finalización programada"
    )
    date_start = fields.Date(
        readonly=True,
        string="Fecha inicio de efectividad"
    )
    date_finished = fields.Char(
        readonly=True,
        string="Fecha final de efectividad"
    )

    date_start1 = fields.Char(
        readonly=True,
    )
    date_end1 = fields.Char(
        readonly=True,
    )
    time_start = fields.Char(
        readonly=True,
        string="Hora Inicial"
    )
    time_end = fields.Char(
        readonly=True,
        string="Hora Final"
    )
    create_date = fields.Char(
        readonly=True,
        string="Fecha Creación"
    )
    create_uid = fields.Char(
        readonly=True,
        string="Creado por"
    )


    qty_producing = fields.Float(
        readonly=True,
        string="Cantidad a producir"
    )
    qty_produced = fields.Float(
        readonly=True,
        string="Cantidad Producida"
    )

    def _select(self):
        select_str = """
            wo.id,
            pro.ot,
            pro.name as wo,
            wo.name as operation,
            '[' || wc.code || '] ' || wc.name as workcenter,
            '[' || pt.default_code || '] ' || pt.name as product,
            pu.name as product_uom,

            wo.date_planned_start,
            wo.date_planned_finished,

            wo.date_start::date ,
            wo.date_finished,

            wo.date_start1,
            wo.date_end1,

            wo.time_start,
            wo.time_end,

            wo.create_date,
            rp.name as create_uid,

            wo.qty_producing,
            wo.qty_produced

        """
        return select_str

    def _from(self):
        from_str = """
            mrp_workorder wo

            JOIN mrp_production pro
            ON wo.production_id = pro.id

            JOIN mrp_workcenter wc
            ON wo.workcenter_id = wc.id

            JOIN product_template pt
            ON wo.product_id = pt.id

            JOIN product_uom pu
            ON pro.product_uom_id = pu.id

            JOIN res_users ru
            ON wo.create_uid = ru.id

            JOIN res_partner rp
            ON ru.partner_id = rp.id
        """
        return from_str

    def _group_by(self):
        group_by_str = ""
        return group_by_str

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        query = "CREATE or REPLACE VIEW %s as (SELECT %s FROM %s %s)"
        self.env.cr.execute(query % (
            self._table,
            self._select(),
            self._from(),
            self._group_by()
            )
        )
