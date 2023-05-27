from odoo import models, fields
from datetime import datetime

class FacturaModel(models.Model):
    _name = 'isca_incidencia.factura_model'
    _description = 'Modelo de Facturas'

    name = fields.Binary(string="Pagina")
    fechaCreacion=fields.Datetime(string="Fecha de creacion",default=lambda self:datetime.now())
    inventario = fields.Many2one("isca_incidencia.inventario_model",string="Invenario afectado")