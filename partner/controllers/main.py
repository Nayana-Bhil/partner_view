from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/mypath', type="http", website=True)
    def mypath(self, **kwargs):
        students = request.env['student'].search([])
        return request.render('partner.my_template', {'students': students})

    @http.route('/create_student', type="http", website=True)
    def create_student(self, **kwargs):
        return request.render('partner.create_student')

    @http.route('/submit_form', type="http", method="POST", csrf=False, website=True)
    def submit_form(self, **kwargs):
        request.env['student'].create(kwargs)
        return http.local_redirect('/mypath')

    @http.route('/delete_student/<model("student"):st_remove>', type="http", website=True)
    def delete_student(self, st_remove, **kwargs):
        st_remove.unlink()
        return http.local_redirect('/mypath')

