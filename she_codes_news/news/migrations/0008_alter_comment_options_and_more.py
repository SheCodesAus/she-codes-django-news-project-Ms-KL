# Generated by Django 4.1.3 on 2022-12-11 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='comment_active',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='comment_created_on',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='email',
            new_name='comment_email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='comment_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='commenter_name',
        ),
    ]
