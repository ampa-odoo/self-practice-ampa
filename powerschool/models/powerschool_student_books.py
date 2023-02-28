from odoo import models,fields,exceptions,api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class PowerschoolStudentBooks(models.Model):
    
    _name = "powerschool.student.books"
    _description = "Student's library books details"
    _rec_name = "book_name"

    book_serial_number = fields.Char(required=True)
    student_id = fields.Many2one("powerschool.student",string="Student")
    book_name = fields.Char()
    issue_date = fields.Date(default=fields.date.today())
    actual_return_date = fields.Date()
    return_date = fields.Date(compute="_compute_return_date")
    count = fields.Integer(compute="_compute_count")
    fine = fields.Integer(compute="_compute_fine")
    # books_count = fields.Integer(compute="_compute_books_issued")

    @api.depends("issue_date")
    def _compute_return_date(self):
        for record in self:
            record.return_date = record.issue_date + relativedelta(days=15)
            
    # for calculating fine 
    @api.depends("return_date","actual_return_date")
    def _compute_count(self):
        for record in self:
            if record.actual_return_date:
                record.count = (record.actual_return_date - record.return_date).days
            else:
                record.count = 0

    @api.depends("count","return_date","actual_return_date")
    def _compute_fine(self):
            for record in self:
                if record.actual_return_date:
                    record.fine = record.count * 5
                else:
                    record.fine = 0

    # for calculating books issued by each student
    @api.depends("book_serial_number")
    def _compute_books_issued(self):
        for record in self:
            if record.book_serial_number:
                record.books_count = len(record.book_serial_number)
            else:
                record.books_count = 0
