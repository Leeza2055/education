# Generated by Django 2.2.3 on 2019-07-20 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logo')),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('facebook', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='program')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('syllabus', models.FileField(upload_to='syllabus')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='teacher')),
                ('is_hod', models.BooleanField(default=False)),
                ('education', models.CharField(max_length=50)),
                ('post', models.CharField(choices=[('lecturer', 'Lecturer'), ('assistant_professor', 'Assistant Professor'), ('professor', 'Professor')], max_length=100)),
                ('program', models.ManyToManyField(to='eduapp.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('credit_hour', models.CharField(max_length=50)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.Semester')),
            ],
        ),
    ]
