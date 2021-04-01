# For copyright and license notices, see __manifest__.py file in module root
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):
    # Volvio a aparecer la misma de la migracion anterior donde el lote M0000133/B10
    # borro los lotes y dejo solo en del ubicaciones virtuales / produccion

    # select name, sq.id,* from stock_quant sq
    # JOIN stock_production_lot spl
    # ON sq.lot_id = spl.id
    # where name = 'M0000133/B10'
    _logger.info('Delete quants')
    cr.execute("""
        delete from stock_quant
        where id in (5730,7030)
    """)

    # En Inventario aparece en Chubut Idm139 lote M0000149/B3 Con stock 0 pero
    # reservado 38,55kg ¿ tiene arreglo?
    _logger.info('Delete quants')
    cr.execute("""
        delete from stock_quant
        where id in (2594)
    """)

# aca hubo que buscarlo por el id porque el nombre tenia un espacio al final
# select sq.id, spl.name, reserved_quantity, * from stock_quant sq
# JOIN stock_production_lot spl
# ON sq.lot_id = spl.id
# JOIN stock_location sl
# ON sl.id = sq.location_id
# where sq.lot_id = 96

# 2 lotes de idm117 en Chous/stock con reservado 1379 y 1891 kgs reservados y 0 a man
# lotes 64182/131032 136736/67875

    _logger.info('Delete quants')
    cr.execute("""
        delete from stock_quant
        where id in (188,3135)
    """)
