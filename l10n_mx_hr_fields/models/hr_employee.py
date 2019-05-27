# Copyright <2019> <BerrySoft MX>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    # Citizenship fields
    curp = fields.Char(string="CURP")
    #social_insurance_number = fields.Char() REPLACED BY ssnid in hr_employee_ssn
    identification_id = fields.Char(string="INE")

