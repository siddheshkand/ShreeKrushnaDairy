from django.db import models

# Bank module
t_type = (
    ('ck', 'By Check'),
    ('ch', 'By Cash'),
    ('cd', 'By Card'),
    ('ol', 'Online'),
)


class Bank(models.Model):
    name_of_bank = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=20, null=True)
    account_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name_of_bank


class Transaction(models.Model):
    transaction_name = models.CharField(max_length=200)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=4, choices=t_type)
    transaction_date = models.DateField()

    def __str__(self):
        return self.transaction_name
