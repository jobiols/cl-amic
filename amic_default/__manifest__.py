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
    'name': 'AMIC',
    'version': '11.0.0.0.7',
    'license': 'Other OSI approved licence',
    'category': 'Default Application',
    'summary': 'Customization for AMIC',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'author': 'jeo Software',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',
        'mrp',
        'hr',

        # additional applications
        'mrp_workorder',  # ordenes de trabajo
        # 'web_gantt', no anda bien.
        # 'mrp_mps',  # plan maestro de produccion
        'mrp_account',  # contabilidad analitica en fabricacion

        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ce',

        # utilitarios adicionales
        'backend_theme_v11',
        # preview bom
        'mrp_bom_structure_html',

        # desarrollo especifico para amic
        'customer_product_names',  # nombres de prod <> por cliente
        'mrp_lot_attributes',  # caracteristicas de trazabilidad
        'mrp_ot',  # generacion de ordenes de trabajo
        'pre_printed_stock_picking',  # remito preimpreso
        'mrp_easy_prod',  # wizard para encontrar rapidamente la ot produccion
        'mrp_production_cancel',
        'amic_reports',
        'product_label_amic',

        # requerido por la restriccion de menuitems
        'mail', 'calendar', 'contacts', 'mrp', 'sale', 'purchase', 'stock',
        'account', 'hr', 'base'
    ],
    'data': [
        'security/menuitem_security.xml',
        'views/menuitems.xml'
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    # Aca empiezan las extensiones

    'env-ver': '2',
    'odoo-license': 'CE',
    'config': [],

    'port': '8069',

    'git-repos': [
        'git@github.com:jobiols/cl-amic.git',
        'git@github.com:jobiols/odoo-addons.git',
        'git@github.com:jobiols/jeo-addons.git',

        'git@github.com:ingadhoc/odoo-argentina.git',
        'git@github.com:ingadhoc/argentina-sale.git',
        'git@github.com:ingadhoc/account-financial-tools.git',
        'git@github.com:ingadhoc/account-payment.git',
        'git@github.com:ingadhoc/miscellaneous.git',
        'git@github.com:ingadhoc/argentina-reporting.git',
        'git@github.com:ingadhoc/reporting-engine.git',
        'git@github.com:ingadhoc/aeroo_reports.git',
        'git@github.com:ingadhoc/sale.git',
        'git@github.com:ingadhoc/odoo-support.git',
        'git@github.com:ingadhoc/product.git',
        'git@github.com:ingadhoc/stock.git',
        'git@github.com:ingadhoc/account-invoicing.git',
        'git@github.com:ingadhoc/patches.git',

        'git@github.com:oca/queue.git',
        'git@github.com:oca/partner-contact.git',
        'git@github.com:oca/web.git',
        'git@github.com:oca/server-tools.git',
        'git@github.com:oca/social.git',
        'git@github.com:oca/server-ux.git',
        'git@github.com:oca/server-brand.git',
        'git@github.com:oca/manufacture.git',
        'git@github.com:oca/manufacture-reporting.git',
        'git@github.com:oca/management-system.git',
        'git@github.com:oca/sale-workflow.git',
        'git@github.com:oca/stock-logistics-warehouse.git',
        'git@github.com:oca/stock-logistics-reporting.git',
        'git@github.com:oca/stock-logistics-workflow.git',
        'git@github.com:oca/knowledge.git',
        'git@github.com:oca/hr.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:11.1-alpine',
        'nginx nginx',
        'aeroo adhoc/aeroo-docs',
    ],

}
