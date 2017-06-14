# -*- coding: utf-8 -*-
from django import forms

class IndexForm(forms.Form):
    name = forms.CharField(required="True", max_length=30)
    last_name = forms.CharField(required="True", max_length=40)
