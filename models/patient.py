# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _
from odoo.exceptions import ValidationError


class ResPartners(models.Model):
    _inherit = 'res.partner'



class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'


    name = fields.Char(string="Contact Number")
    name_seq = fields.Char(string='patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], default='male', string="Gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string="Age Group", compute='set_age_group', store=True)
    patient_name = fields.Char(string='Name')
    patient_city = fields.Char(string='City')
    patient_age = fields.Integer('Age', track_visibility="always", group_operator=False)
    notes = fields.Text(string="Registration Note")
    image = fields.Binary(string="Image", attachment=True)
    active = fields.Boolean("Active", default=True)
    doctor_id = fields.Many2one('hospital.doctor', string="doctor")
    email_id = fields.Char(string="Email")
    user_id = fields.Many2one('res.users', string="PRO")

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(Patient, self).create(vals)
        return result
