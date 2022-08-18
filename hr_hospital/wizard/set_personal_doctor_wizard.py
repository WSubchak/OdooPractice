from odoo import fields, models


class SetPersonalDoctor(models.TransientModel):
    _name = 'hr_hospital.doctor.wizard'
    _description = 'Set new personal doctor'

    name = fields.Char()
    doctor_id = fields.Many2one("hr_hospital.doctor", string='New personal doctor')
    patient_ids = fields.Many2many("hr_hospital.patient")

    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res['patient_ids'] = [(6, 0, self._context.get('active_ids'))]
        return res

    def action_set(self):
        for rec in self.patient_ids:
            rec.doctor_id = self.doctor_id
