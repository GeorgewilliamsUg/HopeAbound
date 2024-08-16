# Generated by Django 4.2.14 on 2024-08-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Child_class', models.CharField(choices=[('P1', 'Primary 1'), ('P2', 'Primary 2'), ('P3', 'Primary 3'), ('P4', 'Primary 4'), ('P5', 'Primary 5'), ('P6', 'Primary 6'), ('P7', 'Primary 7'), ('S', 'Secondary'), ('T', 'Tertiary'), ('u', 'University')], max_length=10)),
                ('is_orphan', models.BooleanField(default=False)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='children')),
                ('story', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
