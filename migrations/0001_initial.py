# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DataFormType'
        db.create_table('relatori_dataformtype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='1e7a708f-a632-47f5-90f3-21a85c776941', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=64, db_index=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sheet_index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('relatori', ['DataFormType'])

        # Adding model 'DataForm'
        db.create_table('relatori_dataform', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='54077440-c3f6-43ae-acd3-bda070d53b4e', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('data_form_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports', to=orm['relatori.DataFormType'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(related_name='data_forms', to=orm['simple_locations.Facility'])),
            ('month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('relatori', ['DataForm'])

        # Adding model 'Cell'
        db.create_table('relatori_cell', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='9a03bb1f-7d71-4929-8904-e9fb0f8a0d0a', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('data_form_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cells', to=orm['relatori.DataFormType'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('spreadsheet_cell', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('relatori', ['Cell'])

        # Adding model 'CellData'
        db.create_table('relatori_celldata', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='aa295621-d067-4243-9e5c-8906420e3cad', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('data_form', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cell_data', to=orm['relatori.DataForm'])),
            ('cell', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'cell_data', to=orm['relatori.Cell'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
        ))
        db.send_create_signal('relatori', ['CellData'])

        # Adding model 'DataGroup'
        db.create_table('relatori_datagroup', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='1ea7bf90-0d00-4e03-b288-22c94c428174', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('col', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('row', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(default='64838e78-4b66-43b7-8efd-3db66cba1a82', unique=True, max_length=36, primary_key=True, db_index=True)),
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
            ('uuid', self.gf('django.db.models.fields.CharField')(default='63d73dfd-bce7-4b52-a32d-c8c9d196df88', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('indicator_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'indicators', to=orm['relatori.IndicatorType'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'indicators', to=orm['simple_locations.Facility'])),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('relatori', ['Indicator'])

        # Adding model 'DenominatorType'
        db.create_table('relatori_denominatortype', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='e2ceb1f8-0839-461d-8614-7ec0510d9777', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
        ))
        db.send_create_signal('relatori', ['DenominatorType'])

        # Adding model 'DenominatorSource'
        db.create_table('relatori_denominatorsource', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='77dca727-8aff-40a5-9127-87f37f2cf224', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('relatori', ['DenominatorSource'])

        # Adding model 'Denominator'
        db.create_table('relatori_denominator', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='b8c59372-9bbd-468b-89bb-d57919e0f7da', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('denominator_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'denominators', to=orm['relatori.DenominatorType'])),
            ('denominator_source', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'denominators', null=True, to=orm['relatori.DenominatorSource'])),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominators', null=True, to=orm['simple_locations.Area'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='denominators', null=True, to=orm['simple_locations.Facility'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('relatori', ['Denominator'])

        # Adding model 'Settings'
        db.create_table('relatori_settings', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='a5989d81-a37d-4b1e-b8ce-96304ce1ae9f', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple_locations.Facility'])),
            ('denominator_source', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'settings', null=True, to=orm['relatori.DenominatorSource'])),
        ))
        db.send_create_signal('relatori', ['Settings'])

        # Adding model 'Option'
        db.create_table('relatori_option', (
            ('uuid', self.gf('django.db.models.fields.CharField')(default='f9394ff3-f206-4fae-a9b9-c3cc4f296192', unique=True, max_length=36, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('datagroup', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'options', to=orm['relatori.DataGroup'])),
        ))
        db.send_create_signal('relatori', ['Option'])


    def backwards(self, orm):
        
        # Deleting model 'DataFormType'
        db.delete_table('relatori_dataformtype')

        # Deleting model 'DataForm'
        db.delete_table('relatori_dataform')

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

        # Deleting model 'Option'
        db.delete_table('relatori_option')


    models = {
        'relatori.cell': {
            'Meta': {'object_name': 'Cell'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            'data_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cells'", 'to': "orm['relatori.DataFormType']"}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'60a95749-f0d7-4b4f-b88c-c3397a2b17ab'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.celldata': {
            'Meta': {'object_name': 'CellData'},
            'cell': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.Cell']"}),
            'data_form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.DataForm']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'844236c8-1048-4deb-a5f1-87f3de6ddd2d'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'})
        },
        'relatori.dataform': {
            'Meta': {'object_name': 'DataForm'},
            'data_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': "orm['relatori.DataFormType']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'data_forms'", 'to': "orm['simple_locations.Facility']"}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'b73eae78-fcb7-4c65-a573-5d3600d4043e'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'relatori.dataformtype': {
            'Meta': {'object_name': 'DataFormType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'sheet_index': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'cd3fe13c-8385-432c-91bd-96ef3cb086fa'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'relatori.datagroup': {
            'Meta': {'object_name': 'DataGroup'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'data_groups'", 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'col': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'row': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'acd7512d-7908-47f3-b6c0-24bdd08afa30'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '140', 'blank': 'True'})
        },
        'relatori.denominator': {
            'Meta': {'object_name': 'Denominator'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominators'", 'null': 'True', 'to': "orm['simple_locations.Area']"}),
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'denominators'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'denominators'", 'to': "orm['relatori.DenominatorType']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'denominators'", 'null': 'True', 'to': "orm['simple_locations.Facility']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'42ab00e9-5741-4e8a-a26c-0dbf1769cee3'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.denominatorsource': {
            'Meta': {'object_name': 'DenominatorSource'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'cc0bc855-3b78-4447-932c-35256c2e15b6'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.denominatortype': {
            'Meta': {'object_name': 'DenominatorType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'5ef09689-dc65-4f96-918b-de68de0b4333'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['simple_locations.Facility']"}),
            'indicator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['relatori.IndicatorType']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'d24ff243-ce91-48fe-b90d-920b9c2ea1e0'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.indicatortype': {
            'Meta': {'object_name': 'IndicatorType'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'indicator_type'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_type'", 'null': 'True', 'to': "orm['relatori.DenominatorType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'58932353-83dc-4430-902a-ab10786d78f6'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.option': {
            'Meta': {'object_name': 'Option'},
            'datagroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'options'", 'to': "orm['relatori.DataGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'2e12ad28-5fc1-43e0-8b53-99343385a764'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.settings': {
            'Meta': {'object_name': 'Settings'},
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'settings'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simple_locations.Facility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c890db88-d27b-4721-927a-f08103480bde'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
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
        'simple_locations.facility': {
            'Meta': {'object_name': 'Facility'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'facility'", 'null': 'True', 'to': "orm['simple_locations.Area']"}),
            'catchment_areas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'catchment'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['simple_locations.Area']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simple_locations.Point']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'facility'", 'null': 'True', 'to': "orm['simple_locations.Facility']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simple_locations.FacilityType']", 'null': 'True', 'blank': 'True'})
        },
        'simple_locations.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
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
