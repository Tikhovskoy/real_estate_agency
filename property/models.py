from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    new_building = models.BooleanField('Новостройка', null=True, blank=True)
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField('Город, где находится квартира', max_length=50, db_index=True)
    town_district = models.CharField('Район города', max_length=50, blank=True)
    address = models.TextField('Адрес квартиры', blank=True)
    floor = models.CharField('Этаж', max_length=3, blank=True)

    rooms_number = models.IntegerField('Количество комнат', db_index=True)
    living_area = models.IntegerField('Жилая площадь (кв.м)', null=True, blank=True)

    has_balcony = models.BooleanField('Есть балкон', blank=True)
    active = models.BooleanField('Активно', db_index=True)
    construction_year = models.IntegerField('Год постройки дома', null=True, blank=True, db_index=True)

    likes = models.ManyToManyField(User, related_name='liked_flats', verbose_name='Кто лайкнул', blank=True)
    owners = models.ManyToManyField('Owner', related_name='flats_as_owner', blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} — {self.price}₽'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто жаловался', related_name='complaints')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name='Квартира', related_name='complaints')
    complaint_text = models.TextField('Текст жалобы')

    def __str__(self):
        return f'Жалоба от {self.user} на {self.flat}'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    pure_phone = PhoneNumberField('Телефон владельца', region='RU', blank=False, null=False)

    def __str__(self):
        return self.name
