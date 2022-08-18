from odoo import fields, models


class HrHospitalResearch(models.Model):
    _name = 'hr_hospital.research'
    _description = 'Research'

    name = fields.Char()
    active = fields.Boolean(default=True)
    patient_id = fields.Many2one("hr_hospital.patient")
    doctor_id = fields.Many2one("hr_hospital.doctor")
    research_type_id = fields.Many2one("hr_hospital.research.type")
    sample_type_id = fields.Many2one("hr_hospital.sample.type")
    conclusion = fields.Text()
