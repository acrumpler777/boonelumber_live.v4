from django.db.models import F, Count, Sum
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import csv
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def inventory_main(request):
    context = {}
    return render(request, 'inventory_management/inventory_main.html', context)


@login_required(login_url='login')
def update_inventory(request):
    context = {}
    return render(request, 'inventory_management/inventory_management.html', context)


@login_required(login_url='login')
def purchase_order_func(request):
    if request.method == 'POST':
        form = POForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']


            unique_product1 = form.cleaned_data['unique_product1']
            order_quantity1 = form.cleaned_data['order_quantity1']
            product1_db = product.objects.get(unique_product=unique_product1)
            product1_db.total_quantity = F('total_quantity') + order_quantity1
            product1_db.save()

            if (form.cleaned_data['unique_product2'] == None and form.cleaned_data['order_quantity2'] > 0) \
                    or (form.cleaned_data['unique_product3'] == None and form.cleaned_data['order_quantity3']) > 0\
                    or (form.cleaned_data['unique_product4'] == None and form.cleaned_data['order_quantity4']) > 0\
                    or (form.cleaned_data['unique_product5'] == None and form.cleaned_data['order_quantity5']) > 0\
                    or (form.cleaned_data['unique_product6'] == None and form.cleaned_data['order_quantity6']) > 0\
                    or (form.cleaned_data['unique_product7'] == None and form.cleaned_data['order_quantity7']) > 0\
                    or (form.cleaned_data['unique_product8'] == None and form.cleaned_data['order_quantity8']) > 0\
                    or (form.cleaned_data['unique_product9'] == None and form.cleaned_data['order_quantity9']) > 0\
                    or (form.cleaned_data['unique_product10'] == None and form.cleaned_data['order_quantity10']) > 0\
                    or (form.cleaned_data['unique_product11'] == None and form.cleaned_data['order_quantity11']) > 0\
                    or (form.cleaned_data['unique_product12'] == None and form.cleaned_data['order_quantity12']) > 0\
                    or (form.cleaned_data['unique_product13'] == None and form.cleaned_data['order_quantity13']) > 0\
                    or (form.cleaned_data['unique_product14'] == None and form.cleaned_data['order_quantity14']) > 0\
                    or (form.cleaned_data['unique_product15'] == None and form.cleaned_data['order_quantity15']) > 0\
                    or (form.cleaned_data['unique_product16'] == None and form.cleaned_data['order_quantity16']) > 0\
                    or (form.cleaned_data['unique_product17'] == None and form.cleaned_data['order_quantity17']) > 0\
                    or (form.cleaned_data['unique_product18'] == None and form.cleaned_data['order_quantity18']) > 0\
                    or (form.cleaned_data['unique_product19'] == None and form.cleaned_data['order_quantity19']) > 0\
                    or (form.cleaned_data['unique_product20'] == None and form.cleaned_data['order_quantity20']) > 0:

                messages.info(request,
                              'All orders with quantity greater than 0 must be associated with a product.',
                              extra_tags='warning')
                context = {
                    'form': form,
                }
                return render(request, 'inventory_management/purchase_order.html', context)
            else:

                if form.cleaned_data['unique_product2'] == None:
                    unique_product2= None
                    order_quantity2= None
                else:
                    unique_product2 = form.cleaned_data['unique_product2']
                    order_quantity2 = form.cleaned_data['order_quantity2']
                    product2_db = product.objects.get(unique_product=unique_product2)
                    product2_db.total_quantity = F('total_quantity') + order_quantity2
                    product2_db.save()

            if form.cleaned_data['unique_product3'] == None:
                unique_product3= None
                order_quantity3= None
            else:
                unique_product3 = form.cleaned_data['unique_product3']
                order_quantity3 = form.cleaned_data['order_quantity3']
                product3_db = product.objects.get(unique_product=unique_product3)
                product3_db.total_quantity = F('total_quantity') + order_quantity3
                product3_db.save()

            if form.cleaned_data['unique_product4'] == None:
                unique_product4= None
                order_quantity4= None
            else:
                unique_product4 = form.cleaned_data['unique_product4']
                order_quantity4 = form.cleaned_data['order_quantity4']
                product4_db = product.objects.get(unique_product=unique_product4)
                product4_db.total_quantity = F('total_quantity') + order_quantity4
                product4_db.save()

            if form.cleaned_data['unique_product5'] == None:
                unique_product5= None
                order_quantity5= None
            else:
                unique_product5 = form.cleaned_data['unique_product5']
                order_quantity5 = form.cleaned_data['order_quantity5']
                product5_db = product.objects.get(unique_product=unique_product5)
                product5_db.total_quantity = F('total_quantity') + order_quantity5
                product5_db.save()

            if form.cleaned_data['unique_product6'] == None:
                unique_product6= None
                order_quantity6= None
            else:
                unique_product6 = form.cleaned_data['unique_product6']
                order_quantity6 = form.cleaned_data['order_quantity6']
                product6_db = product.objects.get(unique_product=unique_product6)
                product6_db.total_quantity = F('total_quantity') + order_quantity6
                product6_db.save()

            if form.cleaned_data['unique_product7'] == None:
                unique_product7= None
                order_quantity7= None
            else:
                unique_product7 = form.cleaned_data['unique_product7']
                order_quantity7 = form.cleaned_data['order_quantity7']
                product7_db = product.objects.get(unique_product=unique_product7)
                product7_db.total_quantity = F('total_quantity') + order_quantity7
                product7_db.save()

            if form.cleaned_data['unique_product8'] == None:
                unique_product8= None
                order_quantity8= None
            else:
                unique_product8 = form.cleaned_data['unique_product8']
                order_quantity8 = form.cleaned_data['order_quantity8']
                product8_db = product.objects.get(unique_product=unique_product8)
                product8_db.total_quantity = F('total_quantity') + order_quantity8
                product8_db.save()

            if form.cleaned_data['unique_product9'] == None:
                unique_product9= None
                order_quantity9= None
            else:
                unique_product9 = form.cleaned_data['unique_product9']
                order_quantity9 = form.cleaned_data['order_quantity9']
                product9_db = product.objects.get(unique_product=unique_product9)
                product9_db.total_quantity = F('total_quantity') + order_quantity9
                product9_db.save()

            if form.cleaned_data['unique_product10'] == None:
                unique_product10= None
                order_quantity10= None
            else:
                unique_product10 = form.cleaned_data['unique_product10']
                order_quantity10 = form.cleaned_data['order_quantity10']
                product10_db = product.objects.get(unique_product=unique_product10)
                product10_db.total_quantity = F('total_quantity') + order_quantity10
                product10_db.save()

            if form.cleaned_data['unique_product11'] == None:
                unique_product11= None
                order_quantity11= None
            else:
                unique_product11 = form.cleaned_data['unique_product11']
                order_quantity11 = form.cleaned_data['order_quantity11']
                product11_db = product.objects.get(unique_product=unique_product11)
                product11_db.total_quantity = F('total_quantity') + order_quantity11
                product11_db.save()

            if form.cleaned_data['unique_product12'] == None:
                unique_product12= None
                order_quantity12= None
            else:
                unique_product12 = form.cleaned_data['unique_product12']
                order_quantity12 = form.cleaned_data['order_quantity12']
                product12_db = product.objects.get(unique_product=unique_product12)
                product12_db.total_quantity = F('total_quantity') + order_quantity12
                product12_db.save()

            if form.cleaned_data['unique_product13'] == None:
                unique_product13= None
                order_quantity13= None
            else:
                unique_product13 = form.cleaned_data['unique_product13']
                order_quantity13 = form.cleaned_data['order_quantity13']
                product13_db = product.objects.get(unique_product=unique_product13)
                product13_db.total_quantity = F('total_quantity') + order_quantity13
                product13_db.save()

            if form.cleaned_data['unique_product14'] == None:
                unique_product14= None
                order_quantity14= None
            else:
                unique_product14 = form.cleaned_data['unique_product14']
                order_quantity14 = form.cleaned_data['order_quantity14']
                product14_db = product.objects.get(unique_product=unique_product14)
                product14_db.total_quantity = F('total_quantity') + order_quantity14
                product14_db.save()

            if form.cleaned_data['unique_product15'] == None:
                unique_product15= None
                order_quantity15= None
            else:
                unique_product15 = form.cleaned_data['unique_product15']
                order_quantity15 = form.cleaned_data['order_quantity15']
                product15_db = product.objects.get(unique_product=unique_product15)
                product15_db.total_quantity = F('total_quantity') + order_quantity15
                product15_db.save()

            if form.cleaned_data['unique_product16'] == None:
                unique_product16= None
                order_quantity16= None
            else:
                unique_product16 = form.cleaned_data['unique_product16']
                order_quantity16 = form.cleaned_data['order_quantity16']
                product16_db = product.objects.get(unique_product=unique_product16)
                product16_db.total_quantity = F('total_quantity') + order_quantity16
                product16_db.save()

            if form.cleaned_data['unique_product17'] == None:
                unique_product17= None
                order_quantity17= None
            else:
                unique_product17 = form.cleaned_data['unique_product17']
                order_quantity17 = form.cleaned_data['order_quantity17']
                product17_db = product.objects.get(unique_product=unique_product17)
                product17_db.total_quantity = F('total_quantity') + order_quantity17
                product17_db.save()

            if form.cleaned_data['unique_product18'] == None:
                unique_product18= None
                order_quantity18= None
            else:
                unique_product18 = form.cleaned_data['unique_product18']
                order_quantity18 = form.cleaned_data['order_quantity18']
                product18_db = product.objects.get(unique_product=unique_product18)
                product18_db.total_quantity = F('total_quantity') + order_quantity18
                product18_db.save()

            if form.cleaned_data['unique_product19'] == None:
                unique_product19= None
                order_quantity19= None
            else:
                unique_product19 = form.cleaned_data['unique_product19']
                order_quantity19 = form.cleaned_data['order_quantity19']
                product19_db = product.objects.get(unique_product=unique_product19)
                product19_db.total_quantity = F('total_quantity') + order_quantity19
                product19_db.save()

            if form.cleaned_data['unique_product20'] == None:
                unique_product20= None
                order_quantity20= None
            else:
                unique_product20 = form.cleaned_data['unique_product20']
                order_quantity20 = form.cleaned_data['order_quantity20']
                product20_db = product.objects.get(unique_product=unique_product20)
                product20_db.total_quantity = F('total_quantity') + order_quantity20
                product20_db.save()


            db_insert = purchase_order_model(company=company, address=address, phone=phone, email=email, date=date,
                                       unique_product1=unique_product1, order_quantity1=order_quantity1,
                                       unique_product2=unique_product2, order_quantity2=order_quantity2,
                                       unique_product3=unique_product3, order_quantity3=order_quantity3,
                                       unique_product4=unique_product4, order_quantity4=order_quantity4,
                                       unique_product5=unique_product5, order_quantity5=order_quantity5,
                                       unique_product6=unique_product6, order_quantity6=order_quantity6,
                                       unique_product7=unique_product7, order_quantity7=order_quantity7,
                                       unique_product8=unique_product8, order_quantity8=order_quantity8,
                                       unique_product9=unique_product9, order_quantity9=order_quantity9,
                                       unique_product10=unique_product10, order_quantity10=order_quantity10,
                                       unique_product11=unique_product11, order_quantity11=order_quantity11,
                                       unique_product12=unique_product12, order_quantity12=order_quantity12,
                                       unique_product13=unique_product13, order_quantity13=order_quantity13,
                                       unique_product14=unique_product14, order_quantity14=order_quantity14,
                                       unique_product15=unique_product15, order_quantity15=order_quantity15,
                                       unique_product16=unique_product16, order_quantity16=order_quantity16,
                                       unique_product17=unique_product17, order_quantity17=order_quantity17,
                                       unique_product18=unique_product18, order_quantity18=order_quantity18,
                                       unique_product19=unique_product19, order_quantity19=order_quantity19,
                                       unique_product20=unique_product20, order_quantity20=order_quantity20, created_by = request.user.username,)
            db_insert.save()

        return redirect('inventory_management')


    form = POForm()
    context = {
                'form':form
               }
    return render(request, 'inventory_management/purchase_order.html', context)


