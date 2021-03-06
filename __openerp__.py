# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Modifications",

    'summary': """
        Modificaciones para los pedidos de compra""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Warren Castro",
    'website': "http://www.recicladorasanmiguel.com.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'purchase_order_modifications_report.xml',       
        'views/report_tiquete_compra.xml',
        'views/report_factura_de_compra_fotos.xml',
        'views/report_certificado_co2.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
