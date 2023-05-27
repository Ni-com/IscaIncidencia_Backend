from odoo import models, fields
from datetime import datetime
class UsuarioModel(models.Model):
    _name = 'isca_incidencia.usuario_model'
    _description = 'Modelo de Usuarios'

    name = fields.Char(string="Nombre")
    apellidos = fields.Text(string="Apellidos")
    usuario = fields.Char(string="Usuario")
    password = fields.Text(string="Password")

    registro = fields.One2many("isca_incidencia.registro_model","usuario",string="Registros")
    inventarioCreado = fields.One2many("isca_incidencia.inventario_model","usuario",string="Inventario Generado")
    incidenciasCreadas = fields.One2many("isca_incidencia.incidencia_model","creador",string="Incidencias Creadas")
    incidenciasAsignadas = fields.One2many("isca_incidencia.incidencia_model","asignado",string="Incidencias Asignadas")
    rol = fields.Many2one("isca_incidencia.rol_model",string="Rol")
    reparador = fields.Boolean(string="Reparador", related='rol.reparador')
    activo=fields.Boolean(string="Esta dado de alta", default='true')
    
    categorias = fields.Many2many(
        comodel_name='isca_incidencia.categoria_model',
        relation='isca_categoria_usuario_rel',
        column1='usuarios',
        column2='categorias',
        string='Categorias asignadas'
    )
    
   
    
