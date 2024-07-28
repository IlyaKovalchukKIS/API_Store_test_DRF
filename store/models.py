from django.db import models


class Advertisement(models.Model):
    id_advertisement = models.BigIntegerField(null=False)
    title = models.CharField()
    author = models.CharField()
    count_view = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["position"]
