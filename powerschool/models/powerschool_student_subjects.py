from odoo import models,fields


class PowerSchoolStudentSubjects(models.Model):

    _name = "powerschool.student.subjects"
    _description = "Student subjects portal"

    subjectName = fields.Char()
    facultyName = fields.Char()
    standard = fields.Char()
    subjectBook = fields.Binary(string="File")