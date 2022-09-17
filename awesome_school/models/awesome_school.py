# -*- coding: utf-8 -*-

from odoo import models, fields, api


class awesome_school(models.Model):
    _name = 'awesome.school'
    _description = 'Awesome School'

    name = fields.Char("Name", required=True)
    supervisor_id = fields.Many2one("res.partner","Supervisor", required=True)
    establishment_date = fields.Date("Established On")

    street = fields.Char("Street", required=True)
    street2 = fields.Char("Street 2")
    city = fields.Char("City", required=True)
    zip = fields.Char("Zip Code")
    state_id = fields.Many2one("res.country.state", "State", required=True)
    country_id = fields.Many2one("res.country", "Country", required=True)

    classroom_ids = fields.Many2many("awesome.classroom", string="Classrooms")
