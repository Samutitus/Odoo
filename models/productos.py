# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class productos(models.Model):
    _name = 'productos'
    _description = 'Permite definir las características de un producto'
    _inherit = 'sag.base'

    name = fields.Char(string='Nombre producto')
    state = fields.Selection([('a', 'Nuevo'),('b', 'Como nuevo'),('c', 'En buen estado'),('d', 'En condiciones aceptables'),('e', 'Lo ha dado todo')],string='Estado del producto' ,required=True)
    vendedor = fields.Many2many('vendedor', string='Vendedor', required=True)
    precioUnidad = fields.Char(string='Precio por unidad', required=True)
    
