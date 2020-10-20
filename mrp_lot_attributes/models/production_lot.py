# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _


class ProductionLot(models.Model):
    _inherit = "stock.production.lot"

    colada = fields.Char(
        string='COLADA'
    )
    tt = fields.Char(
        string='TT',
        help='Tratamiento Termico'
    )
    paquete = fields.Char(
        string='PAQUETE'
    )
    ot = fields.Char(
        string='OT',
        help='Orden de Trabajo'
    )
    remito_proveedor = fields.Char(
        string='Remito Proveedor'
    )
    fecha_remito = fields.Date(
    )
    aceria = fields.Char(
        string='Proveedor'
    )
    unit_lot_weight = fields.Float(
        help="Peso unitario de los productos del lote en Kg.",
        readonly=True,
        string='Peso del producto',
        compute="_compute_unit_lot_weight"
    )
    produced_lot_weight = fields.Float(
        help="Peso unitario del producto calculado en produccion, como la suma"
             "de los pesos de los componentes"
    )
    done = fields.Boolean(
        string='Terminado',
        help='Marca que este lote esta terminado y no debe mostrarse en '
             'fabricacion al elegir lotes para los componentes.'
    )
    invisible = fields.Boolean(
        help="Campo tecnico para definir si el lote es visible o no al seleccionarlo",
        compute="_compute_invisible",
        store=True
    )

    @api.multi
    @api.onchange('product_qty','done')
    def _compute_invisible(self):
        for rec in self:
            rec.invisible = rec.product_qty <= 0 or rec.done

    @api.onchange('tt')
    def check_tt(self):
        for rec in self:
            if rec.tt:
                stock_obj = self.env['stock.production.lot']
                chk = stock_obj.search([('tt', '=', rec.tt)])
                if chk:
                    names = chk.mapped('name')
                    names = ', '.join(names)
                    msg = _('El numero de TT que acaba de ingresar ya existe '
                            'en el lote %s, no deberian existir numeros de TT '
                            'duplicados') % names
                    mess = {
                        'title': _('TT Duplicado'),
                        'message': msg
                    }
                    return {'warning': mess}

    @api.multi
    def get_attributes(self, prod=False, internal=True):
        for rec in self:
            ret = []
            if rec.ot and \
                (internal or (prod and prod.att_ot)):
                ret.append(rec.ot)
            if rec.aceria and \
                (internal or (prod and prod.att_aceria)):
                ret.append('Proveedor=%s' % rec.aceria)
            if rec.colada and \
                (internal or (prod and prod.att_colada)):
                ret.append('Colada=%s' % rec.colada)
            if rec.paquete and \
                (internal or (prod and prod.att_paquete)):
                ret.append('Paquete=%s' % rec.paquete)
            if rec.tt and \
                (internal or (prod and prod.att_tt)):
                ret.append('TT=%s' % rec.tt)
            if rec.remito_proveedor and \
                (internal or (prod and prod.att_remito_proveedor)):
                ret.append('Remito: %s' % rec.remito_proveedor)
            if rec.fecha_remito and \
                (internal or (prod and prod.att_fecha_remito)):
                ret.append('Fecha Remito: %s' % rec.fecha_remito)
            return '(%s)' % ', '.join(ret) if ret else ""

    def _compute_unit_lot_weight(self):
        for rec in self:
            if rec.product_id.weight:
                # si el producto tiene peso distinto de cero el peso es el
                # declarado en el producto
                rec.unit_lot_weight = rec.product_id.weight
            else:
                # si el producto no tiene peso declarado se toma el peso
                # unitario calculado al fabricar el producto
                rec.unit_lot_weight = rec.produced_lot_weight

    def propagate_from(self, parent_lot):
        """ Mover los atributos de un lote a otro teniendo en cuenta que si
            ya existe no lo tengo que copiar.
        """

        def propagate_attr(source, dest):

            # no hay nada, escribo False en el atributo
            if not dest and not source:
                return False

            # hay algo en el lote origen y nada en el destino escribo origen
            if not dest and source:
                return source

            # hay algo en el lote destino y nada en el origen, no lo toco
            if dest and not source:
                return dest

            # hay cosas en los dos lotes, si en el atributo destino no esta el
            # atributo origen, si esta no toco el destino.
            if dest.find(source) == -1:
                return dest + ', ' + source
            else:
                return dest

        self.ot = propagate_attr(parent_lot.ot, self.ot)
        self.tt = propagate_attr(parent_lot.tt, self.tt)
        self.colada = propagate_attr(parent_lot.colada, self.colada)
        self.paquete = propagate_attr(parent_lot.paquete, self.paquete)
        self.remito_proveedor = propagate_attr(parent_lot.remito_proveedor,
                                               self.remito_proveedor)
        self.fecha_remito = propagate_attr(parent_lot.fecha_remito,
                                           self.fecha_remito)
        self.aceria = propagate_attr(parent_lot.aceria, self.aceria)
