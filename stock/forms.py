from django import forms

class OrderForm(forms.Form):
    product_name = forms.ChoiceField(label='Product', choices=[], initial=0)
    quantity = forms.IntegerField(label='Quantity', initial=0)

    def __init__(self, products=None, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        if products:
            self.fields['product_name'].choices = list(enumerate(products))
