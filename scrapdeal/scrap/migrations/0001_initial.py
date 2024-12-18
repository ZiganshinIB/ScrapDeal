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
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название завода')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')),
                ('executors', models.ManyToManyField(blank=True, related_name='factories', to=settings.AUTH_USER_MODEL, verbose_name='Исполнители')),
            ],
            options={
                'verbose_name': 'Завод',
                'verbose_name_plural': 'Заводы',
            },
        ),
    ]
