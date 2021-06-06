from openupgradelib import openupgrade
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):
    """ corregir corrupcion
    """
    cr.execute("""
    -- Corregir el inspector_id y responsible_id que ya no se usaran
    UPDATE qc_issue
    SET
        inspector_id = 44,
        responsible_id = NULL
    """)
