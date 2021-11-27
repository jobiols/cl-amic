# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class your_model(models.Model):
    _inherit = 'stock.move'

    order_ref = fields.Many2many(
        comodel_name='sale.order',
        relation='account_move_line_ids_rel',
        string="Sale Order ref",
        compute='_compute_sale_order'
    )


    @api.multi
    @api.depends('order_ref')
    def _compute_sale_order(self):
        for rec in self:
            account_move_lines_domain = [
                ('name','=', rec.origin),
            ]
            account_move_lines = rec.env['sale.order'].search(
                account_move_lines_domain
            )
            rec.order_ref = account_move_lines