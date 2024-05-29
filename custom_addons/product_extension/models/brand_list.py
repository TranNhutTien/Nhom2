from odoo import fields, models
class Brand(models.Model):
    _name='brand.list'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='Brand List'
    _rec_name='brand'
    brand = fields.Char(string = 'Brand Name', required=True, tracking=True)
    des = fields.Char(string = 'Description')
    email = fields.Char(string = 'Email')
    website = fields.Char(string = 'Website')
    logo = fields.Binary("Logo")
    country = fields.Char(string = 'Country')
