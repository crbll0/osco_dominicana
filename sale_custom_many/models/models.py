# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    invoice_lines_report = fields.One2many('account.move.new.line', 'invoice_id', string='Lineas de impresion',
        copy=False, readonly=True,
        states={'draft': [('readonly', False)]})
    

class AccounMoveLines(models.Model):
    _name = 'account.move.new.line'
    
    name = fields.Char("Descripción")
    qty = fields.Float("Cantidad")
    price_unit = fields.Float("Precio Unitario")
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]", ondelete="restrict")
    tax_ids = fields.Many2many(
        comodel_name='account.tax',
        string="Taxes",
        context={'active_test': False},
        help="Taxes that apply on the base amount")
    price_subtotal = fields.Float(compute='_compute_price', string='Subtotal', store=True)
    price_total = fields.Float("Total")
    
    invoice_id = fields.Many2one('account.move', string='Lines',
        index=True, required=True, readonly=True, auto_join=True, ondelete="cascade",
        check_company=True,
        help="The move of this entry line.")
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
    
    @api.depends('qty','price_unit')
    def _compute_price(self):
        for line in self:
            line.price_subtotal = line.price_unit * line.qty
    
    
    
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        lines = []
        for rec in self.order_line:
            lines.append((0, 0, {
                    'name': rec.name,
                    'price_unit': rec.price_unit,
                    'qty': rec.product_uom_qty,
                    'tax_ids': [(6, 0, rec.tax_id.ids)],
                    'price_total': 0.0,
                    'price_subtotal': rec.price_subtotal,
                    'display_type': rec.display_type,
                    'product_uom_id': rec.product_uom.id,
                }))
        res['invoice_lines_report'] = lines
        return res
            
