from odoo import fields, models
class Brand(models.Model):
    _name='brand.list'
    _description='Brand List'
    _rec_name='brand'
    brand = fields.Char(string = 'Brand Name', required=True)
    des = fields.Char(string = 'Description')
    email = fields.Char(string = 'Email')
    website = fields.Char(string = 'Website')
    logo = fields.Binary("Logo")
    country = fields.Char(string = 'Country')
