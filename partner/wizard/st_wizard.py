from odoo import  fields, models, api

class Student(models.Model):
    _name = 'student.wizard'

    college_id = fields.Many2one('student.college')

    def add_college(self):
    	print("method called....")
    	self.env['student'].browse(self._context.get("active_ids")).update({"college_id":self.college_id})
