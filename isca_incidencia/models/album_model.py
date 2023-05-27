from odoo import models, fields
from datetime import datetime

class AlbumModel(models.Model):
    _name = 'isca_incidencia.album_model'
    _description = 'Modelo de Album'

    name = fields.Binary(string="Foto")
    fechaCreacion=fields.Datetime(string="Fecha de creacion",default=lambda self:datetime.now())
    inventario = fields.Many2one("isca_incidencia.inventario_model",string="Invenario de referencia")
    incidencia = fields.Many2one("isca_incidencia.incidencia_model",string="Incidencia de referencia")