#import csv
import sys
import os
from datetime import datetime

from django import http
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson, translation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.db.models import Sum
from django.db import transaction
from django.http import HttpRequest, QueryDict
from django.core.management import call_command
from django import forms as _dForm
from django.forms.extras.widgets import SelectDateWidget

import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi

import xlrd 
import xlwt
from xlutils.copy import copy

#from hmis import settings
from settings import MEDIA_ROOT, LANGUAGE_CODE, DATABASES
from catalpa.relatori import models, forms, tables#, chart - _cairo i;por braks on windows
from catalpa.simple_locations.models import Facility, Area

from fsms_app.models import FSMSForm

from catalpa.aihun.models import Operation

from django.conf import settings
import copy


@login_required
def index(request):
    return render_to_response('catalpa/relatori/index.html',{
            'user' : request.user,
            'context_instance' : RequestContext(request),})


@login_required
def preferences(request):
    if request.method.upper() == 'GET':
        try:
            data = { 'facility' : models.Settings.objects.all()[0].facility.id }
        except:
            facility = Facility.objects.all()[0]
            data = { 'facility' : facility.id }
        form = forms.SettingsForm(data)
        return render_to_response('catalpa/relatori/settings.html',{
                'form' : form,
                'user' : request.user,
                'context_instance' : RequestContext(request),})

    if request.method.upper() == 'POST':
        form = forms.SettingsForm(request.POST)
        if form.is_valid():
            submit = request.POST.get('submit')
            if submit==u'Save':
                facility = form.cleaned_data['facility']
                try:
                    settings = models.Settings.objects.all()[0]
                except:
                    settings = models.Settings()
                    #settings.creator = request.user
                settings.facility = facility
                settings.save()
        
        messages.success(request, _('Thank you %s, you successfully saved settings.' % (request.user)))    
        return render_to_response('catalpa/relatori/index.html',{
                'user' : request.user,
                'context_instance' : RequestContext(request),})


def query(request):
    if request.method.upper() == 'GET':
        data = {
            'start_month' : 1,
            'end_month' : datetime.now().month,
            'year' : datetime.now().year,
            }
        form = forms.QueryForm(data)

        return render_to_response('catalpa/relatori/query.html',{
            'form' : form,
            'user' : request.user,
            'context_instance' : RequestContext(request),
        })
    elif request.method.upper() == 'POST':
        form = forms.QueryForm(request.POST)
        if form.is_valid():
            submit = request.POST.get('submit')
            if submit==u'Browse':
                data_form_type = form.cleaned_data['data_form_type']
                facility = form.cleaned_data['facility']
                #month_range = (form.cleaned_data['start_month'],form.cleaned_data['end_month'])
                year = form.cleaned_data['year']
                
                #data_forms = models.DataForm.objects.filter(data_form_type=data_form_type, facility=facility, month__range=month_range, year=year)
                data_forms = models.DataForm.objects.filter(data_form_type=data_form_type, facility=facility, year=year)
                return render_to_response('catalpa/relatori/query.html',{
                    'form': form,
                    'result': tables.QueryTable(data_forms, request=request),
                    'user' : request.user,
                    'context_instance' : RequestContext(request),
                })


def summary(request):
    if request.method.upper() == 'GET':

        indicator_type = models.IndicatorType.objects.all()

        return render_to_response('catalpa/relatori/summary.html',{
            'summary': tables.SummaryTable(indicator_type, request=request),
            'user' : request.user,
            'year' : datetime.now().year,
            'context_instance' : RequestContext(request),
        })

