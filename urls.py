from django.conf.urls.defaults import *
from django.conf import settings

from catalpa.relatori import models

urlpatterns = patterns('',
    (r'^new/$', 'catalpa.relatori.views.new'),
    (r'^settings/$', 'catalpa.relatori.views.preferences'),
    (r'^query/$', 'catalpa.relatori.views.query'),
    (r'^cumulative/$', 'catalpa.relatori.views.cumulative'),
    (r'^edit/(?P<item_pk>[\w]{8}(-[\w]{4}){3}-[\w]{12})', 'catalpa.relatori.views.edit'),
    (r'^edit/$', 'catalpa.relatori.views.edit'),
    (r'^view/(?P<item_pk>[\w]{8}(-[\w]{4}){3}-[\w]{12})', 'catalpa.relatori.views.view'),
#    (r'^csv/(?P<item_pk>[\w]{8}(-[\w]{4}){3}-[\w]{12})', 'catalpa.relatori.views.export_csv'),
    (r'^report/$', 'catalpa.relatori.views.report'),
    (r'^cumulative/xls/$', 'catalpa.relatori.views.export_aggregate_to_xls'),
    (r'^data_form/xls/$', 'catalpa.relatori.views.export_to_xls'),
    (r'^summary/$', 'catalpa.relatori.views.summary'),
    (r'^summary_report/$', 'catalpa.relatori.views.summary_report'),
    (r'^summary_report/pdf/$', 'catalpa.relatori.views.summary_report_as_pdf'),
    (r'^sync/$', 'catalpa.relatori.views.sync'),
    (r'^$', 'catalpa.relatori.views.index'),
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATICFILES_ROOT}),
    )
    
if 'reporting' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^reporting/', include('reporting.urls')),
    )
