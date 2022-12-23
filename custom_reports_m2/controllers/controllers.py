# -*- coding: utf-8 -*-
# from odoo import http


# class CustomReportsModifications(http.Controller):
#     @http.route('/custom_reports_modifications/custom_reports_modifications/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_reports_modifications/custom_reports_modifications/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_reports_modifications.listing', {
#             'root': '/custom_reports_modifications/custom_reports_modifications',
#             'objects': http.request.env['custom_reports_modifications.custom_reports_modifications'].search([]),
#         })

#     @http.route('/custom_reports_modifications/custom_reports_modifications/objects/<model("custom_reports_modifications.custom_reports_modifications"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_reports_modifications.object', {
#             'object': obj
#         })
