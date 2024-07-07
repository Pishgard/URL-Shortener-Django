from django.db import models

class Url(models.Model):
    url = models.URLField('لینک')
    slug = models.CharField('لینک کوتاه شده', max_length=120)
    visit = models.IntegerField('تعداد بازدید', default=0)
    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'لینک ها'
        verbose_name = 'لینک'

    def __str__(self):
        return f"{self.slug}"