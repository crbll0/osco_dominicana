from odoo import api, fields, models, tools, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = 'Purchase order'

    branch_id = fields.Many2one('company.branches', string='Branch', domain="[('company_id','=',company_id)]")

    def action_view_invoice(self, invoices=False):
        result = super(PurchaseOrder,self).action_view_invoice(invoices=invoices)
        result['context'] = {
            'default_move_type': 'in_invoice',
            'default_branch_id':self.branch_id.id
        }
        return result
