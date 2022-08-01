from odoo import fields, models


class HrHospitalPatient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection(
        string='Gender selection',
        selection=[('male', 'Male'),
                ('female', 'Female'), ],
        required=True, )
    