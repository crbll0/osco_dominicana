# -*- coding: utf-8 -*-
# from odoo import http


# class SaleCustomMany(http.Controller):
#     @http.route('/sale_custom_many/sale_custom_many', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_custom_many/sale_custom_many/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_custom_many.listing', {
#             'root': '/sale_custom_many/sale_custom_many',
#             'objects': http.request.env['sale_custom_many.sale_custom_many'].search([]),
#         })

#     @http.route('/sale_custom_many/sale_custom_many/objects/<model("sale_custom_many.sale_custom_many"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_custom_many.object', {
#             'object': obj
#         })
