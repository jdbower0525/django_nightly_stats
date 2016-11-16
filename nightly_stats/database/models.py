from django.db import models


class Day(models.Model):
    target_date = models.DateField('date of data')
    day = models.CharField(max_length=10)
    sales = models.IntegerField('total sales', default=0)
    closing_manager = models.CharField(max_length=10)
    lunch_sales = models.IntegerField('lunch sales', default=0)
    lbw = models.FloatField('lbw percentage', default=0)
    takeaway = models.IntegerField('takeaway sales', default=0)
    grill = models.CharField(max_length=15)
    prime_acc = models.FloatField('Prime Accuracy', default=0)
    hw = models.CharField(max_length=15)
    drop = models.FloatField('drop variance', default=0)
