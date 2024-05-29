from odoo import fields, models
class ProductExtension(models.Model):
    _inherit = ['product.template']
    brand = fields.Many2one('brand.list',string = 'Brand')
    manufacture_year = fields.Char(string = 'Manufacture Year')
   
