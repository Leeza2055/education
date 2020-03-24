# Generated by Django 2.2.3 on 2019-07-28 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0004_auto_20190728_1033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Facilities',
        ),
        migrations.AddField(
            model_name='application',
            name='city',
            field=models.CharField(default='hjgjh', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='plus2_pct',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='plus2_transcript',
            field=models.FileField(default='jhghjg', upload_to='plus2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eduapp.Program'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='program_time',
            field=models.CharField(choices=[('day', 'Day'), ('morning', 'Morning')], default='morning', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='slc_marksheet',
            field=models.FileField(default='jhgjgj', upload_to='slc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='slc_pct',
            field=models.DecimalField(decimal_places=2, default=45, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='zip_code',
            field=models.PositiveIntegerField(default=456646),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='date_of_birth',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=50),
        ),
    ]