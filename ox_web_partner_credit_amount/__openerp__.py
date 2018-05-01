# -*- coding: utf-8 -*-
{
    'name': "Consult partner credit",
    'summary': """""",
    'description': """
    """,

    'author': "Wilfredo Moreno García.",
    'website': "https://www.linkedin.com/in/wilfredo-moreno-garc%C3%ADa-b7365263",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
