# -*- coding: utf-8 -*-
# from odoo import http


# class KsNote(http.Controller):
#     @http.route('/ks_note/ks_note', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ks_note/ks_note/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ks_note.listing', {
#             'root': '/ks_note/ks_note',
#             'objects': http.request.env['ks_note.ks_note'].search([]),
#         })

#     @http.route('/ks_note/ks_note/objects/<model("ks_note.ks_note"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ks_note.object', {
#             'object': obj
#         })
