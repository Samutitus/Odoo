# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class comprador(models.Model):
    _name = 'comprador'
    _description = 'Permite definir las características de un comprador'
    _inherit = 'sag.base'

    name = fields.Char(string='Nombre del comprador')
    ventas = fields.Many2many('ventas', string='Ventas')
