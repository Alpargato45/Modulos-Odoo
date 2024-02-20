# -*- coding: utf-8 -*-
{
    'name': "editoriales",

    'summary': """
        Este módulo gestiona editoriales de cómics""",

    'description': """
        Este módulo está pensado para recopilar las distintas editoriales de cómis que venden sus publicaciones en España, incluyendo sus principales colecciones, cómics individuales y autores
    """,

    'author': "Adriano Díaz Benítez",
    'website': "https://github.com/PublioElio",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/editorial.xml',
        'views/coleccion.xml',
        'views/comic.xml',
        'views/autor.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
