# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class tamsah_location_res_user(models.Model):
#     _name = 'tamsah_location_res_user.tamsah_location_res_user'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100