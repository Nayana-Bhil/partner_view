from odoo import  fields, models, api
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta

class user(models.Model):
    _name = 'student'
    _description = "Student detail"

    email = fields.Char(string="Email id")
    name = fields.Char(string="Name")
    age = fields.Char(compute="_calculate_age", store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male')
    address = fields.Text(string="Address")
    mobile_no = fields.Char(string="Contact No")
    birthday = fields.Date(string="Date Of Birth")
    college_id = fields.Many2one('student.college', string="College")
    enrollment_no = fields.Integer(string="Enrollment Number")
    sem_fee = fields.Integer(string="Semester Fee")
    current_date = fields.Date(default=lambda self: fields.Date.today())
    password = fields.Char(string="Password")
    image = fields.Binary(string="Image", attachment = True) 
    hobbies_ids = fields.Many2many('student.hobbies')
    philosophy = fields.Integer()
    geography = fields.Integer()
    psychology = fields.Integer()
    total = fields.Integer(string="Total")
    average = fields.Float()
    total_compute = fields.Integer(compute="_compute_total", store=True)

    @api.depends('birthday')
    def _calculate_age(self):
        for i in self:
            if i.birthday:
                i.age = relativedelta(date.today(), i.birthday).years

    @api.onchange('philosophy', 'geography', 'psychology')
    def _onchange_marks(self):
        self.total = self.philosophy + self.geography + self.psychology
        self.average = self.total / 3

    @api.depends('philosophy', 'geography', 'psychology')
    def _compute_total(self):
        for rec in self:
            rec.total_compute = rec.philosophy + rec.geography + rec.psychology

class College(models.Model):
    _name = 'student.college'

    name = fields.Char("College Name")
    st_record = fields.One2many('student', 'college_id', string="Student Record")

class College(models.Model):
    _name = 'student.hobbies'

    name = fields.Char("Hobbies")

class fullname(models.Model):
    _inherit = 'student'

    full_name = fields.Char("Full Name")
