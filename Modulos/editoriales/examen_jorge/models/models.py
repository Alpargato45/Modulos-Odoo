# -*- coding: utf-8 -*-

from odoo import models, fields, api


class examen_jorge(models.Model):
     _name = 'examen_jorge.examen_jorge'
     _description = 'examen_jorge.examen_jorge'

     name = fields.Char(default="Jorge")
     apellido = fields.Char(default="del Cid Moreno")
     nombreCompleto = fields.Char(string="Nombre Completo", compute="_compute_nombre_completo", store=True)
     direccion = fields.Char(string="Direccion")
     ciudad = fields.Char(String="Ciudad")
     edad = fields.Integer(string="Edad")
     menorOMayor = fields.Char(compute="_compute_menor_o_mayor", store=True)
     sexo = fields.Char(string="Indica tu sexo")

     @api.depends("edad")
     def _compute_menor_o_mayor(self):
        for record in self:
            if record.edad > 18:
                record.menorOMayor = "si"
            else:
                record.menorOMayor = "no"
    
     @api.depends("name", "apellido")
     def _compute_nombre_completo(self):
        for record in self:
            record.nombreCompleto = record.name + " " + record.apellido