# Copyright 2019 jeo Software
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Custom QC',
    'summary': 'Customizacion del control del calidad',
    'version': '11.0.1.0.0',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'category': 'Tools',
    'website': 'http://jeosoft.com.ar',
    'author': 'jeo Software',
    'maintainers': ['jobiols'],
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'quality_control_issue',
        'mgmtsystem',
        'mgmtsystem_nonconformity',
    ],
    'data': [
        'views/qc_issue_form_view.xml'
    ],
}
