# For copyright and license notices, see __manifest__.py file in module root
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):

    # apareció una corrupcion donde el lote M0000133/B10 aparecia duplicado y con un
    # producto Idm004 que no era el correcto el correcto es Idm140
    # Sospechamos que se creo porque hicieron un ajuste de inventario sin lote.

    _logger.info('Delete quant')
    cr.execute("""
        delete from stock_quant
        where id=5729
    """)
