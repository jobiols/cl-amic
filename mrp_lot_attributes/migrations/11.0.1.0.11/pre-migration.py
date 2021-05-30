# For copyright and license notices, see __manifest__.py file in module root
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):
    # El lote aparece con cantidad reservada lo cual no tiene sentido,
    # la forzamos a cero.

    # select name, sq.id,* from stock_quant sq
    # JOIN stock_production_lot spl
    # ON sq.lot_id = spl.id
    # where name = 'M0000055/B13-Q';
    _logger.info('Delete quants')
    cr.execute("""
        update stock_quant
        set reserved_quantity = 0
        where id = 111;
    """)
