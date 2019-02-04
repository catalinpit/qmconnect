# Generated by Django 2.1.2 on 2019-02-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190126_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to='accounts.Profile', verbose_name='Member')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Conversation'),
        ),
    ]
