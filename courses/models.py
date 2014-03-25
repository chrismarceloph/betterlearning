from django.db import models


class Course(models.Model):
    parents = models.ManyToManyField('self', related_name='children', symmetrical=False, blank=True)
    title = models.CharField(max_length=255)
    short_description = models.TextField(max_length=160, help_text='Max 160 characters', blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title
