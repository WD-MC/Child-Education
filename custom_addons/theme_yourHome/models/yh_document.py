from odoo import models, fields

class YourHomeDocuments(models.Model):
    _name = 'yh.documents'
    _description = 'Your Home Documents'

    #document_id = fields.Many2one('res.document', string='Document')
    #title_id = fields.Many2one('res.document.title', domain="[('document_id', '=?', document_id)]", string='Document/Title')
    name = fields.Char(string='Name', required=True)
    #country_id = fields.Many2one('res.country', string='Document')
    #state_id = fields.Many2one('res.country.state', domain="[('country_id', '=?', country_id)]", string='Document/Title')
    description = fields.Text()
    image = fields.Binary()