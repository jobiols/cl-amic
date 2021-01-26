# For copyright and license notices, see __manifest__.py file in module root
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):

# En product_product hay un id = 224 que no se puede borrar y genera esto
# Buscar en stock_move name = 'MOxxx'

    _logger.info('FIX production corruption')
    cr.execute("""
    update stock_move
    set product_qty = 1,
    product_id = 226
    where id = 9323
    """)
