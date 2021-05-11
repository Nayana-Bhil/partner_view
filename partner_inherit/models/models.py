from odoo import  fields, models

class user(models.Model):
    _inherit = 'student'

    review = fields.Char(string="Review")
