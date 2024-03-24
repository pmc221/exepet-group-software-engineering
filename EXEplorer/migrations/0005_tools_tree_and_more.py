# Generated by Django 5.0.2 on 2024-03-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EXEplorer', '0004_remove_userprofile_coins_userprofile_cherries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('toolsID', models.AutoField(primary_key=True, serialize=False, verbose_name='Tools ID')),
                ('toolsName', models.CharField(max_length=100, verbose_name='Tools Name')),
                ('toolsDescription', models.TextField(verbose_name='Tools Description')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree', models.PositiveIntegerField(default=0, verbose_name='tree')),
                ('treeComebackTime', models.DateTimeField(verbose_name='Comeback Time')),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='carbonFootfrint',
            new_name='carbonFootprint',
        ),
    ]