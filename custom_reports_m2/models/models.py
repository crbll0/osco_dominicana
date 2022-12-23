# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import UserError, ValidationError
_logger = logging.getLogger(__name__)

class custom_reports_modifications(models.Model):
    _inherit = 'account.move'
    
    # @api.model
    # def create(self, vals):
        # res = super(custom_reports_modifications, self).create(vals)
        # if res['amount_total'] == 0.0 and res['move_type'] in ['out_invoice', 'in_invoice']:
            # raise ValidationError(('No puede guardar una factura con valor 0'))
        # return res
     # 
    # def write(self, vals):
        # res = super(custom_reports_modifications, self).write(vals)
        # for rec in self:
            # if rec.amount_total == 0.0 and rec.move_type in ['out_invoice', 'in_invoice']:
                # raise ValidationError(('No puede guardar una factura con valor 0'))
        # # _logger.error(("RES", res))
        # # _logger.error(("RESt", vals))
        # # # if res['amount_total'] == 0.0:
            # # # raise ValidationError(('No puede guardar una factura con valor 0'))
        # return res
