from odoo import fields, models


class HrHospitalIllnessCategory(models.Model):
    _name = 'hr_hospital.illness.category'
    _description = 'Illness category'
    _parent_store = True

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('hr_hospital.illness.category', ondelete='cascade')
    parent_path = fields.Char()
    child_id = fields.One2many('hr_hospital.illness.category', 'parent_id')
