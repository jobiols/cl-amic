{
    'name': "Product Label Amic",

    'summary': """
        Agrega reporte de etiquetas en el boton imprimir de una transferencia""",

    'description': """
        Reporte de etiquetas
    """,

    'author': "Joaquin Romero",
    'website': "http://www.jjvrsistemas.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Reportes',
    'version': '11.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','product'],

    # always loaded
    'data': [
        'views/facturapreimpreso.xml',
    ],
}
