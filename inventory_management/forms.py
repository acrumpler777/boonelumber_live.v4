from django.forms import ModelForm, Select
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type= 'date'


queryset=product.objects.all()
type_grade_choice = (
        ("----", "----"),
        ('401 WRC | "401" Clear', '401 WRC | "401" Clear'),
        ('AYC | AYC', 'AYC | AYC'),
        ('C&BTR & Fine Grain D-FIR | Clear', 'C&BTR & Fine Grain D-FIR | Clear'),
        ('C&BTR & Fine Grain D-FIR | C&Btr Fir', 'C&BTR & Fine Grain D-FIR | C&Btr Fir'),
        ('C&BTR & Fine Grain D-FIR | C&Btr Fir T&G VJ', 'C&BTR & Fine Grain D-FIR | C&Btr Fir T&G VJ'),
        ('Cypress | None', 'Cypress | None'),
        ('Cypress | None Rough Board', 'Cypress | None Rough Board'),
        ('Cypress | Sel. Knotty', 'Cypress | Sel. Knotty'),
        ('Cypress | Sel. Knotty Mtn. Siding', 'Cypress | Sel. Knotty Mtn. Siding'),
        ('D-FIR | #1 D-Fir STK', 'D-FIR | #1 D-Fir STK'),
        ('D-FIR | #1 FOHC', 'D-FIR | #1 FOHC'),
        ('D-FIR | Select S1S2E', 'D-FIR | Select S1S2E'),
        ('D-FIR | Select Deck', 'D-FIR | Select Deck'),
        ('EWP | B-Heart', 'EWP | B-Heart'),
        ('EWP | FOHC', 'EWP | FOHC'),
        ('EWP | None Rough Board', 'EWP | None Rough Board'),
        ('EWP | Sel. Knotty', 'EWP | Sel. Knotty'),
        ('EWP | Sel. Knotty Mtn. Siding', 'EWP | Sel. Knotty Mtn. Siding'),
        ('EWP | Sel. Knotty Mtn. Siding KD', 'EWP | Sel. Knotty Mtn. Siding KD'),
        ('Oak | None', 'Oak | None'),
        ('Spruce | FOHC Sitka', 'Spruce | FOHC Sitka'),
        ('Spruce | None', 'Spruce | None'),
        ('Spruce | T&G Decking', 'Spruce | T&G Decking'),
        ('WRC | 3-hole Corner', 'WRC | 3-hole Corner'),
        ('WRC | 3-hole End', 'WRC | 3-hole End'),
        ('WRC | 3-hole Post', 'WRC | 3-hole Post'),
        ('WRC | AJ B-Heart', 'WRC | AJ B-Heart'),
        ('WRC | Bevel', 'WRC | Bevel'),
        ('WRC | B-Heart', 'WRC | B-Heart'),
        ('WRC | Channel Rustic', 'WRC | Channel Rustic'),
        ('WRC | FOHC', 'WRC | FOHC'),
        ('WRC | Haida Skirl', 'WRC | Haida Skirl'),
        ('WRC | Knotty', 'WRC | Knotty'),
        ('WRC | Shiplap', 'WRC | Shiplap'),
        ('WRC | Standard 10', 'WRC | Standard 10'),
        ('WRC | STK', 'WRC | STK'),
        ('WRC | T&G', 'WRC | T&G'),

    )

