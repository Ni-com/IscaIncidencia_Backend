from odoo import models, fields, api
from datetime import datetime
class InventarioModel(models.Model):
    _name = 'isca_incidencia.inventario_model'
    _description = 'Modelo de Inventario'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")
    cantidad=fields.Integer(string="Cantidad",default=1)
    fechaCreacion=fields.Datetime(string="Fecha de creacion",default=lambda self:datetime.now())
    icono = fields.Binary(string="Icono")
    etiqueta=fields.Char(string="Etiqueta", default="0")
    etiquetable = fields.Boolean(string="Etiquetable")
    conIncidencia=fields.Boolean(string="Esta con incidencia", compute='_compute_con_incidencia')
    
    incidencias = fields.One2many("isca_incidencia.incidencia_model","inventario",string="Incidencias")
    
    facturas = fields.One2many("isca_incidencia.factura_model","inventario",string="Paginas de Factura")
    masImagenes = fields.One2many("isca_incidencia.album_model","inventario",string="Mas imagenes del inventario")

    categoria = fields.Many2one("isca_incidencia.categoria_model",string="Categoria")
    usuario = fields.Many2one("isca_incidencia.usuario_model",string="Creado por")
    ubicacion = fields.Many2one("isca_incidencia.ubicacion_model",string="Ubicacion")
    activo=fields.Boolean(string="Esta dado de alta", default='true')

    
    @api.depends('incidencias.estado')
    def _compute_con_incidencia(self):
        for inv in self:
            con_incidencia = any(inc.estado is False for inc in inv.incidencias)
            inv.conIncidencia = con_incidencia