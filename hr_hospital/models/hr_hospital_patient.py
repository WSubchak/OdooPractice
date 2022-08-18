import datetime

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api


class HrHospitalPatient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['hr_hospital.person.mixin', ]

    name = fields.Char()
    active = fields.Boolean(default=True)
    age = fields.Integer(string='Age patient',
                         compute='_compute_age',
                         store=True)
    birthday_date = fields.Date(string='Birthday', required=True)
    passport_series = fields.Char(string='series', required=True, size=2)
    passport_number = fields.Char(string='number', required=True, size=6)
    passport_issued_date = fields.Date(string='date of issued')
    passport_issued_by = fields.Char(string='issued by')

    contact_person_id = fields.Many2one('res.partner', string='Contact person')

    doctor_id = fields.Many2one('hr_hospital.doctor', string='Personal doctor')
    doctor_history_ids = fields.Many2many('hr_hospital.doctor.history')

    @api.depends('birthday_date')
    def _compute_age(self):
        for rec in self:
            now = datetime.date.today()
            if rec.birthday_date:
                difference = relativedelta(now, rec.birthday_date)
                rec.age = difference.years

    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        for rec in self:
            lines = []
            vals = {
                'change_date': datetime.date.today(),
                'patient_id': rec.id,
                'doctor_id': rec.doctor_id
            }
            lines.append((0, 0, vals))
            rec.doctor_history_ids = lines

    # def name_get(self):
    #     return [(rec.name,
    #              "%s %s" % (rec.last_name,
    #                             rec.first_name)
    #              ) for rec in self]
