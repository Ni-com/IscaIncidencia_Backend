from odoo import models, fields
from datetime import datetime

class IncidenciaModel(models.Model):
    _name = 'isca_incidencia.incidencia_model'
    _description = 'Modelo de Incidencia'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")
    fechaAbertura=fields.Datetime(string="Fecha de abertura",default=lambda self:datetime.now())
    fechaCierre=fields.Datetime(string="Fecha de cierre")
    foto = fields.Binary(string="Foto")
    estado = fields.Boolean(string="Esta completa")
    inventario = fields.Many2one("isca_incidencia.inventario_model",string="Invenario afectado")

    registro = fields.One2many("isca_incidencia.registro_model","incidencia",string="Registros")
    creador = fields.Many2one("isca_incidencia.usuario_model",string="Creador")
    asignado = fields.Many2one("isca_incidencia.usuario_model",string="Asignado")
    ubicacion = fields.Many2one("isca_incidencia.ubicacion_model", string="Ubicacion", related="ubicacionInventario")
    masImagenes = fields.One2many("isca_incidencia.album_model","incidencia",string="Mas imagenes de la incidencia")

    ubicacionInventario = fields.Many2one('isca_incidencia.ubicacion_model', string='Ubicacion de inventario', related='inventario.ubicacion')

