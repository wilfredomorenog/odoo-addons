# -*- coding: utf-8 -*-
from openerp import http


class Academy(http.Controller):

    @http.route('/partner/credit/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('ox_web_partner_credit_amount.index', {
            'partners': http.request.env['res.partner'].sudo().search([('ref', '=', kw.get('ref'))]) if kw.get(
                'ref') else False
        })
