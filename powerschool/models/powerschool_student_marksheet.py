from odoo import models,fields

class PowerSchoolMarksheet(models.Model):
    
    _name = "powerschool.student.marksheet"
    _description = "Student's marksheet"

    marksheet_id = fields.Char()
    subject_name = fields.Many2one("powerschool.student.subjects",string="subjects",required=True)
    subject_grade = fields.Many2one("powerschool.student.grades",required=True)
    student_id = fields.Many2one("powerschool.student",string="Student")
    