# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class NoteStudent(models.Model):
    _name = 'note.student'
    _description = 'Student'

    name = fields.Char(string='Name')
    registration_number = fields.Char(string='Registration number')
    date_of_birth = fields.Date(string='Date of birth')
    sex = fields.Selection([('male','Male'),('female','Female')], string='Sex')
    age = fields.Integer(string='Age')
    student_class = fields.Many2one('note.class')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for student in self:
            today = date.today()
            if student.date_of_birth:
                student.age = today.year - student.date_of_birth.year
            else:
                student.age = 0


