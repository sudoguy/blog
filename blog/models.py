# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=u'Автор')
    title = models.CharField(max_length=200, verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name=u'Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name=u'Дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
