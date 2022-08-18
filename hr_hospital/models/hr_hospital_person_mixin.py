from odoo import fields, models


class PersonMixin(models.AbstractModel):
    _name = 'hr_hospital.person.mixin'
    _description = 'Person mixin'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    middle_name = fields.Char(required=True)
    phone = fields.Char(required=True)
    email = fields.Char()
    photo = fields.Image(max_width=256, max_height=256)
    gender = fields.Selection(
        default='other',
        string='Gender selection',
        selection=[('male', 'Male'),
                   ('female', 'Female'),
                   ('other', 'Other'), ],
        required=True, )

    def name_get(self):
        res = []
        for rec in self:
            if rec.middle_name:
                middle_name = rec.middle_name
            else:
                middle_name = ""
            res.append((rec.id,
                        "%s %s %s" % (rec.last_name, rec.first_name, middle_name)
                        ))
        return res
