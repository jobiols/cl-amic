from openupgradelib import openupgrade
import logging

_logger = logging.getLogger(__name__)

@openupgrade.migrate(use_env=True)
def migrate(env, version):
    """ Cambiar el estado done --> progress
    """
    issues = env['qc.issue'].search([('state', '=', 'done')])
    for issue in issues:
        issue.state = 'progress'
        _logger.info("Change Issue state %s", issue.name)
