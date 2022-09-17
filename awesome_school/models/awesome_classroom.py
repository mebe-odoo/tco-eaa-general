# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AwesomeClassroom(models.Model):
    _name = 'awesome.classroom'
    _description = 'Awesome Classroom'

    name = fields.Char("Name", required=True)
    capacity = fields.Integer("Capacity", default=10)
    teacher_id = fields.Many2one("res.partner", "Teacher", required=True)
    student_ids = fields.Many2many("res.partner", string="Students")
