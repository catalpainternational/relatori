# The names here are less than good. Needs revision
from datetime import datetime

from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioFieldRenderer
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _

from health_service.models import HealthFacilityType, HealthFacility
from relatori import models


class NewDataForm(forms.Form):
    facility_queryset = models.Settings.objects.all()[0].facility.descendants.exclude(type__name__icontains="SISCA").exclude(type__name__icontains="Subdistrict")
    facility = forms.ModelChoiceField(label=_('Health Facility'), queryset=facility_queryset, required=False, empty_label=None)
    #facility = forms.ModelChoiceField(label=_('Health Facility'), required=False, empty_label=None)
    #TODO: only look for data form types that are not retired or voided
    data_form_type = forms.ModelChoiceField(label=_('Data Form'), queryset=models.DataFormType.objects.all().order_by('sheet_index'),required=False, empty_label=None)


class QueryForm(forms.Form):
    MONTHS = tuple((x, x) for x in range(13)[1:])
    YEARS = tuple((x, x) for x in range(2010, datetime.now().year+1))
    facility_queryset = models.Settings.objects.all()[0].facility.descendants.exclude(type__name__icontains="SISCA").exclude(type__name__icontains="Subdistrict")
        
    facility = forms.ModelChoiceField(label=_('Health Facility'), queryset=facility_queryset, required=False, empty_label=None)
    #TODO: only look for data form types that are not retired or voided
    data_form_type = forms.ModelChoiceField(label=_('Form'), queryset=models.DataFormType.objects.all(), required=False,empty_label=None)
    year = forms.ChoiceField(label=_('Year'),required=False, choices=YEARS,)


class CumulativeForm(forms.Form):
    MONTHS = tuple((x, x) for x in range(13)[1:])
    YEARS = tuple((x, x) for x in range(2010, datetime.now().year+1))

    # this is hackish but it works at concatenating querysets
    # Get Queryset containing the facility
    facility = HealthFacility.objects.filter(pk=models.Settings.objects.all()[0].facility.pk)

    # Get Queryset containing the facility's children
    descendants = models.Settings.objects.all()[0].facility.descendants.exclude(type__name__icontains="SISCA")

    # concatenate to form new QuerySet
    facility_queryset = facility | descendants 

    # finally, the form itself
    facility = forms.ModelChoiceField(label=_('Health Service'), queryset=facility_queryset, required=False, empty_label=None)
    #TODO: only look for data form types that are not retired or voided
    data_form_type = forms.ModelChoiceField(label=_('Form'), queryset=models.DataFormType.objects.all(), required=False,empty_label=None)
    start_month = forms.ChoiceField(label=_('Start month'), required=False, choices=MONTHS,)
    #start_year = forms.ChoiceField(label=_('Start year'),required=False, choices=YEARS,)
    end_month = forms.ChoiceField(label=_('End month'),required=False, choices=MONTHS,)
    #end_year = forms.ChoiceField(label=_('End year'),required=False, choices=YEARS,)
    year = forms.ChoiceField(label=_('Year'),required=False, choices=YEARS,)


class SummaryReportForm(forms.Form):
    YEARS = tuple((x, x) for x in range(2010, datetime.now().year+1))
    
    # Get Queryset containing the facility
    facility = HealthFacility.objects.filter(pk=models.Settings.objects.all()[0].facility.pk)
    
    # If the facility is set to a subdistrict get the parent district
    if facility[0].type.name.startswith("Subdistrict"):
        facility = HealthFacility.objects.filter(pk=facility[0].parent.pk)
    
    # Get Queryset containing the facility's children
    descendants = facility[0].descendants.filter(type__name__icontains="Subdistrict")
    # concatenate to form new QuerySet
    facility_queryset = facility | descendants
        
     
    # finally, the form itself
    facility = forms.ModelChoiceField(label=_('Health Service'), queryset=facility_queryset, required=False, empty_label=None)
    year = forms.ChoiceField(label=_('Year'),required=False, choices=YEARS,)


class DataFormExcelExportForm(forms.Form):
    data_form = forms.CharField(widget=forms.HiddenInput())


class AggregateDataFormExcelExportForm(forms.Form):
    facility = forms.CharField(widget=forms.HiddenInput())
    data_form_type = forms.CharField(widget=forms.HiddenInput())
    start_month = forms.CharField(widget=forms.HiddenInput())
    end_month = forms.CharField(widget=forms.HiddenInput())
    year = forms.CharField(widget=forms.HiddenInput())


class SyncForm(forms.Form):
    file = forms.FileField(label=_('Choose database file'),)


class SettingsForm(forms.ModelForm):
    class Meta:
        model = models.Settings
        fields = ('facility',)
    
