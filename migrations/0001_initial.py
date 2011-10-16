# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HMISFormType'
        db.create_table('relatori_hmisformtype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='f69f319b-9ff4-4a94-ae98-a8c1fb6c40ae', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hmisformtype_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hmisformtype_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hmisformtype_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=64, db_index=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sheet_index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('relatori', ['HMISFormType'])

        # Adding model 'HMISForm'
        db.create_table('relatori_hmisform', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='9df17b07-bcaa-49f1-8003-1736b443e3e8', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hmisform_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hmisform_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hmisform_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('hmis_form_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', to=orm['relatori.HMISFormType'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(related_name='healthfacility', to=orm['health_service.HealthFacility'])),
            ('month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('relatori', ['HMISForm'])

        # Adding model 'Cell'
        db.create_table('relatori_cell', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='8e6fd6b9-2b02-413b-8d98-ff64cbf901c5', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cell_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cell_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cell_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('hmis_form_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cells', to=orm['relatori.HMISFormType'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('spreadsheet_cell', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('relatori', ['Cell'])

        # Adding model 'CellData'
        db.create_table('relatori_celldata', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='c9faac10-fb20-4e9a-9dfe-91b993630cce', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='celldata_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='celldata_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='celldata_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cell_data', to=orm['relatori.HMISForm'])),
            ('cell', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cell_data', to=orm['relatori.Cell'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
        ))
        db.send_create_signal('relatori', ['CellData'])

        # Adding model 'DataGroup'
        db.create_table('relatori_datagroup', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='c0c48daf-4897-4444-b34e-6f77b956f0ee', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='datagroup_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='datagroup_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='datagroup_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('col', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('row', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('spreadsheet_cell', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=140, blank=True)),
        ))
        db.send_create_signal('relatori', ['DataGroup'])

        # Adding M2M table for field cells on 'DataGroup'
        db.create_table('relatori_datagroup_cells', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datagroup', models.ForeignKey(orm['relatori.datagroup'], null=False)),
            ('cell', models.ForeignKey(orm['relatori.cell'], null=False))
        ))
        db.create_unique('relatori_datagroup_cells', ['datagroup_id', 'cell_id'])

        # Adding model 'IndicatorType'
        db.create_table('relatori_indicatortype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='fb508f85-248c-4ab7-b6c7-6da907b2f881', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicatortype_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicatortype_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicatortype_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('denominator_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicator_type', null=True, to=orm['relatori.DenominatorType'])),
        ))
        db.send_create_signal('relatori', ['IndicatorType'])

        # Adding M2M table for field cells on 'IndicatorType'
        db.create_table('relatori_indicatortype_cells', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('indicatortype', models.ForeignKey(orm['relatori.indicatortype'], null=False)),
            ('cell', models.ForeignKey(orm['relatori.cell'], null=False))
        ))
        db.create_unique('relatori_indicatortype_cells', ['indicatortype_id', 'cell_id'])

        # Adding model 'Indicator'
        db.create_table('relatori_indicator', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='d423e192-f8a5-49ce-a563-f2223b088af7', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicator_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicator_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicator_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('indicator_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'indicators', to=orm['relatori.IndicatorType'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'indicators', to=orm['health_service.HealthFacility'])),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('relatori', ['Indicator'])

        # Adding model 'DenominatorType'
        db.create_table('relatori_denominatortype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='c4b89f5b-cb19-47d5-910c-97d705fba2af', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominatortype_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominatortype_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominatortype_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
        ))
        db.send_create_signal('relatori', ['DenominatorType'])

        # Adding model 'DenominatorSource'
        db.create_table('relatori_denominatorsource', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='865c67a7-902c-4620-8f06-90e9db245c19', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominatorsource_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominatorsource_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominatorsource_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relatori', ['DenominatorSource'])

        # Adding model 'Denominator'
        db.create_table('relatori_denominator', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='d3c47f92-0f32-445d-969c-a1dc09b58669', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominator_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominator_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominator_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('denominator_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'denominators', to=orm['relatori.DenominatorType'])),
            ('denominator_source', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'denominators', null=True, to=orm['relatori.DenominatorSource'])),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominators', to=orm['simple_locations.Area'])),
            ('health_facility', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominators', null=True, to=orm['health_service.HealthFacility'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('relatori', ['Denominator'])

        # Adding model 'Settings'
        db.create_table('relatori_settings', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='53a3c190-b978-407a-9496-47698270844a', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='settings_creator_related', null=True, to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='settings_changed_by_related', null=True, to=orm['auth.User'])),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('voided_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='settings_voided_by_related', null=True, to=orm['auth.User'])),
            ('date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('void_reason', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['health_service.HealthFacility'])),
            ('denominator_source', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'settings', null=True, to=orm['relatori.DenominatorSource'])),
        ))
        db.send_create_signal('relatori', ['Settings'])


    def backwards(self, orm):
        
        # Deleting model 'HMISFormType'
        db.delete_table('relatori_hmisformtype')

        # Deleting model 'HMISForm'
        db.delete_table('relatori_hmisform')

        # Deleting model 'Cell'
        db.delete_table('relatori_cell')

        # Deleting model 'CellData'
        db.delete_table('relatori_celldata')

        # Deleting model 'DataGroup'
        db.delete_table('relatori_datagroup')

        # Removing M2M table for field cells on 'DataGroup'
        db.delete_table('relatori_datagroup_cells')

        # Deleting model 'IndicatorType'
        db.delete_table('relatori_indicatortype')

        # Removing M2M table for field cells on 'IndicatorType'
        db.delete_table('relatori_indicatortype_cells')

        # Deleting model 'Indicator'
        db.delete_table('relatori_indicator')

        # Deleting model 'DenominatorType'
        db.delete_table('relatori_denominatortype')

        # Deleting model 'DenominatorSource'
        db.delete_table('relatori_denominatorsource')

        # Deleting model 'Denominator'
        db.delete_table('relatori_denominator')

        # Deleting model 'Settings'
        db.delete_table('relatori_settings')


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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'46866e3a-09fa-4e4a-8b1f-dd5d09b4b133'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'82bc54b8-9de5-40e5-999f-d9aa9f0efede'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'54e6b9bd-6210-417f-aa07-eeb91b19196a'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'blank': 'True'}),
            'void_reason': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'voided': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'voided_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'datagroup_voided_by_related'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'relatori.denominator': {
            'Meta': {'object_name': 'Denominator'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'denominators'", 'to': "orm['simple_locations.Area']"}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'5630f5d4-5fc1-4d3b-bd7f-467197d2f2f6'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'761efc49-f108-4f7e-8e5c-dafec602b98d'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'b8d43050-f96f-4ad5-b787-661e65677569'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'68597cd0-9d70-423b-8ac8-b8f23f14e144'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'f285ac31-0443-4a4b-8893-1085ba3ee6ef'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'387bc822-ceac-42bd-99ab-d3a142fc2622'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'f3cd84fe-bb09-4899-b284-496cd071feca'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'fc4a6553-ea07-45d4-b70c-e9613a9ef224'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
