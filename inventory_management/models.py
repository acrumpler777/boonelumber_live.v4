from django.db import models
from django.contrib.auth.models import User
from computedfields.models import ComputedFieldsModel, computed
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# Create your models here.
class product(ComputedFieldsModel):
    unique_product = models.CharField("Unique Product", max_length=200, blank=False, unique=True)  # ex. 401 WRC | "401" Clear | 10x10 | 6 ft
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=False)
    total_quantity = models.IntegerField("Total Quantity", blank=False, default=0)
    pcs_Per_Unit = models.IntegerField(null=True, validators=[MinValueValidator(1)], default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default=1,on_delete=models.SET_DEFAULT)

    @computed(models.CharField(max_length=400),
              depends=[['self', ['unique_product']]])
    def inventory_group(self):
        return self.unique_product.split(' | ')[0]

    @computed(models.CharField(max_length=400),
              depends=[['self', ['unique_product']]])
    def grade(self):
        return self.unique_product.split(' | ')[1]

    @computed(models.CharField(max_length=400),
              depends=[['self', ['unique_product']]])
    def size(self):
        return self.unique_product.split(' | ')[2]

    @computed(models.IntegerField(),
              depends=[['self', ['size']]])
    def size_left(self):
        return self.size.split('x')[0]

    @computed(models.IntegerField(),
              depends=[['self', ['size']]])
    def size_right(self):
        return self.size.split('x')[1]

    @computed(models.CharField(max_length=400),
              depends=[['self', ['unique_product']]])
    def length(self):
        return self.unique_product.split(' | ')[3]

    @computed(models.IntegerField(),
              depends=[['self', ['length']]])
    def length_value(self):
        return self.length.split(' ft')[0]

    @computed(models.DecimalField(null=True, max_digits=12, decimal_places=2,
                                  validators=[MinValueValidator(0), MaxValueValidator(100000)]),
              depends=[['self', ['length', 'size', 'total_quantity']]])
    def bF_Total(self):
        return (self.total_quantity) * (int(self.size.split('x')[0]) * int(self.size.split('x')[1])) * \
               (int(self.length.split(' ft')[0]) / 12)

    @computed(models.DecimalField(null=True, max_digits=12, decimal_places=2,
                                  validators=[MinValueValidator(0), MaxValueValidator(100000)]),
              depends=[['self', ['price', 'bF_Total']]])
    def Total_USD(self):
        return (float(self.price) * self.bF_Total) / 1000

    class Meta:
        ordering = ['inventory_group', 'grade', 'size_left', 'size_right', 'length_value']

    def __str__(self):
        return self.unique_product