def summary_report(request):
    if request.method.upper() == 'GET':
        form = forms.SummaryReportForm()

        return render_to_response('catalpa/relatori/summary_report.html',{
            'form' : form,
            'user' : request.user,
            'context_instance' : RequestContext(request),
        })

    elif request.method.upper() == 'POST':
        form = forms.SummaryReportForm(request.POST)
        if form.is_valid():
            facility = form.cleaned_data['facility']
            # generate the bar charts
            chart.chart_by_name_by_quarter('k1', facility)
            chart.chart_by_names(('k1', 'k4'), facility)
            chart.chart_by_name_by_quarter('TT 2+', facility)
            chart.chart_by_name_by_quarter('Labarik  tinan < 5 nebe hetan teben', facility)
            chart.chart_by_name_by_quarter('Labarik tinan < 5 ho Pneomonia', facility)
            chart.chart_by_names(('bcg', 'sarampo'), facility)
            chart.chart_by_names(('polio', 'DPT-1', 'DPT-3'), facility)
            chart.chart_by_names(('weighed', 'moderate', 'severe'), facility)
            chart.chart_by_name_by_quarter('Vitamina', facility)
            chart.chart_by_name_by_quarter('Lumbriga', facility)
            # generate the pie charts
            chart.pie_chart_by_name('Deliveries attended by health personnel', facility)
            chart.pie_chart_by_name('PN-1', facility)
            chart.pie_chart_by_name('Labarik nebe mai foun registru', facility)
            chart.pie_chart_by_name('children weighed', facility)

            #return the template
            return render_to_response('catalpa/relatori/summary_report_index.html',{
                'facility' : facility,
            })
        else:
            return render_to_response('catalpa/relatori/summary_report.html',{
                'form' : form,
                'user' : request.user,
                'context_instance' : RequestContext(request),
            })


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), mimetype='application/pdf')
    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))


def summary_report_as_pdf(request):
    if request.method.upper() == 'GET':
        return render_to_pdf('catalpa/relatori/summary_report_index.html',{
        'facility' : 'District Health Service Manatuto',
        'pagesize':'A4',})
    

def cumulative(request):
    if request.method.upper() == 'GET':
        data = {
            'start_month' : 1,
            'end_month' : datetime.now().month,
            'year' : datetime.now().year,
            }

        form = forms.CumulativeForm(data)

        return render_to_response('catalpa/relatori/cumulative.html',{
            'form' : form,
            'user' : request.user,
            'context_instance' : RequestContext(request),
        })
    elif request.method.upper() == 'POST':
        form = forms.CumulativeForm(request.POST)
        if form.is_valid():

            data_form_type = form.cleaned_data['data_form_type']
            facility = form.cleaned_data['facility']
            # Heavy lifting done Here!  Within the date rage the aggregate value of each cell in the form is computed and stored in a list
            #TODO: could probably do this next block in one line
            month_range = (form.cleaned_data['start_month'],form.cleaned_data['end_month'])
            #year_range = (form.cleaned_data['start_year'],form.cleaned_data['end_year'])
            year = form.cleaned_data['year']

            if facility.type.name == u'District Health Service':
                cell_data = models.CellData.objects.filter(data_form__data_form_type=data_form_type, data_form__facility__parent__parent=facility, data_form__month__range=month_range, data_form__year__contains=year)
            elif facility.type.name == u'Subdistrict Health Service':
                # Aggregation happens here
                cell_data = models.CellData.objects.filter(data_form__data_form_type=data_form_type, data_form__facility__parent=facility, data_form__month__range=month_range, data_form__year__contains=year)
            else:
                cell_data = models.CellData.objects.filter(data_form__data_form_type=data_form_type, data_form__facility=facility, data_form__month__range=month_range, data_form__year__contains=year)

            cells = []

            #TODO: use annotations?
            #value_sums = cell_data.filter(cell__order=cell).annotate(Sum('value')).get('value__sum')
            for cell in range(data_form_type.cells.count()):
                value_sum = cell_data.filter(cell__order=cell).aggregate(Sum('value')).get('value__sum')
                cells.append(value_sum)

            hidden_form = forms.AggregateDataFormExcelExportForm(request.POST)
            fatin = facility.area

            if facility.area != None:
                if facility.area.kind.name == u'District':
                    distritu = facility.area
                    subdistritu = facility.area
                else:
                    distritu = facility.area.get_ancestors().get(kind__name='District')
                    subdistritu = facility.area.get_ancestors().get(kind__name='Subdistrict')
            else:
                distritu = subdistritu = ''


            context = { 
                    'user' : request.user,
                    'fulan' : "%s - %s" % month_range,
                    'tinan' : form.cleaned_data['year'],
                    'code' : facility.code,
                    'distritu' : distritu,
                    'subdistritu' : subdistritu,
                    'fatin' : fatin,
                    'facility' : facility,
                    'data_form_type' : data_form_type,
                    'cells' : cells,
                    'form' : hidden_form,
                    }
            #TODO: sheet_index + 1 is a hack, make it right
            sheet = data_form_type.sheet_index+1
            if sheet < 10:
                sheet = '0%s' % (sheet)
            return render_to_response('forms/form_0%s.html' % (sheet), context,) 
        else:
            return render_to_response('catalpa/relatori/cumulative.html',{
                'form': form,
                'user' : request.user,
                'context_instance' : RequestContext(request),
            })


