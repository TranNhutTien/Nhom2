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

    @api.onchange('previous_invoice')
    def onchange_previous_invoice(self):
        if self.preview_invoice:
            self.partner_id = self.previous_invoice.partner_id
            self.payment_reference = self.previous_invoice.payment_reference
            self.invoice_date = self.previous_invoice.invoice_date
            self.invoice_date_due = self.previous_invoice.invoice_date_due
            self.invoice_payment_term_id = self.previous_invoice.invoice_payment_term_id
            self.currency_id = self.previous_invoice.currency_id
            self.invoice_line_ids = self.previous_invoice.invoice_line_ids
        else:
            self.partner_id=""
            self.invoice_date=""
            self.invoice_date_due=""
            self.invoice_payment_term_id=""
            self.currency_id=""
            self.invoice_line_ids=""