# -*- coding: utf-8 -*-
{
    'name': "Picking Report",

    'summary': """
        Reporte en Conduce
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "GrowIT",
    'website': "https://www.growit.com.do/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/paper_format.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/account_move_inherit.xml',
        # 'views/res_company_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