def report(request):
    if request.method.upper() == 'GET':
        # load some reasonable defaults
        data = { 'start_month' : datetime.now().month-1,
                #'start_year' : datetime.now().year,
                'end_month' : datetime.now().month,
                #'end_year' : datetime.now().year,
                'year' : datetime.now().year,
                }
        form = forms.QueryForm(data)

        return render_to_response('catalpa/relatori/form.html',{
            'form': form,
            'user' : request.user,
            'context_instance' : RequestContext(request),
        })


@login_required
def new(request):
    if request.method.upper() == 'GET':
        data = {
                #'month' : datetime.now().month,
                #'year' : datetime.now().year,
                #'facility' : sl_m.Facility.objects.get(name="MAF Facility 001"),# Settings.objects.all()[0].facility.children.exclude(type__name__icontains="SISCA"),
                }
        form = forms.NewDataForm(data)

        return render_to_response('catalpa/relatori/new.html',{
            'form': form,
            'user' : request.user,
            'context_instance' : RequestContext(request),
        })
    
    elif request.method.upper() == 'POST':
        
        form = forms.NewDataForm(request.POST)
        if form.is_valid():
        
            data_form_type = form.cleaned_data['data_form_type']
            facility = form.cleaned_data['facility']
            
            subdistricts= Area.objects.filter(parent=facility.area)
            form_sucos = []
            form_subdis = ""
            sub_options = []
            n = 1
            sub_options.append((0,""))
            suco_options_string=""
            for sub in subdistricts:
                s=[]
                for suco in Area.objects.filter(parent=sub):
                    s.append((suco.code,suco.name))
                suco_f = _dForm.Select(choices=tuple(s))
                form_sucos.append(suco_f.render("form_suco %d"%n,"suco_form"))
                sub_options.append((n,sub.name))
                n+=1
            
            sub_select = _dForm.Select(choices=tuple(sub_options))
            form_subdis = sub_select.render("form_subdis",'subdis')
            try: distritu = facility.area#.get_ancestors().get(kind__name='District')
            except: distritu = None
            try: subdistritu = facility.area.get_ancestors().get(kind__name='Subdistrict')
            except: subdistritu = None
            
            cells = [0 for cell in  range(data_form_type.cells.count())]
            cell_styles = ['cell_data' for cell in  range(data_form_type.cells.count())]
            fulan_style = 'cell_data'
            tinan_style = 'cell_data'

            ## Generating the HTML 'input' using django forms
            actual_cells = data_form_type.cells.all()


            cell_dico = {}
            for cell in actual_cells:
                dgroups = cell.data_groups.all()
                inp = _dForm.TextInput()
                for dg in dgroups:
                    opti = dg.options.all()
                    if opti.count()==2:
                        oList = tuple((o.value,o.name) for o in opti)
                        inp = _dForm.RadioSelect(choices=oList)
                    elif opti.count()>2:
                        oList = tuple((o.value,("%d:%s" % (o.value,o.name))) for o in opti)
                        inp = _dForm.Select(choices=oList)
                    elif opti.count()==0 and dg.value=="Options - BOOL":
                        inp = _dForm.CheckboxInput()
                    elif opti.count()==0 and dg.value=="Options - DATE":
                        inp = _dForm.DateInput()
                        
                cell.html = inp.render("c.%s" % (cell.spreadsheet_cell),'')
                cell_dico[cell.spreadsheet_cell]=cell
            ## Now sending the actual cells to the template.
            fulan = tuple((n,n) for n in range(1,13))
            fulan = _dForm.Select(choices=fulan)
            fulan = fulan.render("fulan",'')
            
            tinan = tuple((n,n) for n in range(datetime.now().year -1, datetime.now().year+2))
            tinan = _dForm.Select(choices=tinan)
            tinan = tinan.render("tinan",'')

            form_comment = _dForm.Textarea()
            form_comment = form_comment.render("form_commentario","")

            context = { 
                    'user' : request.user,
                    'fulan' : fulan,
                    'fulan_style' : fulan_style,
                    'tinan' : tinan,
                    'tinan_style' : tinan_style,
                    'code' : facility.code,
                    'debug' : "",
                    'distritu' : distritu,
                    'form_subdis' : form_subdis,
                    'form_suco': form_sucos,
                    'fatin' : facility.area,
                    'facility' : facility,
                    'data_form_type_pk' : data_form_type.pk,
                    'cells' : cells,
                    'cell_styles' : cell_styles,
                    'c' : cell_dico,
                    'form_commentario':form_comment,
                    }
            #TODO: sheet_index + 1 is a hack, make it right
            sheet = data_form_type.sheet_index+1
            if sheet < 10:
                sheet = '0%s' % (sheet)
            return render_to_response('forms/form_0%s.html' % (sheet), context,) 
        else:
            return render_to_response('catalpa/relatori/new.html',{
                'form': form,
                'user' : request.user,
                'context_instance' : RequestContext(request),
            })


