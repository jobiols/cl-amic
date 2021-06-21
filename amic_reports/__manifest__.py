# -----------------------------------------------------------------------------
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
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
    'name': 'Amic PIVOT Reports',
    'version': '11.0.1.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Reports',
    'summary': 'Reportes customizados para AMIC',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'author': 'jeo Software',
    'depends': [
        'mrp'
    ],
    'data': [
        'report/sale_order_lines_view.xml',
        'report/purchase_order_lines_view.xml',
        'report/cutted_vol_kg_pivot_view.xml',
        'views/report_menus.xml',
        'security/ir.model.access.csv'
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
