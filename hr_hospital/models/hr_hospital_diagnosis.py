import datetime
from odoo import fields, models, api


class HrHospitalDiagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Hospital Diagnosis'

    name = fields.Char()
    active = fields.Boolean(default=True)
    doctor_id = fields.Many2one("hr_hospital.doctor")
    patient_id = fields.Many2one("hr_hospital.patient")
    illness_id = fields.Many2one("hr_hospital.illness")
    therapy = fields.Text()
    diagnosis_date = fields.Date(
        string='Date of diagnosis',
        required=True, default=datetime.date.today())
    mentor_id = fields.Many2one("hr_hospital.doctor")
    comment = fields.Text()
    research_id = fields.Many2many("hr_hospital.research")

    @api.onchange('doctor_id')
    def onchange_doctor(self):
        for rec in self:
            rec.mentor_id = rec.doctor_id.mentor_id