@login_required
def edit(request, item_pk=None):
    if request.method.upper() == 'GET':
        if item_pk is None:
            try:
                item_pk = request.GET['item_pk']
            except:
                pass
        if item_pk != None:
            cells = [cell.value for cell in  models.CellData.objects.filter(data_form=item_pk).order_by('cell__order')]
            data_form = models.DataForm.objects.get(pk=item_pk)
            
            facility = data_form.facility
            cell_styles = ['cell_data' for cell in  range(data_form.cell_data.count())]
            fulan_style = 'cell_data'
            tinan_style = 'cell_data'
        
            context = { 
                    'user' : request.user,
                    'context_instance' : RequestContext(request),
                    'fulan' : data_form.month,
                    'fulan_style' : fulan_style,
                    'tinan' : data_form.year,
                    'tinan_style' : tinan_style,
                    'code' : facility.code,
                    'distritu' : facility.area.get_ancestors().get(kind__name='District'),
                    'subdistritu' : facility.area.get_ancestors().get(kind__name='Subdistrict'),
                    'fatin' : facility.area,
                    'facility' : facility,
                    'data_form_type_pk' : data_form.data_form_type.pk,
                    'cells'  : cells,
                    'cell_styles' : cell_styles,
                    'data_form' : item_pk,
                    }
            sheet = data_form.data_form_type.sheet_index+1
            if sheet < 10:
                sheet = '0%s' % (sheet)
            return render_to_response('forms/form_0%s.html' % (sheet), context,) 
        else:
            data = { 
                'start_month' : datetime.now().month-1,
                'end_month' : datetime.now().month,
                'year' : datetime.now().year,
                'facility' : '1',
                'data_form_type_pk' : models.DataFormType.objects.all()[0].pk,
                }
            form = forms.QueryForm(data)
            
            return render_to_response('catalpa/relatori/query.html',{
                'user' : request.user,
                'form': form,
                'context_instance' : RequestContext(request),
            })

    elif request.method.upper() == 'POST':
        form = request.POST

        submit = form.get('submit')
        
        if submit == 'Cancel':
            return HttpResponseRedirect('/relatori/new')
        
        facility_id = form.get('facility')
        facility = Facility.objects.get(id=facility_id)  #TODO switch to pk?

        data_form_type_pk = form.get('data_form_type_pk')
        data_form_type = models.DataFormType.objects.get(pk=data_form_type_pk)
        data_form = form.get('data_form')

        # Validation
        invalid = False
        cell_styles = []
        cells = []
        try:
            int(form.get('tinan'))
            tinan_style = 'cell_data'
        except:
            invalid = True
            tinan_style = 'cell_data_error'
        try:
            int(form.get('fulan'))
            fulan_style = 'cell_data'
        except:
            invalid = True
            fulan_style = 'cell_data_error'

        if invalid is False:
            data_form_count = models.DataForm.objects.filter(month=form.get('fulan'), 
                                                    year=form.get('tinan'), 
                                                    facility=form.get('facility'), 
                                                    data_form_type = form.get('data_form_type')).count()
        else:
            data_form_count = 0

        #########################################################
        ## Parsing and re generating the HTML 'input' using django forms
        actual_cells = data_form_type.cells.all()
        cell_dico = {}
        for cell in actual_cells:
            value = form.get('c.%s' % cell.spreadsheet_cell)
            dgroups = cell.data_groups.all()
            inp = _dForm.TextInput()
            type_field="int"

            for dg in dgroups:
                opti = dg.options.all()
                if opti.count()==2:
                    oList = tuple((o.value,o.name) for o in opti)
                    inp = _dForm.RadioSelect(choices=oList)
                elif opti.count()>2:
                    oList = tuple((o.value,("%d:%s" % (o.value,o.name))) for o in opti)
                    inp = _dForm.Select(choices=oList)
                elif opti.count()==0 and dg.value=="Options - BOOL":
                    inp = _dForm.CheckboxInput()
                    type_field="bool"
                elif opti.count()==0 and dg.value=="Options - DATE":
                    inp = _dForm.DateInput()
                    type_field="date"
                elif opti.count()==0 and dg.value=="Options - NAME":
                    type_field="name"
            try:
                if type_field == "int":
                    int(value)
                elif type_field == "date":
                    print "date:"+value
                elif  type_field == "bool":
                    print "bool:"+value
                elif  type_field == "name":
                    print "name:"+value
            except:
                print "Value was not correct:"+cell.spreadsheet_cell
                cell_styles.append('cell_data_error')
                invalid = True
                problem = cell.spreadsheet_cell 

            cell.html = inp.render("c.%s" % (cell.spreadsheet_cell),value)
            cell_dico[cell.spreadsheet_cell]=cell
        ## Now sending the actual cells to the template.
        fulan = tuple((n,n) for n in range(1,13))
        fulan = _dForm.Select(choices=fulan)
        fulan = fulan.render("fulan",form.get('fulan'))
            
        tinan = tuple((n,n) for n in range(datetime.now().year -1, datetime.now().year+2))
        tinan = _dForm.Select(choices=tinan)
        tinan = tinan.render("tinan",form.get('tinan'))
        
        form_comment = _dForm.Textarea()
        form_comment = form_comment.render("form_commentario",form.get('form_commentario'))

        try: distritu = facility.area#.get_ancestors().get(kind__name='District')
        except: distritu = None
        subdistricts= Area.objects.filter(parent=facility.area)
        form_sucos = []
        form_subdis = ""
        sub_options = []
        n = 1
        sub_options.append((0,""))
        suco_options_string=""
        for sub in subdistricts:
            s=[]
            for suco in Area.objects.filter(parent=sub):
                s.append((suco.code,suco.name))
            suco_f = _dForm.Select(choices=tuple(s))
            form_sucos.append(suco_f.render("form_suco %d"%n,"suco_form"))
            sub_options.append((n,sub.name))
            n+=1
            
        sub_select = _dForm.Select(choices=tuple(sub_options))
        form_subdis = sub_select.render("form_subdis",'subdis')
        try: distritu = facility.area#.get_ancestors().get(kind__name='District')
        except: distritu = None
            
        #########################################################
