from openerp import models, fields, api, _


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
    issue_ids = fields.One2many(
        'mgmtsystem.nonconformity',
        'issue_id',
        'Nonconformity'
    )
    determination = fields.Selection(
        [
            ('desvio', 'Desvío'),
            ('retrabajo', 'Retrabajo'),
            ('scrap', 'Scrap'),
        ],
        string="Determinación"
    )

    @api.multi
    def create_nonconformity(self, **kwargs):
        """
        Opens nonconformity form view prefilled with inspection data
        """
        partner = False

        tmp_form_name = "mgmtsystem_nonconformity.view_mgmtsystem_nonconformity_form"
        return {
            # opens nonconformity form view
            'name'      : _('Create Nonconformity on not compliant Inspection'),
            'view_type' : 'form',
            'view_mode' : 'form',
            'res_model' : 'mgmtsystem.nonconformity',
            'view_id'   : self.env.ref(tmp_form_name).id,
            'type'      : 'ir.actions.act_window',

            # fills fields with inspection data
            'context': {
                'default_name'          : _('Issue not compliant'),
                'default_product_id'    : self.product_id.id,
                'default_partner_id'    : partner,
                'default_qty_checked'   : 0, # self.qty_checked,
                'default_issue_id' : self.id
            },

            'target': 'new'
        }