@login_required(login_url='login')
def inventory_adjustment(request):
    if request.method == 'POST':
        form = inventory_adjustment_form(request.POST)
        if form.is_valid():

            unique_product1 = form.cleaned_data['unique_product1']
            order_quantity1 = form.cleaned_data['order_quantity1']

            adjustment_reason = form.cleaned_data['adjustment_reason']

            total_quantity = product.objects.get(unique_product=unique_product1)
            total_quantity = total_quantity.total_quantity
            total_quantity = total_quantity + order_quantity1

            override = form.cleaned_data['override']

            if total_quantity >= 0 or override == "Yes":

                product1_db = product.objects.get(unique_product=unique_product1)
                product1_db.total_quantity = F('total_quantity') + order_quantity1
                product1_db.save()

                db_insert = adjustment_model(unique_product1=unique_product1, order_quantity1=order_quantity1,
                                             adjustment_reason=adjustment_reason, override=override, created_by = request.user.username,)
                db_insert.save()
                return redirect('inventory_management')
            else:
                messages.info(request, 'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product1, total_quantity))
                context = {
                    'form': form,
                }
                return render(request, 'inventory_management/inventory_adjustment.html', context)

    form = inventory_adjustment_form()
    context = {
        'form':form,
    }
    return render(request, 'inventory_management/inventory_adjustment.html', context)

@login_required(login_url='login')
def update_inventory_item(request, pk):
    update_item = product.objects.get(id=pk)


    if request.method == 'POST':
        form = inventory_adjustment_form(request.POST,initial={'unique_product1':update_item})  #alter this form
        if form.is_valid():

            unique_product1 = form.cleaned_data['unique_product1']
            order_quantity1 = form.cleaned_data['order_quantity1']

            adjustment_reason = form.cleaned_data['adjustment_reason']

            total_quantity = product.objects.get(unique_product=unique_product1)
            total_quantity = total_quantity.total_quantity
            total_quantity = total_quantity + order_quantity1

            override = form.cleaned_data['override']

            if total_quantity >= 0 or override == "Yes":

                product1_db = product.objects.get(unique_product=unique_product1)
                product1_db.total_quantity = F('total_quantity') + order_quantity1
                product1_db.save()

                db_insert = adjustment_model(unique_product1=unique_product1, order_quantity1=order_quantity1,
                                             adjustment_reason=adjustment_reason, override=override, created_by = request.user.username,)
                db_insert.save()
                return redirect('view_inventory_All')
            else:
                messages.info(request, 'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product1, total_quantity))
                context = {
                    'form': form,
                }
                return render(request, 'inventory_management/update_inventory.html', context)

    form = inventory_adjustment_form(initial={'unique_product1':update_item})


    context = {
        'form':form,

    }
    return render(request, 'inventory_management/update_inventory.html', context)


@login_required(login_url='login')
def sales_order(request):
    if request.method == 'POST':
        form = Sales_Order_Form(request.POST)
        if form.is_valid():
            to = form.cleaned_data['to']
            ship_to = form.cleaned_data['ship_to']
            phone = form.cleaned_data['phone']
            po_number = form.cleaned_data['po_number']
            sales_rep = form.cleaned_data['sales_rep']
            customer_contact = form.cleaned_data['customer_contact']
            payment_terms = form.cleaned_data['payment_terms']
            shipping_method = form.cleaned_data['shipping_method']
            date = form.cleaned_data['date']
            override = form.cleaned_data['override']

            so_unique_product1 = form.cleaned_data['so_unique_product1']
            so_order_quantity1 = form.cleaned_data['so_order_quantity1']
            unique_product1 = form.cleaned_data['unique_product1']
            order_quantity1 = form.cleaned_data['order_quantity1']

            total_quantity1 = product.objects.get(unique_product=unique_product1)
            total_quantity1 = total_quantity1.total_quantity
            total_quantity1 = total_quantity1 - order_quantity1

            if (form.cleaned_data['so_unique_product1'] == None and form.cleaned_data['so_order_quantity1'] >0)\
                    or (form.cleaned_data['unique_product1'] == None and form.cleaned_data['order_quantity1'] >0)\
                    or (form.cleaned_data['so_order_quantity1'] == 0 and form.cleaned_data['order_quantity1'] >0)\
                    or (form.cleaned_data['so_order_quantity1'] >0 and form.cleaned_data['order_quantity1'] == 0) \
                    or (form.cleaned_data['so_unique_product1'] == None and form.cleaned_data['unique_product1'] != None) \
                    or (form.cleaned_data['so_unique_product1'] != None and form.cleaned_data['unique_product1'] == None) \
                    or (form.cleaned_data['so_unique_product2'] == None and form.cleaned_data['so_order_quantity2'] >0)\
                    or (form.cleaned_data['unique_product2'] == None and form.cleaned_data['order_quantity2'] >0)\
                    or (form.cleaned_data['so_order_quantity2'] == 0 and form.cleaned_data['order_quantity2'] >0)\
                    or (form.cleaned_data['so_order_quantity2'] >0 and form.cleaned_data['order_quantity2'] == 0) \
                    or (form.cleaned_data['so_unique_product2'] == None and form.cleaned_data['unique_product2'] != None) \
                    or (form.cleaned_data['so_unique_product2'] != None and form.cleaned_data['unique_product2'] == None) \
                    or (form.cleaned_data['so_unique_product3'] == None and form.cleaned_data['so_order_quantity3'] > 0) \
                    or (form.cleaned_data['unique_product3'] == None and form.cleaned_data['order_quantity3'] > 0) \
                    or (form.cleaned_data['so_order_quantity3'] == 0 and form.cleaned_data['order_quantity3'] > 0) \
                    or (form.cleaned_data['so_order_quantity3'] > 0 and form.cleaned_data['order_quantity3'] == 0) \
                    or (form.cleaned_data['so_unique_product3'] == None and form.cleaned_data['unique_product3'] != None) \
                    or ( form.cleaned_data['so_unique_product3'] != None and form.cleaned_data['unique_product3'] == None) \
                    or (form.cleaned_data['so_unique_product4'] == None and form.cleaned_data['so_order_quantity4'] > 0) \
                    or (form.cleaned_data['unique_product4'] == None and form.cleaned_data['order_quantity4'] > 0) \
                    or (form.cleaned_data['so_order_quantity4'] == 0 and form.cleaned_data['order_quantity4'] > 0) \
                    or (form.cleaned_data['so_order_quantity4'] > 0 and form.cleaned_data['order_quantity4'] == 0) \
                    or (form.cleaned_data['so_unique_product4'] == None and form.cleaned_data['unique_product4'] != None) \
                    or (form.cleaned_data['so_unique_product4'] != None and form.cleaned_data['unique_product4'] == None) \
                    or (form.cleaned_data['so_unique_product5'] == None and form.cleaned_data['so_order_quantity5'] > 0) \
                    or (form.cleaned_data['unique_product5'] == None and form.cleaned_data['order_quantity5'] > 0) \
                    or (form.cleaned_data['so_order_quantity5'] == 0 and form.cleaned_data['order_quantity5'] > 0) \
                    or (form.cleaned_data['so_order_quantity5'] > 0 and form.cleaned_data['order_quantity5'] == 0) \
                    or (form.cleaned_data['so_unique_product5'] == None and form.cleaned_data['unique_product5'] != None) \
                    or (form.cleaned_data['so_unique_product5'] != None and form.cleaned_data['unique_product5'] == None) \
                    or (form.cleaned_data['so_unique_product6'] == None and form.cleaned_data['so_order_quantity6'] > 0) \
                    or (form.cleaned_data['unique_product6'] == None and form.cleaned_data['order_quantity6'] > 0) \
                    or (form.cleaned_data['so_order_quantity6'] == 0 and form.cleaned_data['order_quantity6'] > 0) \
                    or (form.cleaned_data['so_order_quantity6'] > 0 and form.cleaned_data['order_quantity6'] == 0) \
                    or (form.cleaned_data['so_unique_product6'] == None and form.cleaned_data['unique_product6'] != None) \
                    or ( form.cleaned_data['so_unique_product6'] != None and form.cleaned_data['unique_product6'] == None) \
                    or (form.cleaned_data['so_unique_product7'] == None and form.cleaned_data['so_order_quantity7'] > 0) \
                    or (form.cleaned_data['unique_product7'] == None and form.cleaned_data['order_quantity7'] > 0) \
                    or (form.cleaned_data['so_order_quantity7'] == 0 and form.cleaned_data['order_quantity7'] > 0) \
                    or (form.cleaned_data['so_order_quantity7'] > 0 and form.cleaned_data['order_quantity7'] == 0) \
                    or (form.cleaned_data['so_unique_product7'] == None and form.cleaned_data['unique_product7'] != None) \
                    or (form.cleaned_data['so_unique_product7'] != None and form.cleaned_data['unique_product7'] == None) \
                    or (form.cleaned_data['so_unique_product8'] == None and form.cleaned_data['so_order_quantity8'] > 0) \
                    or (form.cleaned_data['unique_product8'] == None and form.cleaned_data['order_quantity8'] > 0) \
                    or (form.cleaned_data['so_order_quantity8'] == 0 and form.cleaned_data['order_quantity8'] > 0) \
                    or (form.cleaned_data['so_order_quantity8'] > 0 and form.cleaned_data['order_quantity8'] == 0) \
                    or (form.cleaned_data['so_unique_product8'] == None and form.cleaned_data['unique_product8'] != None) \
                    or (form.cleaned_data['so_unique_product8'] != None and form.cleaned_data['unique_product8'] == None) \
                    or (form.cleaned_data['so_unique_product9'] == None and form.cleaned_data['so_order_quantity9'] > 0) \
                    or (form.cleaned_data['unique_product9'] == None and form.cleaned_data['order_quantity9'] > 0) \
                    or (form.cleaned_data['so_order_quantity9'] == 0 and form.cleaned_data['order_quantity9'] > 0) \
                    or (form.cleaned_data['so_order_quantity9'] > 0 and form.cleaned_data['order_quantity9'] == 0) \
                    or (form.cleaned_data['so_unique_product9'] == None and form.cleaned_data['unique_product9'] != None) \
                    or (form.cleaned_data['so_unique_product9'] != None and form.cleaned_data['unique_product9'] == None) \
                    or (form.cleaned_data['so_unique_product10'] == None and form.cleaned_data['so_order_quantity10'] > 0) \
                    or (form.cleaned_data['unique_product10'] == None and form.cleaned_data['order_quantity10'] > 0) \
                    or (form.cleaned_data['so_order_quantity10'] == 0 and form.cleaned_data['order_quantity10'] > 0) \
                    or (form.cleaned_data['so_order_quantity10'] > 0 and form.cleaned_data['order_quantity10'] == 0) \
                    or (form.cleaned_data['so_unique_product10'] == None and form.cleaned_data['unique_product10'] != None) \
                    or (form.cleaned_data['so_unique_product10'] != None and form.cleaned_data['unique_product10'] == None) \
                    or (form.cleaned_data['so_unique_product11'] == None and form.cleaned_data['so_order_quantity11'] > 0) \
                    or (form.cleaned_data['unique_product11'] == None and form.cleaned_data['order_quantity11'] > 0) \
                    or (form.cleaned_data['so_order_quantity11'] == 0 and form.cleaned_data['order_quantity11'] > 0) \
                    or (form.cleaned_data['so_order_quantity11'] > 0 and form.cleaned_data['order_quantity11'] == 0) \
                    or (form.cleaned_data['so_unique_product11'] == None and form.cleaned_data['unique_product11'] != None) \
                    or (form.cleaned_data['so_unique_product11'] != None and form.cleaned_data['unique_product11'] == None) \
                    or (form.cleaned_data['so_unique_product12'] == None and form.cleaned_data['so_order_quantity12'] > 0) \
                    or (form.cleaned_data['unique_product12'] == None and form.cleaned_data['order_quantity12'] > 0) \
                    or (form.cleaned_data['so_order_quantity12'] == 0 and form.cleaned_data['order_quantity12'] > 0) \
                    or (form.cleaned_data['so_order_quantity12'] > 0 and form.cleaned_data['order_quantity12'] == 0) \
                    or (form.cleaned_data['so_unique_product12'] == None and form.cleaned_data['unique_product12'] != None) \
                    or (form.cleaned_data['so_unique_product12'] != None and form.cleaned_data['unique_product12'] == None) \
                    or (form.cleaned_data['so_unique_product13'] == None and form.cleaned_data['so_order_quantity13'] > 0) \
                    or (form.cleaned_data['unique_product13'] == None and form.cleaned_data['order_quantity13'] > 0) \
                    or (form.cleaned_data['so_order_quantity13'] == 0 and form.cleaned_data['order_quantity13'] > 0) \
                    or (form.cleaned_data['so_order_quantity13'] > 0 and form.cleaned_data['order_quantity13'] == 0) \
                    or (form.cleaned_data['so_unique_product13'] == None and form.cleaned_data['unique_product13'] != None) \
                    or (form.cleaned_data['so_unique_product13'] != None and form.cleaned_data['unique_product13'] == None) \
                    or (form.cleaned_data['so_unique_product14'] == None and form.cleaned_data['so_order_quantity14'] > 0) \
                    or (form.cleaned_data['unique_product14'] == None and form.cleaned_data['order_quantity14'] > 0) \
                    or (form.cleaned_data['so_order_quantity14'] == 0 and form.cleaned_data['order_quantity14'] > 0) \
                    or (form.cleaned_data['so_order_quantity14'] > 0 and form.cleaned_data['order_quantity14'] == 0) \
                    or (form.cleaned_data['so_unique_product14'] == None and form.cleaned_data['unique_product14'] != None) \
                    or (form.cleaned_data['so_unique_product14'] != None and form.cleaned_data['unique_product14'] == None) \
                    or (form.cleaned_data['so_unique_product15'] == None and form.cleaned_data['so_order_quantity15'] > 0) \
                    or (form.cleaned_data['unique_product15'] == None and form.cleaned_data['order_quantity15'] > 0) \
                    or (form.cleaned_data['so_order_quantity15'] == 0 and form.cleaned_data['order_quantity15'] > 0) \
                    or (form.cleaned_data['so_order_quantity15'] > 0 and form.cleaned_data['order_quantity15'] == 0) \
                    or (form.cleaned_data['so_unique_product15'] == None and form.cleaned_data['unique_product15'] != None) \
                    or (form.cleaned_data['so_unique_product15'] != None and form.cleaned_data['unique_product15'] == None) \
                    or (form.cleaned_data['so_unique_product16'] == None and form.cleaned_data['so_order_quantity16'] > 0) \
                    or (form.cleaned_data['unique_product16'] == None and form.cleaned_data['order_quantity16'] > 0) \
                    or (form.cleaned_data['so_order_quantity16'] == 0 and form.cleaned_data['order_quantity16'] > 0) \
                    or (form.cleaned_data['so_order_quantity16'] > 0 and form.cleaned_data['order_quantity16'] == 0) \
                    or (form.cleaned_data['so_unique_product16'] == None and form.cleaned_data['unique_product16'] != None) \
                    or (form.cleaned_data['so_unique_product16'] != None and form.cleaned_data['unique_product16'] == None) \
                    or (form.cleaned_data['so_unique_product17'] == None and form.cleaned_data['so_order_quantity17'] > 0) \
                    or (form.cleaned_data['unique_product17'] == None and form.cleaned_data['order_quantity17'] > 0) \
                    or (form.cleaned_data['so_order_quantity17'] == 0 and form.cleaned_data['order_quantity17'] > 0) \
                    or (form.cleaned_data['so_order_quantity17'] > 0 and form.cleaned_data['order_quantity17'] == 0) \
                    or (form.cleaned_data['so_unique_product17'] == None and form.cleaned_data['unique_product17'] != None) \
                    or (form.cleaned_data['so_unique_product17'] != None and form.cleaned_data['unique_product17'] == None) \
                    or (form.cleaned_data['so_unique_product18'] == None and form.cleaned_data['so_order_quantity18'] > 0) \
                    or (form.cleaned_data['unique_product18'] == None and form.cleaned_data['order_quantity18'] > 0) \
                    or (form.cleaned_data['so_order_quantity18'] == 0 and form.cleaned_data['order_quantity18'] > 0) \
                    or (form.cleaned_data['so_order_quantity18'] > 0 and form.cleaned_data['order_quantity18'] == 0) \
                    or (form.cleaned_data['so_unique_product18'] == None and form.cleaned_data['unique_product18'] != None) \
                    or (form.cleaned_data['so_unique_product18'] != None and form.cleaned_data['unique_product18'] == None) \
                    or (form.cleaned_data['so_unique_product19'] == None and form.cleaned_data['so_order_quantity19'] > 0) \
                    or (form.cleaned_data['unique_product19'] == None and form.cleaned_data['order_quantity19'] > 0) \
                    or (form.cleaned_data['so_order_quantity19'] == 0 and form.cleaned_data['order_quantity19'] > 0) \
                    or (form.cleaned_data['so_order_quantity19'] > 0 and form.cleaned_data['order_quantity19'] == 0) \
                    or (form.cleaned_data['so_unique_product19'] == None and form.cleaned_data['unique_product19'] != None) \
                    or (form.cleaned_data['so_unique_product19'] != None and form.cleaned_data['unique_product19'] == None) \
                    or (form.cleaned_data['so_unique_product20'] == None and form.cleaned_data['so_order_quantity20'] > 0) \
                    or (form.cleaned_data['unique_product20'] == None and form.cleaned_data['order_quantity20'] > 0) \
                    or (form.cleaned_data['so_order_quantity20'] == 0 and form.cleaned_data['order_quantity20'] > 0) \
                    or (form.cleaned_data['so_order_quantity20'] > 0 and form.cleaned_data['order_quantity20'] == 0) \
                    or (form.cleaned_data['so_unique_product20'] == None and form.cleaned_data['unique_product20'] != None) \
                    or (form.cleaned_data['so_unique_product20'] != None and form.cleaned_data['unique_product20'] == None):
                messages.info(request,
                              'All orders with quantity greater than 0 must be associated with a product. Also, if fulfillment quantity is greater than 0, then shipping quantity must be greater than 0, and vice versa.',
                              extra_tags="warning1")
                context = {
                    'form':form,
                }
                return render(request, 'inventory_management/sales_order.html', context)



            if form.cleaned_data['so_unique_product2'] == None:
                so_unique_product2 = None
                so_order_quantity2 = None
                unique_product2 = None
                order_quantity2 = None
                total_quantity2 = None
            else:
                so_order_quantity2 = form.cleaned_data['so_order_quantity2']
                so_unique_product2 = form.cleaned_data['unique_product2']
                unique_product2 = form.cleaned_data['unique_product2']
                order_quantity2 = form.cleaned_data['order_quantity2']
                total_quantity2 = product.objects.get(unique_product=unique_product2)
                total_quantity2 = total_quantity2.total_quantity
                total_quantity2 = total_quantity2 - order_quantity2

            if form.cleaned_data['so_unique_product3'] == None:
                so_unique_product3 = None
                so_order_quantity3 = None
                unique_product3 = None
                order_quantity3 = None
                total_quantity3 = None
            else:
                so_order_quantity3 = form.cleaned_data['so_order_quantity3']
                so_unique_product3 = form.cleaned_data['unique_product3']
                unique_product3 = form.cleaned_data['unique_product3']
                order_quantity3 = form.cleaned_data['order_quantity3']
                total_quantity3 = product.objects.get(unique_product=unique_product3)
                total_quantity3 = total_quantity3.total_quantity
                total_quantity3 = total_quantity3 - order_quantity3

            if form.cleaned_data['so_unique_product4'] == None:
                so_unique_product4 = None
                so_order_quantity4 = None
                unique_product4 = None
                order_quantity4 = None
                total_quantity4 = None
            else:
                so_order_quantity4 = form.cleaned_data['so_order_quantity4']
                so_unique_product4 = form.cleaned_data['unique_product4']
                unique_product4 = form.cleaned_data['unique_product4']
                order_quantity4 = form.cleaned_data['order_quantity4']
                total_quantity4 = product.objects.get(unique_product=unique_product4)
                total_quantity4 = total_quantity4.total_quantity
                total_quantity4 = total_quantity4 - order_quantity4

            if form.cleaned_data['so_unique_product5'] == None:
                so_unique_product5 = None
                so_order_quantity5 = None
                unique_product5 = None
                order_quantity5 = None
                total_quantity5 = None
            else:
                so_order_quantity5 = form.cleaned_data['so_order_quantity5']
                so_unique_product5 = form.cleaned_data['unique_product5']
                unique_product5 = form.cleaned_data['unique_product5']
                order_quantity5 = form.cleaned_data['order_quantity5']
                total_quantity5 = product.objects.get(unique_product=unique_product5)
                total_quantity5 = total_quantity5.total_quantity
                total_quantity5 = total_quantity5 - order_quantity5

            if form.cleaned_data['so_unique_product6'] == None:
                so_unique_product6 = None
                so_order_quantity6 = None
                unique_product6 = None
                order_quantity6 = None
                total_quantity6 = None
            else:
                so_order_quantity6 = form.cleaned_data['so_order_quantity6']
                so_unique_product6 = form.cleaned_data['unique_product6']
                unique_product6 = form.cleaned_data['unique_product6']
                order_quantity6 = form.cleaned_data['order_quantity6']
                total_quantity6 = product.objects.get(unique_product=unique_product6)
                total_quantity6 = total_quantity6.total_quantity
                total_quantity6 = total_quantity6 - order_quantity6

            if form.cleaned_data['so_unique_product7'] == None:
                so_unique_product7 = None
                so_order_quantity7 = None
                unique_product7 = None
                order_quantity7 = None
                total_quantity7 = None
            else:
                so_order_quantity7 = form.cleaned_data['so_order_quantity7']
                so_unique_product7 = form.cleaned_data['unique_product7']
                unique_product7 = form.cleaned_data['unique_product7']
                order_quantity7 = form.cleaned_data['order_quantity7']
                total_quantity7 = product.objects.get(unique_product=unique_product7)
                total_quantity7 = total_quantity7.total_quantity
                total_quantity7 = total_quantity7 - order_quantity7

            if form.cleaned_data['so_unique_product8'] == None:
                so_unique_product8 = None
                so_order_quantity8 = None
                unique_product8 = None
                order_quantity8 = None
                total_quantity8 = None
            else:
                so_order_quantity8 = form.cleaned_data['so_order_quantity8']
                so_unique_product8 = form.cleaned_data['unique_product8']
                unique_product8 = form.cleaned_data['unique_product8']
                order_quantity8 = form.cleaned_data['order_quantity8']
                total_quantity8 = product.objects.get(unique_product=unique_product8)
                total_quantity8 = total_quantity8.total_quantity
                total_quantity8 = total_quantity8 - order_quantity8

            if form.cleaned_data['so_unique_product9'] == None:
                so_unique_product9 = None
                so_order_quantity9 = None
                unique_product9 = None
                order_quantity9 = None
                total_quantity9 = None
            else:
                so_order_quantity9 = form.cleaned_data['so_order_quantity9']
                so_unique_product9 = form.cleaned_data['unique_product9']
                unique_product9 = form.cleaned_data['unique_product9']
                order_quantity9 = form.cleaned_data['order_quantity7']
                total_quantity9 = product.objects.get(unique_product=unique_product9)
                total_quantity9 = total_quantity9.total_quantity
                total_quantity9 = total_quantity9 - order_quantity9

            if form.cleaned_data['so_unique_product10'] == None:
                so_unique_product10 = None
                so_order_quantity10 = None
                unique_product10 = None
                order_quantity10 = None
                total_quantity10 = None
            else:
                so_order_quantity10 = form.cleaned_data['so_order_quantity10']
                so_unique_product10 = form.cleaned_data['unique_product10']
                unique_product10 = form.cleaned_data['unique_product10']
                order_quantity10 = form.cleaned_data['order_quantity10']
                total_quantity10 = product.objects.get(unique_product=unique_product10)
                total_quantity10 = total_quantity10.total_quantity
                total_quantity10 = total_quantity10 - order_quantity10

            if form.cleaned_data['so_unique_product11'] == None:
                so_unique_product11 = None
                so_order_quantity11 = None
                unique_product11 = None
                order_quantity11 = None
                total_quantity11 = None
            else:
                so_order_quantity11 = form.cleaned_data['so_order_quantity11']
                so_unique_product11 = form.cleaned_data['unique_product11']
                unique_product11 = form.cleaned_data['unique_product11']
                order_quantity11 = form.cleaned_data['order_quantity11']
                total_quantity11 = product.objects.get(unique_product=unique_product11)
                total_quantity11 = total_quantity11.total_quantity
                total_quantity11 = total_quantity11 - order_quantity11

            if form.cleaned_data['so_unique_product12'] == None:
                so_unique_product12 = None
                so_order_quantity12 = None
                unique_product12 = None
                order_quantity12 = None
                total_quantity12 = None
            else:
                so_order_quantity12 = form.cleaned_data['so_order_quantity12']
                so_unique_product12 = form.cleaned_data['unique_product12']
                unique_product12 = form.cleaned_data['unique_product12']
                order_quantity12 = form.cleaned_data['order_quantity12']
                total_quantity12 = product.objects.get(unique_product=unique_product12)
                total_quantity12 = total_quantity12.total_quantity
                total_quantity12 = total_quantity12 - order_quantity12

            if form.cleaned_data['so_unique_product13'] == None:
                so_unique_product13 = None
                so_order_quantity13 = None
                unique_product13 = None
                order_quantity13 = None
                total_quantity13 = None
            else:
                so_order_quantity13 = form.cleaned_data['so_order_quantity13']
                so_unique_product13 = form.cleaned_data['unique_product13']
                unique_product13 = form.cleaned_data['unique_product13']
                order_quantity13 = form.cleaned_data['order_quantity13']
                total_quantity13 = product.objects.get(unique_product=unique_product13)
                total_quantity13 = total_quantity13.total_quantity
                total_quantity13 = total_quantity13 - order_quantity13

            if form.cleaned_data['so_unique_product14'] == None:
                so_unique_product14 = None
                so_order_quantity14 = None
                unique_product14 = None
                order_quantity14 = None
                total_quantity14 = None
            else:
                so_order_quantity14 = form.cleaned_data['so_order_quantity14']
                so_unique_product14 = form.cleaned_data['unique_product14']
                unique_product14 = form.cleaned_data['unique_product14']
                order_quantity14 = form.cleaned_data['order_quantity14']
                total_quantity14 = product.objects.get(unique_product=unique_product14)
                total_quantity14 = total_quantity14.total_quantity
                total_quantity14 = total_quantity14 - order_quantity14

            if form.cleaned_data['so_unique_product15'] == None:
                so_unique_product15 = None
                so_order_quantity15 = None
                unique_product15 = None
                order_quantity15 = None
                total_quantity15 = None
            else:
                so_order_quantity15 = form.cleaned_data['so_order_quantity15']
                so_unique_product15 = form.cleaned_data['unique_product15']
                unique_product15 = form.cleaned_data['unique_product15']
                order_quantity15 = form.cleaned_data['order_quantity15']
                total_quantity15 = product.objects.get(unique_product=unique_product15)
                total_quantity15 = total_quantity15.total_quantity
                total_quantity15 = total_quantity15 - order_quantity15

            if form.cleaned_data['so_unique_product16'] == None:
                so_unique_product16 = None
                so_order_quantity16 = None
                unique_product16 = None
                order_quantity16 = None
                total_quantity16 = None
            else:
                so_order_quantity16 = form.cleaned_data['so_order_quantity16']
                so_unique_product16 = form.cleaned_data['unique_product16']
                unique_product16 = form.cleaned_data['unique_product16']
                order_quantity16 = form.cleaned_data['order_quantity16']
                total_quantity16 = product.objects.get(unique_product=unique_product16)
                total_quantity16 = total_quantity16.total_quantity
                total_quantity16 = total_quantity16 - order_quantity16

            if form.cleaned_data['so_unique_product17'] == None:
                so_unique_product17 = None
                so_order_quantity17 = None
                unique_product17 = None
                order_quantity17 = None
                total_quantity17 = None
            else:
                so_order_quantity17 = form.cleaned_data['so_order_quantity17']
                so_unique_product17 = form.cleaned_data['unique_product17']
                unique_product17 = form.cleaned_data['unique_product17']
                order_quantity17 = form.cleaned_data['order_quantity17']
                total_quantity17 = product.objects.get(unique_product=unique_product17)
                total_quantity17 = total_quantity17.total_quantity
                total_quantity17 = total_quantity17 - order_quantity17

            if form.cleaned_data['so_unique_product18'] == None:
                so_unique_product18 = None
                so_order_quantity18 = None
                unique_product18 = None
                order_quantity18 = None
                total_quantity18 = None
            else:
                so_order_quantity18 = form.cleaned_data['so_order_quantity18']
                so_unique_product18 = form.cleaned_data['unique_product18']
                unique_product18 = form.cleaned_data['unique_product18']
                order_quantity18 = form.cleaned_data['order_quantity18']
                total_quantity18 = product.objects.get(unique_product=unique_product18)
                total_quantity18 = total_quantity18.total_quantity
                total_quantity18 = total_quantity18 - order_quantity18

            if form.cleaned_data['so_unique_product19'] == None:
                so_unique_product19 = None
                so_order_quantity19 = None
                unique_product19 = None
                order_quantity19 = None
                total_quantity19 = None
            else:
                so_order_quantity19 = form.cleaned_data['so_order_quantity19']
                so_unique_product19 = form.cleaned_data['unique_product19']
                unique_product19 = form.cleaned_data['unique_product19']
                order_quantity19 = form.cleaned_data['order_quantity19']
                total_quantity19 = product.objects.get(unique_product=unique_product19)
                total_quantity19 = total_quantity19.total_quantity
                total_quantity19 = total_quantity19 - order_quantity19

            if form.cleaned_data['so_unique_product20'] == None:
                so_unique_product20 = None
                so_order_quantity20 = None
                unique_product20 = None
                order_quantity20 = None
                total_quantity20 = None
            else:
                so_order_quantity20 = form.cleaned_data['so_order_quantity20']
                so_unique_product20 = form.cleaned_data['unique_product20']
                unique_product20 = form.cleaned_data['unique_product20']
                order_quantity20 = form.cleaned_data['order_quantity20']
                total_quantity20 = product.objects.get(unique_product=unique_product20)
                total_quantity20 = total_quantity20.total_quantity
                total_quantity20 = total_quantity20 - order_quantity20


            #######################################################################
            if (total_quantity1 >= 0 and (total_quantity2 is None or total_quantity2 >= 0)
                and (total_quantity3 is None or total_quantity3 >= 0)
                and (total_quantity5 is None or total_quantity5 >= 0)
                and (total_quantity6 is None or total_quantity6 >= 0)
                and (total_quantity7 is None or total_quantity7 >= 0)
                and (total_quantity8 is None or total_quantity8 >= 0)
                and (total_quantity9 is None or total_quantity9 >= 0)
                and (total_quantity10 is None or total_quantity10 >= 0)
                and (total_quantity11 is None or total_quantity11 >= 0)
                and (total_quantity12 is None or total_quantity12 >= 0)
                and (total_quantity13 is None or total_quantity13 >= 0)
                and (total_quantity14 is None or total_quantity14 >= 0)
                and (total_quantity15 is None or total_quantity15 >= 0)
                and (total_quantity16 is None or total_quantity16 >= 0)
                and (total_quantity17 is None or total_quantity17 >= 0)
                and (total_quantity18 is None or total_quantity18 >= 0)
                and (total_quantity19 is None or total_quantity19 >= 0)
                and (total_quantity20 is None or total_quantity20 >= 0)) or override == "Yes":

                product1_db = product.objects.get(unique_product=unique_product1)
                product1_db.total_quantity = F('total_quantity') - order_quantity1
                product1_db.save()

                if unique_product2 == None:
                    pass
                else:
                    product2_db = product.objects.get(unique_product=unique_product2)
                    product2_db.total_quantity = F('total_quantity') - order_quantity2
                    product2_db.save()

                if unique_product3 == None:
                    pass
                else:
                    product3_db = product.objects.get(unique_product=unique_product3)
                    product3_db.total_quantity = F('total_quantity') - order_quantity3
                    product3_db.save()

                if unique_product4 == None:
                    pass
                else:
                    product4_db = product.objects.get(unique_product=unique_product4)
                    product4_db.total_quantity = F('total_quantity') - order_quantity4
                    product4_db.save()

                if unique_product5 == None:
                    pass
                else:
                    product5_db = product.objects.get(unique_product=unique_product5)
                    product5_db.total_quantity = F('total_quantity') - order_quantity5
                    product5_db.save()

                if unique_product6 == None:
                    pass
                else:
                    product6_db = product.objects.get(unique_product=unique_product6)
                    product6_db.total_quantity = F('total_quantity') - order_quantity6
                    product6_db.save()

                if unique_product7 == None:
                    pass
                else:
                    product7_db = product.objects.get(unique_product=unique_product7)
                    product7_db.total_quantity = F('total_quantity') - order_quantity7
                    product7_db.save()

                if unique_product8 == None:
                    pass
                else:
                    product8_db = product.objects.get(unique_product=unique_product8)
                    product8_db.total_quantity = F('total_quantity') - order_quantity8
                    product8_db.save()

                if unique_product9 == None:
                    pass
                else:
                    product9_db = product.objects.get(unique_product=unique_product9)
                    product9_db.total_quantity = F('total_quantity') - order_quantity9
                    product9_db.save()

                if unique_product10 == None:
                    pass
                else:
                    product10_db = product.objects.get(unique_product=unique_product10)
                    product10_db.total_quantity = F('total_quantity') - order_quantity10
                    product10_db.save()

                if unique_product11 == None:
                    pass
                else:
                    product11_db = product.objects.get(unique_product=unique_product11)
                    product11_db.total_quantity = F('total_quantity') - order_quantity11
                    product11_db.save()

                if unique_product12 == None:
                    pass
                else:
                    product12_db = product.objects.get(unique_product=unique_product12)
                    product12_db.total_quantity = F('total_quantity') - order_quantity12
                    product12_db.save()

                if unique_product13 == None:
                    pass
                else:
                    product13_db = product.objects.get(unique_product=unique_product13)
                    product13_db.total_quantity = F('total_quantity') - order_quantity13
                    product13_db.save()

                if unique_product14 == None:
                    pass
                else:
                    product14_db = product.objects.get(unique_product=unique_product14)
                    product14_db.total_quantity = F('total_quantity') - order_quantity14
                    product14_db.save()

                if unique_product15 == None:
                    pass
                else:
                    product15_db = product.objects.get(unique_product=unique_product15)
                    product15_db.total_quantity = F('total_quantity') - order_quantity15
                    product15_db.save()

                if unique_product16 == None:
                    pass
                else:
                    product16_db = product.objects.get(unique_product=unique_product16)
                    product16_db.total_quantity = F('total_quantity') - order_quantity16
                    product16_db.save()

                if unique_product17 == None:
                    pass
                else:
                    product17_db = product.objects.get(unique_product=unique_product17)
                    product17_db.total_quantity = F('total_quantity') - order_quantity17
                    product17_db.save()

                if unique_product18 == None:
                    pass
                else:
                    product18_db = product.objects.get(unique_product=unique_product18)
                    product18_db.total_quantity = F('total_quantity') - order_quantity18
                    product18_db.save()

                if unique_product19 == None:
                    pass
                else:
                    product19_db = product.objects.get(unique_product=unique_product19)
                    product19_db.total_quantity = F('total_quantity') - order_quantity19
                    product19_db.save()

                if unique_product20 == None:
                    pass
                else:
                    product20_db = product.objects.get(unique_product=unique_product20)
                    product20_db.total_quantity = F('total_quantity') - order_quantity20
                    product20_db.save()

                db_insert = sales_order_model(to=to, ship_to=ship_to, po_number=po_number, phone=phone,
                                              sales_rep=sales_rep,
                                              customer_contact=customer_contact, shipping_method=shipping_method,
                                              payment_terms=payment_terms, date=date, override=override,
                                              so_unique_product1=so_unique_product1,
                                              so_order_quantity1=so_order_quantity1,
                                              so_unique_product2=so_unique_product2,
                                              so_order_quantity2=so_order_quantity2,
                                              so_unique_product3=so_unique_product3,
                                              so_order_quantity3=so_order_quantity3,
                                              so_unique_product4=so_unique_product4,
                                              so_order_quantity4=so_order_quantity4,
                                              so_unique_product5=so_unique_product5,
                                              so_order_quantity5=so_order_quantity5,
                                              so_unique_product6=so_unique_product6,
                                              so_order_quantity6=so_order_quantity6,
                                              so_unique_product7=so_unique_product7,
                                              so_order_quantity7=so_order_quantity7,
                                              so_unique_product8=so_unique_product8,
                                              so_order_quantity8=so_order_quantity8,
                                              so_unique_product9=so_unique_product9,
                                              so_order_quantity9=so_order_quantity9,
                                              so_unique_product10=so_unique_product10,
                                              so_order_quantity10=so_order_quantity10,
                                              so_unique_product11=so_unique_product11,
                                              so_order_quantity11=so_order_quantity11,
                                              so_unique_product12=so_unique_product12,
                                              so_order_quantity12=so_order_quantity12,
                                              so_unique_product13=so_unique_product13,
                                              so_order_quantity13=so_order_quantity13,
                                              so_unique_product14=so_unique_product14,
                                              so_order_quantity14=so_order_quantity14,
                                              so_unique_product15=so_unique_product15,
                                              so_order_quantity15=so_order_quantity15,
                                              so_unique_product16=so_unique_product16,
                                              so_order_quantity16=so_order_quantity16,
                                              so_unique_product17=so_unique_product17,
                                              so_order_quantity17=so_order_quantity17,
                                              so_unique_product18=so_unique_product18,
                                              so_order_quantity18=so_order_quantity18,
                                              so_unique_product19=so_unique_product19,
                                              so_order_quantity19=so_order_quantity19,
                                              so_unique_product20=so_unique_product20,
                                              so_order_quantity20=so_order_quantity20,
                                              unique_product1=unique_product1, order_quantity1=order_quantity1,
                                              unique_product2=unique_product2, order_quantity2=order_quantity2,
                                              unique_product3=unique_product3, order_quantity3=order_quantity3,
                                              unique_product4=unique_product4, order_quantity4=order_quantity4,
                                              unique_product5=unique_product5, order_quantity5=order_quantity5,
                                              unique_product6=unique_product6, order_quantity6=order_quantity6,
                                              unique_product7=unique_product7, order_quantity7=order_quantity7,
                                              unique_product8=unique_product8, order_quantity8=order_quantity8,
                                              unique_product9=unique_product9, order_quantity9=order_quantity9,
                                              unique_product10=unique_product10, order_quantity10=order_quantity10,
                                              unique_product11=unique_product11, order_quantity11=order_quantity11,
                                              unique_product12=unique_product12, order_quantity12=order_quantity12,
                                              unique_product13=unique_product13, order_quantity13=order_quantity13,
                                              unique_product14=unique_product14, order_quantity14=order_quantity14,
                                              unique_product15=unique_product15, order_quantity15=order_quantity15,
                                              unique_product16=unique_product16, order_quantity16=order_quantity16,
                                              unique_product17=unique_product17, order_quantity17=order_quantity17,
                                              unique_product18=unique_product18, order_quantity18=order_quantity18,
                                              unique_product19=unique_product19, order_quantity19=order_quantity19,
                                              unique_product20=unique_product20, order_quantity20=order_quantity20, created_by = request.user.username,)
                db_insert.save()
                return redirect('inventory_management')
                ##########################################
            else:

                if total_quantity1 == None or total_quantity1>=0:
                    pass
                else:
                    messages.info(request, 'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product1, total_quantity1),
                                  extra_tags='unique_product1')

                if total_quantity2 == None or total_quantity2>=0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product2, total_quantity2),
                                  extra_tags='unique_product2')
                if total_quantity3 == None or total_quantity3>=0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product3, total_quantity3),
                                  extra_tags='unique_product3')
                if total_quantity4 == None or total_quantity4>=0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product4, total_quantity4),
                                  extra_tags='unique_product4')

                if total_quantity5 == None or total_quantity5>=0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product5, total_quantity5),
                                  extra_tags='unique_product5')

                if total_quantity6 == None or total_quantity6 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product6, total_quantity6),
                                  extra_tags='unique_product6')

                if total_quantity7 == None or total_quantity7 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product7, total_quantity7),
                                  extra_tags='unique_product7')

                if total_quantity8 == None or total_quantity8 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product8, total_quantity8),
                                  extra_tags='unique_product8')

                if total_quantity9 == None or total_quantity9 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product9, total_quantity9),
                                  extra_tags='unique_product9')

                if total_quantity10 == None or total_quantity10 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product10, total_quantity10),
                                  extra_tags='unique_product_10')

                if total_quantity11 == None or total_quantity11 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product11, total_quantity11),
                                  extra_tags='unique_product_11')

                if total_quantity12 == None or total_quantity12 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product12, total_quantity12),
                                  extra_tags='unique_product_12')

                if total_quantity13 == None or total_quantity13 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product13, total_quantity13),
                                  extra_tags='unique_product_13')

                if total_quantity14 == None or total_quantity14 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product14, total_quantity14),
                                  extra_tags='unique_product_14')

                if total_quantity15 == None or total_quantity15 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product15, total_quantity15),
                                  extra_tags='unique_product_15')

                if total_quantity16 == None or total_quantity16 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product16, total_quantity16),
                                  extra_tags='unique_product_16')

                if total_quantity17 == None or total_quantity17 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product17, total_quantity17),
                                  extra_tags='unique_product_17')

                if total_quantity18 == None or total_quantity18 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product18, total_quantity18),
                                  extra_tags='unique_product_18')

                if total_quantity19 == None or total_quantity19 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product19, total_quantity19),
                                  extra_tags="unique_product_19")

                if total_quantity20 == None or total_quantity20 >= 0:
                    pass
                else:
                    messages.info(request,
                                  'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product20, total_quantity20),
                                  extra_tags='unique_product_20')

                ##################################################
                context = {
                    'form': form,
                }
                return render(request, 'inventory_management/sales_order.html', context)

    form = Sales_Order_Form()
    context = {
        "form":form,
    }
    return render(request, 'inventory_management/sales_order.html', context)


