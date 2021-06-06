from openupgradelib import openupgrade
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):
    """ corregir corrupcion
    """
    cr.execute("""
    -- Corregir el inspector1_id
    UPDATE qc_issue
    SET
        inspector1_id = 8;
    """)

    cr.execute("""
    -- Corregir el responsible1_id
    UPDATE qc_issue
    SET
        inspector1_id = 20,
        responsible1_id = 5
    where id in (330, 332);
    """)
