# Generated by Django 5.0.7 on 2024-11-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('division_id', models.IntegerField(blank=True, null=True)),
                ('district_id', models.IntegerField(blank=True, null=True)),
                ('subdistrict_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'admins',
            },
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('application_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=510)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('religion', models.CharField(max_length=255)),
                ('birth_country', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_division_id', models.IntegerField()),
                ('birth_district_id', models.IntegerField()),
                ('birth_subdistrict_id', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('father_name', models.CharField(max_length=255)),
                ('father_nid', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=255)),
                ('mother_nid', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=20)),
                ('relationship', models.CharField(choices=[('mother', 'mother'), ('father', 'father'), ('brother', 'brother'), ('sister', 'sister')], max_length=10)),
                ('division_id', models.IntegerField()),
                ('district_id', models.IntegerField()),
                ('subdistrict_id', models.IntegerField()),
                ('healthcare_id', models.IntegerField()),
                ('application_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'applicants',
            },
        ),
        migrations.CreateModel(
            name='BabyReg',
            fields=[
                ('reg_no', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('birth', models.CharField(blank=True, max_length=20, null=True)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_nid', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_nid', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('vaccine_centre', models.CharField(blank=True, max_length=255, null=True)),
                ('user_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'baby_reg',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'districts',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'divisions',
            },
        ),
        migrations.CreateModel(
            name='Healthcare',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'healthcare',
            },
        ),
        migrations.CreateModel(
            name='Subdistrict',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'subdistricts',
            },
        ),
        migrations.CreateModel(
            name='VaccinationSchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('application_id', models.CharField(max_length=100)),
                ('healthcare_id', models.IntegerField()),
                ('vaccine_id', models.IntegerField()),
                ('volunteer_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'vaccination_schedule',
            },
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vaccine_code', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vaccine',
            },
        ),
        migrations.CreateModel(
            name='VaccineStatus',
            fields=[
                ('application_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vaccine_status',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'volunteers',
            },
        ),
        migrations.AlterField(
            model_name='citizen',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='father_nid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='mother_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='mother_nid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='permanent_district',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='permanent_division',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='permanent_upazila',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='present_district',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='present_division',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='present_upazila',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='username',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='citizen',
            table='citizen',
        ),
    ]
