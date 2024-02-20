# -*- coding: utf-8 -*-

from odoo import models, fields, api


class calculadora(models.Model):
     _name = 'calculadora.calculadora'
     _description = 'Modulo Calculadora'

     value = fields.Integer(string="Primer valor")
     value2 = fields.Integer(string="Segundo valor")
     valueResultado = fields.Integer(string="resultado",readonly=True,compute="_calcular",store=True)

     #cada vez que cambie el valor y valor 2 se llama a la funcion                                
     @api.depends('value','value2')
     def _calcular(self):
         for record in self:
             record.valueResultado = int(record.value)+int(record.value2)