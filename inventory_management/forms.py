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

    type_grade_choice = (
        ("----", "----"),
        ('401 WRC | "401" Clear', '401 WRC | "401" Clear'),
        ('AYC | AYC', 'AYC | AYC'),
        ('C&BTR & Fine Grain D-FIR | C&Btr Fir', 'C&BTR & Fine Grain D-FIR | C&Btr Fir'),
        ('C&BTR & Fine Grain D-FIR | C&Btr Fir T&G VJ', 'C&BTR & Fine Grain D-FIR | C&Btr Fir T&G VJ'),
        ('C&BTR & Fine Grain D-FIR | Clear', 'C&BTR & Fine Grain D-FIR | Clear'),
        ('Cypress | None', 'Cypress | None'),
        ('Cypress | None Rough Board', 'Cypress | None Rough Board'),
        ('Cypress | Sel. Knotty', 'Cypress | Sel. Knotty'),
        ('Cypress | Sel. Knotty Mtn. Siding', 'Cypress | Sel. Knotty Mtn. Siding'),


    )

    size_choices = (
        ("----", "----"),
        ('1.25x12', '1.25x12'),
        ('1.25x16', '1.25x16'),
        ('1.5x12', '1.5x12'),
        ('1x4', '1x4'),
        ('1x6', '1x6'),
        ('1x8', '1x8'),
        ('1x10', '1x10'),
        ('1x12', '1x12'),
        ('2x4', '2x4'),
        ('2x6', '2x6'),
        ('2x8', '2x8'),
        ('2x10', '2x10'),
        ('2x12', '2x12'),
        ('2x14', '2x14'),
        ('2x16', '2x16'),
        ('3x6', '3x6'),
        ('3x8', '3x8'),
        ('3x10', '3x10'),
        ('3x12', '3x12'),
        ('3x14', '3x14'),
        ('3x16', '3x16'),
        ('4x4', '4x4'),
        ('4x6', '4x6'),
        ('4x8', '4x8'),
        ('4x10', '4x10'),
        ('4x12', '4x12'),
        ('4x14', '4x14'),
        ('4x16', '4x16'),
        ('4x18', '4x18'),
        ('4x20', '4x20'),
        ('4x24', '4x24'),
        ('6x6', '6x6'),
        ('6x8', '6x8'),
        ('6x10', '6x10'),
        ('6x12', '6x12'),
        ('6x14', '6x14'),
        ('6x16', '6x16'),
        ('6x18', '6x18'),
        ('6x20', '6x20'),
        ('6x22', '6x22'),
        ('8x8', '8x8'),
        ('8x9', '8x9'),
        ('8x10', '8x10'),
        ('8x11', '8x11'),
        ('8x12', '8x12'),
        ('8x13', '8x13'),
        ('8x14', '8x14'),
        ('8x15', '8x15'),
        ('8x16', '8x16'),
        ('8x18', '8x18'),
        ('8x20', '8x20'),
        ('8x21', '8x21'),
        ('10x10', '10x10'),
        ('10x12', '10x12'),
        ('10x14', '10x14'),
        ('10x15', '10x15'),
        ('10x16', '10x16'),
        ('10x18', '10x18'),
        ('10x20', '10x20'),
        ('12x12', '12x12'),
        ('12x13', '12x13'),
        ('12x14', '12x14'),
        ('12x15', '12x15'),
        ('12x16', '12x16'),
        ('12x18', '12x18'),
        ('12x20', '12x20'),
        ('12x24', '12x24'),
        ('14x14', '14x14'),
        ('16x16', '16x16'),
        ('18x18', '18x18'),
        ('20x20', '20x20'),
        ('24x24', '24x24'),
    )

    length_choices = (
        ("----", "----"),
        ('6 ft', '6 ft'),
        ('7 ft', '7 ft'),
        ('7.5 ft', '7.5 ft'),
        ('8 ft', '8 ft'),
        ('9 ft', '9 ft'),
        ('10 ft', '10 ft'),
        ('11 ft', '11 ft'),
        ('12 ft', '12 ft'),
        ('13 ft', '13 ft'),
        ('14 ft', '14 ft'),
        ('15 ft', '15 ft'),
        ('16 ft', '16 ft'),
        ('17 ft', '17 ft'),
        ('18 ft', '18 ft'),
        ('19 ft', '19 ft'),
        ('20 ft', '20 ft'),
        ('21 ft', '21 ft'),
        ('22 ft', '22 ft'),
        ('23 ft', '23 ft'),
        ('24 ft', '24 ft'),
        ('26 ft', '26 ft'),
        ('28 ft', '28 ft'),
        ('30 ft', '30 ft'),
        ('32 ft', '32 ft'),
        ('34 ft', '34 ft'),
        ('36 ft', '38 ft'),
        ('40 ft', '40 ft'),


    )



    type_grade1 = forms.ChoiceField(label='Type | Grade #1', choices=type_grade_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    size1 = forms.ChoiceField(label='Size', choices=size_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    length1 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity1 = forms.IntegerField(label='Order Quantity #1', initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade2 = forms.ChoiceField(label='Type | Grade #1', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size2 = forms.ChoiceField(label='Size', choices=size_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    length2 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity2 = forms.IntegerField(label='Order Quantity #2', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade3 = forms.ChoiceField(label='Type | Grade #3', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size3 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length3 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity3 = forms.IntegerField(label='Order Quantity #3', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade4 = forms.ChoiceField(label='Type | Grade #4', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size4 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length4 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity4 = forms.IntegerField(label='Order Quantity #4', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade5 = forms.ChoiceField(label='Type | Grade #5', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size5 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length5 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity5 = forms.IntegerField(label='Order Quantity #5', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade6 = forms.ChoiceField(label='Type | Grade #6', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size6 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length6 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity6 = forms.IntegerField(label='Order Quantity #6', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade7 = forms.ChoiceField(label='Type | Grade #7', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size7 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length7 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity7 = forms.IntegerField(label='Order Quantity #7', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade8 = forms.ChoiceField(label='Type | Grade #8', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size8 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length8 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity8 = forms.IntegerField(label='Order Quantity #8', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade9 = forms.ChoiceField(label='Type | Grade #9', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size9 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length9 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity9 = forms.IntegerField(label='Order Quantity #9', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade10 = forms.ChoiceField(label='Type | Grade #10', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size10 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length10 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity10 = forms.IntegerField(label='Order Quantity #20', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade11 = forms.ChoiceField(label='Type | Grade #11', choices=type_grade_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    size11 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length11 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity11 = forms.IntegerField(label='Order Quantity #11', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade12 = forms.ChoiceField(label='Type | Grade #12', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size12 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length12 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity12 = forms.IntegerField(label='Order Quantity #12', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade13 = forms.ChoiceField(label='Type | Grade #13', choices=type_grade_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    size13 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length13 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity13 = forms.IntegerField(label='Order Quantity #13', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade14 = forms.ChoiceField(label='Type | Grade #14', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size14 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length14 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity14 = forms.IntegerField(label='Order Quantity #14', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade15 = forms.ChoiceField(label='Type | Grade #15', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size15 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length15 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity15 = forms.IntegerField(label='Order Quantity #15', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade16 = forms.ChoiceField(label='Type | Grade #16', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size16 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length16 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity16 = forms.IntegerField(label='Order Quantity #16', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade17 = forms.ChoiceField(label='Type | Grade #17', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size17 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length17 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity17 = forms.IntegerField(label='Order Quantity #17', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade18 = forms.ChoiceField(label='Type | Grade #18', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size18 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length18 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity18 = forms.IntegerField(label='Order Quantity #18', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade19 = forms.ChoiceField(label='Type | Grade #19', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size19 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length19 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity19 = forms.IntegerField(label='Order Quantity #19', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade20 = forms.ChoiceField(label='Type | Grade #20', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size20 = forms.ChoiceField(label='Size', choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length20 = forms.ChoiceField(label='Length', choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity20 = forms.IntegerField(label='Order Quantity #20', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))


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


