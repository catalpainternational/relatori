from datetime import datetime
from catalpa.relatori import models
from django.db.models import Sum


def indicators_by_facility(facility):
    """
    Prints out all indicators for the given health_service.models.HealthFaclility
    """
    for indicator_type in models.IndicatorType.objects.all():
        numerator = indicator_type.cells.filter(cell_data__data_form__facility=facility).aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
        denominator = models.Denominator.objects.get(denominator_type=indicator_type.denominator_type, health_facility=facility).value
        indicator = float(numerator) / float(denominator)
        print int(indicator * 100), indicator_type.name


def indicators_in_subdistrict(parent):
    """
    Prints out all indicators for the given parent health_service.models.HealthFacility
    """
    #perform sanity check and see if the HealthFaclility passed has any children
    if parent.has_children:
        for indicator_type in models.IndicatorType.objects.all():
            print ''
            print indicator_type.name
#            for facility in parent.children.exclude(type__name="SISCA"):
            for facility in parent.children.filter(type__name="CHC"):
                numerator = indicator_type.cells.filter(cell_data__data_form__facility=facility).aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
                denominator = models.Denominator.objects.get(denominator_type=indicator_type.denominator_type, health_facility=parent.children.filter(type__name="CHC")[0]).value
                if numerator == None:
                    numerator = 0
                indicator = int(float(numerator) / float(denominator) * 100)
                print "%d      %d       %d    %s" % (numerator, denominator, indicator, facility)


#indicators_in_subdistrict(parent)    


def indicators_in_district(parent):
    """
    Prints out all indicators for the given parent health_service.models.HealthFacility
    returns the dataset in dictionary containing the indicator name and a list of tuples for use in pycha            
            dataset = [
                    ('ermera', [[0, 50]]),
                    ('hatolia', [[0, 30]]),
                    ('letefoho', [[0, 20]]),
                    ]
    """
    #perform sanity check and see if the HealthFaclility passed has any children
    if parent.has_children:
        for indicator_type in models.IndicatorType.objects.all():
            print ''
            print indicator_type.name
#            for facility in parent.children.exclude(type__name="SISCA"):
            for facility in parent.descendants.filter(type__name="CHC").exclude(name__icontains='BOSOK'):
                numerator = indicator_type.cells.filter(cell_data__data_form__facility=facility).aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
                denominator = models.Denominator.objects.get(denominator_type=indicator_type.denominator_type, health_facility=facility).value
                if numerator == None:
                    numerator = 0
                indicator = int(float(numerator) / float(denominator) * 100)
                print "%d      %d       %d    %s" % (numerator, denominator, indicator, facility)


#indicators_in_district(parent)    


def indicator_by_type(parent, indicator_type):
    """
    Prints out indicators for the given 
            parent of type health_service.models.HealthFacility
            indicator_type of type relatori.models.IndicatorType

    Returns the dataset in list containing a list of tuples for use in pycha            
    """
    indicators = []
    numerator = denominator = average = 0
    
    print ''
    print indicator_type.name
#        for facility in parent.children.exclude(type__name="SISCA"):
    facility_index = 0
    for facility in parent.descendants.filter(type__name="CHC").exclude(name__icontains='BOSOK'):
        facility_numerator = indicator_type.cells.filter(cell_data__data_form__facility=facility,cell_data__data_form__year__exact=2011).aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
        if facility_numerator is not None:
            numerator += facility_numerator
        denominator += models.Denominator.objects.get(denominator_type=indicator_type.denominator_type, health_facility=facility).value
    indicators.append(('yes', [[0, numerator]]))
    indicators.append(('no', [[0, denominator]]))
    print "%d      %d      %s" % (numerator, denominator, parent.name)
    return indicators


#indicator_by_type(parent, indicator_type)    


def indicators_by_parent_by_type(parent, indicator_type):
    """
    Prints out indicators for the given 
            parent of type health_service.models.HealthFacility
            indicator_type of type relatori.models.IndicatorType

    Returns the dataset in list containing a list of tuples for use in pycha            
    """
    #perform sanity check and see if the HealthFaclility passed has any children
    indicators = []
    average = 0
    if parent.has_children:
        print ''
        print indicator_type.name
