# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _

class ProjectKanban(models.Model):
    _inherit = 'project.project'

    phone_cus = fields.Char(related='partner_id.phone', readonly=True)
    email_cus = fields.Char(related='partner_id.email', readonly=True)
    city_cus = fields.Char(related='partner_id.city', readonly=True)
    phone_manager = fields.Char(related='user_id.phone', readonly=True)
	
