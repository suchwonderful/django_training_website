from django.apps import AppConfig


class TelebotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telebot'

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'