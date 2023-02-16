from odoo import models,fields,api,exceptions
from dateutil.relativedelta import relativedelta
from datetime import datetime

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
    birthdate = fields.Date(string='Birthdate')
    standard = fields.Integer(required=True,default="1",copy=False)
    address = fields.Char()
    referal_from = fields.Char()
    referal_to = fields.Char()
    height = fields.Float(string="Height(in cms)") 
    weight = fields.Float(string="Weight(in kgs)")
    mobile = fields.Char()
    email = fields.Char()
    total_fees = fields.Integer(required=True)
    
    
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
    # totalfees = fields.Integer()
    state = fields.Selection(selection=[
        ('counselling','Counselling'),
        ('admission confirmed','Admission Confirmed'),
        ('fees paid','Fees Paid'),
        ]
        )
    image = fields.Binary()
    marksheet_ids = fields.One2many("powerschool.student.marksheet","student_id")
    fees_ids = fields.One2many("powerschool.student.fees","student_id")
    #course_id = fields.Many2one('student.course', string='Course')

    # now to calculate the age on the basis of DOB
    age = fields.Integer(string='Age', compute='_compute_age', inverse='_inverse_age')
    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                birthdate = datetime.strptime(str(record.birthdate), '%Y-%m-%d').date()
                today = datetime.today().date()
                age = relativedelta(today, birthdate).years
                record.age = age

            # The strptime() method creates a datetime object from the given string.
            # Note: You cannot create datetime object from every string. The string needs to be in a certain format.

    def _inverse_age(self):
        for record in self:
            if record.age:
                today = datetime.today().date()
                birthdate = today - relativedelta(years=record.age)
                record.birthdate = birthdate.strftime('%Y-%m-%d')
        
            # The strftime() method returns a string representing date and time using date, time or datetime object.
    totalfees_paid_tillnow = fields.Integer(compute="_compute_total_fees_paid")
    @api.depends('totalfees_paid_tillnow')
    def _compute_total_fees_paid(self):
         for student in self:
             PowerschoolStudentFees = self.env['powerschool.student.fees'].search([('student_id', '=', student.id)])
             if PowerschoolStudentFees:
                 student.totalfees_paid_tillnow = sum(PowerschoolStudentFees.mapped('amount'))
             
              

# to compute remaining fees based on fees paid

    remaining_fees = fields.Integer(compute="_compute_remaining_fees")
    @api.depends('totalfees_paid_tillnow')
    def _compute_remaining_fees(self):
        for record in self:
            if (record.total_fees!=0):
                record.remaining_fees = record.total_fees-record.totalfees_paid_tillnow
            else:
                record.remaining_fees = record.total_fees
    



