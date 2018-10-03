from django.db import models

# Bank module
t_type = (
    ('ck', 'By Check'),
    ('ch', 'By Cash'),
    ('cd', 'By Card'),
    ('ol', 'Online'),
)

# New Account
RELATIONS = (
    ('farmer', 'शेतकरी'),
    ('friend', 'मित्र'),
    ('family', 'परिवार'),
    ('customer', 'ग्राहक'),
    ('Guest', 'पाहुणे'),
)


# शेतकरी
# मित्र
# परिवार
# ग्राहक
# पाहुणे


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


class Account(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    relation = models.CharField(max_length=100, choices=RELATIONS)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    registration_date = models.DateField(auto_now=True)
    date_of_birth = models.DateField()
