from django.db import models

TIP_PHOTO = ((0, 'Индивидуальная'),
             (1, 'Семейная'),
             (2, 'Парная'),
             (3, 'Видеоролики с фото'),
             (4, 'Детская'),
             (5, 'Мероприятия'),
             (6, 'Животные'),
             (7, 'Коллаж')
             )


class Zapis(models.Model):
    class Meta:
        verbose_name = 'Запись на фото'
        verbose_name_plural = 'Запись на фото'

    name = models.CharField('Имя', max_length=255, blank=False, null=False)
    email = models.CharField('email', max_length=255, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=255, blank=False, null=False)
    date = models.DateField('Дата записиси', auto_now_add=False, editable=True, null=True, blank=True)
    type_photoset = models.IntegerField('Тип фотосессии', choices=TIP_PHOTO, null=False, blank=False)
    comment = models.CharField('Комментарий пользователя', max_length=3000, blank=True, null=True)


class Back(models.Model):
    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'

    name_back = models.CharField('Имя', max_length=255, blank=False, null=False)
    email_back = models.CharField('email', max_length=255, blank=False, null=False)
    phone_back = models.CharField('Телефон', max_length=255, blank=False, null=False)
