# Generated by Django 2.0.5 on 2018-11-08 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0027_auto_20180907_0251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='installer',
            options={'ordering': ('version',)},
        ),
        migrations.AddField(
            model_name='installer',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moderator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gamelink',
            name='website',
            field=models.CharField(blank=True, choices=[('wikipedia', 'Wikipedia'), ('pcgamingwiki', 'PCGamingWiki'), ('mobygames', 'MobyGames'), ('winehq', 'WineHQ AppDB'), ('lemonamiga', 'Lemon Amiga'), ('github', 'Github'), ('origin', 'Origin'), ('battlenet', 'Battle.net'), ('ubisoft', 'Ubisoft')], max_length=32),
        ),
    ]
