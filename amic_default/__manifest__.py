# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'AMIC',
    'version': '11.0.0.0.3',
    'license': 'Other OSI approved licence',
    'category': 'Default Application',
    'summary': 'Customization for AMIC',
    "development_status": "Alpha",
    'author': 'jeo Software',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',
        'mrp',

        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ce',

        # utilitarios adicionales
        'backend_theme_v11',

        # desarrollo especifico para amic
        'customer_product_names',  # nombres de prod <> por cliente
        'mrp_lot_attributes'  # caracteristicas de trazabilidad
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    # port where odoo starts serving pages
    'port': '8069',

    # example repos version 1
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-amic', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},

        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools',
         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting',
         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '11.0'},

        {'usr': 'oca', 'repo': 'partner-contact', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'web', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-tools', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'social', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-ux', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-brand', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'manufacture', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'management-system', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '11.0'},

    ],

    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '11.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ],

}
