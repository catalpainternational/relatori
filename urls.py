from django.conf.urls.defaults import *
from django.conf import settings

from hmis.relatori import models

urlpatterns = patterns('',
    (r'^new/$', 'hmis.relatori.views.new'),
    (r'^settings/$', 'hmis.relatori.views.preferences'),
    (r'^query/$', 'hmis.relatori.views.query'),
    (r'^cumulative/$', 'hmis.relatori.views.cumulative'),
    (r'^edit/(?P<item_pk>[\w]{8}(-[\w]{4}){3}-[\w]{12})', 'hmis.relatori.views.edit'),
    (r'^edit/$', 'hmis.relatori.views.edit'),
    (r'^view/(?P<item_pk>[\w]{8}(-[\w]{4}){3}-[\w]{12})', 'hmis.relatori.views.view'),
#    (r'^csv/(?P<item_pk>[\w]{8}(-[\w]{4}){3}-[\w]{12})', 'hmis.relatori.views.export_csv'),
    (r'^report/$', 'hmis.relatori.views.report'),
    (r'^cumulative/xls/$', 'hmis.relatori.views.export_aggregate_to_xls'),
    (r'^data_form/xls/$', 'hmis.relatori.views.export_to_xls'),
    (r'^summary/$', 'hmis.relatori.views.summary'),
    (r'^summary_report/$', 'hmis.relatori.views.summary_report'),
    (r'^summary_report/pdf/$', 'hmis.relatori.views.summary_report_as_pdf'),
    (r'^sync/$', 'hmis.relatori.views.sync'),
    (r'^$', 'hmis.relatori.views.index'),
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATICFILES_ROOT}),
    )
    
if 'reporting' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^reporting/', include('reporting.urls')),
    )
