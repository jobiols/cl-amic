from odoo import models, fields


class MgmtsystemNonconformity(models.Model):

    _inherit = "mgmtsystem.nonconformity"

    issue_id = fields.Many2one(
        'qc.issue'
    )
