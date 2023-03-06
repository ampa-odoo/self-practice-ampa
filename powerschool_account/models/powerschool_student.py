from odoo import models,Command

class PowerschoolStudent(models.Model):
    _name = "powerschool.student"
    _description = "Student Management portal"
    _inherit = "powerschool.student"

    def _compute_total_fees_paid(self):
        print("hi")
        self.env['account.move'].check_access_rights('write')
        self.env['account.move'].check_access_rule('write')
        self.env['account.move'].create(
            {
                
                'partner_id': self.name_id.id,
                'move_type' : 'out_invoice',
                'invoice_line_ids' : [
                    Command.create({
                        'name' : self.name_id,
                        'quantity' : 1,
                        'price_unit' : (self.total_fees - self.totalfees_paid_tillnow)
                    }),
                ]
            }
        )
        return super()._compute_total_fees_paid()