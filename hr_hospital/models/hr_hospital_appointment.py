import datetime
from odoo import fields, models


class HrHospitalAppointment(models.Model):
    _name = 'hr_hospital.appointment'
    _description = 'Appointment'

    name = fields.Char()
    active = fields.Boolean(default=True)
    doctor_id = fields.Many2one("hr_hospital.doctor")
    patient_id = fields.Many2one("hr_hospital.patient")
    appointment_date = fields.Datetime(
        string='Date & time',
        required=True, default=datetime.datetime.today())
    diagnosis_id = fields.Many2one("hr_hospital.diagnosis")
    research_id = fields.Many2many("hr_hospital.research")
    recommendation = fields.Text()
