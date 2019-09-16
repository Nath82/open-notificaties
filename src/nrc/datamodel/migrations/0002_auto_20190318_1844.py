# Generated by Django 2.1.7 on 2019-03-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="filter",
            options={
                "ordering": ("id",),
                "verbose_name": "filter-onderdeel",
                "verbose_name_plural": "filter-onderdelen",
            },
        ),
        migrations.AlterModelOptions(
            name="filtergroup",
            options={"verbose_name": "filter", "verbose_name_plural": "filters"},
        ),
        migrations.AlterModelOptions(
            name="kanaal",
            options={"verbose_name": "kanaal", "verbose_name_plural": "kanalen"},
        ),
        migrations.AlterField(
            model_name="abonnement",
            name="auth",
            field=models.CharField(
                blank=True,
                help_text='Autorisatie header invulling voor het vesturen naar de "Callback URL". Voorbeeld: Bearer a4daa31...',
                max_length=1000,
                verbose_name="Autorisatie header",
            ),
        ),
        migrations.AlterField(
            model_name="abonnement",
            name="callback_url",
            field=models.URLField(
                help_text="De URL waar notificaties naar toe gestuurd dienen te worden. Deze URL dient uit te komen bij een API die geschikt is om notificaties op te ontvangen.",
                unique=True,
                verbose_name="Callback URL",
            ),
        ),
        migrations.AlterField(
            model_name="filter",
            name="key",
            field=models.CharField(max_length=100, verbose_name="Sleutel"),
        ),
        migrations.AlterField(
            model_name="filter",
            name="value",
            field=models.CharField(max_length=1000, verbose_name="Waarde"),
        ),
        migrations.AlterField(
            model_name="kanaal",
            name="documentatie_link",
            field=models.URLField(
                blank=True,
                default="",
                help_text="URL naar documentatie.",
                verbose_name="Documentatie link",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="kanaal",
            name="naam",
            field=models.CharField(
                help_text='Naam van het kanaal (ook wel "Exchange" genoemd) dat de bron vertegenwoordigd.',
                max_length=50,
                unique=True,
                verbose_name="Naam",
            ),
        ),
    ]
