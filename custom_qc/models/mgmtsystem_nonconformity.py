from odoo import models, fields


class MgmtsystemNonconformity(models.Model):

    _inherit = "mgmtsystem.nonconformity"

    issue_id = fields.Many2one(
        'qc.issue'
    )
    operator_id = fields.Many2one(
        'hr.employee',
        help='Operador que esta a cargo de la producción',
        string="Operador"
    )
