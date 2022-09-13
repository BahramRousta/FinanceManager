from django.db import models

from accounts.models import CustomUser


class Bank(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # logo = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50,
                            unique=True)

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    parent = models.OneToOneField(Category,
                                  on_delete=models.CASCADE)
    name = models.CharField(max_length=50,
                            unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.parent}"


class Transition(models.Model):
    owner = models.ForeignKey(CustomUser,
                              on_delete=models.CASCADE,
                              related_name='transition')
    name = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,
                                     on_delete=models.CASCADE)
    time_milis = models.PositiveIntegerField(null=True,
                                             blank=True)
    time_local = models.CharField(max_length=100,
                                  null=True,
                                  blank=True)
    time_type = models.IntegerField(null=True,
                                    blank=True)
    description = models.TextField(null=True,
                                   blank=True)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    RENT = 'Rent'
    DEBT = 'Debt'
    BUY = 'Buy'

    OPERATION_CHOICES = [
        (RENT, 'وام'),
        (DEBT, 'بدهی'),
        (BUY, 'خرید'),
    ]

    operation = models.CharField(max_length=10,
                                 choices=OPERATION_CHOICES)

    def __str__(self) -> str:
        return self.name
