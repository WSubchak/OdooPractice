{
    'name': "Hospital Management System",

    'summary': """
        Hospital Management System for doctors and patients
        ....""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sofis.tech / Volodymyr Subchak",
    'website': "http://www.sofis.tech",
    'sequence': -100,
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'category': 'Human Resources',
    'version': '15.0.1.0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_patientcard_views.xml',
        'views/hr_hospital_diagnosis_views.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
