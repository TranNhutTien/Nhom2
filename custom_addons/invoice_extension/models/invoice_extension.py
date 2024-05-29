from odoo import fields, models, api
class InvoiceExtension(models.Model):
    _inherit = "account.move"
    previous_invoice = fields.Many2one("account.move", domain="[('move_type', '=', 'out_invoice')]", string="Previous Invoice")
    
    



