# -*- coding: utf-8 -*-
{
    'name': "Employee fields for Mexico",

    'summary': """
        Adds fields for employee management in Mexico.""",

    'description': """
        Adds fields for employee management in Mexico such as INE, and employment anniversary.
        Replaces identification ID string with 'CURP'.
    """,

    'author': "BerrySoft MX, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/l10n-mexico",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Employees',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
    ],
}