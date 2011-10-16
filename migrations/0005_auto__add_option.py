# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Option'
        db.create_table('relatori_option', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='63f1f221-af38-4c11-b5cd-2eac79f91ebe', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('datagroup', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'options', to=orm['relatori.DataGroup'])),
        ))
        db.send_create_signal('relatori', ['Option'])


    def backwards(self, orm):
        
        # Deleting model 'Option'
        db.delete_table('relatori_option')


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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'45f52c68-0219-41a8-a09f-f05e14d67fe7'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.celldata': {
            'Meta': {'object_name': 'CellData'},
            'cell': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.Cell']"}),
            'data_form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.DataForm']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c542b591-917e-43b4-88e3-dc04a1f820db'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'})
        },
        'relatori.dataform': {
            'Meta': {'object_name': 'DataForm'},
            'data_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': "orm['relatori.DataFormType']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'data_forms'", 'to': "orm['health_service.HealthFacility']"}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'4c7bc911-b8e1-4e83-bff8-6204a78435fa'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'relatori.dataformtype': {
            'Meta': {'object_name': 'DataFormType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'sheet_index': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'83f29c02-92c0-4eb6-9568-0dc6082449b9'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'relatori.datagroup': {
            'Meta': {'object_name': 'DataGroup'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'data_groups'", 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'col': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'row': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'8d7a2f58-07ef-495b-a886-af1650be81bc'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'fb100076-ca70-4065-b3d7-5a151cbc7417'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.denominatorsource': {
            'Meta': {'object_name': 'DenominatorSource'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'f2c1669f-9af9-4bf3-8613-d02d3dbfe304'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.denominatortype': {
            'Meta': {'object_name': 'DenominatorType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'0b8f631d-c9ab-4cf7-95f1-18a392e9aea9'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['health_service.HealthFacility']"}),
            'indicator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['relatori.IndicatorType']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'f4930709-f3ee-47e8-b67a-8912b701b858'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.indicatortype': {
            'Meta': {'object_name': 'IndicatorType'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'indicator_type'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_type'", 'null': 'True', 'to': "orm['relatori.DenominatorType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'bba67115-3978-4480-be74-12df0da32a8e'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.option': {
            'Meta': {'object_name': 'Option'},
            'datagroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'options'", 'to': "orm['relatori.DataGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'cb5d0c8c-bb67-46e2-920e-7c443ba896de'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.settings': {
            'Meta': {'object_name': 'Settings'},
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'settings'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['health_service.HealthFacility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'0a66d69c-ca21-476b-bb37-23057b1bb9b2'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
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