size_choices = (
    ("----", "----"),
    ('.875x4', '.875x4'),
    ('.875x6', '.875x6'),
    ('.875x8', '.875x8'),
    ('.875x10', '.875x10'),
    ('.875x12', '.875x12'),
    ('1.25x6', '1.25x6'),
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
    ('3x18', '3x18'),
    ('3x20', '3x20'),
    ('3.5x6', '3.5x6'),
    ('4x4', '4x4'),
    ('4x6', '4x6'),
    ('4x8', '4x8'),
    ('4x10', '4x10'),
    ('4x12', '4x12'),
    ('4x14', '4x14'),
    ('4x16', '4x16'),
    ('4x18', '4x18'),
    ('4x20', '4x20'),
    ('4x22', '4x22'),
    ('4x24', '4x24'),
    ('5x12', '5x12'),
    ('6x6', '6x6'),
    ('6x8', '6x8'),
    ('6x10', '6x10'),
    ('6x12', '6x12'),
    ('6x14', '6x14'),
    ('6x16', '6x16'),
    ('6x18', '6x18'),
    ('6x20', '6x20'),
    ('6x22', '6x22'),
    ('6x24', '6x24'),
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
    ('8x22', '8x22'),
    ('8x24', '8x24'),
    ('10x10', '10x10'),
    ('10x12', '10x12'),
    ('10x14', '10x14'),
    ('10x15', '10x15'),
    ('10x16', '10x16'),
    ('10x18', '10x18'),
    ('10x20', '10x20'),
    ('10x22', '10x22'),
    ('10x24', '10x24'),
    ('12x12', '12x12'),
    ('12x13', '12x13'),
    ('12x14', '12x14'),
    ('12x15', '12x15'),
    ('12x16', '12x16'),
    ('12x18', '12x18'),
    ('12x20', '12x20'),
    ('12x22', '12x22'),
    ('12x24', '12x24'),
    ('12x32', '12x32'),
    ('14x14', '14x14'),
    ('14x18', '14x18'),
    ('16x16', '16x16'),
    ('16x18', '16x18'),
    ('16x20', '16x20'),
    ('16x24', '16x24'),
    ('18x18', '18x18'),
    ('20x20', '20x20'),
    ('24x24', '24x24'),
)

