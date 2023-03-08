from odoo import models, fields, api
from . import base

class almacen(models.Model):
    _name = 'almacen'
    _description = 'Permite crear  un almacen que tenga productos'
    _inherit = 'sag.base'

    name = fields.Char(string='Nombre del almacen', required=True)
    direccion = fields.Char(string='Direccion del almacen', required=True)
    productos = fields.Many2many('productos', string='Productos')
    