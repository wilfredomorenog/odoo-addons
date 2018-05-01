# -*- coding: utf-8 -*-

import csv
import logging
import tempfile

from openerp import models, fields, api, _
from openerp.exceptions import ValidationError

_logger = logging.getLogger('PARTNER CREDIT AMOUNT')


class PartnerAmountresidual(models.Model):
    _inherit = 'res.partner'

    amount_residual = fields.Float(string='Amount residual')
    residual_history_ids = fields.One2many('res.partner.residual.history', 'partner_id', string='Residual history')

class PartnerAmountResidualHistory(models.Model):
    _name = 'res.partner.residual.history'

    amount_residual = fields.Float(string='Amount residual')
    partner_id = fields.Many2one('res.partner', string='Partner')


class Amountresidual(models.TransientModel):
    _name = 'partner.credit.amount'

    file = fields.Binary(string='File', help='File format .csv separate for ;')

    @api.multi
    def update_partner_credit_amount(self):
        file_path = tempfile.gettempdir() + '/update.csv'
        f = open(file_path, 'wb')
        f.write(self.file.decode('base64'))
        f.close()
        data_reader = csv.reader(open(file_path), delimiter=',')
        c = 0
        for content in data_reader:
            if len(content) == 3:
                if c > 0:
                    credit = content[2].replace(',', '').replace('-', '0').strip()
                    ref = content[0].strip()
                    try:
                        self.env.cr.execute(
                            ''' INSERT INTO res_partner_residual_history(partner_id,write_uid,write_date,amount_residual) 
                                        SELECT id, {user}, now(), {credit} FROM res_partner WHERE ref = '{ref}' '''.format(
                                user=self.env.user.id, credit=credit, ref=ref))
                        self.env.cr.execute(
                            ''' UPDATE res_partner SET amount_residual = amount_residual + {credit}::float WHERE ref = '{ref}' '''.format(
                                credit=credit, ref=ref))
                    except:
                        raise ValidationError(
                            _(
                                'There was an error updating the {ref} reference with the {value} value. Please verify').format(
                                ref=ref, value=credit))
            else:
                raise ValidationError(
                    _(
                        'The import file configured is 3 columns and the one that you try to upload has {}. Please verify.').format(
                        str(len(content))))
            c += 1
        return True
