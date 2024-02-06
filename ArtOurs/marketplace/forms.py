from django import forms

class OrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=0, max_value=5)
    comment = forms.CharField(widget=forms.Textarea)
