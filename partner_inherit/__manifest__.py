{
    'name': 'student_inherit',
    'version': '1.0',
    'category': 'Student inherited Info',
    'sequence': 5,
    'summary': 'student module',
    'depends': ['partner'],

    'description': """
            module for student information demo
            """,
            

    'data' : [
        'security/ir.model.access.csv',
        'views/student_inherit_views.xml',
    ],

    'application' : True

}