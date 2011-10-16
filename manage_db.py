from django.db import transaction
from settings import DATABASES as dbs
from health_service.models import HealthFacility, HealthFacilityType
from relatori import models


@transaction.commit_on_success
def copy_databases():
    for db in dbs:
        if db != 'default' and models.DataForm.objects.using(db).filter(facility=facility).count() > 0:
            for form in models.DataForm.objects.using(db).filter(facility=facility):
                form.save(using='default')
                form.facility = target_facility
                form.save(using='default')
                for cell_data in models.CellData.objects.using(db).filter(report=form):
                    cell_data.save(using='default')

@transaction.commit_on_success
def transfer_db(facility, target_facility, db_name):
    if db != 'default' and models.DataForm.objects.using(db_name).filter(facility=facility).count() > 0:
        for form in models.DataForm.objects.using(db_name).filter(facility=facility):
            form.save(using='default')
            form.facility = target_facility
            form.save(using='default')
            for cell_data in models.CellData.objects.using(db_name).filter(report=form):
                cell_data.save(using='default')


def check_for_forms(facility):
    for db in dbs:
#        if db != 'default':
        print models.DataForm.objects.using(db).filter(facility=facility).count(), facility, db


@transaction.commit_on_success
def import_from_database(source_db, target_db='default'):
    from datetime import datetime
    start = datetime.now()
    i = 0
    j = 0
    for form in models.DataForm.objects.using(source_db).all():
         if models.DataForm.objects.using(target_db).filter(pk=form.pk).count() == 0:
            form.save(using=target_db)
            i = i + 1
            for cell_data in models.CellData.objects.using(source_db).filter(report=form):
                cell_data.save(using=target_db)
                j = j + 1
    finish = datetime.now()
    print i, j, start, finish


def import_from_all_databases():
    for db in dbs:
        if db != 'default':
            import_from_database(db)


def check_forms_in_databases():
    from datetime import datetime
    start = datetime.now()
    i = 0
    for db in dbs:
        if db != 'default':
            for form in models.DataForm.objects.using(db).all():
                if models.DataForm.objects.using('default').filter(pk=form.pk).count() != 0:
                    i = i + 1
    finish = datetime.now()
    return i, start, finish
