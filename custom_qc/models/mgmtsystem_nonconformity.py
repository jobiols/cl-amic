from odoo import models, fields, api


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

    @api.model
    def create(self, vals):
        """ el partner_id es requerido en el modelo asi que el pongo el admin para que
            me deje pasar.
        """
        vals['partner_id'] = 1
        return super(MgmtsystemNonconformity, self).create(vals)
