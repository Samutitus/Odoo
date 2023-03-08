# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class vendedor(models.Model):
    _name = 'vendedor'
    _description = 'Permite definir las características de un vendedor'
    _inherit = 'sag.base'

    name = fields.Char(string='Nombre vendedor')
    productos = fields.Many2many('productos', string='Productos')
