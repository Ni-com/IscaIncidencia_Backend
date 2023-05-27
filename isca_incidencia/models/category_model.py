from odoo import models, fields

class CategoryModel(models.Model):
    _name = 'isca_incidencia.category_model'
    _description = 'Modulo de categoria'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")
    photo = fields.Binary("Photo")
    album = fields.Many2many('ir.attachment', string='Album')
    
    

    
    