# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    id = models.IntegerField()
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    brief_description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'company'


class CompanyComment(models.Model):
    id = models.IntegerField()
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'company_comment'


class Qualification(models.Model):
    id = models.IntegerField()
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey('Topic', models.DO_NOTHING, blank=True, null=True)
    subtopic = models.ForeignKey('Subtopic', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qualification'


class QualificationSubtype(models.Model):
    id = models.IntegerField()
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    qualification_type = models.ForeignKey('QualificationType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qualification_subtype'


class QualificationType(models.Model):
    id = models.IntegerField()
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'qualification_type'


class Source(models.Model):
    id = models.IntegerField()
    type = models.ForeignKey('SourceType', models.DO_NOTHING, blank=True, null=True)
    subtype = models.ForeignKey('SourceSubtype', models.DO_NOTHING, blank=True, null=True)
    media = models.ForeignKey('SourceMedia', models.DO_NOTHING, blank=True, null=True)
    link = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'source'


class SourceComment(models.Model):
    id = models.IntegerField()
    source = models.ForeignKey(Source, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'source_comment'


class SourceMedia(models.Model):
    id = models.IntegerField()
    media = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'source_media'


class SourceSubtype(models.Model):
    id = models.IntegerField()
    subtype = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'source_subtype'


class SourceType(models.Model):
    id = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'source_type'


class Statement(models.Model):
    id = models.IntegerField()
    text = models.TextField(blank=True, null=True)  # This field type is a guess.
    subtopic_company = models.ForeignKey('SubtopicCompany', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statement'


class StatementComment(models.Model):
    id = models.IntegerField()
    statement = models.ForeignKey(Statement, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'statement_comment'


class StatementSource(models.Model):
    id = models.IntegerField()
    statement = models.ForeignKey('SubtopicCompany', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey(Source, models.DO_NOTHING, blank=True, null=True)
    is_backing = models.NullBooleanField()
    replacement_text = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'statement_source'


class StatementSourceComments(models.Model):
    id = models.IntegerField()
    statement_source = models.ForeignKey(StatementSource, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'statement_source_comments'


class Subtopic(models.Model):
    id = models.IntegerField()
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    topic = models.ForeignKey('Topic', models.DO_NOTHING, blank=True, null=True)
    subtopic_company = models.ForeignKey('SubtopicCompany', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subtopic'


class SubtopicComment(models.Model):
    id = models.IntegerField()
    subtopic = models.ForeignKey(Subtopic, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'subtopic_comment'


class SubtopicCompany(models.Model):
    id = models.IntegerField()
    subtopic = models.ForeignKey(Subtopic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subtopic_company'


class SubtopicCompanyComment(models.Model):
    id = models.IntegerField()
    subtopic_company = models.ForeignKey(SubtopicCompany, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'subtopic_company_comment'


class Topic(models.Model):
    id = models.IntegerField()
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'topic'


class TopicComment(models.Model):
    id = models.IntegerField()
    topic = models.ForeignKey(Topic, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'topic_comment'


class TopicCompany(models.Model):
    id = models.IntegerField()
    topic = models.ForeignKey(Topic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topic_company'


class TopicCompanyComment(models.Model):
    id = models.IntegerField()
    topic_company = models.ForeignKey(TopicCompany, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'topic_company_comment'


class User(models.Model):
    id = models.IntegerField()
    email = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    date_joined = models.DateTimeField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    nickname = models.TextField(blank=True, null=True)  # This field type is a guess.
    password = models.TextField(blank=True, null=True)  # This field type is a guess.
    photo_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    fb_username = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_photo_id_verified = models.NullBooleanField()
    bio = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user'


class Vote(models.Model):
    id = models.IntegerField()
    qualification = models.ForeignKey(QualificationType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vote'