#        for cell in data_form_type.cells.all():
#            c.append(form.get('c.%s' % cell.spreadsheet_cell))
#            try:
#                int(cells[i])
#                cell_styles.append('cell_data')
#            except:
#                cell_styles.append('cell_data_error')
#                invalid = True
#                problem=i

        if (data_form_count is not 0) and (data_form is u''):
            invalid = True
            fulan_style = 'cell_data_error'
            tinan_style = 'cell_data_error'             
            messages.error(request, _(u'Form with this month and year already exists.'))
        if invalid:
            messages.error(request, _(u'Save failed. Please fix error.'))
            
            context = { 
                    'user' : request.user,
                    'context_instance' : RequestContext(request),
                    'fulan' : fulan,
                    'fulan_style' : fulan_style,
                    'tinan' : tinan,
                    'tinan_style' : tinan_style,
                    'code' : facility.code,
                    'distritu' : distritu,
                    #'subdistritu' : subdistritu,
                    'form_subdis' : form_subdis,
                    'form_suco': form_sucos,
                    'fatin' : facility.area,
                    'facility' : facility,
                    'data_form_type_pk' : data_form_type_pk,
                    'data_form' : data_form,
                    'cells' : cells,
                    'cell_styles' : cell_styles,
                    'c' : cell_dico,
                    'form_commentario':form_comment,
                    }
            #TODO: sheet_index + 1 is a hack, make it right
            sheet = data_form_type.sheet_index+1
            if sheet < 10:
                sheet = '0%s' % (sheet)
            return render_to_response('forms/form_0%s.html' % (sheet), 
                                        context, context_instance=RequestContext(request)) 
        
        if (data_form != u'') and (data_form != None):
            data_form = models.DataForm.objects.get(pk=data_form)
            data_form.month = form.get('fulan')
            data_form.year = form.get('tinan')
            data_form.save()
            op = Operation()
            op.modify(request.user,data_form,'Data update')
            op.save()

            for cell_data in data_form.cell_data.all():
                cell_data.value = form.get('c.%s' % cell_data.cell.spreadsheet_cell)
                cell_data.save()
        else:
            data_form = models.DataForm(data_form_type = data_form_type,
                                facility = facility, 
                                year = form.get('tinan'),
                                month = form.get('fulan')
                                #creator = request.user
                                        )
            data_form.save()
            op = Operation()
            op.create(request.user,data_form,'Initial entry')
            op.save()
            
            for cell in data_form_type.cells.all():
                cell_data = models.CellData(data_form = data_form,
                                            cell = cell,
                                            value = form.get('c.%s' % cell.spreadsheet_cell)
                                            #creator = request.user
                                            )
                cell_data.save()

       
        messages.success(request, _(u'Thank you, you successfully saved %(type)s (%(month)s/%(year)s) for %(facility)s.') % {'type': data_form.data_form_type, 'month': data_form.month, 'year': data_form.year, 'facility': data_form.facility})

        if submit == 'Save':
            if form.get('data_form') == u'': #TODO: Check this behavior
                # if there is no data_form id then we know that we're working on a new form
                return HttpResponseRedirect('/relatori/new')
            else:
                # otherwise it already exists and we'll redirect to the search page
                return HttpResponseRedirect('/relatori/query')

            context = { 
                    'user' : request.user,
                    'context_instance' : RequestContext(request),
                    'fulan' : form.get('fulan'),
                    'tinan' : form.get('tinan'),
                    'code' : facility.code,
                    'distritu' : facility.area.get_ancestors().get(kind__name='District'),
                    'subdistritu' : facility.area.get_ancestors().get(kind__name='Subdistrict'),
                    'fatin' : facility.area,
                    'facility' : facility,
                    'data_form_type' : data_form_type,
                    'data_form' : data_form
                    }
            #TODO: sheet_index + 1 is a hack, make it right
            sheet = data_form_type.sheet_index+1
            if sheet < 10:
                sheet = '0%s' % (sheet)
            return render_to_response('forms/form_0%s.html' % (sheet), context,) 


