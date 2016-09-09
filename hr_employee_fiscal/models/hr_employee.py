# -*- coding: utf-8 -*-
###########################################################################
#
# © 2016 Juan Jose Lopez Garcia <jjlopezg74@gmail.com>.
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
###########################################################################
from openerp import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    fiscal_ids = fields.One2many('hr.employee.fiscal', 'employee_id', string='Datos Fiscales')