length_choices = (
    ("----", "----"),
    ('3 ft', '3 ft'),
    ('4 ft', '4 ft'),
    ('5 ft', '5 ft'),
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
    ('36 ft', '36 ft'),
    ('38 ft', '38 ft'),
    ('40 ft', '40 ft'),

)
class POForm(forms.Form):
    company = forms.CharField(label='Company', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    address = forms.CharField(label='Address', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    phone = forms.CharField(label='Phone', required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control' }))
    email = forms.EmailField(label='Email', required=False, widget=forms.TextInput(attrs={'class': 'form-control' }))
    date = forms.DateField(label='Date', widget=DateInput(attrs={'class': 'form-control' }), required=False)

    type_grade1 = forms.ChoiceField(choices=type_grade_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    size1 = forms.ChoiceField(choices=size_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    length1 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity1 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade2 = forms.ChoiceField( choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size2 = forms.ChoiceField(choices=size_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    length2 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity2 = forms.IntegerField(label='Order Quantity #2', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade3 = forms.ChoiceField(label='Type | Grade #3', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size3 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length3 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity3 = forms.IntegerField(label='Order Quantity #3', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade4 = forms.ChoiceField(label='Type | Grade #4', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size4 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length4 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity4 = forms.IntegerField(label='Order Quantity #4', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade5 = forms.ChoiceField(label='Type | Grade #5', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size5 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length5 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity5 = forms.IntegerField(label='Order Quantity #5', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade6 = forms.ChoiceField(label='Type | Grade #6', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size6 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length6 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity6 = forms.IntegerField(label='Order Quantity #6', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade7 = forms.ChoiceField(label='Type | Grade #7', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size7 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length7 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity7 = forms.IntegerField(label='Order Quantity #7', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade8 = forms.ChoiceField(label='Type | Grade #8', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size8 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length8 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity8 = forms.IntegerField(label='Order Quantity #8', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade9 = forms.ChoiceField(label='Type | Grade #9', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size9 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length9 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity9 = forms.IntegerField(label='Order Quantity #9', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade10 = forms.ChoiceField(label='Type | Grade #10', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size10 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length10 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity10 = forms.IntegerField(label='Order Quantity #20', required=False, initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade11 = forms.ChoiceField(label='Type | Grade #11', choices=type_grade_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    size11 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length11 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity11 = forms.IntegerField(label='Order Quantity #11', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade12 = forms.ChoiceField(label='Type | Grade #12', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size12 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length12 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity12 = forms.IntegerField(label='Order Quantity #12', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade13 = forms.ChoiceField(label='Type | Grade #13', choices=type_grade_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    size13 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length13 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity13 = forms.IntegerField(label='Order Quantity #13', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade14 = forms.ChoiceField(label='Type | Grade #14', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size14 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length14 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity14 = forms.IntegerField(label='Order Quantity #14', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade15 = forms.ChoiceField(label='Type | Grade #15', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size15 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length15 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity15 = forms.IntegerField(label='Order Quantity #15', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade16 = forms.ChoiceField(label='Type | Grade #16', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size16 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length16 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity16 = forms.IntegerField(label='Order Quantity #16', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade17 = forms.ChoiceField(label='Type | Grade #17', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size17 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length17 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity17 = forms.IntegerField(label='Order Quantity #17', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade18 = forms.ChoiceField(label='Type | Grade #18', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size18 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length18 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity18 = forms.IntegerField(label='Order Quantity #18', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade19 = forms.ChoiceField(label='Type | Grade #19', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size19 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length19 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity19 = forms.IntegerField(label='Order Quantity #19', required=False, initial=0, min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade20 = forms.ChoiceField(label='Type | Grade #20', choices=type_grade_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    size20 = forms.ChoiceField(choices=size_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    length20 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
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
    type_grade1 = forms.ChoiceField(choices=type_grade_choice, required=False,  widget=forms.Select(attrs={'class': 'form-control'}))
    size1 = forms.ChoiceField(choices=size_choices, required=False,  widget=forms.Select(attrs={'class': 'form-control'}))
    length1 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity1 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade1 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size1 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length1 = forms.ChoiceField(choices=length_choices,widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity1 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade2 = forms.ChoiceField(choices=type_grade_choice, required=False,  widget=forms.Select(attrs={'class': 'form-control'}))
    size2 = forms.ChoiceField(choices=size_choices, required=False,  widget=forms.Select(attrs={'class': 'form-control'}))
    length2 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity2 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade2 = forms.ChoiceField( choices=type_grade_choice, required=False,  widget=forms.Select(attrs={'class': 'form-control'}))
    so_size2 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length2 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity2 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade3 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    size3 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    length3 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity3 = forms.IntegerField(initial=0, min_value=0, required=False,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade3 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_size3 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_length3 = forms.ChoiceField(choices=length_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity3 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade4 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    size4 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    length4 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity4 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade4 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_size4 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_length4 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity4 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade5 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size5 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    length5 = forms.ChoiceField(choices=length_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity5 = forms.IntegerField(initial=0, min_value=0, required=False,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade5 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size5 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_length5 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity5 = forms.IntegerField(initial=0, min_value=0, required=False,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade6 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size6 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    length6 = forms.ChoiceField(choices=length_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity6 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade6 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size6 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length6 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity6 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade7 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    size7 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    length7 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity7 = forms.IntegerField(initial=0, min_value=0, required=False,widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade7 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_size7 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length7 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity7 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade8 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    size8 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length8 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity8 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade8 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_size8 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_length8 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity8 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade9 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    size9 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    length9 = forms.ChoiceField(choices=length_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity9 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade9 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_size9 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length9 = forms.ChoiceField(choices=length_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity9 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade10 = forms.ChoiceField(choices=type_grade_choice, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    size10 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    length10 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity10 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade10 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size10 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_length10 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity10 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade11 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size11 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length11 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity11 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade11 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size11 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length11 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity11 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade12 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size12 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length12 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity12 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade12 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size12 = forms.ChoiceField(choices=size_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_length12 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity12 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade13 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size13 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length13 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity13 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade13 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size13 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length13 = forms.ChoiceField(choices=length_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity13 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade14 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size14 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length14 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity14 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade14 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size14 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length14 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity14 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade15 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size15 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length15 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity15 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade15 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size15 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length15 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity15 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade16 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size16 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length16 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity16 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade16 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size16 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length16 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity16 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade17 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size17 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length17 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity17 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade17 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size17 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length17 = forms.ChoiceField(choices=length_choices, required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity17 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade18 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size18 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length18 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity18 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade18 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size18 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length18 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity18 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade19 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size19 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length19 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity19 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade19 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size19 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length19 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity19 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    type_grade20 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    size20 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    length20 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    order_quantity20 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    so_type_grade20 = forms.ChoiceField(choices=type_grade_choice, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_size20 = forms.ChoiceField(choices=size_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_length20 = forms.ChoiceField(choices=length_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    so_order_quantity20 = forms.IntegerField(initial=0, min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))






