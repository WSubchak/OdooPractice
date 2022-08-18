from odoo import fields, models


class HrHospitalIllness(models.Model):
    _name = 'hr_hospital.illness'
    _description = 'Illness'

    name = fields.Char()
    active = fields.Boolean(default=True)
    illness_category_id = fields.Many2one('hr_hospital.illness.category', required=True)
    comment = fields.Text()
