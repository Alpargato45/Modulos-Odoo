# -*- coding: utf-8 -*-

from odoo import models, fields, api

class editorial(models.Model):
    _name = 'editoriales.editorial'
    _description = 'editoriales.editorial'
    _rec_name = 'nombre'

    id_editorial = fields.Integer(string='Id de la editorial: ',help='Identificador único de la editorial')
    nombre = fields.Char(string="Nombre de la editorial: ",
                         help='Introduzca un nombre para la editorial',
                         required=True)
    sede = fields.Char(string="Sede: ",help="¿Dónde tiene sede esta editorial?",
                       required=True)
    logo = fields.Binary(string="Logo de la editorial: ")
    colecciones = fields.One2many(
        'editoriales.coleccion',
	    'editorial', 
        string='Colecciones: ')
    autores = fields.Many2many(comodel_name='editoriales.autor',
                                relation='editoriales_autores',
                                column1='id_editorial',
                                column2='id_autor')

class coleccion(models.Model):
    _name = 'editoriales.coleccion'
    _description = 'editoriales.coleccion'
    _rec_name = 'nombre'
    
    id_coleccion = fields.Integer(string='Id de la colección: ',
                                  help='Identificador único de la colección')
    nombre = fields.Char(string="Nombre de la colección: ",
                         help='Introduzca el nombre de la colección')
    editorial = fields.Many2one('editoriales.editorial',
                                string="Editorial: ")
    comics = fields.One2many('editoriales.comic',
	                        'coleccion', 
                            string='Comics: ')

class comic(models.Model):    
    _name = 'editoriales.comic'
    _description = 'editoriales.comic'
    _rec_name = 'nombre'
    
    id_comic = fields.Integer(string='Id del cómic: ',
                              help='Identificador único del cómic')
    nombre = fields.Char(string="Nombre del cómic: ",
                         help='Nombre del cómic')
    portada = fields.Binary(sting="Portada")
    autores = fields.Many2many(comodel_name='editoriales.autor',
                                relation='comics_autores',
                                column1='id_comic',
                                column2='id_autor')
    coleccion = fields.Many2one('editoriales.coleccion',
                                string="Colección: ")
    
class autor(models.Model):
    _name = 'editoriales.autor'
    _description = 'editoriales.autor'
    _rec_name = 'nombre_apellidos'
    
    id_autor = fields.Integer(string='Id del autor: ',
                              help='Identificador único del autor')
    imagen = fields.Binary(string="Imagen del autor")
    nombre_apellidos = fields.Char(string="Nombre y apellidos: ",
                                   help='Nombre y apellidos del autor')
    creditos = fields.Selection([('ilustrador','Ilustrador'),('guionista','Guionista'),('entintador','Entintador')],string="Créditos: ")
    comics = fields.Many2many(comodel_name='editoriales.comic',
                                relation='comics_autores',
                                column1='id_autor',
                                column2='id_comic')
    editoriales = fields.Many2many(comodel_name='editoriales.editorial',
                                relation='editoriales_autores',
                                column1='id_autor',
                                column2='id_editorial')