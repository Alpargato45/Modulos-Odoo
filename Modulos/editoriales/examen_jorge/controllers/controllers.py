# -*- coding: utf-8 -*-
# from odoo import http


# class ExamenJorge(http.Controller):
#     @http.route('/examen_jorge/examen_jorge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen_jorge/examen_jorge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen_jorge.listing', {
#             'root': '/examen_jorge/examen_jorge',
#             'objects': http.request.env['examen_jorge.examen_jorge'].search([]),
#         })

#     @http.route('/examen_jorge/examen_jorge/objects/<model("examen_jorge.examen_jorge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen_jorge.object', {
#             'object': obj
#         })
