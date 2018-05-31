from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120)

    def __str__(self):
        return "Клиент %s %s " % (self.name, self.email)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'All Subscriber'
