# Generated by Django 4.0.3 on 2022-05-03 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('totalPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('address', models.TextField(default='N/A')),
                ('cart_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('image_url', models.TextField(default='N/A')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(default='N/A')),
                ('image_url', models.TextField(default='N/A')),
                ('phone', models.BigIntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('item_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='N/A', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('cart_Id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.cart')),
                ('food_Id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurant'),
        ),
        migrations.AddIndex(
            model_name='restaurant',
            index=models.Index(fields=['name'], name='rest_name_idx'),
        ),
        migrations.AddIndex(
            model_name='food',
            index=models.Index(fields=['name'], name='food_name_idx'),
        ),
        migrations.AddIndex(
            model_name='food',
            index=models.Index(fields=['price'], name='price_idx'),
        ),
    ]
