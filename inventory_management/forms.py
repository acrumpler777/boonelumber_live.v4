from django.forms import ModelForm, Select
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type= 'date'


queryset=product.objects.all()

class POForm(forms.Form):
    company = forms.CharField(label='Company', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    address = forms.CharField(label='Address', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    phone = forms.CharField(label='Phone', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    email = forms.EmailField(label='Email', required=False, widget=forms.TextInput(attrs={'class': 'form-control' }))
    date = forms.DateField(label='Date', widget=DateInput(attrs={'class': 'form-control' }), required=False)



    unique_product1 = forms.ModelChoiceField(label='Product #1', queryset=queryset, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity1 = forms.IntegerField(label='Order Quantity #1', initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product2 = forms.ModelChoiceField(label='Product #2', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity2 = forms.IntegerField(label='Order Quantity #2', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product3 = forms.ModelChoiceField(label='Product #3', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity3 = forms.IntegerField(label='Order Quantity #3', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product4 = forms.ModelChoiceField(label='Product #4', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity4 = forms.IntegerField(label='Order Quantity #4', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product5 = forms.ModelChoiceField(label='Product #5', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity5 = forms.IntegerField(label='Order Quantity #5', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product6 = forms.ModelChoiceField(label='Product #6', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity6 = forms.IntegerField(label='Order Quantity #6', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product7 = forms.ModelChoiceField(label='Product #7', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity7 = forms.IntegerField(label='Order Quantity #7', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product8 = forms.ModelChoiceField(label='Product #8', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity8 = forms.IntegerField(label='Order Quantity #8', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product9 = forms.ModelChoiceField(label='Product #9', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity9 = forms.IntegerField(label='Order Quantity #9', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product10 = forms.ModelChoiceField(label='Product #10', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity10 = forms.IntegerField(label='Order Quantity #10', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product11 = forms.ModelChoiceField(label='Product #11', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity11 = forms.IntegerField(label='Order Quantity #11', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product12 = forms.ModelChoiceField(label='Product #12', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity12 = forms.IntegerField(label='Order Quantity #12', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product13 = forms.ModelChoiceField(label='Product #13', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity13 = forms.IntegerField(label='Order Quantity #13', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product14 = forms.ModelChoiceField(label='Product #14', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity14 = forms.IntegerField(label='Order Quantity #14', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product15 = forms.ModelChoiceField(label='Product #15', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity15 = forms.IntegerField(label='Order Quantity #15', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product16 = forms.ModelChoiceField(label='Product #16', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity16 = forms.IntegerField(label='Order Quantity #16', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product17 = forms.ModelChoiceField(label='Product #17', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity17 = forms.IntegerField(label='Order Quantity #17', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product18 = forms.ModelChoiceField(label='Product #18', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity18 = forms.IntegerField(label='Order Quantity #18', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product19 = forms.ModelChoiceField(label='Product #19', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity19 = forms.IntegerField(label='Order Quantity #19', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    unique_product20 = forms.ModelChoiceField(label='Product #20', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity20 = forms.IntegerField(label='Order Quantity #20', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))


override_choices = (
    ("----", "----"),
    ("Yes","Yes"),
)

class inventory_adjustment_form(forms.Form):

    unique_product1 = forms.ModelChoiceField(label='Product', widget=forms.Select(attrs={'class': 'form-control'}), queryset=queryset)
    order_quantity1 = forms.IntegerField(label='Adjustment Quantity', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    adjustment_reason = forms.CharField(label='Reason for Adjustment', required=False, max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control' }))
    override = forms.ChoiceField(label='Select "Yes" to process an override', choices=override_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))



sales_rep_choices = (
    ("----", "----"),
    ("JEG", "JEG"),
)

shipping_method_choices = (
    ("----", "----"),
    ("A'ville", "A'ville"),
)

payment_term_choices = (
    ("----", "----"),
    ("Net 14", "Net 14"),
    ("Net 30", "Net 30"),
)

class Sales_Order_Form(forms.Form):
    to = forms.CharField(label='To', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    ship_to = forms.CharField(label='Ship To', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    phone = forms.CharField(label='Phone', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    po_number = forms.CharField(label='P.O. Number', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    sales_rep = forms.ChoiceField(label='Sales Rep Name', choices=sales_rep_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    customer_contact = forms.CharField(label='Customer Contact', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    shipping_method = forms.ChoiceField(label='Shipping Method', choices=shipping_method_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    payment_terms = forms.ChoiceField(label='Payment Terms', choices=payment_term_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=DateInput(attrs={'class': 'form-control' }), required=False)
    override = forms.ChoiceField(label='Select "Yes" to process an override', choices=override_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    #Sale order items
    so_unique_product1 = forms.ModelChoiceField(label='Product #1', queryset=queryset, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity1 = forms.IntegerField(label='Order Quantity #1', initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product2 = forms.ModelChoiceField(label='Product #2', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity2 = forms.IntegerField(label='Order Quantity #2', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product3 = forms.ModelChoiceField(label='Product #3', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity3 = forms.IntegerField(label='Order Quantity #3', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product4 = forms.ModelChoiceField(label='Product #4', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity4 = forms.IntegerField(label='Order Quantity #4', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product5 = forms.ModelChoiceField(label='Product #5', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity5 = forms.IntegerField(label='Order Quantity #5', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product6 = forms.ModelChoiceField(label='Product #6', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity6 = forms.IntegerField(label='Order Quantity #6', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product7 = forms.ModelChoiceField(label='Product #7', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity7 = forms.IntegerField(label='Order Quantity #7', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product8 = forms.ModelChoiceField(label='Product #8', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity8 = forms.IntegerField(label='Order Quantity #8', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product9 = forms.ModelChoiceField(label='Product #9', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity9 = forms.IntegerField(label='Order Quantity #9', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product10 = forms.ModelChoiceField(label='Product #10', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity10 = forms.IntegerField(label='Order Quantity #10', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product11 = forms.ModelChoiceField(label='Product #11', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity11 = forms.IntegerField(label='Order Quantity #11', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product12 = forms.ModelChoiceField(label='Product #12', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity12 = forms.IntegerField(label='Order Quantity #12', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product13 = forms.ModelChoiceField(label='Product #13', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity13 = forms.IntegerField(label='Order Quantity #13', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product14 = forms.ModelChoiceField(label='Product #14', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity14 = forms.IntegerField(label='Order Quantity #14', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product15 = forms.ModelChoiceField(label='Product #15', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity15 = forms.IntegerField(label='Order Quantity #15', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product16 = forms.ModelChoiceField(label='Product #16', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity16 = forms.IntegerField(label='Order Quantity #16', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product17 = forms.ModelChoiceField(label='Product #17', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity17 = forms.IntegerField(label='Order Quantity #17', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product18 = forms.ModelChoiceField(label='Product #18', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity18 = forms.IntegerField(label='Order Quantity #18', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product19 = forms.ModelChoiceField(label='Product #19', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity19 = forms.IntegerField(label='Order Quantity #19', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    so_unique_product20 = forms.ModelChoiceField(label='Product #20', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity20 = forms.IntegerField(label='Order Quantity #20', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    # Product fulfilled to account for cut
    unique_product1 = forms.ModelChoiceField(label='Fulfillment Product #1', queryset=queryset, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity1 = forms.IntegerField(label='Fulfillment Quantity #1', initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product2 = forms.ModelChoiceField(label='Fulfillment Product #2', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity2 = forms.IntegerField(label='Fulfillment Quantity #2', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product3 = forms.ModelChoiceField(label='Fulfillment Product #3', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity3 = forms.IntegerField(label='Fulfillment Quantity #3', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product4 = forms.ModelChoiceField(label='Fulfillment Product #4', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity4 = forms.IntegerField(label='Fulfillment Quantity #4', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product5 = forms.ModelChoiceField(label='Fulfillment Product #5', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity5 = forms.IntegerField(label='Fulfillment Quantity #5', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product6 = forms.ModelChoiceField(label='Fulfillment Product #6', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity6 = forms.IntegerField(label='Fulfillment Quantity #6', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product7 = forms.ModelChoiceField(label='Fulfillment Product #7', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity7 = forms.IntegerField(label='Fulfillment Quantity #7', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product8 = forms.ModelChoiceField(label='Fulfillment Product #8', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity8 = forms.IntegerField(label='Fulfillment Quantity #8', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product9 = forms.ModelChoiceField(label='Fulfillment Product #9', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity9 = forms.IntegerField(label='Fulfillment Quantity #9', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product10 = forms.ModelChoiceField(label='Fulfillment Product #10', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity10 = forms.IntegerField(label='Fulfillment Quantity #10', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product11 = forms.ModelChoiceField(label='Fulfillment Product #11', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity11 = forms.IntegerField(label='Fulfillment Quantity #11', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product12 = forms.ModelChoiceField(label='Fulfillment Product #12', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity12 = forms.IntegerField(label='Fulfillment Quantity #12', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product13 = forms.ModelChoiceField(label='Fulfillment Product #13', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity13 = forms.IntegerField(label='Fulfillment Quantity #13', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product14 = forms.ModelChoiceField(label='Fulfillment Product #14', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity14 = forms.IntegerField(label='Fulfillment Quantity #14', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product15 = forms.ModelChoiceField(label='Fulfillment Product #15', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity15 = forms.IntegerField(label='Fulfillment Quantity #15', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product16 = forms.ModelChoiceField(label='Fulfillment Product #16', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity16 = forms.IntegerField(label='Fulfillment Quantity #16', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product17 = forms.ModelChoiceField(label='Fulfillment Product #17', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity17 = forms.IntegerField(label='Fulfillment Quantity #17', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product18 = forms.ModelChoiceField(label='Fulfillment Product #18', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity18 = forms.IntegerField(label='Fulfillment Quantity #18', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product19 = forms.ModelChoiceField(label='Fulfillment Product #19', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity19 = forms.IntegerField(label='Fulfillment Quantity #19', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unique_product20 = forms.ModelChoiceField(label='Fulfillment Product #20', queryset=queryset, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity20 = forms.IntegerField(label='Fulfillment Quantity #20', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))


