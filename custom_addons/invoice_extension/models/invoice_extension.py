from odoo import fields, models, api
class InvoiceExtension(models.Model):
    _inherit = "account.move"
    previous_invoice = fields.Many2one("account.move", domain="[('move_type', '=', 'out_invoice')]", string="Previous Invoice")

    partner_id = fields.Many2one('res.partner',string='Partner')
    payment_reference = fields.Char(string='Payment Reference')
    invoice_date = fields.Date(string='Invoice/Bill Date')
    invoice_date_due = fields.Date(string='Due Date')
    invoice_payment_term_id = fields.Many2one('account.payment.term', string='Payment Terms')
    currency_id = fields.Many2one('res.currency',string='Currency')
    invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice lines')
    product_id = fields.Many2one('product.product', string='Product')
    name = fields.Char(string='Label')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    discount = fields.Float(string='Discount (%)')
    tax_ids = fields.Many2many(comodel_name='account.tax', string="Taxes")