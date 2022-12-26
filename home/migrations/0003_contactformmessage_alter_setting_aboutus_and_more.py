# Generated by Django 4.1.3 on 2022-12-24 22:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_setting_facebook_alter_setting_instagram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('message', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('New ', 'New'), ('Read', 'Read')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]