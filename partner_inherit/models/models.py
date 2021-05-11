from odoo import  fields, models, api

class Student_Inheritance(models.Model):
    _name = 'student.inherit'
    _description = "Student Inherited Data"
    _inherit = 'student'

    deartment = fields.Char(string="Dapartment Name")
    review = fields.Char(string="Review")