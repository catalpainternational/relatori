# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('relatori_hmisform','hmis_form_type_id','data_form_type_id')
        db.rename_column('relatori_cell','hmis_form_type_id','data_form_type_id')
        db.rename_column('relatori_celldata','report_id','data_form_id')

        db.rename_table('relatori_hmisformtype','relatori_dataformtype')
        db.rename_table('relatori_hmisform','relatori_dataform')
        
        db.create_index('relatori_cell', ['data_form_type_id'])
        db.create_index('relatori_celldata', ['cell_id'])
        db.create_index('relatori_celldata', ['data_form_id'])
        db.create_index('relatori_dataform', ['data_form_type_id'])
        db.create_index('relatori_dataform', ['facility_id'])
        db.create_index('relatori_dataformtype', ['name'])
        db.create_index('relatori_dataformtype', ['code'])
        db.create_index('relatori_datagroup', ['value'])
        db.create_index('relatori_datagroup_cells', ['cell_id'])
        db.create_index('relatori_datagroup_cells', ['datagroup_id'])
        db.create_index('relatori_denominator', ['denominator_type_id'])
        db.create_index('relatori_denominator', ['denominator_source_id'])
        db.create_index('relatori_denominator', ['health_facility_id'])
        db.create_index('relatori_denominator', ['area_id'])
        db.create_index('relatori_denominatorsource', ['name'])
        db.create_index('relatori_denominatortype', ['name'])
        db.create_index('relatori_indicator', ['facility_id'])
        db.create_index('relatori_indicator', ['indicator_type_id'])
        db.create_index('relatori_indicatortype', ['denominator_type_id'])
        db.create_index('relatori_indicatortype', ['name'])
        db.create_index('relatori_indicatortype_cells', ['cell_id'])
        db.create_index('relatori_indicatortype_cells', ['indicatortype_id'])
        db.create_index('relatori_settings', ['facility_id'])
        db.create_index('relatori_settings', ['denominator_source_id'])

        from django.contrib.auth.models import User
        from relatori.models import DataForm
        from catalpa.aihun.models import Operation
        
        officer = User.objects.filter(username='chcofficer')[0]
        for form in DataForm.objects.all():
                op = Operation()
                op.create(officer,form,"Actually the migration date")
                op.save()

        pass


    def backwards(self, orm):
        db.rename_column('relatori_dataform','data_form_type_id','hmis_form_type_id')
        db.rename_column('relatori_cell','data_form_type_id','hmis_form_type_id')
        db.rename_column('relatori_celldata','data_form_id','report_id')

        db.rename_table('relatori_dataformtype','relatori_hmisformtype')
        db.rename_table('relatori_dataform','relatori_hmisform')

        db.create_index('relatori_hmisform', ['hmis_form_type_id'])
        db.create_index('relatori_cell', ['hmis_form_type_id'])
        db.create_index('relatori_celldata', ['report_id'])

        pass


    models = {
        'health_service.healthfacility': {
            'Meta': {'object_name': 'HealthFacility'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'facility'", 'null': 'True', 'to': "orm['simple_locations.Area']"}),
            'catchment_areas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'catchment'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['simple_locations.Area']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simple_locations.Point']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'facility'", 'null': 'True', 'to': "orm['health_service.HealthFacility']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['health_service.HealthFacilityType']", 'null': 'True', 'blank': 'True'})
        },
        'health_service.healthfacilitytype': {
            'Meta': {'object_name': 'HealthFacilityType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'relatori.cell': {
            'Meta': {'object_name': 'Cell'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            'data_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cells'", 'to': "orm['relatori.DataFormType']"}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'4fa8cfc9-ea98-4cfb-950b-9d0e30df1214'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.celldata': {
            'Meta': {'object_name': 'CellData'},
            'cell': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.Cell']"}),
            'data_form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.DataForm']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'974bd398-382e-4d79-b524-3448b9415002'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'})
        },
        'relatori.dataform': {
            'Meta': {'object_name': 'DataForm'},
            'data_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': "orm['relatori.DataFormType']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'data_forms'", 'to': "orm['health_service.HealthFacility']"}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c262ee79-8ab1-423e-8d07-eddc6296da0a'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'relatori.dataformtype': {
            'Meta': {'object_name': 'DataFormType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'sheet_index': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c7c2dbe5-e04a-40c4-91ee-f3ea74881436'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'relatori.datagroup': {
            'Meta': {'object_name': 'DataGroup'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'data_groups'", 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'col': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'row': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'145e0d35-b10e-4405-af32-49b8fb133395'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'blank': 'True'})
        },
        'relatori.denominator': {
            'Meta': {'object_name': 'Denominator'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominators'", 'null': 'True', 'to': "orm['simple_locations.Area']"}),
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'denominators'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'denominators'", 'to': "orm['relatori.DenominatorType']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'health_facility': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominators'", 'null': 'True', 'to': "orm['health_service.HealthFacility']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'4a93fefc-fc35-4bc6-9bc8-56c9f06bcce6'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.denominatorsource': {
            'Meta': {'object_name': 'DenominatorSource'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'93818f0a-03f8-499a-ab57-9ebe29951569'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.denominatortype': {
            'Meta': {'object_name': 'DenominatorType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'b0d8bb3e-b25e-467b-98b5-28734ff003c4'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['health_service.HealthFacility']"}),
            'indicator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['relatori.IndicatorType']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'e5c2602f-89db-4b6e-aed3-3a5b82c505cc'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.indicatortype': {
            'Meta': {'object_name': 'IndicatorType'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'indicator_type'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_type'", 'null': 'True', 'to': "orm['relatori.DenominatorType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'14ac29a5-f335-4727-a250-b9a95c45f350'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.settings': {
            'Meta': {'object_name': 'Settings'},
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'settings'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['health_service.HealthFacility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'be4d4c42-95cc-49e2-9d04-1a9efd36d043'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'simple_locations.area': {
            'Meta': {'unique_together': "(('code', 'kind'),)", 'object_name': 'Area'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simple_locations.AreaType']", 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simple_locations.Point']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['simple_locations.Area']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'simple_locations.areatype': {
            'Meta': {'object_name': 'AreaType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'simple_locations.point': {
            'Meta': {'object_name': 'Point'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'})
        }
    }

    complete_apps = ['relatori']
