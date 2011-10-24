from django.contrib import admin
from django.utils.translation import ugettext as _
from django.conf.urls.defaults import patterns

from catalpa.aihun.admin import Admin

from catalpa.relatori import models
from catalpa.lib.autocomplete_admin import FkAutocompleteAdmin, InlineAutocompleteAdmin

class OptionAdmin(admin.ModelAdmin):
#class OptionAdmin(admin.TabularInline):
    model = models.Option
    fields = ['name', 'value', 'datagroup']
    list_display = ['datagroup','value','name']
    extra = 1

class DataFormTypeAdmin(Admin, admin.ModelAdmin):
    model = models.DataFormType
    fields = ['name', 'description', 'code', 'sheet_index', 'version']
    list_display = ['name','code',]


class DataFormAdmin(Admin, admin.ModelAdmin):
    model = models.DataForm
    fields = ['data_form_type', 'facility', 'month', 'year']
    search_fields = ['data_form_type__name','facility__name']
    list_display = ['facility','data_form_type','month', 'year']
    list_filter = ( 'month', 'year','data_form_type__code',)


class CellAdmin(Admin, admin.ModelAdmin):
    model = models.Cell
    fields = ['data_form_type', 'col', 'row', 'order', 'spreadsheet_cell',]
    list_display = ['data_form_type', 'col', 'row', 'order',]
    search_fields = ['data_form_type__name','col', 'row',]


class DataGroupAdmin(Admin, admin.ModelAdmin):
    model = models.DataGroup
    fields = ['cells', 'value', 'col', 'row', 'spreadsheet_cell']
    search_fields = ['value']
   # inlines = [OptionAdmin,]
    
class CellInlineAdmin(Admin, admin.TabularInline):
    model = models.Cell
    extra = 1


class IndicatorAdmin(Admin, admin.ModelAdmin):
    model = models.Indicator

class IndicatorTypeAdmin(Admin, admin.ModelAdmin):
    model = models.IndicatorType
    
    #inlines = [CellInlineAdmin,]


class DenominatorAdmin(Admin, FkAutocompleteAdmin):
    model = models.Denominator

    search_fields = ['facility__name', 'area__name']
    list_display = ['denominator_type', 'facility', 'area', 'value',]
    list_filter = ('denominator_type',)
    related_search_fields = {'area': ('^name',),
                            'facility': ('^name',),}

class DenominatorTypeAdmin(Admin, FkAutocompleteAdmin):
    model = models.DenominatorType

class DenominatorTypeSource(Admin, admin.ModelAdmin):
    model = models.DenominatorSource

class SettingsAdmin(Admin, admin.ModelAdmin):
    model = models.Settings

    
admin.site.register(models.DataForm, DataFormAdmin)
admin.site.register(models.DataFormType, DataFormTypeAdmin)
admin.site.register(models.Cell, CellAdmin)
admin.site.register(models.DataGroup, DataGroupAdmin)
admin.site.register(models.Option, OptionAdmin)
admin.site.register(models.Indicator, IndicatorAdmin)
admin.site.register(models.IndicatorType, IndicatorTypeAdmin)
admin.site.register(models.Denominator, DenominatorAdmin)
admin.site.register(models.DenominatorType, DenominatorTypeAdmin)
admin.site.register(models.DenominatorSource, DenominatorTypeSource)
admin.site.register(models.Settings, SettingsAdmin)
