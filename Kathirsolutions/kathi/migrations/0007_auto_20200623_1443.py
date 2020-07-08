# Generated by Django 3.0.3 on 2020-06-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kathi', '0006_employee_empid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empid', models.CharField(max_length=10)),
                ('activity', models.CharField(max_length=500)),
                ('workid', models.CharField(max_length=10)),
                ('plannedtime', models.IntegerField(default=0)),
                ('actualtime', models.IntegerField(default=0)),
                ('pic', models.ImageField(default=None, upload_to='')),
                ('work_remark', models.IntegerField(default=0)),
                ('submission_remark', models.IntegerField(default=0)),
                ('isComplete', models.IntegerField(default=0)),
                ('dependancy', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignedworks',
            name='planneddate',
        ),
    ]