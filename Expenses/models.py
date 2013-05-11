from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget


class ExpenseSheet(models.Model):
    created_by = models.ForeignKey(User, to_field='id', related_name="sheet_belongs_to")
    title = models.CharField(max_length=15)
    expiry = models.DateField(blank=False)
    collaborators = models.ManyToManyField(User, related_name="is_a_collaborator")
    total = models.IntegerField(default=0, blank=False)


class Expense(models.Model):
    created_by = models.ForeignKey(User)
    belongs_to_sheet = models.ForeignKey(ExpenseSheet)
    purpose = models.CharField(max_length=15, blank=False)
    amount = models.IntegerField(blank=False)


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('purpose', 'amount')


class ExpenseSheetForm(ModelForm):
        class Meta:
            model = ExpenseSheet
            fields = ('collaborators','title','expiry')
            widgets = {'expiry': SelectDateWidget}