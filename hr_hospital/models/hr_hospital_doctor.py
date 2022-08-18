from odoo import fields, models


class HrHospitalDoctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['hr_hospital.person.mixin', ]

    name = fields.Char()
    active = fields.Boolean(default=True)
    speciality = fields.Char(required=True)
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one("hr_hospital.doctor", string="Mentor", domain=[('is_intern', '=', False)])

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, '%s %s' % (rec.last_name, rec.first_name)))
    #     return result