@login_required
def view(request, item_pk):
    cells = [cell_data.value for cell_data in  models.CellData.objects.filter(data_form=item_pk).order_by('cell__order')]

    data_form = models.DataForm.objects.get(pk=item_pk)
    data_form_type = data_form.data_form_type
    facility = data_form.facility
    
    form = forms.DataFormExcelExportForm({'data_form' : item_pk})
    context = { 
            'user' : request.user,
            'context_instance' : RequestContext(request),
            'fulan' : data_form.month,
            'tinan' : data_form.year,
            'code' : facility.code,
            'distritu' : facility.area.get_ancestors().get(kind__name='District'),
            'subdistritu' : facility.area.get_ancestors().get(kind__name='Subdistrict'),
            'fatin' : facility.area,
            'facility' : facility,
            'cells'  : cells,
            'data_form' : data_form,
            'form' : form,
            'item_pk' : item_pk,
            }

    sheet = data_form_type.sheet_index+1
    if sheet < 10:
        sheet = '0%s' % (sheet)
    return render_to_response('forms/form_0%s.html' % (sheet), context,) 


#def _export_csv(request, item_id):
    # Create the HttpResponse object with the appropriate CSV header.
#    response = HttpResponse(mimetype='text/csv')
#    response['Content-Disposition'] = 'attachment; filename=export.csv'

