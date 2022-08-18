import datetime
from odoo import fields, models


class HrHospitalDoctorHistory(models.Model):
    _name = 'hr_hospital.doctor.history'
    _description = 'Personal Doctor History'

    name = fields.Char()
    active = fields.Boolean(default=True)
    doctor_id = fields.Many2one("hr_hospital.doctor")
    patient_id = fields.Many2one("hr_hospital.patient")
    change_date = fields.Date(
        string='Date',
        required=True, default=datetime.date.today())
