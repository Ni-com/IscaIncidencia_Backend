from odoo import models, fields

class CategoriaModel(models.Model):
    _name = 'isca_incidencia.categoria_model'
    _description = 'Modelo de categoria'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion", default="")

    inventario = fields.One2many("isca_incidencia.inventario_model","categoria",string="Inventario")
    responsable = fields.Many2one("isca_incidencia.usuario_model",string="Responsable por defecto")

    usuarios = fields.Many2many(
        comodel_name='isca_incidencia.usuario_model',
        relation='isca_categoria_usuario_rel',
        column1='categorias',
        column2='usuarios',
        string='Usuarios asignados'
    )
