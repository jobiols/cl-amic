from openerp import models, fields


class QcIssueForm(models.Model):
    _inherit = "qc.issue"

    workcenter_1_id = fields.Many2one(
        'mrp.workcenter',
    )
    workcenter_2_id = fields.Many2one(
        'mrp.workcenter',
    )
    workcenter_3_id = fields.Many2one(
        'mrp.workcenter',
    )
    issue_date = fields.Date(

    )
