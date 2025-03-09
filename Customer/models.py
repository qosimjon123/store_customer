from django.db import models
from django.core.validators import MinValueValidator


class Client(models.Model):
    """
    Основная информация о клиенте в онлайн-магазине.
    Связана с пользователем из API аутентификации через user_id.
    """
    user_id = models.PositiveIntegerField(
        primary_key=True,
        editable=False,
        unique=True,
        null=False,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    loyalty_points = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    is_active = models.BooleanField(
        default=True,
    )


    def __str__(self):
        return f"{self.email} ({self.user_id})"





# Модель адреса клиента
class ClientAddress(models.Model):
    address_id = models.PositiveIntegerField(
        primary_key=True,
        default= None,
        editable=False,
    )
    client = models.ForeignKey(  # Здесь должно быть поле client
        Client,
        on_delete=models.CASCADE,
        related_name="addresses",  # Это поле связи с клиентом
    )
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["client", "is_default"]),
        ]

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country} ({self.client.email})"
