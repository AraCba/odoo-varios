# -*- coding: utf-8 -*-
##############################################################################
#
#    Módulo Docentes para Odoo
#    Copyright (C) Araceli Acosta.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
##############################################################################

import time

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
#from odoo.addons.docentes.models.base import Base



TIPODOC = [('dni','DNI'),('lc','LC'),('le','LE'),('pas','PAS'),('ci','CI')]
SEXO = [('f', 'Femenino'),('m','Masculino'), ('o', 'Otro')]


class Partner(models.Model):
    '''Partner'''
    _inherit = 'res.partner'

#    email2 = fields.Char('Otro Correo electrónico', size=240)
    nombre = fields.Char('Nombre(s)')
    apellido = fields.Char('Apellido(s)')
    validado = fields.Boolean('Contacto validado', default=False)
    tipodni = fields.Selection(TIPODOC,'Tipo doc')
    dni = fields.Integer('N documento')
    sexo = fields.Selection(SEXO,'Sexo')
    ano_nacimiento = fields.Integer('Año aproximado de nacimiento')
  
    observado = fields.Boolean('Observado?')
    observacion = fields.Char('Observación')

    fuente = fields.Char('Fuente')
  
    
    facebook_url = fields.Char('Facebook')
    twitter_url = fields.Char('Twitter')
    youtube_url = fields.Char('Youtube')
    instagram_url = fields.Char('Instagram')
    googleplus_url = fields.Char('Google+')

    _defaults = {
    }


#Partner()

