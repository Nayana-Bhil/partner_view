{
    'name': 'student',
    'version': '1.0',
    'category': 'Student Info',
    'sequence': 5,
    'summary': 'student module',
    'depends': ['base'],

    'description': """
            module for student demo
            """,
            

    'data' : [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/partner_view.xml',
    ],

    'application' : True

}