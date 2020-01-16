# Generated by Django 3.0.2 on 2020-01-16 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_boast', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('net_votes', models.IntegerField(default=0)),
            ],
        ),
    ]
