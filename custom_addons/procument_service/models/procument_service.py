from odoo import fields, models, api, _

class ProcumentService(models.Model):
    _name = "procument.service"
    _description = "Procument Service"
   
    name = fields.Char(string='Order Reference', readonly=True, default=lambda self: _('New'))
    date = fields.Date(string="Order Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    vendor_id = fields.Many2one("res.partner", string="Vendor", required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('procument.service') or _('New')
        res = super(ProcumentService, self).create(vals)
        return res

    

