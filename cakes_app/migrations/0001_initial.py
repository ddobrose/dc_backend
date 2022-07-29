# Generated by Django 4.0.6 on 2022-07-28 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(choices=[('Very Vanilla', 'Very Vanilla'), ('Crazy Coco', 'Crazy Coco'), ('Sweetie Strawberry', 'Sweetie Strawberry'), ('Birthday Bonanza', 'Birthday Bonanza'), ('Loco Lemon', 'Loco Lemon'), ('White Coco Razz', 'White Coco Razz'), ('Gluten Free Cookie Craze', 'Gluten Free Cookie Craze'), ('Ridiculous Red Velvet', 'Ridiculous Red Velvet'), ('Scintillating Cinnamon', 'Scintillating Cinnamon'), ('Crisp Carrot', 'Crisp Carrot')], max_length=100)),
                ('occasion', models.CharField(blank=True, max_length=100)),
                ('frosting_level', models.CharField(choices=[('None', 'None'), ('Drizzle', 'Drizzle'), ('Normal', 'Normal'), ('Extra', 'Extra')], default='Normal', max_length=100)),
                ('decoration', models.CharField(choices=[('Happy Birthday', 'Happy Birthday'), ('Graduation', 'Graduation'), ('Independence Day', 'Independence Day'), ('Thank You', 'Thank You'), ('Just Because', 'Just Because'), ('None', 'None')], default='None', max_length=100)),
                ('message_card', models.CharField(blank=True, max_length=200)),
                ('size', models.CharField(choices=[('Dozen Cupcakes', 'Dozen Cupcakes'), ('Personal Size Cake', 'Personal Size Cake'), ('Triple Tower Personal Size Cakes', 'Triple Tower Personal Size Cakes'), ('12 box of Personal Size Cakes', '12 box of Personal Size Cakes'), ('8 Inch Cake', '8 Inch Cake'), ('10 Inch Cake', '10 Inch Cake'), ('Layered Cake(10in bottom 8in top)', 'Layered Cake(10in bottom 8in top)')], max_length=100)),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField(null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cakes_app.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_flavor', models.CharField(choices=[('Very Vanilla', 'Very Vanilla'), ('Crazy Coco', 'Crazy Coco'), ('Sweetie Strawberry', 'Sweetie Strawberry'), ('Birthday Bonanza', 'Birthday Bonanza'), ('Loco Lemon', 'Loco Lemon'), ('White Coco Razz', 'White Coco Razz'), ('Gluten Free Cookie Craze', 'Gluten Free Cookie Craze'), ('Ridiculous Red Velvet', 'Ridiculous Red Velvet'), ('Scintillating Cinnamon', 'Scintillating Cinnamon'), ('Crisp Carrot', 'Crisp Carrot')], default='Very Vanilla', max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='cakes_app.guest'),
        ),
    ]