@login_required(login_url='login')
def view_inventory_All(request):
    items = product.objects.all()
    context = {
        'items': items,

    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_401_WRC(request):
    items = product.objects.filter(inventory_group='401 WRC')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_AYC(request):
    items = product.objects.filter(inventory_group='AYC')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_CandBTR(request):
    items = product.objects.filter(inventory_group='C&BTR & Fine Grain D-FIR')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_Cypress(request):
    items = product.objects.filter(inventory_group='Cypress')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_D_FIR(request):
    items = product.objects.filter(inventory_group='D-FIR')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_EWP(request):
    items = product.objects.filter(inventory_group='EWP')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_Oak(request):
    items = product.objects.filter(inventory_group='Oak')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_Spruce(request):
    items = product.objects.filter(inventory_group='Spruce')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def view_inventory_WRC(request):
    items = product.objects.filter(inventory_group='WRC')
    context = {
        'items': items,
    }
    return render(request, 'inventory_management/view_inventory.html', context)


@login_required(login_url='login')
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="All_Products.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Unique Product', 'Price', 'Total Quantity', 'Inventory Group', 'Grade', 'Length', 'Pcs/Unit', 'Size', 'B.F. Total', 'Total USD'])

    users = product.objects.all().values_list('id', 'unique_product', 'price', 'total_quantity', 'inventory_group', 'grade', 'length', 'pcs_Per_Unit', 'size', 'bF_Total', 'Total_USD')
    for user in users:
        writer.writerow(user)

    return response


@login_required(login_url='login')
def analyze_inventory(request):
    dataset1 = product.objects.order_by().values('inventory_group').annotate(total=Sum('total_quantity'))  # shows count quantity by inventory group

    dataset1_labels = []
    dataset1_values=[]
    for dic in dataset1:
        count = 0
        for val, cal in dic.items():
            if count==0:
                if cal == 'C&BTR & Fine Grain D-FIR':
                    cal = 'CBTR'
                    dataset1_labels.append(cal)
                    count += 1
                else:
                    dataset1_labels.append(cal)
                    count += 1
            else:
                dataset1_values.append(cal)

    dataset2 = product.objects.order_by().values('inventory_group').annotate(total=Sum('Total_USD'))  # shows dollar sum by inventory group

    dataset2_labels = []
    dataset2_values = []
    for dic in dataset2:
        count = 0
        for val, cal in dic.items():
            if count==0:
                if cal == 'C&BTR & Fine Grain D-FIR':
                    cal = 'CBTR'
                    dataset2_labels.append(cal)
                    count += 1
                else:
                    dataset2_labels.append(cal)
                    count+=1
            else:
                dataset2_values.append(cal)


    dataset3 = product.objects.order_by('total_quantity').values('unique_product').annotate(total=Sum('total_quantity'))  # shows 10 products with the lowest inventory count
    dataset3_labels = []
    dataset3_values = []

    total_count = 0
    for dic in dataset3:
        total_count+=1
        if total_count <=10:
            count = 0
            for val, cal in dic.items():
                if count == 0:
                    dataset3_labels.append(cal)
                    count += 1
                else:
                    dataset3_values.append(cal)

    dataset3_zip = list(zip(dataset3_labels, dataset3_values))

    dataset4 = product.objects.order_by('-total_quantity').values('unique_product').annotate(
        total=Sum('total_quantity'))  # shows 10 products with the highest inventory count
    dataset4_labels = []
    dataset4_values = []

    total_count = 0
    for dic in dataset4:
        total_count += 1
        if total_count <= 10:
            count = 0
            for val, cal in dic.items():
                if count == 0:
                    dataset4_labels.append(cal)
                    count += 1
                else:
                    dataset4_values.append(cal)

    dataset4_zip = list(zip(dataset4_labels, dataset4_values))


    context = {
        'dataset1_labels':dataset1_labels,
        'dataset1_values': dataset1_values,
        'dataset2_labels': dataset2_labels,
        'dataset2_values': dataset2_values,
        'dataset3_zip': dataset3_zip,
        'dataset4_zip': dataset4_zip,

    }
    return render(request, 'inventory_management/analyze_inventory.html', context)