class purchase_order_model(models.Model):
    company = models.CharField('Company', blank=True, null=True, max_length=200)
    address = models.CharField('Address', blank=True, null=True, max_length=200)
    phone = models.CharField('Phone', blank=True, null=True, max_length=200)
    email = models.EmailField('Email', blank=True, null=True)
    date = models.CharField('Date', blank=True, null=True, max_length=200)

    unique_product1 = models.CharField("Unique Product #1", max_length=200, blank=True, null=True)
    order_quantity1 = models.IntegerField("Order Quantity #1", blank=True, null=True)
    unique_product2 = models.CharField("Unique Product #2", max_length=200, blank=True, null=True)
    order_quantity2 = models.IntegerField("Order Quantity #2", blank=True, null=True)
    unique_product3 = models.CharField("Unique Product #3", max_length=200, blank=True, null=True)
    order_quantity3 = models.IntegerField("Order Quantity #3", blank=True, null=True)
    unique_product4 = models.CharField("Unique Product #4", max_length=200, blank=True, null=True)
    order_quantity4 = models.IntegerField("Order Quantity #4", blank=True, null=True)
    unique_product5 = models.CharField("Unique Product #5", max_length=200, blank=True, null=True)
    order_quantity5 = models.IntegerField("Order Quantity #5", blank=True, null=True)
    unique_product6 = models.CharField("Unique Product #6", max_length=200, blank=True, null=True)
    order_quantity6 = models.IntegerField("Order Quantity #6", blank=True, null=True)
    unique_product7 = models.CharField("Unique Product #7", max_length=200, blank=True, null=True)
    order_quantity7 = models.IntegerField("Order Quantity #7", blank=True, null=True)
    unique_product8 = models.CharField("Unique Product #8", max_length=200, blank=True, null=True)
    order_quantity8 = models.IntegerField("Order Quantity #8", blank=True, null=True)
    unique_product9 = models.CharField("Unique Product #9", max_length=200, blank=True, null=True)
    order_quantity9 = models.IntegerField("Order Quantity #9", blank=True, null=True)
    unique_product10 = models.CharField("Unique Product #10", max_length=200, blank=True, null=True)
    order_quantity10 = models.IntegerField("Order Quantity #10", blank=True, null=True)
    unique_product11 = models.CharField("Unique Product #11", max_length=200, blank=True, null=True)
    order_quantity11 = models.IntegerField("Order Quantity #11", blank=True, null=True)
    unique_product12 = models.CharField("Unique Product #12", max_length=200, blank=True, null=True)
    order_quantity12 = models.IntegerField("Order Quantity #12", blank=True, null=True)
    unique_product13 = models.CharField("Unique Product #13", max_length=200, blank=True, null=True)
    order_quantity13 = models.IntegerField("Order Quantity #13", blank=True, null=True)
    unique_product14 = models.CharField("Unique Product #14", max_length=200, blank=True, null=True)
    order_quantity14 = models.IntegerField("Order Quantity #14", blank=True, null=True)
    unique_product15 = models.CharField("Unique Product #15", max_length=200, blank=True, null=True)
    order_quantity15 = models.IntegerField("Order Quantity #15", blank=True, null=True)
    unique_product16 = models.CharField("Unique Product #16", max_length=200, blank=True, null=True)
    order_quantity16 = models.IntegerField("Order Quantity #16", blank=True, null=True)
    unique_product17 = models.CharField("Unique Product #17", max_length=200, blank=True, null=True)
    order_quantity17 = models.IntegerField("Order Quantity #17", blank=True, null=True)
    unique_product18 = models.CharField("Unique Product #18", max_length=200, blank=True, null=True)
    order_quantity18 = models.IntegerField("Order Quantity #18", blank=True, null=True)
    unique_product19 = models.CharField("Unique Product #19", max_length=200, blank=True, null=True)
    order_quantity19 = models.IntegerField("Order Quantity #19", blank=True, null=True)
    unique_product20 = models.CharField("Unique Product #20", max_length=200, blank=True, null=True)
    order_quantity20 = models.IntegerField("Order Quantity #20", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return 'Purchase Order #{0}'.format(self.id)

class adjustment_model(models.Model):

    unique_product1 = models.CharField("Unique Product", max_length=200)
    order_quantity1 = models.IntegerField('Adjustment Quantity')
    adjustment_reason = models.CharField('Reason For Adjustment', blank=True, null=True, max_length=2000)
    override = models.CharField("Override", blank=True, null=True, max_length=200)

    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return 'Adjustment #{0}'.format(self.id)


class sales_order_model(models.Model):
    to = models.CharField('To', blank=True, null=True, max_length=200)
    ship_to = models.CharField('Ship To', blank=True, null=True, max_length=200)
    phone = models.CharField('Phone', blank=True, null=True, max_length=200)
    po_number = models.CharField('P.O. Number', blank=True, null=True, max_length=200)
    sales_rep = models.CharField("Sales Rep Name", blank=True, null=True, max_length=200)
    customer_contact = models.CharField('Customer Contact', blank=True, null=True, max_length=200)
    shipping_method = models.CharField("Shipping Method", blank=True, null=True, max_length=200)
    payment_terms = models.CharField("Payment Terms", blank=True, null=True, max_length=200)
    date = models.CharField('Date', blank=True, null=True, max_length=200)
    override = models.CharField("Override", blank=True, null=True, max_length=200)

    so_unique_product1 = models.CharField("Unique Product #1", max_length=200, blank=True, null=True)
    so_order_quantity1 = models.IntegerField("Order Quantity #1", blank=True, null=True)
    so_unique_product2 = models.CharField("Unique Product #2", max_length=200, blank=True, null=True)
    so_order_quantity2 = models.IntegerField("Order Quantity #2", blank=True, null=True)
    so_unique_product3 = models.CharField("Unique Product #3", max_length=200, blank=True, null=True)
    so_order_quantity3 = models.IntegerField("Order Quantity #3", blank=True, null=True)
    so_unique_product4 = models.CharField("Unique Product #4", max_length=200, blank=True, null=True)
    so_order_quantity4 = models.IntegerField("Order Quantity #4", blank=True, null=True)
    so_unique_product5 = models.CharField("Unique Product #5", max_length=200, blank=True, null=True)
    so_order_quantity5 = models.IntegerField("Order Quantity #5", blank=True, null=True)
    so_unique_product6 = models.CharField("Unique Product #6", max_length=200, blank=True, null=True)
    so_order_quantity6 = models.IntegerField("Order Quantity #6", blank=True, null=True)
    so_unique_product7 = models.CharField("Unique Product #7", max_length=200, blank=True, null=True)
    so_order_quantity7 = models.IntegerField("Order Quantity #7", blank=True, null=True)
    so_unique_product8 = models.CharField("Unique Product #8", max_length=200, blank=True, null=True)
    so_order_quantity8 = models.IntegerField("Order Quantity #8", blank=True, null=True)
    so_unique_product9 = models.CharField("Unique Product #9", max_length=200, blank=True, null=True)
    so_order_quantity9 = models.IntegerField("Order Quantity #9", blank=True, null=True)
    so_unique_product10 = models.CharField("Unique Product #10", max_length=200, blank=True, null=True)
    so_order_quantity10 = models.IntegerField("Order Quantity #10", blank=True, null=True)
    so_unique_product11 = models.CharField("Unique Product #11", max_length=200, blank=True, null=True)
    so_order_quantity11 = models.IntegerField("Order Quantity #11", blank=True, null=True)
    so_unique_product12 = models.CharField("Unique Product #12", max_length=200, blank=True, null=True)
    so_order_quantity12 = models.IntegerField("Order Quantity #12", blank=True, null=True)
    so_unique_product13 = models.CharField("Unique Product #13", max_length=200, blank=True, null=True)
    so_order_quantity13 = models.IntegerField("Order Quantity #13", blank=True, null=True)
    so_unique_product14 = models.CharField("Unique Product #14", max_length=200, blank=True, null=True)
    so_order_quantity14 = models.IntegerField("Order Quantity #14", blank=True, null=True)
    so_unique_product15 = models.CharField("Unique Product #15", max_length=200, blank=True, null=True)
    so_order_quantity15 = models.IntegerField("Order Quantity #15", blank=True, null=True)
    so_unique_product16 = models.CharField("Unique Product #16", max_length=200, blank=True, null=True)
    so_order_quantity16 = models.IntegerField("Order Quantity #16", blank=True, null=True)
    so_unique_product17 = models.CharField("Unique Product #17", max_length=200, blank=True, null=True)
    so_order_quantity17 = models.IntegerField("Order Quantity #17", blank=True, null=True)
    so_unique_product18 = models.CharField("Unique Product #18", max_length=200, blank=True, null=True)
    so_order_quantity18 = models.IntegerField("Order Quantity #18", blank=True, null=True)
    so_unique_product19 = models.CharField("Unique Product #19", max_length=200, blank=True, null=True)
    so_order_quantity19 = models.IntegerField("Order Quantity #19", blank=True, null=True)
    so_unique_product20 = models.CharField("Unique Product #20", max_length=200, blank=True, null=True)
    so_order_quantity20 = models.IntegerField("Order Quantity #20", blank=True, null=True)


    # Product fulfilled to account for cut
    unique_product1 = models.CharField("Fulfillment Product #1", max_length=200, blank=True, null=True)
    order_quantity1 = models.IntegerField("Fulfillment Quantity #1", blank=True, null=True)
    unique_product2 = models.CharField("Fulfillment Product #2", max_length=200, blank=True, null=True)
    order_quantity2 = models.IntegerField("Fulfillment Quantity #2", blank=True, null=True)
    unique_product3 = models.CharField("Fulfillment Product #3", max_length=200, blank=True, null=True)
    order_quantity3 = models.IntegerField("Fulfillment Quantity #3", blank=True, null=True)
    unique_product4 = models.CharField("Fulfillment Product #4", max_length=200, blank=True, null=True)
    order_quantity4 = models.IntegerField("Fulfillment Quantity #4", blank=True, null=True)
    unique_product5 = models.CharField("Fulfillment Product #5", max_length=200, blank=True, null=True)
    order_quantity5 = models.IntegerField("Fulfillment Quantity #5", blank=True, null=True)
    unique_product6 = models.CharField("Fulfillment Product #6", max_length=200, blank=True, null=True)
    order_quantity6 = models.IntegerField("Fulfillment Quantity #6", blank=True, null=True)
    unique_product7 = models.CharField("Fulfillment Product #7", max_length=200, blank=True, null=True)
    order_quantity7 = models.IntegerField("Fulfillment Quantity #7", blank=True, null=True)
    unique_product8 = models.CharField("Fulfillment Product #8", max_length=200, blank=True, null=True)
    order_quantity8 = models.IntegerField("Fulfillment Quantity #8", blank=True, null=True)
    unique_product9 = models.CharField("Fulfillment Product #9", max_length=200, blank=True, null=True)
    order_quantity9 = models.IntegerField("Fulfillment Quantity #9", blank=True, null=True)
    unique_product10 = models.CharField("Fulfillment Product #10", max_length=200, blank=True, null=True)
    order_quantity10 = models.IntegerField("Fulfillment Quantity #10", blank=True, null=True)
    unique_product11 = models.CharField("Fulfillment Product #11", max_length=200, blank=True, null=True)
    order_quantity11 = models.IntegerField("Fulfillment Quantity #11", blank=True, null=True)
    unique_product12 = models.CharField("Fulfillment Product #12", max_length=200, blank=True, null=True)
    order_quantity12 = models.IntegerField("Fulfillment Quantity #12", blank=True, null=True)
    unique_product13 = models.CharField("Fulfillment Product #13", max_length=200, blank=True, null=True)
    order_quantity13 = models.IntegerField("Fulfillment Quantity #13", blank=True, null=True)
    unique_product14 = models.CharField("Fulfillment Product #14", max_length=200, blank=True, null=True)
    order_quantity14 = models.IntegerField("Fulfillment Quantity #14", blank=True, null=True)
    unique_product15 = models.CharField("Fulfillment Product #15", max_length=200, blank=True, null=True)
    order_quantity15 = models.IntegerField("Fulfillment Quantity #15", blank=True, null=True)
    unique_product16 = models.CharField("Fulfillment Product #16", max_length=200, blank=True, null=True)
    order_quantity16 = models.IntegerField("Fulfillment Quantity #16", blank=True, null=True)
    unique_product17 = models.CharField("Fulfillment Product #17", max_length=200, blank=True, null=True)
    order_quantity17 = models.IntegerField("Fulfillment Quantity #17", blank=True, null=True)
    unique_product18 = models.CharField("Fulfillment Product #18", max_length=200, blank=True, null=True)
    order_quantity18 = models.IntegerField("Fulfillment Quantity #18", blank=True, null=True)
    unique_product19 = models.CharField("Fulfillment Product #19", max_length=200, blank=True, null=True)
    order_quantity19 = models.IntegerField("Fulfillment Quantity #19", blank=True, null=True)
    unique_product20 = models.CharField("Fulfillment Product #20", max_length=200, blank=True, null=True)
    order_quantity20 = models.IntegerField("Fulfillment Quantity #20", blank=True, null=True)


    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return 'Sales Order #{0}'.format(self.id)


