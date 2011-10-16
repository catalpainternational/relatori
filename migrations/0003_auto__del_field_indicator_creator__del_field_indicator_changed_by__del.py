# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Indicator.creator'
        db.delete_column('relatori_indicator', 'creator_id')

        # Deleting field 'Indicator.changed_by'
        db.delete_column('relatori_indicator', 'changed_by_id')

        # Deleting field 'Indicator.void_reason'
        db.delete_column('relatori_indicator', 'void_reason')

        # Deleting field 'Indicator.date_created'
        db.delete_column('relatori_indicator', 'date_created')

        # Deleting field 'Indicator.date_changed'
        db.delete_column('relatori_indicator', 'date_changed')

        # Deleting field 'Indicator.voided_by'
        db.delete_column('relatori_indicator', 'voided_by_id')

        # Deleting field 'Indicator.voided'
        db.delete_column('relatori_indicator', 'voided')

        # Deleting field 'Indicator.date_voided'
        db.delete_column('relatori_indicator', 'date_voided')

        # Deleting field 'CellData.creator'
        db.delete_column('relatori_celldata', 'creator_id')

        # Deleting field 'CellData.voided'
        db.delete_column('relatori_celldata', 'voided')

        # Deleting field 'CellData.date_created'
        db.delete_column('relatori_celldata', 'date_created')

        # Deleting field 'CellData.changed_by'
        db.delete_column('relatori_celldata', 'changed_by_id')

        # Deleting field 'CellData.void_reason'
        db.delete_column('relatori_celldata', 'void_reason')

        # Deleting field 'CellData.date_changed'
        db.delete_column('relatori_celldata', 'date_changed')

        # Deleting field 'CellData.voided_by'
        db.delete_column('relatori_celldata', 'voided_by_id')

        # Deleting field 'CellData.date_voided'
        db.delete_column('relatori_celldata', 'date_voided')

        # Deleting field 'Cell.creator'
        db.delete_column('relatori_cell', 'creator_id')

        # Deleting field 'Cell.voided'
        db.delete_column('relatori_cell', 'voided')

        # Deleting field 'Cell.date_changed'
        db.delete_column('relatori_cell', 'date_changed')

        # Deleting field 'Cell.date_voided'
        db.delete_column('relatori_cell', 'date_voided')

        # Deleting field 'Cell.changed_by'
        db.delete_column('relatori_cell', 'changed_by_id')

        # Deleting field 'Cell.void_reason'
        db.delete_column('relatori_cell', 'void_reason')

        # Deleting field 'Cell.date_created'
        db.delete_column('relatori_cell', 'date_created')

        # Deleting field 'Cell.voided_by'
        db.delete_column('relatori_cell', 'voided_by_id')

        # Deleting field 'HMISForm.creator'
        db.delete_column('relatori_hmisform', 'creator_id')

        # Deleting field 'HMISForm.date_changed'
        db.delete_column('relatori_hmisform', 'date_changed')

        # Deleting field 'HMISForm.voided'
        db.delete_column('relatori_hmisform', 'voided')

        # Deleting field 'HMISForm.changed_by'
        db.delete_column('relatori_hmisform', 'changed_by_id')

        # Deleting field 'HMISForm.void_reason'
        db.delete_column('relatori_hmisform', 'void_reason')

        # Deleting field 'HMISForm.date_created'
        db.delete_column('relatori_hmisform', 'date_created')

        # Deleting field 'HMISForm.voided_by'
        db.delete_column('relatori_hmisform', 'voided_by_id')

        # Deleting field 'HMISForm.date_voided'
        db.delete_column('relatori_hmisform', 'date_voided')

        # Deleting field 'DataGroup.changed_by'
        db.delete_column('relatori_datagroup', 'changed_by_id')

        # Deleting field 'DataGroup.creator'
        db.delete_column('relatori_datagroup', 'creator_id')

        # Deleting field 'DataGroup.voided'
        db.delete_column('relatori_datagroup', 'voided')

        # Deleting field 'DataGroup.date_changed'
        db.delete_column('relatori_datagroup', 'date_changed')

        # Deleting field 'DataGroup.void_reason'
        db.delete_column('relatori_datagroup', 'void_reason')

        # Deleting field 'DataGroup.date_created'
        db.delete_column('relatori_datagroup', 'date_created')

        # Deleting field 'DataGroup.voided_by'
        db.delete_column('relatori_datagroup', 'voided_by_id')

        # Deleting field 'DataGroup.date_voided'
        db.delete_column('relatori_datagroup', 'date_voided')

        # Deleting field 'DenominatorSource.creator'
        db.delete_column('relatori_denominatorsource', 'creator_id')

        # Deleting field 'DenominatorSource.voided'
        db.delete_column('relatori_denominatorsource', 'voided')

        # Deleting field 'DenominatorSource.date_changed'
        db.delete_column('relatori_denominatorsource', 'date_changed')

        # Deleting field 'DenominatorSource.changed_by'
        db.delete_column('relatori_denominatorsource', 'changed_by_id')

        # Deleting field 'DenominatorSource.void_reason'
        db.delete_column('relatori_denominatorsource', 'void_reason')

        # Deleting field 'DenominatorSource.date_created'
        db.delete_column('relatori_denominatorsource', 'date_created')

        # Deleting field 'DenominatorSource.voided_by'
        db.delete_column('relatori_denominatorsource', 'voided_by_id')

        # Deleting field 'DenominatorSource.date_voided'
        db.delete_column('relatori_denominatorsource', 'date_voided')

        # Deleting field 'HMISFormType.creator'
        db.delete_column('relatori_hmisformtype', 'creator_id')

        # Deleting field 'HMISFormType.voided'
        db.delete_column('relatori_hmisformtype', 'voided')

        # Deleting field 'HMISFormType.date_created'
        db.delete_column('relatori_hmisformtype', 'date_created')

        # Deleting field 'HMISFormType.changed_by'
        db.delete_column('relatori_hmisformtype', 'changed_by_id')

        # Deleting field 'HMISFormType.void_reason'
        db.delete_column('relatori_hmisformtype', 'void_reason')

        # Deleting field 'HMISFormType.date_changed'
        db.delete_column('relatori_hmisformtype', 'date_changed')

        # Deleting field 'HMISFormType.voided_by'
        db.delete_column('relatori_hmisformtype', 'voided_by_id')

        # Deleting field 'HMISFormType.date_voided'
        db.delete_column('relatori_hmisformtype', 'date_voided')

        # Deleting field 'Denominator.void_reason'
        db.delete_column('relatori_denominator', 'void_reason')

        # Deleting field 'Denominator.changed_by'
        db.delete_column('relatori_denominator', 'changed_by_id')

        # Deleting field 'Denominator.creator'
        db.delete_column('relatori_denominator', 'creator_id')

        # Deleting field 'Denominator.date_created'
        db.delete_column('relatori_denominator', 'date_created')

        # Deleting field 'Denominator.date_changed'
        db.delete_column('relatori_denominator', 'date_changed')

        # Deleting field 'Denominator.voided_by'
        db.delete_column('relatori_denominator', 'voided_by_id')

        # Deleting field 'Denominator.voided'
        db.delete_column('relatori_denominator', 'voided')

        # Deleting field 'Denominator.date_voided'
        db.delete_column('relatori_denominator', 'date_voided')

        # Deleting field 'IndicatorType.creator'
        db.delete_column('relatori_indicatortype', 'creator_id')

        # Deleting field 'IndicatorType.voided'
        db.delete_column('relatori_indicatortype', 'voided')

        # Deleting field 'IndicatorType.date_changed'
        db.delete_column('relatori_indicatortype', 'date_changed')

        # Deleting field 'IndicatorType.date_voided'
        db.delete_column('relatori_indicatortype', 'date_voided')

        # Deleting field 'IndicatorType.void_reason'
        db.delete_column('relatori_indicatortype', 'void_reason')

        # Deleting field 'IndicatorType.date_created'
        db.delete_column('relatori_indicatortype', 'date_created')

        # Deleting field 'IndicatorType.voided_by'
        db.delete_column('relatori_indicatortype', 'voided_by_id')

        # Deleting field 'IndicatorType.changed_by'
        db.delete_column('relatori_indicatortype', 'changed_by_id')

        # Deleting field 'Settings.creator'
        db.delete_column('relatori_settings', 'creator_id')

        # Deleting field 'Settings.voided'
        db.delete_column('relatori_settings', 'voided')

        # Deleting field 'Settings.date_changed'
        db.delete_column('relatori_settings', 'date_changed')

        # Deleting field 'Settings.changed_by'
        db.delete_column('relatori_settings', 'changed_by_id')

        # Deleting field 'Settings.void_reason'
        db.delete_column('relatori_settings', 'void_reason')

        # Deleting field 'Settings.date_created'
        db.delete_column('relatori_settings', 'date_created')

        # Deleting field 'Settings.voided_by'
        db.delete_column('relatori_settings', 'voided_by_id')

        # Deleting field 'Settings.date_voided'
        db.delete_column('relatori_settings', 'date_voided')

        # Deleting field 'DenominatorType.creator'
        db.delete_column('relatori_denominatortype', 'creator_id')

        # Deleting field 'DenominatorType.voided'
        db.delete_column('relatori_denominatortype', 'voided')

        # Deleting field 'DenominatorType.date_changed'
        db.delete_column('relatori_denominatortype', 'date_changed')

        # Deleting field 'DenominatorType.changed_by'
        db.delete_column('relatori_denominatortype', 'changed_by_id')

        # Deleting field 'DenominatorType.void_reason'
        db.delete_column('relatori_denominatortype', 'void_reason')

        # Deleting field 'DenominatorType.date_created'
        db.delete_column('relatori_denominatortype', 'date_created')

        # Deleting field 'DenominatorType.voided_by'
        db.delete_column('relatori_denominatortype', 'voided_by_id')

        # Deleting field 'DenominatorType.date_voided'
        db.delete_column('relatori_denominatortype', 'date_voided')


    def backwards(self, orm):
        
        # Adding field 'Indicator.creator'
        db.add_column('relatori_indicator', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicator_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Indicator.changed_by'
        db.add_column('relatori_indicator', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicator_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Indicator.void_reason'
        db.add_column('relatori_indicator', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Indicator.date_created'
        raise RuntimeError("Cannot reverse this migration. 'Indicator.date_created' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Indicator.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'Indicator.date_changed' and its values cannot be restored.")

        # Adding field 'Indicator.voided_by'
        db.add_column('relatori_indicator', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicator_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Indicator.voided'
        db.add_column('relatori_indicator', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'Indicator.date_voided'
        db.add_column('relatori_indicator', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'CellData.creator'
        db.add_column('relatori_celldata', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='celldata_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'CellData.voided'
        db.add_column('relatori_celldata', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'CellData.date_created'
        raise RuntimeError("Cannot reverse this migration. 'CellData.date_created' and its values cannot be restored.")

        # Adding field 'CellData.changed_by'
        db.add_column('relatori_celldata', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='celldata_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'CellData.void_reason'
        db.add_column('relatori_celldata', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'CellData.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'CellData.date_changed' and its values cannot be restored.")

        # Adding field 'CellData.voided_by'
        db.add_column('relatori_celldata', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='celldata_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'CellData.date_voided'
        db.add_column('relatori_celldata', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Cell.creator'
        db.add_column('relatori_cell', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cell_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Cell.voided'
        db.add_column('relatori_cell', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Cell.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'Cell.date_changed' and its values cannot be restored.")

        # Adding field 'Cell.date_voided'
        db.add_column('relatori_cell', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Cell.changed_by'
        db.add_column('relatori_cell', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cell_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Cell.void_reason'
        db.add_column('relatori_cell', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Cell.date_created'
        raise RuntimeError("Cannot reverse this migration. 'Cell.date_created' and its values cannot be restored.")

        # Adding field 'Cell.voided_by'
        db.add_column('relatori_cell', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cell_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'HMISForm.creator'
        db.add_column('relatori_hmisform', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hmisform_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'HMISForm.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'HMISForm.date_changed' and its values cannot be restored.")

        # Adding field 'HMISForm.voided'
        db.add_column('relatori_hmisform', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'HMISForm.changed_by'
        db.add_column('relatori_hmisform', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hmisform_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'HMISForm.void_reason'
        db.add_column('relatori_hmisform', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'HMISForm.date_created'
        raise RuntimeError("Cannot reverse this migration. 'HMISForm.date_created' and its values cannot be restored.")

        # Adding field 'HMISForm.voided_by'
        db.add_column('relatori_hmisform', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hmisform_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'HMISForm.date_voided'
        db.add_column('relatori_hmisform', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'DataGroup.changed_by'
        db.add_column('relatori_datagroup', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='datagroup_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DataGroup.creator'
        db.add_column('relatori_datagroup', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='datagroup_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DataGroup.voided'
        db.add_column('relatori_datagroup', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'DataGroup.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'DataGroup.date_changed' and its values cannot be restored.")

        # Adding field 'DataGroup.void_reason'
        db.add_column('relatori_datagroup', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'DataGroup.date_created'
        raise RuntimeError("Cannot reverse this migration. 'DataGroup.date_created' and its values cannot be restored.")

        # Adding field 'DataGroup.voided_by'
        db.add_column('relatori_datagroup', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='datagroup_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DataGroup.date_voided'
        db.add_column('relatori_datagroup', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'DenominatorSource.creator'
        db.add_column('relatori_denominatorsource', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominatorsource_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DenominatorSource.voided'
        db.add_column('relatori_denominatorsource', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'DenominatorSource.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'DenominatorSource.date_changed' and its values cannot be restored.")

        # Adding field 'DenominatorSource.changed_by'
        db.add_column('relatori_denominatorsource', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominatorsource_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DenominatorSource.void_reason'
        db.add_column('relatori_denominatorsource', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'DenominatorSource.date_created'
        raise RuntimeError("Cannot reverse this migration. 'DenominatorSource.date_created' and its values cannot be restored.")

        # Adding field 'DenominatorSource.voided_by'
        db.add_column('relatori_denominatorsource', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominatorsource_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DenominatorSource.date_voided'
        db.add_column('relatori_denominatorsource', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'HMISFormType.creator'
        db.add_column('relatori_hmisformtype', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hmisformtype_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'HMISFormType.voided'
        db.add_column('relatori_hmisformtype', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'HMISFormType.date_created'
        raise RuntimeError("Cannot reverse this migration. 'HMISFormType.date_created' and its values cannot be restored.")

        # Adding field 'HMISFormType.changed_by'
        db.add_column('relatori_hmisformtype', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hmisformtype_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'HMISFormType.void_reason'
        db.add_column('relatori_hmisformtype', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'HMISFormType.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'HMISFormType.date_changed' and its values cannot be restored.")

        # Adding field 'HMISFormType.voided_by'
        db.add_column('relatori_hmisformtype', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hmisformtype_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'HMISFormType.date_voided'
        db.add_column('relatori_hmisformtype', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Denominator.void_reason'
        db.add_column('relatori_denominator', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # Adding field 'Denominator.changed_by'
        db.add_column('relatori_denominator', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominator_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Denominator.creator'
        db.add_column('relatori_denominator', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominator_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Denominator.date_created'
        raise RuntimeError("Cannot reverse this migration. 'Denominator.date_created' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Denominator.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'Denominator.date_changed' and its values cannot be restored.")

        # Adding field 'Denominator.voided_by'
        db.add_column('relatori_denominator', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominator_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Denominator.voided'
        db.add_column('relatori_denominator', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'Denominator.date_voided'
        db.add_column('relatori_denominator', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'IndicatorType.creator'
        db.add_column('relatori_indicatortype', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicatortype_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'IndicatorType.voided'
        db.add_column('relatori_indicatortype', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'IndicatorType.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'IndicatorType.date_changed' and its values cannot be restored.")

        # Adding field 'IndicatorType.date_voided'
        db.add_column('relatori_indicatortype', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'IndicatorType.void_reason'
        db.add_column('relatori_indicatortype', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'IndicatorType.date_created'
        raise RuntimeError("Cannot reverse this migration. 'IndicatorType.date_created' and its values cannot be restored.")

        # Adding field 'IndicatorType.voided_by'
        db.add_column('relatori_indicatortype', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicatortype_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'IndicatorType.changed_by'
        db.add_column('relatori_indicatortype', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicatortype_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Settings.creator'
        db.add_column('relatori_settings', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='settings_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Settings.voided'
        db.add_column('relatori_settings', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Settings.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'Settings.date_changed' and its values cannot be restored.")

        # Adding field 'Settings.changed_by'
        db.add_column('relatori_settings', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='settings_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Settings.void_reason'
        db.add_column('relatori_settings', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Settings.date_created'
        raise RuntimeError("Cannot reverse this migration. 'Settings.date_created' and its values cannot be restored.")

        # Adding field 'Settings.voided_by'
        db.add_column('relatori_settings', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='settings_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'Settings.date_voided'
        db.add_column('relatori_settings', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'DenominatorType.creator'
        db.add_column('relatori_denominatortype', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominatortype_creator_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DenominatorType.voided'
        db.add_column('relatori_denominatortype', 'voided', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'DenominatorType.date_changed'
        raise RuntimeError("Cannot reverse this migration. 'DenominatorType.date_changed' and its values cannot be restored.")

        # Adding field 'DenominatorType.changed_by'
        db.add_column('relatori_denominatortype', 'changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominatortype_changed_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DenominatorType.void_reason'
        db.add_column('relatori_denominatortype', 'void_reason', self.gf('django.db.models.fields.CharField')(default='', max_length=765, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'DenominatorType.date_created'
        raise RuntimeError("Cannot reverse this migration. 'DenominatorType.date_created' and its values cannot be restored.")

        # Adding field 'DenominatorType.voided_by'
        db.add_column('relatori_denominatortype', 'voided_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='denominatortype_voided_by_related', null=True, to=orm['auth.User'], blank=True), keep_default=False)

        # Adding field 'DenominatorType.date_voided'
        db.add_column('relatori_denominatortype', 'date_voided', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


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
            'hmis_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cells'", 'to': "orm['relatori.HMISFormType']"}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'86c56ba9-0ee2-4d77-b28a-79c196157266'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.celldata': {
            'Meta': {'object_name': 'CellData'},
            'cell': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.Cell']"}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cell_data'", 'to': "orm['relatori.HMISForm']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'ea6c8fb4-b6e8-4cdc-890f-b7ad3c1fdd49'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'})
        },
        'relatori.datagroup': {
            'Meta': {'object_name': 'DataGroup'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'data_groups'", 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'col': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'row': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'spreadsheet_cell': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'fc578e0d-641c-43e3-bacf-e47bddcaad82'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'a3562ec6-dce0-434a-8424-b8be53ae390d'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.denominatorsource': {
            'Meta': {'object_name': 'DenominatorSource'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'af91aba1-96d8-4b02-b6ef-d7528bd0f548'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.denominatortype': {
            'Meta': {'object_name': 'DenominatorType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c216dfdf-1e54-4546-af02-487c31fe0fc3'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.hmisform': {
            'Meta': {'object_name': 'HMISForm'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hmis_forms'", 'to': "orm['health_service.HealthFacility']"}),
            'hmis_form_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': "orm['relatori.HMISFormType']"}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'d6f81fba-ec1b-4f12-83bc-0fb6c379f7fd'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'relatori.hmisformtype': {
            'Meta': {'object_name': 'HMISFormType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'sheet_index': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'9005714c-a726-4f0b-af26-f719d86d6be1'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'relatori.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['health_service.HealthFacility']"}),
            'indicator_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'indicators'", 'to': "orm['relatori.IndicatorType']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'ccdc6691-81a4-42dd-a663-c63f900d732c'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'relatori.indicatortype': {
            'Meta': {'object_name': 'IndicatorType'},
            'cells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'indicator_type'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['relatori.Cell']"}),
            'denominator_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicator_type'", 'null': 'True', 'to': "orm['relatori.DenominatorType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'f14cb11f-3930-42ce-adea-874b2b9d1ec4'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
        },
        'relatori.settings': {
            'Meta': {'object_name': 'Settings'},
            'denominator_source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'settings'", 'null': 'True', 'to': "orm['relatori.DenominatorSource']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['health_service.HealthFacility']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'e878f0e9-b282-4795-b1ba-718df756ba91'", 'unique': 'True', 'max_length': '36', 'primary_key': 'True', 'db_index': 'True'})
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
