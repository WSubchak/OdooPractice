from odoo import fields, models


class HrHospitalPatientCard(models.Model):
    _name = 'hr_hospital.patientcard'
    _description = 'Hospital Patient Card'

    name = fields.Char()