#        for facility in parent.children.exclude(type__name="SISCA"):
        facility_index = 0
        for facility in parent.descendants.filter(type__name="CHC").exclude(name__icontains='BOSOK'):
            numerator = indicator_type.cells.filter(cell_data__data_form__facility=facility,cell_data__data_form__year__exact=2011).aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
            denominator = models.Denominator.objects.get(denominator_type=indicator_type.denominator_type, health_facility=facility).value
            if numerator == None:
                numerator = 0
            indicator = int(float(numerator) / float(denominator) * 100)
            average += indicator
            indicators.append((facility.name, [[0,indicator]]))
            print "%d      %d       %d    %s" % (numerator, denominator, indicator, facility)
    print "Average: %d    %s" % (average / indicators.__len__(), parent)
    # Add average to the begining of the list
    indicators.insert(0, (parent.type.name+' '+parent.name, [[0, average / indicators.__len__()]]))
    return indicators


#indicators_by_parent_by_type(parent, indicator_type)    


def indicators_by_parent_by_type_by_quarter(parent, indicator_type):
    """
    Prints out indicators for the given 
            parent of type health_service.models.HealthFacility
            indicator_type of type relatori.models.IndicatorType

    Returns the dataset in list containing a list of tuples for use in pycha            
    """
    #Some convienece variables. Each Quarter is indended to be inclusive all Quarters that preceed it. Goofy, I know.
    Q1 = ('Q1', range(1,4))
    Q2 = ('Q2', range(1,7))
    Q3 = ('Q3', range(1,10))
    Q4 = ('Q4', range(1,13))
    quarters = [Q1, Q2, Q3, Q4]
    #perform sanity check and see if the HealthFaclility passed has any children
    indicators = []
    if parent.has_children:
        print ''
        print indicator_type.name
        for quarter in quarters:
            average = 0
            facility_index = 0
            facility_indicators = []
#            for facility in parent.children.exclude(type__name="SISCA"):
            # if no data exists for any month within the quarter then break out of the for loop. Slices are cool.
            if indicator_type.cells.filter(cell_data__data_form__month__in=quarter[1][-3:],cell_data__data_form__year__exact=datetime.now().year).count() == 0:
                break
            print ''
            print '    ', quarter[0]
            for facility in parent.descendants.filter(type__name="CHC").exclude(name__icontains='BOSOK'):
                numerator = indicator_type.cells.filter(cell_data__data_form__facility=facility, cell_data__data_form__month__in=quarter[1],cell_data__data_form__year__exact=datetime.now().year).aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
                denominator = models.Denominator.objects.get(denominator_type=indicator_type.denominator_type, health_facility=facility).value
                if numerator == None:
                    numerator = 0
                indicator = int(float(numerator) / float(denominator) * 100)
                average += indicator
                facility_indicators.append([facility_index, indicator])
                facility_index += 1
                print "%d      %d       %d    %s" % (numerator, denominator, indicator, facility)
            # Add average to the begining of the list
            facility_indicators.insert(0,[facility_index, average / facility_indicators.__len__()])
            print "Average: %d    %s" % (average / facility_indicators.__len__(), parent)
            indicators.append((quarter[0],facility_indicators))
    return indicators

#indicators_by_parent_by_type_by_quarter(parent, indicator_type)


def indicators_by_parent_by_types(parent, indicator_types):
    """
    Prints out indicators for the given 
            parent of type health_service.models.HealthFacility
            indicator_type of type relatori.models.IndicatorType

    Returns the dataset in list containing a list of tuples for use in pycha            
    """
    #perform sanity check and see if the HealthFaclility passed has any children
    indicators = []
    if parent.has_children:
        for indicator_type in indicator_types:
            print ''
            print indicator_type.name
            average = 0
            facility_index = 0
            facility_indicators = []
    #        for facility in parent.children.exclude(type__name="SISCA"):
            # if no data exists for any month within the quarter then break out of the for loop. Slices are cool.
            for facility in parent.descendants.filter(type__name="CHC").exclude(name__icontains='BOSOK'):
                numerator = indicator_type.cells.filter(cell_data__data_form__facility=facility,cell_data__data_form__year__exact=datetime.now().year).aggregate(Sum('cell_data__value')).get('cell_data__value__sum')
                denominator = models.Denominator.objects.get(denominator_type=indicator_type.denominator_type, health_facility=facility).value
                if numerator == None:
                    numerator = 0
                indicator = int(float(numerator) / float(denominator) * 100)
                average += indicator
                facility_indicators.append([facility_index, indicator])
                facility_index += 1
                print "%d      %d       %d    %s" % (numerator, denominator, indicator, facility)
            # Add average to the begining of the list
            facility_indicators.insert(0,[facility_index, average / facility_indicators.__len__()])
            print "Average: %d    %s" % (average / facility_indicators.__len__(), parent)
            indicators.append((indicator_type.name, facility_indicators))
    return indicators


#indicators_by_parent_by_types(parent, indicator_type)    

