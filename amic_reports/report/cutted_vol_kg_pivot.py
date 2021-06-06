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

    def _select(self):
        select_str = """
            SELECT  wo.id,
                    pro.ot
        """
        return select_str

    def _from(self):
        from_str = """
            mrp_workorder wo

            JOIN mrp_production pro
            on wo.production_id = pro.id
        """
        return from_str

    def _group_by(self):
        group_by_str = ""
        return group_by_str

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        query = "CREATE or REPLACE VIEW %s as (%s FROM %s %s)"
        self.env.cr.execute(query % (
            self._table,
            self._select(),
            self._from(),
            self._group_by()
            )
        )
