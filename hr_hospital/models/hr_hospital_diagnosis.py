from odoo import fields, models


class HrHospitalDiagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Hospital Diagnosis'

    name = fields.Char()
