from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    brief_description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'company'


class CompanyComment(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'company_comment'


class Qualification(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey('UserAdditionalInfo', models.CASCADE)
    topic = models.ForeignKey('Topic', models.CASCADE)
    subtopic = models.ForeignKey('Subtopic', models.CASCADE)
    qualification_type = models.ForeignKey('QualificationType', models.CASCADE)
    qualification_subtype = models.ForeignKey('QualificationSubtype', models.CASCADE)

    class Meta:
        db_table = 'qualification'


class QualificationSubtype(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)
    qualification_type = models.ForeignKey('QualificationType', models.CASCADE)

    class Meta:
        db_table = 'qualification_subtype'


class QualificationType(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'qualification_type'


class Source(models.Model):
    type = models.ForeignKey('SourceType', models.CASCADE)
    subtype = models.ForeignKey('SourceSubtype', models.CASCADE)
    media = models.ForeignKey('SourceMedia', models.CASCADE)
    link = models.CharField(max_length=1000)

    class Meta:
        db_table = 'source'


class SourceComment(models.Model):
    source = models.ForeignKey(Source, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'source_comment'


class SourceMedia(models.Model):
    media = models.CharField(max_length=70)

    class Meta:
        db_table = 'source_media'


class SourceSubtype(models.Model):
    subtype = models.CharField(max_length=70)

    class Meta:
        db_table = 'source_subtype'


class SourceType(models.Model):
    type = models.CharField(max_length=70)

    class Meta:
        db_table = 'source_type'


class Statement(models.Model):
    text = models.CharField(max_length=1000)
    subtopic_company = models.ForeignKey('SubtopicCompany', models.CASCADE)

    class Meta:
        db_table = 'statement'


class StatementComment(models.Model):
    statement = models.ForeignKey(Statement, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'statement_comment'


class StatementSource(models.Model):
    statement = models.ForeignKey('SubtopicCompany', models.CASCADE)
    source = models.ForeignKey(Source, models.CASCADE)
    is_backing = models.BooleanField()
    replacement_text = models.CharField(max_length=1000)

    class Meta:
        db_table = 'statement_source'


class StatementSourceComments(models.Model):
    statement_source = models.ForeignKey(StatementSource, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'statement_source_comments'


class Subtopic(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)
    topic = models.ForeignKey('Topic', models.CASCADE)

    class Meta:
        db_table = 'subtopic'


class SubtopicComment(models.Model):
    subtopic = models.ForeignKey(Subtopic, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'subtopic_comment'


class SubtopicCompany(models.Model):
    subtopic = models.ForeignKey(Subtopic, models.CASCADE)
    company = models.ForeignKey(Company, models.CASCADE)

    class Meta:
        db_table = 'subtopic_company'


class SubtopicCompanyComment(models.Model):
    subtopic_company = models.ForeignKey(SubtopicCompany, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'subtopic_company_comment'


class Topic(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'topic'


class TopicComment(models.Model):
    topic = models.ForeignKey(Topic, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'topic_comment'


class TopicCompany(models.Model):
    topic = models.ForeignKey(Topic, models.CASCADE)
    company = models.ForeignKey(Company, models.CASCADE)

    class Meta:
        db_table = 'topic_company'


class TopicCompanyComment(models.Model):
    topic_company = models.ForeignKey(TopicCompany, models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'topic_company_comment'


class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=70, null=True)
    photo_link = models.CharField(max_length=70, null=True)
    fb_username = models.CharField(max_length=70, null=True)
    is_photo_id_verified = models.BooleanField()
    bio = models.CharField(max_length=5000, null=True)
    class Meta:
        db_table = 'user_additional'


class Vote(models.Model):
    qualification = models.ForeignKey(QualificationType, models.CASCADE)
    voter = models.ForeignKey(UserAdditionalInfo, models.CASCADE)

    class Meta:
        db_table = 'vote'
