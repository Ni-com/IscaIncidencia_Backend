# -*- coding: utf-8 -*-
{
    'name': "IscaIncidencia",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nico",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/category_view.xml',
        'views/categoria_view.xml',
        'views/rol_view.xml',
        'views/inventario_view.xml',
        'views/usuario_view.xml',
        'views/ubicacion_view.xml',
        'views/incidencia_view.xml',
        'views/registro_view.xml',
        'views/factura_view.xml',
        'views/album_view.xml',

        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
