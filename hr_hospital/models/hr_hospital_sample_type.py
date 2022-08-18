from odoo import fields, models


class HrHospitalSampleType(models.Model):
    _name = 'hr_hospital.sample.type'
    _description = 'Sample Type'

    name = fields.Char()
    active = fields.Boolean(default=True)
