from django import forms
from .models import Pizza
# class PizzaForm(forms.Form): #django form class
#     topping1 = forms.CharField(label='Topping1',max_length=100,widget=forms.PasswordInput)
#     topping2 = forms.CharField(label='Topping2', max_length=100,widget=forms.Textarea)
#     size = forms.ChoiceField(label='size',choices=[('small','small'),
#                                                    ('medium','medium'),
#                                                    ('large','large')])

#dijango model form

class PizzaForm(forms.ModelForm):
    class Meta:
        model=Pizza
        fields = ['topping1','topping2','size']
        # labels = {'topping1':'T1'}
        # widgets ={'topping2':forms.PasswordInput}

class MultiplePizzaForm(forms.Form): # django form class
    number = forms.IntegerField(min_value=2,max_value=10)