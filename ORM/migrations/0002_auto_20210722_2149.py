# Generated by Django 3.2.4 on 2021-07-22 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('telephone', models.BigIntegerField()),
                ('addr', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='图书id')),
                ('title', models.CharField(max_length=32)),
                ('publishDate', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Authors', models.ManyToManyField(to='ORM.Author')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ORM.publish')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='authorDetail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ORM.authordetail'),
        ),
    ]
