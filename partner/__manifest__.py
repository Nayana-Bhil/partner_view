{
    'name': 'student',
    'version': '1.0',
    'category': 'Student Info',
    'sequence': 5,
    'summary': 'student module',
    'depends': ['web'],

    'description': """
            module for student demo
            """,
            

    'data' : [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/partner_view.xml',
        'views/template.xml',
        'wizard/st_wizard.xml',
        'report/student_report.xml',
    ],

    'application' : True

}