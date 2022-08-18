from odoo import fields, models


class HrHospitalResearchType(models.Model):
    _name = 'hr_hospital.research.type'
    _description = 'Research type'

    name = fields.Char()
    active = fields.Boolean(default=True)

    parent_id = fields.Many2one('hr_hospital.research.type', ondelete='cascade')
    parent_path = fields.Char()
    child_id = fields.One2many('hr_hospital.research.type', 'parent_id')
