# -*- coding: utf-8 -*-

from odoo import models, fields, api


class coche(models.Model):
    _name = 'concesionario.coche'
    _description = 'concesionario.coche'
    _rec_name = 'modelo'

    modelo = fields.Char(string="Modelo")
    anioCreacion = fields.Date(string="Fecha de creación")
    puertas = fields.Integer(string="Número de puertas")
    motor = fields.Selection([('gasolina',"Gasolina"),("diesel","Diesel"),("electrico","Eléctrico")], string="Tipo de Motor")
    marca = fields.Many2one('concesionario.marca', string="Marca")

class marca(models.Model):
    _name = 'concesionario.marca'
    _description = 'concesionario.marca'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre")
    coches = fields.One2many("concesionario.coche", "marca", string="Nombre")
    sede = fields.Char(string="Sede")
    director = fields.Char(string="Director")
    direccion = fields.Char(string="Dirección")

class Concesionario(models.Model):
    _name = 'concesionario.concesionario'
    _description = 'Concesionario'

    name = fields.Char(string="Nombre")
    coches = fields.Many2many("concesionario.coche", string="Coches")