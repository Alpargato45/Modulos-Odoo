# -*- coding: utf-8 -*-
# from odoo import http


# class Calculadora(http.Controller):
#     @http.route('/calculadora/calculadora', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calculadora/calculadora/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('calculadora.listing', {
#             'root': '/calculadora/calculadora',
#             'objects': http.request.env['calculadora.calculadora'].search([]),
#         })

#     @http.route('/calculadora/calculadora/objects/<model("calculadora.calculadora"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calculadora.object', {
#             'object': obj
#         })
