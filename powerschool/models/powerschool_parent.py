from odoo import models,fields

class PowerschoolParent(models.Model):
    _name = "powerschool.parent"
    _description = "Parents Details portal"

    studentName = fields.Char()
    # note here we need to add the selection field to select the already added students
    parent = fields.Selection(
        string = "parent",
        selection = [('father','Father'),('mother','Mother'),('other guardian','Other Guardian')],
        default="mother",
        required=True
    )
    name = fields.Char()
    mobile = fields.Char(required=True)
    email = fields.Char(required=True)
    occupation = fields.Selection(
        string = "Occupation",
        selection=[('bussiness','Bussiness'),('job','Job'),('other','Other')]
    )
    AadharNo = fields.Char(required=True)
    Income = fields.Selection(
        string = "Family Income",
        selection=[('<2.5 lakhs','<2.5 lakhs'),
        ('2.5 lakhs to 5 lakhs','2.5 lakhs to 5 lakhs'),
        ('5 lakhs to 7.5 lakhs','5 lakhs to 7.5 lakhs'),
        ('above 7.5lakhs','above 7.5 lakhs')]
    )