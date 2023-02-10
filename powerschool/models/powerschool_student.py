from odoo import models,fields
from dateutil.relativedelta import relativedelta

class PowerschoolStudent(models.Model):

    _name = "powerschool.student"
    _description = "Student Management portal"

     
    name = fields.Char(required=True,string="Name")
    gender = fields.Selection(
        string = "Gender",
        selection = [('male','Male'),('female','Female')],
        default="male",
        required=True
    )
    birthdate = fields.Date(default=fields.Datetime.today())
    standard = fields.Integer(required=True,default="1",copy=False)
    address = fields.Char(required=True)
    referal_from = fields.Char()
    referal_to = fields.Char()
    height = fields.Float(string="Height(in cms)") 
    weight = fields.Float(string="Weight(in kgs)")
    mobile = fields.Char()
    email = fields.Char()
    Aadharno = fields.Char()
    tshirtSize = fields.Selection(
        string='Tshirt-Size',
        selection=[('xx small', 'XX Small'), ('x small', 'X Small'), ('small', 'Small'), ('medium', 'Medium'),('large','Large'),('x large','X Large')],
        help="Select student's Tshirt Size!",
        required=True,
        default="small",
        copy=False
        )
    admissionDate = fields.Date(default=fields.Datetime.today(),required=True)
    feesDueDate = fields.Date(default=lambda self: fields.Datetime.now()+relativedelta(months=3),copy=False,string="Fee Installment(Due date)")
    Disabled = fields.Boolean()
    parents = fields.Selection(string="Parents",selection=[('a','A'),('b','B')])
    fees = fields.Char()
    state = fields.Selection([
        ('counselling','Counselling'),
        ('admission confirmed','Admission Confirmed'),
        ('fees paid','Fees Paid'),
        ]
        )
    image = fields.Binary()
    marksheet_ids = fields.One2many("powerschool.student.marksheet","student_id")
    #course_id = fields.Many2one('student.course', string='Course')
