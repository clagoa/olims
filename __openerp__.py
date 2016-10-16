# -*- coding: utf-8 -*-
{
    'name': "OLiMS",

    'summary': """Open Source LIMS""",

    'description': """
        OLiMS Modules:
            - Analysis management
            - Sampling management
    """,

    'author': "Lablynx Inc.",
    'website': "http://www.lablynx.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','mail','report','report_webkit'],

    # always loaded
    'data': [
        'data/res.groups.csv',
        'demo.xml',
        'views/olims.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        'security/ir.model.access.csv',
        'workflows/sample_workflow.xml',
        'data/workflow.csv',
        'data/workflow.activity.csv',
        'data/workflow.transition.csv',
        'data/olims.country.csv',
        'data/olims.state.csv',
        'olims_report.xml',
        'views/report_sample.xml',
        'views/report_analysisper_service.xml',
        'views/report_analysisper_sample_type.xml',
        'views/report_sample_received_vs_reported.xml',
        'views/report_ar_and_analyses_per_client.xml',
        'views/report_analyses_per_department.xml',
        'views/report_analysesperformedpertotal.xml',
        'views/report_dataentrydaybook.xml',
        'views/report_analysis_request.xml',
        'views/report_invoice_detail.xml',
        'views/report_order_detail.xml',
        'wizard/olims_report_commom_view.xml',
        'wizard/olims_report_sample_view.xml',
        'wizard/olims_report_analysisper_service.xml',
        'wizard/olims_analysis_per_sample_type_report.xml',
        'wizard/olims_sample_received_vs_reported_view.xml',
        'wizard/olims_ar_and_analyses_per_client_view.xml',
        'wizard/olims_analyses_per_department_view.xml',
        'wizard/olims_analysesperformedpertotal_view.xml',
        'wizard/olims_dataentrydaybook_view.xml',
        'views/olimsscheduler.xml',
        'security/olims_security.xml',
        'views/templates.xml',
        'views/labpal_database_template.xml',
        'views/labpal_experiment_template.xml',
        'views/labpal_mail_template.xml',
        'views/views.xml',
        'views/report_ws_manage_results.xml',
        'views/print_sample_labels.xml',
        'views/mail_template_data.xml',
        'wizard/message_dialog_box.xml',
        'views/analysis_request_labels.xml',
        'views/ws_print_ar_label.xml',
        'views/ws_manage_results_analysis.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
        'data/res.users.csv',
        'data/olims.lab_contact.csv',
        'data/olims.department.csv',
        'data/olims.lab_product.csv',
        'data/olims.ar_priority.csv',
        'data/olims.client.csv',
        'data/olims.contact.csv',
        'data/olims.container_type.csv',
        'data/olims.preservation.csv',
        'data/olims.storage_location.csv',
        'data/olims.container.csv',
        'data/olims.sample_matrix.csv',
        'data/olims.sample_type.csv',
        'data/olims.sample_point.csv',
        'data/olims.method.csv',
        'data/olims.manufacturer.csv',
        'data/olims.supplier.csv',
        'data/olims.supplier_contact.csv',
        'data/olims.instrument_type.csv',
        'data/olims.instrument.csv',
        'data/olims.analysis_category.csv',
        'data/olims.calculation.csv',
        'data/olims.analysis_service.csv',
        'data/olims.records_field_artemplates.csv',
        'data/olims.analysis_profile.csv',
        'data/olims.specification.csv',
        'data/olims.analysis_spec.csv',
        'data/olims.ar_template.csv',
        'data/olims.sampling_deviation.csv',
        'data/olims.users_login_detail.csv',
    ],

    'css': ['static/css/js/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    #Added installation method for odoo to recognize new module
    'installable': True,
    'application': True,
    'auto_install': False,
    'web_preload': True,
}

