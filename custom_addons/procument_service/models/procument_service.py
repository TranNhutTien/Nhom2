from odoo import fields, models, api, _

class ProcumentService(models.Model):
    _name = "procument.service"
    _description = "Procument Service"
   
    name = fields.Char(string='Order Reference', readonly=True, default=lambda self: _('New'))
    date = fields.Date(string="Order Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    vendor_id = fields.Many2one("res.partner", string="Vendor", required=True)
    order_line_ids = fields.One2many("procument.service.lines", "procument_service_id", string="Order Lines")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('procument.service') or _('New')
        res = super(ProcumentService, self).create(vals)
        return res

class ProcumentServiceLines(models.Model):
    _name = "procument.service.lines"
    _description = "Procument Service Lines"

    product_id = fields.Many2one("product.product", string="Product", required=True)
    quantity = fields.Integer(string="Quantity", default=1)
    unit_price = fields.Float(string="Unit Price")
    procument_service_id = fields.Many2one("procument.service", string="Procument Service")
    total = fields.Float(string="Total", compute="_compute_total")

    @api.depends('product_id','quantity','unit_price')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.quantity * rec.unit_price
