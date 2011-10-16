# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Denominator.area'
        db.alter_column('relatori_denominator', 'area_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['simple_locations.Area']))


    def backwards(self, orm):
        
        # Changing field 'Denominator.area'
        db.alter_column('relatori_denominator', 'area_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['simple_locations.Area']))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cell_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'col': ('django.db.models.fields.IntegerField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cell_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hmis_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cells'", 'to': "orm['relatori.HMISFormType']"}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'d0c37f05-966d-468c-93a8-c7d054df0972'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cell_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.celldata': {
            'Meta': {'object_name': 'CellData'},
            'cell': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.Cell']"}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'celldata_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'celldata_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.HMISForm']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'ef537dee-10a4-4384-9d80-7167f4c9213f'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'celldata_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.datagroup': {
            'Meta': {'object_name': 'DataGroup'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'data_groups'", 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'datagroup_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'col': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'datagroup_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'row': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'bbca7de8-abc7-4cc4-a62d-a303da58eabd'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'blank': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'datagroup_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.denominator': {
            'Meta': {'object_name': 'Denominator'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominators'", 'null': 'True', 'to': "orm['simple_locations.Area']"}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominator_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominator_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'denominators'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'denominators'", 'to': "orm['relatori.DenominatorType']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'health_facility': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominators'", 'null': 'True', 'to': "orm['health_service.HealthFacility']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'3d54d79e-865b-4c9d-9747-257d89c883ee'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominator_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.denominatorsource': {
            'Meta': {'object_name': 'DenominatorSource'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominatorsource_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominatorsource_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'b97c03aa-2ee5-4c8f-991e-abe88e69a336'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominatorsource_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.denominatortype': {
            'Meta': {'object_name': 'DenominatorType'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominatortype_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominatortype_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'2e7687d6-1c41-4faf-8445-ce10cbb2720f'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominatortype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.hmisform': {
            'Meta': {'object_name': 'HMISForm'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hmisform_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hmisform_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'healthfacility'", 'to': "orm['health_service.HealthFacility']"}),
            'hmis_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': "orm['relatori.HMISFormType']"}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'72c66b68-77f1-4078-b5e9-c58111c12957'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hmisform_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'relatori.hmisformtype': {
            'Meta': {'object_name': 'HMISFormType'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hmisformtype_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hmisformtype_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'sheet_index': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'eff94f3a-a7a1-45e1-ad00-54f6d55b2eb8'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hmisformtype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['health_service.HealthFacility']"}),
            'indicator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['relatori.IndicatorType']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'0e038b9e-4ea8-45ae-b919-10ecdf1ee8b5'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.indicatortype': {
            'Meta': {'object_name': 'IndicatorType'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'indicator_type'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicatortype_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicatortype_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_type'", 'null': 'True', 'to': "orm['relatori.DenominatorType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'b95b3655-dc9a-4ead-ae75-de5397610b7a'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicatortype_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.settings': {
            'Meta': {'object_name': 'Settings'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'settings_changed_by_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'settings_creator_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voided': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'settings'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['health_service.HealthFacility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c542d343-81fa-479b-a115-b90b59c64f51'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'settings_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
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
