# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import pytz

#class ResCompany(models.Model):
 #   _inherit = 'res.company'

  #  account_journal_id = fields.Many2one('account.journal', string='Diario')

class AccountMove(models.Model):
    _inherit = 'stock.picking'
    hora_actual = fields.Datetime(compute="_compute_hora_actual")

    @api.depends('hora_actual')
    def _compute_hora_actual(self):
        self.hora_actual = datetime.now(pytz.timezone('America/Santo_Domingo')).strftime('%Y-%m-%d %H:%M:%S')
        #now= datetime.strftime(fields.Datetime.context_timestamp(self, datetime.now()), "%Y-%m-%d %H:%M:%S")
#.strftime('%Y:%m%H:%M:%S')
