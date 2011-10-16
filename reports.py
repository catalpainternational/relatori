import reporting
from django.db.models import Sum, Avg, Count
from relatori import models
from health_service.models import HealthFacility


class IndicatorReport(reporting.Report):
    model = models.Indicator
    verbose_name = 'K1 Indicator Report'

    #use annotations (or something else) to calculate indicators?
    annotate = (                    # Annotation fields (tupples of field, func, title)
        ('value', Sum, 'Total'),     # example of custom title for column 
    )
    aggregate = (                   # columns that will be aggregated (syntax the same as for annotate)
        ('value', Sum, 'Total'),
    )
    group_by = [                   # list of fields and lookups for group-by options
        'facility',
    ]
    list_filter = [                # This are report filter options (similar to django-admin)
       'facility',
    ]
    detail_list_display = [        # if detail_list_display is defined user will be able to see how rows was grouped  
        'indicator_type',
    ]

    date_hierarchy = 'date_created' # the same as django-admin

reporting.register('Indicator', IndicatorReport) # Do not forget to 'register' your class in reports

class HealthFacilityReport(reporting.Report):
    model = models.HealthFacility
    verbose_name = 'HealthFacility Indicator Report'

    #use annotations (or something else) to calculate indicators?
    annotate = (                    # Annotation fields (tupples of field, func, title)
        ('indicators', Sum, 'Total'),     # example of custom title for column 
    )
    aggregate = (                   # columns that will be aggregated (syntax the same as for annotate)
        ('type', Sum, 'Total'),
    )
    group_by = [                   # list of fields and lookups for group-by options
        'type',
    ]
    list_filter = [                # This are report filter options (similar to django-admin)
       'type',
    ]
    detail_list_display = [        # if detail_list_display is defined user will be able to see how rows was grouped  
        'type',
    ]

    date_hierarchy = 'date_created' # the same as django-admin

reporting.register('HealthFacility', HealthFacilityReport) # Do not forget to 'register' your class in reports