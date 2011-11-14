from django.db import models
# from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from catalpa.simple_locations.models import Area, Facility

from catalpa.aihun.models import Model, ModelType

class DataFormType(ModelType):
    """
    This model represents a specific data form type, such as SMI
    """
    code = models.CharField(_('code'), max_length=64, db_index=True)
    version = models.CharField(_('version'), max_length=10,)
    sheet_index = models.IntegerField(_('sheet index'),)

    class Meta:
        verbose_name = _('Form Type')
        verbose_name_plural = _('Form Types')

    def __unicode__(self,):
#        return u"%s - %s" % (self.name, self.code,)
        return u"%s" % (self.code,)


class DataForm(Model):
    data_form_type = models.ForeignKey(DataFormType, related_name="reports") #TODO: change to data_form_types
    facility = models.ForeignKey(Facility, related_name="data_forms")
    month = models.IntegerField(_('month'), blank=True, null=True)
    year = models.IntegerField(_('year'), blank=True, null=True)

    class Meta:
        verbose_name = _('Form')
        verbose_name_plural = _('Forms')


    def __unicode__(self,):
        return u"%s :: %s (%s/%s)" % (self.data_form_type, self.facility, self.month, self.year)


class Cell(Model):
    data_form_type = models.ForeignKey(DataFormType, related_name=_('cells'), db_index=True)
    col =  models.IntegerField(_('col'),)
    row = models.IntegerField(_('row'),)
    order = models.IntegerField(_('order'))
    spreadsheet_cell = models.CharField(_('spreedsheet cell'), max_length=4,)

    def __unicode__(self,):
        return u"(%s, %s) %s" % (self.col, self.row, self.spreadsheet_cell)


class CellData(Model):
    data_form = models.ForeignKey(DataForm, related_name=_('cell_data'), db_index=True)
    cell = models.ForeignKey(Cell, related_name=_('cell_data'),db_index=True)
    value = models.CharField(_('value'), max_length=140, blank=True)

    class Meta:
        verbose_name = _('Cell data')
        verbose_name_plural = _('Cell data')


class DataGroup(Model):
    cells = models.ManyToManyField(Cell, related_name=_('data_groups'),db_index=True) #TODO: better as ForeignKey?
    #options = models.ManyToManyField(Option, related_name=_('data_groups'))

    col = models.CharField(_('col'), max_length=10,blank=True)
    row = models.CharField(_('row'), max_length=10,blank=True)
    spreadsheet_cell = models.CharField(_('spreedsheet cell'), max_length=4, blank=True)
    value = models.CharField(_('value'), max_length=140, blank=True, db_index=True)

    class Meta:
        verbose_name = _('DataGroup')
        verbose_name_plural = _('DataGroups')

    def __unicode__(self,):
        return u"%s" % (self.value)


class IndicatorType(ModelType):
    cells = models.ManyToManyField(Cell, null=True, blank=True, related_name=_('indicator_type'))
    denominator_type = models.ForeignKey('DenominatorType', null=True, blank=True, related_name='indicator_type')

    class Meta:
        verbose_name = _('Indicator Type')
        verbose_name_plural = _('Indicator Types')

    def __unicode__(self,):
        return u"%s: %s" % (self.name, self.description)


class Indicator(Model):
    indicator_type = models.ForeignKey(IndicatorType, related_name=_('indicators'))
    facility = models.ForeignKey(Facility, related_name=_('indicators'))
    slug = models.CharField(_('slug'), max_length=50,)
    start_date = models.DateField(_('start date'),)
    end_date = models.DateField(_('end date'),)
    value = models.IntegerField(_('value'),)

    def set_value(self,):
        self.value = self.indicator_type.cells.aggregate(Sum('cell_data__value')).values()[0]
        #return aggregate value of self.indicator_type.datagroup.filter(month, year)

    #@property
    #def coverage_rate(self):
    #   denominator = self.indicator_type.denominator_type.denominators.get(start_date, end_date,) # for catchment area
    #   numerator = self.value
    #   return numerator/denominator

    class Meta:
        verbose_name = _('Indicator')
        verbose_name_plural = _('Indicators')

    def __unicode__(self,):
        return u"%s : %s" % (self.indicator_type, self.facility)


class DenominatorType(ModelType):


    class Meta:
        verbose_name = _('Denominator Type')
        verbose_name_plural = _('Denominator Types')

    def __unicode__(self,):
        return u"%s" % (self.name,)


class DenominatorSource(ModelType):
    """
    Denominator Source
        An example of a source would be Census 2010 or RSF (Family Registry)
    """
    start_date = models.DateField(_('start date'),)
    end_date = models.DateField(_('end date'),)


    class Meta:
        verbose_name = _('Denominator Source')
        verbose_name_plural = _('Denominator Sources')


    def __unicode__(self,):
        return u"%s" % (self.name,)


class Denominator(Model):
    denominator_type = models.ForeignKey(DenominatorType, related_name=_('denominators'))
    denominator_source = models.ForeignKey(DenominatorSource, null=True, blank=True, related_name=_('denominators'))
    slug = models.CharField(_('slug'), max_length=140, null=True, blank=True,)
    area = models.ForeignKey(Area, related_name='denominators', null=True, blank=True,)
    facility = models.ForeignKey(Facility, related_name='denominators', null=True, blank=True,) #TODO: perhaps this isn't needed
    start_date = models.DateField(_('start date'),)# Is this really needed, the denomitator source also has start and end dates
    end_date = models.DateField(_('end date'),) # Is this really needed, the denomitator source also has start and end dates
    value = models.IntegerField(_('value'),)

    class Meta:
        verbose_name = _('Denominator')
        verbose_name_plural = _('Denominators')

    def __unicode__(self,):
        name = ''
        if self.facility is not None:
            name += self.facility.__unicode__()
        if self.area is not None:
            name += self.area.__unicode__()
        return u"%s : %s :: %s" % (name, self.denominator_type, self.value,)


class Settings(Model):
    facility = models.ForeignKey(Facility,)
    denominator_source = models.ForeignKey(DenominatorSource, null=True, blank=True, related_name=_('settings'))

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _('Settings')

    def __unicode__(self,):
        return u"Chosen Location: %s" % (self.facility,)

class Option(Model):
    name = models.CharField(_('name'),max_length=200)
    value =  models.IntegerField(_('value'))
    datagroup = models.ForeignKey(DataGroup, related_name=_('options'))

    def __unicode__(self,):
        return u"%s : %s :: %s" % (self.name, self.value,self.datagroup)

#######################################################
#
#   Summary
#   Month, Year to one Date type to new Period class?
#
