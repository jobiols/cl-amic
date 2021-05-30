from openupgradelib import openupgrade
import logging

_logger = logging.getLogger(__name__)

@openupgrade.migrate(use_env=True)
def migrate(env, version):
    """ Revisar los campos inspector_id y responsible_id porque estamos cambiandole
        el modelo de referencia
    """
    issues = env['qc.issue'].search([])
    for issue in issues:
        issue.inspector_id = False
        _logger.info("Change Issue inspector_id %s", issue.name)
