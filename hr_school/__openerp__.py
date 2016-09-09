#-*- coding:utf-8 -*-
###########################################################################
#
# © 2016 Juan Jose Lopez Garcia <jjlopezg74@gmail.com>.
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
###########################################################################
{
    'name': 'Proyecto Conecta - Titulaciones',
    'version': '9.0.1.0.0',
    'author': 'JJLopezG',
    'website': 'http://www.tuconecta.es',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': '',
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': """
    """,
    'images': ['images/school.jpeg'],
    "depends" : [
                'base',
                'hr'
                ],
    "data" : [
        'data/hr.school.academy.csv',
        "security/ir.model.access.csv",
        'views/hr_employee_view.xml',
        'views/hr_school_academy_view.xml',
        'views/hr_school_language_view.xml',
    ],
}
