# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cantante(models.Model):
    _name = 'musica.cantante'
    _description = 'musica.cantante'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Cantante")
    foto = fields.Binary(string="Foto del cantante:")
    anioDebut = fields.Date(string="Año Debut")
    aniosActivos = fields.Integer(string="Años Activos")
    numeroOyentes = fields.Integer(string="Número de Oyentes")
    nacionalidad = fields.Char(string="Nacionalidad")
    premios = fields.One2many('musica.premio', "premiado", string="Premios")
    canciones = fields.Many2many(comodel_name="musica.cancion", relation="cancion_cantante", column1="nombre", column2="titulo")

class premio(models.Model):
    _name = 'musica.premio'
    _description = 'musica.premio'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre")
    categoria = fields.Selection([("mejorCancion","Mejor Canción"),("mejorArtista","Mejor Artista"),("mejorColaboracion","Mejor Colaboración"),("mejorLetra","Mejor Letra")], string="Categoría del Premio")
    premiado = fields.Many2one('musica.cantante', string="Cantante Premiado")

class album(models.Model):
    _name = 'musica.album'
    _description = 'musica.album'
    _rec_name = 'titulo'

    titulo = fields.Char(string="Título")
    portada = fields.Binary(string="Portada del Álbum:")
    fechaSalida = fields.Date(string="Fecha de Salida")
    escuchasTotales = fields.Integer(string="Escuchas Totales", compute='_compute_escuchas_totales')
    trackList = fields.One2many('musica.cancion', "album", string="TrackList")

    @api.depends('trackList')
    def _compute_escuchas_totales(self):
        for album in self:
            album.escuchasTotales = sum(album.trackList.mapped('escuchas'))

class cancion(models.Model):
    _name = 'musica.cancion'
    _description = 'musica.cancion'
    _rec_name = 'titulo'

    titulo = fields.Char(string="Título")
    portada = fields.Binary(string="Portada de la canción:")
    cantantes = fields.Many2many(comodel_name="musica.cantante",relation="cancion_cantante",column1="titulo", column2="nombre")
    duracion = fields.Float(string="Duración")
    fechaSalida = fields.Date(string="Fecha Salida")
    escuchas = fields.Integer(string="Escuchas")
    album = fields.Many2one('musica.album', string="Album")