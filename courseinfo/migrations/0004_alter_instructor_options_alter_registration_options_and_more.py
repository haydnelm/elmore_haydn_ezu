# Generated by Django 5.1.6 on 2025-02-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0003_alter_period_options_alter_semester_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['section', 'student']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['course', 'section_name', 'semester']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AddConstraint(
            model_name='instructor',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_instructor'),
        ),
        migrations.AddConstraint(
            model_name='registration',
            constraint=models.UniqueConstraint(fields=('section', 'student'), name='unique_registration'),
        ),
        migrations.AddConstraint(
            model_name='section',
            constraint=models.UniqueConstraint(fields=('semester', 'course', 'section_name'), name='unique_section'),
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_student'),
        ),
    ]