#    writer = csv.writer(response)
#    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
#    return response


#def _export_xls(request, item_pk):

#    report = models.DataForm.objects.get(pk=item_pk)
#    workbook_for_reading = xlrd.open_workbook(settings.WORKBOOK_PATH)
#    sheet_for_reading = workbook_for_reading.sheet_by_index(report.data_form_type.sheet_index)
    
#    workbook_for_writing = xlwt.Workbook()
#    sheet_for_writing = workbook_for_writing.add_sheet(report.data_form_type.code, cell_overwrite_ok=True)
    
    # we populate the new sheet with the conical sheet
#    for row in range(sheet_for_reading.nrows):
#        for col in range(sheet_for_reading.ncols):
#            sheet_for_writing.write(row, col, sheet_for_reading.cell(row, col).value)
    
    # we overwrite padded cells with actual data
#    for cell_data in report.cell_data.all():
#        sheet_for_writing.write(cell_data.cell.row, cell_data.cell.col, cell_data.value)
    
    # Create the HttpResponse object with the appropriate xls header.
#    response = HttpResponse(mimetype='application/vnd.ms-excel')
#    response['Content-Disposition'] = 'attachment; filename=data_%s.xls' % report.data_form_type.code
#    workbook_for_writing.save(response)
#    return response


def export_to_xls(request):

    if request.method.upper() == 'POST':
        form = forms.DataFormExcelExportForm(request.POST)

        if form.is_valid():
        
            data_form = models.DataForm.objects.get(pk=form.cleaned_data['data_form'])
            workbook_for_reading = xlrd.open_workbook(settings.WORKBOOK_PATH)
            sheet_for_reading = workbook_for_reading.sheet_by_index(data_form.data_form_type.sheet_index)
            
            workbook_for_writing = xlwt.Workbook()
            sheet_for_writing = workbook_for_writing.add_sheet(data_form.data_form_type.code, cell_overwrite_ok=True)
            
            # we populate the new sheet with the conical sheet
            for row in range(sheet_for_reading.nrows):
                for col in range(sheet_for_reading.ncols):
                    sheet_for_writing.write(row, col, sheet_for_reading.cell(row, col).value)
            
            # we overwrite padded cells with actual data
            for cell_data in data_form.cell_data.all():
                sheet_for_writing.write(cell_data.cell.row, cell_data.cell.col, cell_data.value)
            
            # Create the HttpResponse object with the appropriate xls header.
            response = HttpResponse(mimetype='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=data_%s.xls' % data_form.data_form_type.code
        
            workbook_for_writing.save(response)
            return response


def export_aggregate_to_xls(request):

    if request.method.upper() == u'POST':
        form = forms.AggregateDataFormExcelExportForm(request.POST)
        
        if form.is_valid():
        
            data_form_type = models.DataFormType.objects.get(pk=form.cleaned_data['data_form_type'])
            facility_pk = form.cleaned_data['facility']
            facility = Facility.objects.get(pk=facility_pk)
            month_range = (form.cleaned_data['start_month'], form.cleaned_data['end_month'])
            #year_range = (form.cleaned_data['start_year'], form.cleaned_data['end_year'])
            year = form.cleaned_data['year']
            workbook_for_reading = xlrd.open_workbook(settings.WORKBOOK_PATH)
            sheet_for_reading = workbook_for_reading.sheet_by_index(data_form_type.sheet_index)
            
            workbook_for_writing = xlwt.Workbook()
            sheet_for_writing = workbook_for_writing.add_sheet(data_form_type.code, cell_overwrite_ok=True)
            
            # we populate the new sheet with the conical sheet
            for row in range(sheet_for_reading.nrows):
                for col in range(sheet_for_reading.ncols):
                    sheet_for_writing.write(row, col, sheet_for_reading.cell(row, col).value)
            
            # Check to see if the facility if a Subdistrict Health Service or District Health Service
            # Heavy lifting done Here!  Within the date rage the aggregate value of each cell in the form is computed and stored in a list
            if facility.type.name == u'District Health Service':
                cell_data = models.CellData.objects.filter(data_form__data_form_type=data_form_type, data_form__facility__parent__parent=facility, data_form__month__range=month_range, data_form__year__contains=year)
            elif facility.type.name == u'Subdistrict Health Service':
                # Aggregation happens here
                cell_data = models.CellData.objects.filter(data_form__data_form_type=data_form_type, data_form__facility__parent=facility, data_form__month__range=month_range, data_form__year__contains=year)
            else:
                cell_data = models.CellData.objects.filter(data_form__data_form_type=data_form_type, data_form__facility=facility, data_form__month__range=month_range, data_form__year__contains=year)

            cells = []
            for cell in range(data_form_type.cells.count()):
                value_sum = cell_data.filter(cell__order=cell).aggregate(Sum('value')).get('value__sum')
                cells.append(value_sum)

            # we overwrite padded cells with actual data
            for cell in range(data_form_type.cells.count()):
                cell_data_set = cell_data.filter(cell__order=cell)
                value_sum = cell_data_set.aggregate(Sum('value')).get('value__sum')
                sheet_for_writing.write(cell_data_set[0].cell.row, cell_data_set[0].cell.col, value_sum)
            
            # Create the HttpResponse object with the appropriate xls header.
            response = HttpResponse(mimetype='application/vnd.ms-excel')
            response['Content-Disposition'] = u'attachment; filename=data_%s.xls' % data_form_type.code
        
            workbook_for_writing.save(response)
            return response
            

@login_required
def sync(request):
    if request.method.upper() == 'GET':
        
        if request.GET.get('submit') == u'Export':
            date = datetime.now()

            db = DATABASES['default']['NAME']
            response = HttpResponse(open(db,'rb'),mimetype='application/x-sqlite3')
            response['Content-Disposition'] = u'attachment; filename=data_database_%s_%s_%s.db' % (date.year, date.month, date.day)
            return response
            
        else:
            form = forms.SyncForm()
            return render_to_response('catalpa/relatori/sync.html',{
                    'form' : form,
                    'user' : request.user,
                    'context_instance' : RequestContext(request),})

    if request.method.upper() == 'POST':
        form = forms.SyncForm(request.POST, request.FILES)

        if form.is_valid():
            submit = request.POST['submit']
            if submit==u'Import':      
                if 'file' in request.FILES:
                    f = request.FILES['file']   
                    filename = f.name
                    path = '%s/%s' % (MEDIA_ROOT, filename)
                    file_writer = open(path, 'wb')
                    for chunk in f.chunks():
                        file_writer.write(chunk)
                    file_writer.close()
                    try:
                        if path.endswith(".json"):
                            import_from_json(path)
                        elif path.endswith(".db"):
                            import_from_database(path)
                        
                        translation.activate(LANGUAGE_CODE)
                        os.remove(path)
                        messages.success(request, _('Thank you %s, you synced your data' % (request.user)))
                        return render_to_response('catalpa/relatori/index.html',{
                                'user' : request.user,
                                'context_instance' : RequestContext(request),})
                    except Exception as ex:
                        try:
                            os.remove(path)
                        except:
                            pass
                        messages.error(request, _('There was an error with your Database Sync. Please try again. %s' % (ex)))
    
                    return render_to_response('catalpa/relatori/sync.html',{
                                'user' : request.user,
                                'context_instance' : RequestContext(request),})

def import_from_json(json_file, target_db='default'):
    call_command('loaddata', json_file, verbosity=0)


@transaction.commit_on_success
def import_from_database(source_db, target_db='default'):
    """ I only tried this on sqlite to sqlite transfer """
    from django.db import connection

    cursor = connection.cursor()
    cursor.execute("ATTACH DATABASE %s as K",[source_db])
    transaction.commit_unless_managed()
    for m in [models.DataForm,models.CellData,catalpa.aihun.models.Operation]:
        cmd = "INSERT OR REPLACE INTO %s SELECT * FROM K.%s" % (m._meta.db_table,m._meta.db_table)
        cursor.execute(cmd)
        transaction.commit_unless_managed()
    cursor.execute("DETACH K")
    transaction.commit_unless_managed()
