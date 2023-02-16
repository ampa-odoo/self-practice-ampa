from odoo import models,fields,exceptions,api

class PowerschoolStudentFees(models.Model):
    
    _name = "powerschool.student.fees"
    _description = "Student's fees details"

    fees_serial_number = fields.Char()
    amount = fields.Integer()
    date = fields.Date(default=fields.Datetime.today(),required=True)
    student_id = fields.Many2one("powerschool.student",string="Student")
    status = fields.Selection(
            
            [('verified','Verified'),
             ('not verified','Not Verified')]
             ,default = "not verified",
             string="Fees details"
    )
#     to calculate the amount of fees paid till now so that we can directly use it in calculating the remaining fees
#     totalfees_paid_tillnow = fields.Char(compute="_compute_totalfees_paid")
#     @api.depends('fees_paid')
#     def _compute_totalfees_paid(self):
#          for record in self:
#               total = sum(student.fees_paid for student in record.student_id.fees_ids)
#               record.totalfees_paid_tillnow = total
              
               #for manually verifying the fees
    def verified_fees(self):
            self.status = "verified"
        #     raise exceptions.UserError("Fees Verified")
    def notverified_fees(self):
        self.status = "not verified"
        # raise exceptions.UserError("Fees Not Verified")