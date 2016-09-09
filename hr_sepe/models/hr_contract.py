# -*- encoding: utf-8 -*-
###########################################################################
#
# © 2016 Juan Jose Lopez Garcia <jjlopezg74@gmail.com>.
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
###########################################################################

from openerp import models, fields, api, _

class HrContract(models.Model):
    _inherit = 'hr.contract'

    sepe_ids = fields.One2many('hr.sepe', 'contract_id', string='Comunicacion SEPE')
