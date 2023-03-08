# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields, api
from . import base

class ventas(models.Model):
    _name = 'ventas'
    _description = 'Permite crear  un ventas que tenga productos'
    _inherit = 'sag.base'

    name = fields.Char(string='Nombre del ventas' ,required=True)
    num = fields.Integer(string='Cantidad de productos' ,required=True,min_value=1)
    precio = fields.Char(string='Precio del pedido', required=True)
    fecha = fields.Date(string='Fecha de la venta', default=date.today(), required=True) 
    comprador = fields.Many2one('comprador', string='Comprador', required=True)
    vendedor = fields.Many2one('vendedor', string='Vendedor', required=True)
    productos = fields.Many2many('productos', string='Productos', required=True, related='vendedor.productos')
