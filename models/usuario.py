# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class usuario(models.Model):
    _name = 'usuario'
    _description = 'Permite definir las características de un usuario'
    _inherit = 'sag.base'

    name = fields.Char(string='Nombre del usuario', required=True)
    email = fields.Char(string='Email', required=True) 
    
