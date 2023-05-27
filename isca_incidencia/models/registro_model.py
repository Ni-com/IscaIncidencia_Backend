from odoo import models, fields
from datetime import datetime

class RegistroModel(models.Model):
    _name = 'isca_incidencia.registro_model'
    _description = 'Modelo de registro'

    name = fields.Datetime(string="Fecha",default=lambda self:datetime.now())
    comentario = fields.Text(string="Comentario")
    usuario = fields.Many2one("isca_incidencia.usuario_model",string="Usuario")
    incidencia = fields.Many2one("isca_incidencia.incidencia_model",string="Incidencia")
    