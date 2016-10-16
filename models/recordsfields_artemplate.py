from openerp import fields, models, api
from base_olims_model import BaseOLiMSModel
from openerp.tools.translate import _

schema = (fields.Many2one(string='Services',
                   comodel_name='olims.analysis_service',
                   domain="[('category', '=', Category)]",
                   relation='recordfield_service'),
          fields.Boolean(string='Hidden',readonly=False),
          fields.Float(string='Price', default=0.00,compute='_ComputeServicePriceField'),
        fields.Many2one(string='Partition',
                  comodel_name='olims.partition_ar_template'),
        fields.Many2one(string='Category',
                    comodel_name='olims.analysis_category'),
          )
analysis_schema = (fields.Many2one(string='Priority',
                                   comodel_name='olims.ar_priority'),
                   fields.Many2one(string='Partition',
                                   comodel_name='olims.ar_partition'),
                   fields.Char(string="Error"),
                   fields.Char(string="Min"),
                   fields.Char(string="Max"),
                   fields.Many2one(string='analysis_request_id', comodel_name ='olims.analysis_request'),
                   )

class RecodrdsFieldARTemplate(models.Model, BaseOLiMSModel): 
    _name='olims.records_field_artemplates'

    @api.onchange('Services')
    def _ComputeServicePriceField(self):
        # set auto-changing field
        for item in self:
            if item.Services:
                item.Price = item.Services.Price
    @api.onchange('Services')
    def _OnChangeGetServiceHiddenField(self):
        # set auto-changing field
        if self.Services:
            self.Hidden = self.Services.Hidden
class ARAnalysis(models.Model, BaseOLiMSModel):
    _inherit = 'olims.records_field_artemplates'
    _name = 'olims.ar_analysis'

    @api.multi
    def show_delete_warring_message_form(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        form_id = ir_model_data.get_object_reference('olims', 'view_delete_message_dialog_box')[1]
        return {
            'name': _('Confirm'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'olims.message_dialog_box',
            'views': [(form_id, 'form')],
            'view_id': form_id,
            'target': 'new',
        }
    
RecodrdsFieldARTemplate.initialze(schema)
ARAnalysis.initialze(analysis_schema)