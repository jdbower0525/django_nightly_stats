from __future__ import unicode_literals
import datetime

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 20:08


from django.db import migrations


def add_days(apps, schema_editor):
    Day = apps.get_model("database", "Day")
    one = Day(target_date=datetime.date(2016, 11, 1), day="Tuesday",
              sales=13000, closing_manager="Nicole", lunch_sales=3000,
              lbw=13.5, takeaway=3444, grill='Gaspar', prime_acc=75.5,
              hw='Steph', drop=3.45)
    one.save()
    two = Day(target_date=datetime.date(2016, 11, 2), day='Wednesday',
              sales=6000, closing_manager='Ryan', lunch_sales=1500,
              lbw=11.5, takeaway=2400, grill='Jaime', prime_acc=81.2,
              hw='Sean', drop=-3.2)
    two.save()
    three = Day(target_date=datetime.date(2016, 11, 3), day='Thursday',
                sales=12000, closing_manager='Nici', lunch_sales=1500,
                lbw=12.5, takeaway=3400, grill='Jose', prime_acc=72.2,
                hw='Shae', drop=3.4)
    three.save()
    four = Day(target_date=datetime.date(2016, 11, 4), day='Friday',
               sales=18550, closing_manager='Nicole', lunch_sales=4550,
               lbw=9.5, takeaway=1200, grill='Gaspar', prime_acc=82.2,
               hw='Steph', drop=2.3)
    four.save()
    five = Day(target_date=datetime.date(2016, 11, 5), day='Saturday',
               sales=21143, closing_manager='Nicole', lunch_sales=3550,
               lbw=13.4, takeaway=4000, grill='Rojas', prime_acc=62.2,
               hw='Steph', drop=4.5)
    five.save()
    six = Day(target_date=datetime.date(2016, 11, 6), day='Sunday',
              sales=13000, closing_manager='Ryan', lunch_sales=2340,
              lbw=11.4, takeaway=2300, grill='Gaspar', prime_acc=72.2,
              hw='Sean', drop=-3.4)
    six.save()
    seven = Day(target_date=datetime.date(2016, 11, 7), day='Monday',
                sales=9800, closing_manager='Nicole', lunch_sales=2340,
                lbw=9.8, takeaway=2220, grill='Jose', prime_acc=71.2,
                hw='Steph', drop=4.54)
    seven.save()
    eight = Day(target_date=datetime.date(2016, 11, 8), day='Tuesday',
                sales=7800, closing_manager='Jenn', lunch_sales=5140,
                lbw=12.4, takeaway=1120, grill='Gaspar', prime_acc=81.2,
                hw='Steph', drop=1.54)
    eight.save()
    nine = Day(target_date=datetime.date(2016, 11, 9), day='Wednesday',
               sales=8700, closing_manager='Ryan', lunch_sales=3330,
               lbw=12.4, takeaway=1120, grill='Gaspar', prime_acc=61.2,
               hw='Shae', drop=.54)
    nine.save()
    ten = Day(target_date=datetime.date(2016, 11, 10), day='Thursday',
              sales=6500, closing_manager='Nicole', lunch_sales=2330,
              lbw=11.4, takeaway=2120, grill='Jose', prime_acc=81.2,
              hw='Sean', drop=-3.54)
    ten.save()
    eleven = Day(target_date=datetime.date(2016, 11, 11), day='Friday',
                 sales=15000, closing_manager='Nici', lunch_sales=4330,
                 lbw=12.4, takeaway=3820, grill='Jamie', prime_acc=64.2,
                 hw='Shae', drop=4.54)
    eleven.save()
    twelve = Day(target_date=datetime.date(2016, 11, 12), day='Saturday',
                 sales=19450, closing_manager='Ryan', lunch_sales=5430,
                 lbw=9.4, takeaway=1230, grill='Gaspar', prime_acc=74.2,
                 hw='Steph', drop=2.34)
    twelve.save()
    thirteen = Day(target_date=datetime.date(2016, 11, 13), day='Sunday',
                   sales=12500, closing_manager='Jenn', lunch_sales=2230,
                   lbw=11.4, takeaway=4330, grill='Gaspar', prime_acc=54.2,
                   hw='Sean', drop=.44)
    thirteen.save()
    fourteen = Day(target_date=datetime.date(2016, 11, 14), day='Monday',
                   sales=8550, closing_manager='Nicole', lunch_sales=1130,
                   lbw=9.4, takeaway=2230, grill='Jose', prime_acc=77.2,
                   hw='Sean', drop=3.33)
    fourteen.save()
    fifteen = Day(target_date=datetime.date(2016, 11, 15), day='Tuesday',
                  sales=6900, closing_manager='Jenn', lunch_sales=2232,
                  lbw=12.4, takeaway=4230, grill='Gaspar', prime_acc=81.2,
                  hw='Steph', drop=1.33)
    fifteen.save()
    sixteen = Day(target_date=datetime.date(2016, 11, 16), day='Wednesday',
                  sales=8800, closing_manager='Nicole', lunch_sales=1228,
                  lbw=11.8, takeaway=2230, grill='Gaspar', prime_acc=61.2,
                  hw='Steph', drop=.33)
    sixteen.save()
    seventeen = Day(target_date=datetime.date(2016, 11, 17), day='Thursday',
                    sales=9550, closing_manager='Nici', lunch_sales=4321,
                    lbw=12.1, takeaway=2330, grill='Rojas', prime_acc=51.2,
                    hw='Sean', drop=-3.33)
    seventeen.save()
    eighteen = Day(target_date=datetime.date(2016, 11, 18), day='Friday',
                   sales=13500, closing_manager='Ryan', lunch_sales=1223,
                   lbw=9.8, takeaway=3440, grill='Nicole', prime_acc=77.3,
                   hw='Shae', drop=2.11)
    eighteen.save()
    nineteen = Day(target_date=datetime.date(2016, 11, 19), day='Saturday',
                   sales=19500, closing_manager='Nici', lunch_sales=4321,
                   lbw=12.1, takeaway=2330, grill='Rojas', prime_acc=81.2,
                   hw='Sean', drop=2.11)
    nineteen.save()
    twenty = Day(target_date=datetime.date(2016, 11, 20), day='Sunday',
                 sales=12000, closing_manager='Jenn', lunch_sales=2221,
                 lbw=9.8, takeaway=4110, grill='Gaspar', prime_acc=77.2,
                 hw='Steph', drop=.53)
    twenty.save()


class Migration(migrations.Migration):
    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_days)
    ]
