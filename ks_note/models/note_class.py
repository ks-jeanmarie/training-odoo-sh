# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NoteClass(models.Model):
    _name = 'note.class'
    _description = 'Class'

    name = fields.Char(string='Name')
    student_number = fields.Integer(string='Student number', compute='_compute_student_number')
    class_student = fields.One2many('note.student','student_class', string='Student')

    @api.depends('class_student')
    def _compute_student_number(self):
        for student in self:
            student.student_number = len(student.class_student)