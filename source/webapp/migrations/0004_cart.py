# Generated by Django 4.1.3 on 2022-12-12 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_product_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='количество')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='webapp.product', verbose_name='продукт в корзине')),
            ],
        ),
    ]