from odoo import models,fields


class PowerSchoolStudentSubjects(models.Model):

    _name = "powerschool.student.subjects"
    _description = "Student subjects portal"
    _rec_name = 'subjectName'

    subjectName = fields.Char()
    facultyName = fields.Char()
    standard = fields.Char()
    subjectBook = fields.Binary(string="File")

    def name_get(self):
        result = []
        for aman in self:
            result.append((aman.id, "std-%s- %s" % (aman.standard, aman.subjectName or '')))
        return result