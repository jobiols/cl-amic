# For copyright and license notices, see __manifest__.py file in module root
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):

    _logger.info('FIX production corruption')
    cr.execute("""
    update stock_move
    set product_qty = 1,
    product_id = 226
    where id = 8936
    """)
    cr.execute("""
    update stock_move
    set product_qty = 5,
        product_id = 226
    where id = 8929
    """)
