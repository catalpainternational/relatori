from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db.models import Sum

import djtables

from catalpa.relatori import models

class QueryTable(djtables.Table):
    hmis_form_type = djtables.Column(name=_('Form'), value=lambda cell: cell.object,  link=lambda cell: "../view/%s/" % cell.object.pk, sortable=False,)
    #Fetch the changed date from the operation where it would be latest operation that 
    #date_changed  = djtables.Column(name=_('Date of Last Change'), value=lambda cell: '%s/%s/%s' % (cell.object.date_changed.day, cell.object.date_changed.month, cell.object.date_changed.year), sortable=False,)
    date_changed  = djtables.Column(name=_('Date of Last Change'), value=lambda cell: '%s/%s/%s' % (cell.object.last_modified.day, cell.object.last_modified.month, cell.object.last_modified.year), sortable=True,)
    
    
    class Meta:
        per_page = 12
        #order_by = "date_changed"


class SummaryTable(djtables.Table):
    #denominator_type = lambda cell: cell.object.denominator_type
    
    #denominator = models.Denominator.objects.filter(denominator_type = denominator_type,).aggregate(Sum('value'))['value__sum']
    #indicator_raw = indicator_type.cells.aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
    #indicator_percent = float(indicator_raw) / float(denominator) * 100
    
    indicator_type = djtables.Column(name=_('Indicator'), value=lambda cell: cell.object.name, sortable=False,)
    #total  = djtables.Column(name=_('Total'), value=indicator_raw, sortable=False,)
    target = djtables.Column(name=_('Target'), value=lambda cell: cell.object.cells.aggregate(Sum('cell_data__value')).get('cell_data__value__sum'), sortable=False,)
    #percent = djtables.Column(name=_('Coverage Rate'), value=indicator_percent, sortable=False,)

    class Meta:
        per_page = 25
