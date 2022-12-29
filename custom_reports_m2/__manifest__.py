# -*- coding: utf-8 -*-
{
    'name': "Reportes Media Pagina",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Isias Mateo: Isias1626@gmail.com",
    'website': "https://github.com/TheHardest18",
    'category': 'Uncategorized',
    'version': '15.0.0.0.1',
    'depends': ['base', 'account', 'l10n_do_accounting', 'stock'],
    'data': [
        # 'security/ir.model.access.csv',
        #'views/paper_format.xml',
        'views/a5_format.xml',
        'views/picking_report.xml',
        'views/payment_report.xml',
	# 'views/account_move_inherit.xml',
        # 'views/report_medium.xml',
        'views/account_new_report.xml',
    ],
}
