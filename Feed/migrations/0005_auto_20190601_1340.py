# Generated by Django 2.2.1 on 2019-06-01 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Feed', '0004_event_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('time', models.DateTimeField(auto_now=True)),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Post/')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='NewsSource', to='Feed.Source')),
            ],
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Post/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
