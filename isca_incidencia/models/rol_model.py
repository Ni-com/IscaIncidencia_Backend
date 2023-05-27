from odoo import models, fields

class RolModel(models.Model):
    _name = 'isca_incidencia.rol_model'
    _description = 'Modelo de Rol'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")
    reparador = fields.Boolean(string="Reparador")
    
    usuarios = fields.One2many("isca_incidencia.usuario_model","rol",string="Usuarios")
    