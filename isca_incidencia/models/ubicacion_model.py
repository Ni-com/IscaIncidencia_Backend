from odoo import models, fields

class UbicacionModel(models.Model):
    _name = 'isca_incidencia.ubicacion_model'
    _description = 'Modelo de ubicacion'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")

    inventario = fields.One2many("isca_incidencia.inventario_model","ubicacion",string="Inventario")
    incidencia = fields.One2many("isca_incidencia.incidencia_model","ubicacion",string="Incidencia")
    