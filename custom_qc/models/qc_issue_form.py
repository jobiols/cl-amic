from openerp import models, fields


class QcIssueForm(models.Model):
    _inherit = "qc.issue"

    workcenter_id = fields.Many2one(
        'mrp.workcenter'
    )
