# -*- coding: utf-8 -*-
# from odoo import http


# class NakhamGroupToDraftSaleOrder(http.Controller):
#     @http.route('/nakham_group_to_draft_sale_order/nakham_group_to_draft_sale_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nakham_group_to_draft_sale_order/nakham_group_to_draft_sale_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nakham_group_to_draft_sale_order.listing', {
#             'root': '/nakham_group_to_draft_sale_order/nakham_group_to_draft_sale_order',
#             'objects': http.request.env['nakham_group_to_draft_sale_order.nakham_group_to_draft_sale_order'].search([]),
#         })

#     @http.route('/nakham_group_to_draft_sale_order/nakham_group_to_draft_sale_order/objects/<model("nakham_group_to_draft_sale_order.nakham_group_to_draft_sale_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nakham_group_to_draft_sale_order.object', {
#             'object': obj
#         })
