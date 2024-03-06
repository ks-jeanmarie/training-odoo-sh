# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class NoteStudent(models.Model):
    _name = 'note.note'
    _description = 'Note'

    name = fields.Char(string='Name')
    subject = fields.Many2one('note.subject', string='Subject')
    student = fields.Many2one('note.student', string='Student')
    note = fields.Integer(string='Note')

    @api.onchange('date')
    def _onchange_date(self):
        for note in self:
            note.date = date.today()