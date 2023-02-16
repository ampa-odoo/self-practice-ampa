from odoo import models,fields


class PowerschoolStudentGrades(models.Model):

    _name = "powerschool.student.grades"
    _description = "Student Result Grades portal"

    name = fields.Char()
    priority = fields.Char()