# -*- coding: utf-8 -*-
# from odoo import http


# class Editoriales(http.Controller):
#     @http.route('/editoriales/editoriales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/editoriales/editoriales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('editoriales.listing', {
#             'root': '/editoriales/editoriales',
#             'objects': http.request.env['editoriales.editoriales'].search([]),
#         })

#     @http.route('/editoriales/editoriales/objects/<model("editoriales.editoriales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('editoriales.object', {
#             'object': obj
#         })
