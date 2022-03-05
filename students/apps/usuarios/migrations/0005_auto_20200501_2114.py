# Generated by Django 2.2.6 on 2020-05-02 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0004_auto_20200501_2044"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("grade", models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name="CoursePerStudent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("courses", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="usuarios.Course")),
                ("students", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="usuarios.Student")),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="grades",
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="usuarios.Grade"),
        ),
    ]
