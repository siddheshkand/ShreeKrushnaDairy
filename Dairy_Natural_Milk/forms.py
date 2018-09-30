from django import forms

from . import models


class CreateTransaction(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = [
            'transaction_name',
            'bank_id',
            'amount',
            'transaction_type',
            'transaction_date',
        ]
