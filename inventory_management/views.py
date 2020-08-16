from django.db.models import F, Count, Sum
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import csv
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


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

            type_grade1 = form.cleaned_data['type_grade1']
            size1 = form.cleaned_data['size1']
            length1 = form.cleaned_data['length1']
            unique_product1= '{0} | {1} | {2}'.format(type_grade1, size1, length1)
            order_quantity1 = form.cleaned_data['order_quantity1']
            if unique_product1 == "---- | ---- | ----":
                product1_db = True
            else:
                product1_db = product.objects.filter(unique_product=unique_product1).exists()

            type_grade2 = form.cleaned_data['type_grade2']
            size2 = form.cleaned_data['size2']
            length2 = form.cleaned_data['length2']
            unique_product2 = '{0} | {1} | {2}'.format(type_grade2, size2, length2)
            order_quantity2 = form.cleaned_data['order_quantity2']
            if unique_product2 == "---- | ---- | ----":
                product2_db = True
            else:
                product2_db = product.objects.filter(unique_product=unique_product2).exists()

            type_grade3 = form.cleaned_data['type_grade3']
            size3 = form.cleaned_data['size3']
            length3 = form.cleaned_data['length3']
            unique_product3 = '{0} | {1} | {2}'.format(type_grade3, size3, length3)
            order_quantity3 = form.cleaned_data['order_quantity3']
            if unique_product3 == "---- | ---- | ----":
                product3_db = True
            else:
                product3_db = product.objects.filter(unique_product=unique_product3).exists()

            type_grade4 = form.cleaned_data['type_grade4']
            size4 = form.cleaned_data['size4']
            length4 = form.cleaned_data['length4']
            unique_product4 = '{0} | {1} | {2}'.format(type_grade4, size4, length4)
            order_quantity4 = form.cleaned_data['order_quantity4']
            if unique_product4 == "---- | ---- | ----":
                product4_db = True
            else:
                product4_db = product.objects.filter(unique_product=unique_product4).exists()

            type_grade5 = form.cleaned_data['type_grade5']
            size5 = form.cleaned_data['size5']
            length5 = form.cleaned_data['length5']
            unique_product5 = '{0} | {1} | {2}'.format(type_grade5, size5, length5)
            order_quantity5 = form.cleaned_data['order_quantity5']
            if unique_product5 == "---- | ---- | ----":
                product5_db = True
            else:
                product5_db = product.objects.filter(unique_product=unique_product5).exists()

            type_grade6 = form.cleaned_data['type_grade6']
            size6 = form.cleaned_data['size6']
            length6 = form.cleaned_data['length6']
            unique_product6 = '{0} | {1} | {2}'.format(type_grade6, size6, length6)
            order_quantity6 = form.cleaned_data['order_quantity6']
            if unique_product6 == "---- | ---- | ----":
                product6_db = True
            else:
                product6_db = product.objects.filter(unique_product=unique_product6).exists()

            type_grade7 = form.cleaned_data['type_grade7']
            size7 = form.cleaned_data['size7']
            length7 = form.cleaned_data['length7']
            unique_product7 = '{0} | {1} | {2}'.format(type_grade7, size7, length7)
            order_quantity7 = form.cleaned_data['order_quantity7']
            if unique_product7 == "---- | ---- | ----":
                product7_db = True
            else:
                product7_db = product.objects.filter(unique_product=unique_product7).exists()

            type_grade8 = form.cleaned_data['type_grade8']
            size8 = form.cleaned_data['size8']
            length8 = form.cleaned_data['length8']
            unique_product8 = '{0} | {1} | {2}'.format(type_grade8, size8, length8)
            order_quantity8 = form.cleaned_data['order_quantity8']
            if unique_product8 == "---- | ---- | ----":
                product8_db = True
            else:
                product8_db = product.objects.filter(unique_product=unique_product8).exists()

            type_grade9 = form.cleaned_data['type_grade9']
            size9 = form.cleaned_data['size9']
            length9 = form.cleaned_data['length9']
            unique_product9 = '{0} | {1} | {2}'.format(type_grade9, size9, length9)
            order_quantity9 = form.cleaned_data['order_quantity9']
            if unique_product9 == "---- | ---- | ----":
                product9_db = True
            else:
                product9_db = product.objects.filter(unique_product=unique_product9).exists()

            type_grade10 = form.cleaned_data['type_grade10']
            size10 = form.cleaned_data['size10']
            length10 = form.cleaned_data['length10']
            unique_product10 = '{0} | {1} | {2}'.format(type_grade10, size10, length10)
            order_quantity10 = form.cleaned_data['order_quantity10']
            if unique_product10 == "---- | ---- | ----":
                product10_db = True
            else:
                product10_db = product.objects.filter(unique_product=unique_product10).exists()

            type_grade11 = form.cleaned_data['type_grade11']
            size11 = form.cleaned_data['size11']
            length11 = form.cleaned_data['length11']
            unique_product11 = '{0} | {1} | {2}'.format(type_grade11, size11, length11)
            order_quantity11 = form.cleaned_data['order_quantity11']
            if unique_product11 == "---- | ---- | ----":
                product11_db = True
            else:
                product11_db = product.objects.filter(unique_product=unique_product11).exists()

            type_grade12 = form.cleaned_data['type_grade12']
            size12 = form.cleaned_data['size12']
            length12 = form.cleaned_data['length12']
            unique_product12 = '{0} | {1} | {2}'.format(type_grade12, size12, length12)
            order_quantity12 = form.cleaned_data['order_quantity12']
            if unique_product12 == "---- | ---- | ----":
                product12_db = True
            else:
                product12_db = product.objects.filter(unique_product=unique_product12).exists()

            type_grade13 = form.cleaned_data['type_grade13']
            size13 = form.cleaned_data['size13']
            length13 = form.cleaned_data['length13']
            unique_product13 = '{0} | {1} | {2}'.format(type_grade13, size13, length13)
            order_quantity13 = form.cleaned_data['order_quantity13']
            if unique_product13 == "---- | ---- | ----":
                product13_db = True
            else:
                product13_db = product.objects.filter(unique_product=unique_product13).exists()

            type_grade14 = form.cleaned_data['type_grade14']
            size14 = form.cleaned_data['size14']
            length14 = form.cleaned_data['length14']
            unique_product14 = '{0} | {1} | {2}'.format(type_grade14, size14, length14)
            order_quantity14 = form.cleaned_data['order_quantity14']
            if unique_product14 == "---- | ---- | ----":
                product14_db = True
            else:
                product14_db = product.objects.filter(unique_product=unique_product14).exists()

            type_grade15 = form.cleaned_data['type_grade15']
            size15 = form.cleaned_data['size15']
            length15 = form.cleaned_data['length15']
            unique_product15 = '{0} | {1} | {2}'.format(type_grade15, size15, length15)
            order_quantity15 = form.cleaned_data['order_quantity15']
            if unique_product15 == "---- | ---- | ----":
                product15_db = True
            else:
                product15_db = product.objects.filter(unique_product=unique_product15).exists()

            type_grade16 = form.cleaned_data['type_grade16']
            size16 = form.cleaned_data['size16']
            length16 = form.cleaned_data['length16']
            unique_product16 = '{0} | {1} | {2}'.format(type_grade16, size16, length16)
            order_quantity16 = form.cleaned_data['order_quantity16']
            if unique_product16 == "---- | ---- | ----":
                product16_db = True
            else:
                product16_db = product.objects.filter(unique_product=unique_product16).exists()

            type_grade17 = form.cleaned_data['type_grade17']
            size17 = form.cleaned_data['size17']
            length17 = form.cleaned_data['length17']
            unique_product17 = '{0} | {1} | {2}'.format(type_grade17, size17, length17)
            order_quantity17 = form.cleaned_data['order_quantity17']
            if unique_product17 == "---- | ---- | ----":
                product17_db = True
            else:
                product17_db = product.objects.filter(unique_product=unique_product17).exists()

            type_grade18 = form.cleaned_data['type_grade18']
            size18 = form.cleaned_data['size18']
            length18 = form.cleaned_data['length18']
            unique_product18 = '{0} | {1} | {2}'.format(type_grade18, size18, length18)
            order_quantity18 = form.cleaned_data['order_quantity18']
            if unique_product18 == "---- | ---- | ----":
                product18_db = True
            else:
                product18_db = product.objects.filter(unique_product=unique_product18).exists()

            type_grade19 = form.cleaned_data['type_grade19']
            size19 = form.cleaned_data['size19']
            length19 = form.cleaned_data['length19']
            unique_product19 = '{0} | {1} | {2}'.format(type_grade19, size19, length19)
            order_quantity19 = form.cleaned_data['order_quantity19']
            if unique_product19 == "---- | ---- | ----":
                product19_db = True
            else:
                product19_db = product.objects.filter(unique_product=unique_product19).exists()

            type_grade20 = form.cleaned_data['type_grade20']
            size20 = form.cleaned_data['size20']
            length20 = form.cleaned_data['length20']
            unique_product20 = '{0} | {1} | {2}'.format(type_grade20, size20, length20)
            order_quantity20 = form.cleaned_data['order_quantity20']
            if unique_product20 == "---- | ---- | ----":
                product20_db = True
            else:
                product20_db = product.objects.filter(unique_product=unique_product20).exists()

            if (order_quantity1 > 0 and (type_grade1 == "----" or size1 == "----" or length1 == "----")) \
                        or (order_quantity2 > 0 and (type_grade2 == "----" or size2 == "----" or length2 == "----")) \
                        or (order_quantity3 > 0 and (type_grade3 == "----" or size3 == "----" or length3 == "----")) \
                        or (order_quantity4 > 0 and (type_grade4 == "----" or size4 == "----" or length4 == "----")) \
                        or (order_quantity5 > 0 and (type_grade5 == "----" or size5 == "----" or length5 == "----")) \
                        or (order_quantity6 > 0 and (type_grade6 == "----" or size6 == "----" or length6 == "----")) \
                        or (order_quantity7 > 0 and (type_grade7 == "----" or size7 == "----" or length7 == "----")) \
                        or (order_quantity8 > 0 and (type_grade8 == "----" or size8 == "----" or length8 == "----")) \
                        or (order_quantity9 > 0 and (type_grade9 == "----" or size9 == "----" or length9 == "----")) \
                        or (order_quantity10 > 0 and (type_grade10 == "----" or size10 == "----" or length10 == "----")) \
                        or (order_quantity11 > 0 and (type_grade11 == "----" or size11 == "----" or length11 == "----")) \
                        or (order_quantity12 > 0 and (type_grade12 == "----" or size12 == "----" or length12 == "----")) \
                        or (order_quantity13 > 0 and (type_grade13 == "----" or size13 == "----" or length13 == "----")) \
                        or (order_quantity14 > 0 and (type_grade14 == "----" or size14 == "----" or length14 == "----")) \
                        or (order_quantity15 > 0 and (type_grade15 == "----" or size15 == "----" or length15 == "----")) \
                        or (order_quantity16 > 0 and (type_grade16 == "----" or size16 == "----" or length16 == "----")) \
                        or (order_quantity17 > 0 and (type_grade17 == "----" or size17 == "----" or length17 == "----")) \
                        or (order_quantity18 > 0 and (type_grade18 == "----" or size18 == "----" or length18 == "----")) \
                        or (order_quantity19 > 0 and (type_grade19 == "----" or size19 == "----" or length19 == "----")) \
                        or (order_quantity20 > 0 and (type_grade20 == "----" or size20 == "----" or length20 == "----")):

                messages.info(request,
                              'All orders with quantity greater than 0 must be associated with a product.',
                              extra_tags='warning')
                context = {
                    'form': form,
                }
                return render(request, 'inventory_management/purchase_order.html', context)


            elif product1_db == False or product2_db == False or product3_db == False or product4_db == False or \
                product5_db == False or product6_db == False or product7_db == False or product8_db == False or \
                product9_db == False or product10_db == False or product11_db == False or product12_db == False or \
                product13_db == False or product14_db == False or product15_db == False or product16_db == False or \
                product17_db == False or product18_db == False or product19_db == False or product20_db == False:
                if product1_db == False:
                    messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product1),
                                  extra_tags='exist1')
                if product2_db == False:
                    messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product2),
                                  extra_tags='exist2')
                if product3_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product3),
                                  extra_tags='exist3')
                if product4_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product4),
                                  extra_tags='exist4')
                if product5_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product5),
                                  extra_tags='exist5')
                if product6_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product6),
                                  extra_tags='exist6')
                if product7_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product7),
                                  extra_tags='exist7')
                if product8_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product8),
                                  extra_tags='exist8')
                if product9_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product9),
                                  extra_tags='exist9')
                if product10_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product10),
                                  extra_tags='exist_10')
                if product11_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product11),
                                  extra_tags='exist_11')
                if product12_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product12),
                                  extra_tags='exist_12')
                if product13_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product13),
                                  extra_tags='exist_13')
                if product14_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product14),
                                  extra_tags='exist_14')
                if product15_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product15),
                                  extra_tags='exist_15')
                if product16_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product16),
                                  extra_tags='exist_16')
                if product17_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product17),
                                  extra_tags='exist_17')
                if product18_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product18),
                                  extra_tags='exist_18')
                if product19_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product19),
                                  extra_tags='exist_19')
                if product20_db == False:
                   messages.info(request,'Product "{0}" does not exist. Contact administrator to add product to inventory.'.format(
                                      unique_product20),
                                  extra_tags='exist_20')
                context = {
                    'form': form,
                }
                return render(request, 'inventory_management/purchase_order.html', context)

            else:
                if unique_product1 == "---- | ---- | ----":
                    unique_product1 = None
                    order_quantity1 = None
                else:
                    product1_db = product.objects.get(unique_product=unique_product1)
                    product1_db.total_quantity = F('total_quantity') + order_quantity1
                    product1_db.save()

                if unique_product2 == "---- | ---- | ----":
                    unique_product2= None
                    order_quantity2= None
                else:
                    product2_db = product.objects.get(unique_product=unique_product2)
                    product2_db.total_quantity = F('total_quantity') + order_quantity2
                    product2_db.save()

                if unique_product3 == "---- | ---- | ----":
                    unique_product3= None
                    order_quantity3= None
                else:
                    product3_db = product.objects.get(unique_product=unique_product3)
                    product3_db.total_quantity = F('total_quantity') + order_quantity3
                    product3_db.save()

                if unique_product4 == "---- | ---- | ----":
                    unique_product4= None
                    order_quantity4= None
                else:
                    product4_db = product.objects.get(unique_product=unique_product4)
                    product4_db.total_quantity = F('total_quantity') + order_quantity4
                    product4_db.save()

                if unique_product5 == "---- | ---- | ----":
                    unique_product5= None
                    order_quantity5= None
                else:
                    product5_db = product.objects.get(unique_product=unique_product5)
                    product5_db.total_quantity = F('total_quantity') + order_quantity5
                    product5_db.save()

                if unique_product6 == "---- | ---- | ----":
                    unique_product6= None
                    order_quantity6= None
                else:
                    product6_db = product.objects.get(unique_product=unique_product6)
                    product6_db.total_quantity = F('total_quantity') + order_quantity6
                    product6_db.save()

                if unique_product7 == "---- | ---- | ----":
                    unique_product7= None
                    order_quantity7= None
                else:
                    product7_db = product.objects.get(unique_product=unique_product7)
                    product7_db.total_quantity = F('total_quantity') + order_quantity7
                    product7_db.save()

                if unique_product8 == "---- | ---- | ----":
                    unique_product8= None
                    order_quantity8= None
                else:
                    product8_db = product.objects.get(unique_product=unique_product8)
                    product8_db.total_quantity = F('total_quantity') + order_quantity8
                    product8_db.save()

                if unique_product9 == "---- | ---- | ----":
                    unique_product9= None
                    order_quantity9= None
                else:
                    product9_db = product.objects.get(unique_product=unique_product9)
                    product9_db.total_quantity = F('total_quantity') + order_quantity9
                    product9_db.save()

                if unique_product10 == "---- | ---- | ----":
                    unique_product10= None
                    order_quantity10= None
                else:
                    product10_db = product.objects.get(unique_product=unique_product10)
                    product10_db.total_quantity = F('total_quantity') + order_quantity10
                    product10_db.save()

                if unique_product11 == "---- | ---- | ----":
                    unique_product11= None
                    order_quantity11= None
                else:
                    product11_db = product.objects.get(unique_product=unique_product11)
                    product11_db.total_quantity = F('total_quantity') + order_quantity11
                    product11_db.save()

                if unique_product12 == "---- | ---- | ----":
                    unique_product12= None
                    order_quantity12= None
                else:
                    product12_db = product.objects.get(unique_product=unique_product12)
                    product12_db.total_quantity = F('total_quantity') + order_quantity12
                    product12_db.save()

                if unique_product13 == "---- | ---- | ----":
                    unique_product13= None
                    order_quantity13= None
                else:
                    product13_db = product.objects.get(unique_product=unique_product13)
                    product13_db.total_quantity = F('total_quantity') + order_quantity13
                    product13_db.save()

                if unique_product14 == "---- | ---- | ----":
                    unique_product14= None
                    order_quantity14= None
                else:
                    product14_db = product.objects.get(unique_product=unique_product14)
                    product14_db.total_quantity = F('total_quantity') + order_quantity14
                    product14_db.save()

                if unique_product15 == "---- | ---- | ----":
                    unique_product15= None
                    order_quantity15= None
                else:
                    product15_db = product.objects.get(unique_product=unique_product15)
                    product15_db.total_quantity = F('total_quantity') + order_quantity15
                    product15_db.save()

                if unique_product16 == "---- | ---- | ----":
                    unique_product16= None
                    order_quantity16= None
                else:
                    product16_db = product.objects.get(unique_product=unique_product16)
                    product16_db.total_quantity = F('total_quantity') + order_quantity16
                    product16_db.save()

                if unique_product17 == "---- | ---- | ----":
                    unique_product17= None
                    order_quantity17= None
                else:
                    product17_db = product.objects.get(unique_product=unique_product17)
                    product17_db.total_quantity = F('total_quantity') + order_quantity17
                    product17_db.save()

                if unique_product18 == "---- | ---- | ----":
                    unique_product18= None
                    order_quantity18= None
                else:
                    product18_db = product.objects.get(unique_product=unique_product18)
                    product18_db.total_quantity = F('total_quantity') + order_quantity18
                    product18_db.save()

                if unique_product19 == "---- | ---- | ----":
                    unique_product19= None
                    order_quantity19= None
                else:
                    product19_db = product.objects.get(unique_product=unique_product19)
                    product19_db.total_quantity = F('total_quantity') + order_quantity19
                    product19_db.save()

                if unique_product20 == "---- | ---- | ----":
                    unique_product20= None
                    order_quantity20= None
                else:
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
        form = inventory_adjustment_form(request.POST,initial={'unique_product1':update_item})
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

            type_grade1 = form.cleaned_data['type_grade1']
            size1 = form.cleaned_data['size1']
            length1 = form.cleaned_data['length1']
            unique_product1 = '{0} | {1} | {2}'.format(type_grade1, size1, length1)
            order_quantity1 = form.cleaned_data['order_quantity1']
            if unique_product1 == "---- | ---- | ----":
                product1_db = True
            else:
                product1_db = product.objects.filter(unique_product=unique_product1).exists()

            so_type_grade1 = form.cleaned_data['so_type_grade1']
            so_size1 = form.cleaned_data['so_size1']
            so_length1 = form.cleaned_data['so_length1']
            so_unique_product1 = '{0} | {1} | {2}'.format(so_type_grade1, so_size1, so_length1)
            so_order_quantity1 = form.cleaned_data['so_order_quantity1']
            if so_unique_product1 == "---- | ---- | ----":
                so_product1_db = True
            else:
                so_product1_db = product.objects.filter(unique_product=so_unique_product1).exists()

            type_grade2 = form.cleaned_data['type_grade2']
            size2 = form.cleaned_data['size2']
            length2 = form.cleaned_data['length2']
            unique_product2 = '{0} | {1} | {2}'.format(type_grade2, size2, length2)
            order_quantity2 = form.cleaned_data['order_quantity2']
            if unique_product2 == "---- | ---- | ----":
                product2_db = True
            else:
                product2_db = product.objects.filter(unique_product=unique_product2).exists()

            so_type_grade2 = form.cleaned_data['so_type_grade2']
            so_size2 = form.cleaned_data['so_size2']
            so_length2 = form.cleaned_data['so_length2']
            so_unique_product2 = '{0} | {1} | {2}'.format(so_type_grade2, so_size2, so_length2)
            so_order_quantity2 = form.cleaned_data['so_order_quantity2']
            print(so_unique_product2)
            if so_unique_product2 == "---- | ---- | ----":
                so_product2_db = True
            else:
                so_product2_db = product.objects.filter(unique_product=so_unique_product2).exists()

            type_grade3 = form.cleaned_data['type_grade3']
            size3 = form.cleaned_data['size3']
            length3 = form.cleaned_data['length3']
            unique_product3 = '{0} | {1} | {2}'.format(type_grade3, size3, length3)
            order_quantity3 = form.cleaned_data['order_quantity3']
            if unique_product3 == "---- | ---- | ----":
                product3_db = True
            else:
                product3_db = product.objects.filter(unique_product=unique_product3).exists()

            so_type_grade3 = form.cleaned_data['so_type_grade3']
            so_size3 = form.cleaned_data['so_size3']
            so_length3 = form.cleaned_data['so_length3']
            so_unique_product3 = '{0} | {1} | {2}'.format(so_type_grade3, so_size3, so_length3)
            so_order_quantity3 = form.cleaned_data['so_order_quantity3']
            if so_unique_product3 == "---- | ---- | ----":
                so_product3_db = True
            else:
                so_product3_db = product.objects.filter(unique_product=so_unique_product3).exists()

            type_grade4 = form.cleaned_data['type_grade4']
            size4 = form.cleaned_data['size4']
            length4 = form.cleaned_data['length4']
            unique_product4 = '{0} | {1} | {2}'.format(type_grade4, size4, length4)
            order_quantity4 = form.cleaned_data['order_quantity4']
            if unique_product4 == "---- | ---- | ----":
                product4_db = True
            else:
                product4_db = product.objects.filter(unique_product=unique_product4).exists()

            so_type_grade4 = form.cleaned_data['so_type_grade4']
            so_size4 = form.cleaned_data['so_size4']
            so_length4 = form.cleaned_data['so_length4']
            so_unique_product4 = '{0} | {1} | {2}'.format(so_type_grade4, so_size4, so_length4)
            so_order_quantity4 = form.cleaned_data['so_order_quantity4']
            if so_unique_product4 == "---- | ---- | ----":
                so_product4_db = True
            else:
                so_product4_db = product.objects.filter(unique_product=so_unique_product4).exists()

            type_grade5 = form.cleaned_data['type_grade5']
            size5 = form.cleaned_data['size5']
            length5 = form.cleaned_data['length5']
            unique_product5 = '{0} | {1} | {2}'.format(type_grade5, size5, length5)
            order_quantity5 = form.cleaned_data['order_quantity5']
            if unique_product5 == "---- | ---- | ----":
                product5_db = True
            else:
                product5_db = product.objects.filter(unique_product=unique_product5).exists()

            so_type_grade5 = form.cleaned_data['so_type_grade5']
            so_size5 = form.cleaned_data['so_size5']
            so_length5 = form.cleaned_data['so_length5']
            so_unique_product5 = '{0} | {1} | {2}'.format(so_type_grade5, so_size5, so_length5)
            so_order_quantity5 = form.cleaned_data['so_order_quantity5']
            if so_unique_product5 == "---- | ---- | ----":
                so_product5_db = True
            else:
                so_product5_db = product.objects.filter(unique_product=so_unique_product5).exists()

            type_grade6 = form.cleaned_data['type_grade6']
            size6 = form.cleaned_data['size6']
            length6 = form.cleaned_data['length6']
            unique_product6 = '{0} | {1} | {2}'.format(type_grade6, size6, length6)
            order_quantity6 = form.cleaned_data['order_quantity6']
            if unique_product6 == "---- | ---- | ----":
                product6_db = True
            else:
                product6_db = product.objects.filter(unique_product=unique_product6).exists()

            so_type_grade6 = form.cleaned_data['so_type_grade6']
            so_size6 = form.cleaned_data['so_size6']
            so_length6 = form.cleaned_data['so_length6']
            so_unique_product6 = '{0} | {1} | {2}'.format(so_type_grade6, so_size6, so_length6)
            so_order_quantity6 = form.cleaned_data['so_order_quantity6']
            if so_unique_product6 == "---- | ---- | ----":
                so_product6_db = True
            else:
                so_product6_db = product.objects.filter(unique_product=so_unique_product6).exists()

            type_grade7 = form.cleaned_data['type_grade7']
            size7 = form.cleaned_data['size7']
            length7 = form.cleaned_data['length7']
            unique_product7 = '{0} | {1} | {2}'.format(type_grade7, size7, length7)
            order_quantity7 = form.cleaned_data['order_quantity7']
            if unique_product7 == "---- | ---- | ----":
                product7_db = True
            else:
                product7_db = product.objects.filter(unique_product=unique_product7).exists()

            so_type_grade7 = form.cleaned_data['so_type_grade7']
            so_size7 = form.cleaned_data['so_size7']
            so_length7 = form.cleaned_data['so_length7']
            so_unique_product7 = '{0} | {1} | {2}'.format(so_type_grade7, so_size7, so_length7)
            so_order_quantity7 = form.cleaned_data['so_order_quantity7']
            if so_unique_product7 == "---- | ---- | ----":
                so_product7_db = True
            else:
                so_product7_db = product.objects.filter(unique_product=so_unique_product7).exists()

            type_grade8 = form.cleaned_data['type_grade8']
            size8 = form.cleaned_data['size8']
            length8 = form.cleaned_data['length8']
            unique_product8 = '{0} | {1} | {2}'.format(type_grade8, size8, length8)
            order_quantity8 = form.cleaned_data['order_quantity8']
            if unique_product8 == "---- | ---- | ----":
                product8_db = True
            else:
                product8_db = product.objects.filter(unique_product=unique_product8).exists()

            so_type_grade8 = form.cleaned_data['so_type_grade8']
            so_size8 = form.cleaned_data['so_size8']
            so_length8 = form.cleaned_data['so_length8']
            so_unique_product8 = '{0} | {1} | {2}'.format(so_type_grade8, so_size8, so_length8)
            so_order_quantity8 = form.cleaned_data['so_order_quantity8']
            if so_unique_product8 == "---- | ---- | ----":
                so_product8_db = True
            else:
                so_product8_db = product.objects.filter(unique_product=so_unique_product8).exists()

            type_grade9 = form.cleaned_data['type_grade9']
            size9 = form.cleaned_data['size9']
            length9 = form.cleaned_data['length9']
            unique_product9 = '{0} | {1} | {2}'.format(type_grade9, size9, length9)
            order_quantity9 = form.cleaned_data['order_quantity9']
            if unique_product9 == "---- | ---- | ----":
                product9_db = True
            else:
                product9_db = product.objects.filter(unique_product=unique_product9).exists()

            so_type_grade9 = form.cleaned_data['so_type_grade9']
            so_size9 = form.cleaned_data['so_size9']
            so_length9 = form.cleaned_data['so_length9']
            so_unique_product9 = '{0} | {1} | {2}'.format(so_type_grade9, so_size9, so_length9)
            so_order_quantity9 = form.cleaned_data['so_order_quantity9']
            if so_unique_product9 == "---- | ---- | ----":
                so_product9_db = True
            else:
                so_product9_db = product.objects.filter(unique_product=so_unique_product9).exists()

            type_grade10 = form.cleaned_data['type_grade10']
            size10 = form.cleaned_data['size10']
            length10 = form.cleaned_data['length10']
            unique_product10 = '{0} | {1} | {2}'.format(type_grade10, size10, length10)
            order_quantity10 = form.cleaned_data['order_quantity10']
            if unique_product10 == "---- | ---- | ----":
                product10_db = True
            else:
                product10_db = product.objects.filter(unique_product=unique_product10).exists()

            so_type_grade10 = form.cleaned_data['so_type_grade10']
            so_size10 = form.cleaned_data['so_size10']
            so_length10 = form.cleaned_data['so_length10']
            so_unique_product10 = '{0} | {1} | {2}'.format(so_type_grade10, so_size10, so_length10)
            so_order_quantity10 = form.cleaned_data['so_order_quantity10']
            if so_unique_product10 == "---- | ---- | ----":
                so_product10_db = True
            else:
                so_product10_db = product.objects.filter(unique_product=so_unique_product10).exists()

            type_grade11 = form.cleaned_data['type_grade11']
            size11 = form.cleaned_data['size11']
            length11 = form.cleaned_data['length11']
            unique_product11 = '{0} | {1} | {2}'.format(type_grade11, size11, length11)
            order_quantity11 = form.cleaned_data['order_quantity11']
            if unique_product11 == "---- | ---- | ----":
                product11_db = True
            else:
                product11_db = product.objects.filter(unique_product=unique_product11).exists()

            so_type_grade11 = form.cleaned_data['so_type_grade11']
            so_size11 = form.cleaned_data['so_size11']
            so_length11 = form.cleaned_data['so_length11']
            so_unique_product11 = '{0} | {1} | {2}'.format(so_type_grade11, so_size11, so_length11)
            so_order_quantity11 = form.cleaned_data['so_order_quantity11']
            if so_unique_product11 == "---- | ---- | ----":
                so_product11_db = True
            else:
                so_product11_db = product.objects.filter(unique_product=so_unique_product11).exists()

            type_grade12 = form.cleaned_data['type_grade12']
            size12 = form.cleaned_data['size12']
            length12 = form.cleaned_data['length12']
            unique_product12 = '{0} | {1} | {2}'.format(type_grade12, size12, length12)
            order_quantity12 = form.cleaned_data['order_quantity12']
            if unique_product12 == "---- | ---- | ----":
                product12_db = True
            else:
                product12_db = product.objects.filter(unique_product=unique_product12).exists()

            so_type_grade12 = form.cleaned_data['so_type_grade12']
            so_size12 = form.cleaned_data['so_size12']
            so_length12 = form.cleaned_data['so_length12']
            so_unique_product12 = '{0} | {1} | {2}'.format(so_type_grade12, so_size12, so_length12)
            so_order_quantity12 = form.cleaned_data['so_order_quantity12']
            if so_unique_product12 == "---- | ---- | ----":
                so_product12_db = True
            else:
                so_product12_db = product.objects.filter(unique_product=so_unique_product12).exists()

            type_grade13 = form.cleaned_data['type_grade13']
            size13 = form.cleaned_data['size13']
            length13 = form.cleaned_data['length13']
            unique_product13 = '{0} | {1} | {2}'.format(type_grade13, size13, length13)
            order_quantity13 = form.cleaned_data['order_quantity13']
            if unique_product13 == "---- | ---- | ----":
                product13_db = True
            else:
                product13_db = product.objects.filter(unique_product=unique_product13).exists()

            so_type_grade13 = form.cleaned_data['so_type_grade13']
            so_size13 = form.cleaned_data['so_size13']
            so_length13 = form.cleaned_data['so_length13']
            so_unique_product13 = '{0} | {1} | {2}'.format(so_type_grade13, so_size13, so_length13)
            so_order_quantity13 = form.cleaned_data['so_order_quantity13']
            if so_unique_product13 == "---- | ---- | ----":
                so_product13_db = True
            else:
                so_product13_db = product.objects.filter(unique_product=so_unique_product13).exists()

            type_grade14 = form.cleaned_data['type_grade14']
            size14 = form.cleaned_data['size14']
            length14 = form.cleaned_data['length14']
            unique_product14 = '{0} | {1} | {2}'.format(type_grade14, size14, length14)
            order_quantity14 = form.cleaned_data['order_quantity14']
            if unique_product14 == "---- | ---- | ----":
                product14_db = True
            else:
                product14_db = product.objects.filter(unique_product=unique_product14).exists()

            so_type_grade14 = form.cleaned_data['so_type_grade14']
            so_size14 = form.cleaned_data['so_size14']
            so_length14 = form.cleaned_data['so_length14']
            so_unique_product14 = '{0} | {1} | {2}'.format(so_type_grade14, so_size14, so_length14)
            so_order_quantity14 = form.cleaned_data['so_order_quantity14']
            if so_unique_product14 == "---- | ---- | ----":
                so_product14_db = True
            else:
                so_product14_db = product.objects.filter(unique_product=so_unique_product14).exists()

            type_grade15 = form.cleaned_data['type_grade15']
            size15 = form.cleaned_data['size15']
            length15 = form.cleaned_data['length15']
            unique_product15 = '{0} | {1} | {2}'.format(type_grade15, size15, length15)
            order_quantity15 = form.cleaned_data['order_quantity15']
            if unique_product15 == "---- | ---- | ----":
                product15_db = True
            else:
                product15_db = product.objects.filter(unique_product=unique_product15).exists()

            so_type_grade15 = form.cleaned_data['so_type_grade15']
            so_size15 = form.cleaned_data['so_size15']
            so_length15 = form.cleaned_data['so_length15']
            so_unique_product15 = '{0} | {1} | {2}'.format(so_type_grade15, so_size15, so_length15)
            so_order_quantity15 = form.cleaned_data['so_order_quantity15']
            if so_unique_product15 == "---- | ---- | ----":
                so_product15_db = True
            else:
                so_product15_db = product.objects.filter(unique_product=so_unique_product15).exists()

            type_grade16 = form.cleaned_data['type_grade16']
            size16 = form.cleaned_data['size16']
            length16 = form.cleaned_data['length16']
            unique_product16 = '{0} | {1} | {2}'.format(type_grade16, size16, length16)
            order_quantity16 = form.cleaned_data['order_quantity16']
            if unique_product16 == "---- | ---- | ----":
                product16_db = True
            else:
                product16_db = product.objects.filter(unique_product=unique_product16).exists()

            so_type_grade16 = form.cleaned_data['so_type_grade16']
            so_size16 = form.cleaned_data['so_size16']
            so_length16 = form.cleaned_data['so_length16']
            so_unique_product16 = '{0} | {1} | {2}'.format(so_type_grade16, so_size16, so_length16)
            so_order_quantity16 = form.cleaned_data['so_order_quantity16']
            if so_unique_product16 == "---- | ---- | ----":
                so_product16_db = True
            else:
                so_product16_db = product.objects.filter(unique_product=so_unique_product16).exists()

            type_grade17 = form.cleaned_data['type_grade17']
            size17 = form.cleaned_data['size17']
            length17 = form.cleaned_data['length17']
            unique_product17 = '{0} | {1} | {2}'.format(type_grade17, size17, length17)
            order_quantity17 = form.cleaned_data['order_quantity17']
            if unique_product17 == "---- | ---- | ----":
                product17_db = True
            else:
                product17_db = product.objects.filter(unique_product=unique_product17).exists()

            so_type_grade17 = form.cleaned_data['so_type_grade17']
            so_size17 = form.cleaned_data['so_size17']
            so_length17 = form.cleaned_data['so_length17']
            so_unique_product17 = '{0} | {1} | {2}'.format(so_type_grade17, so_size17, so_length17)
            so_order_quantity17 = form.cleaned_data['so_order_quantity17']
            if so_unique_product17 == "---- | ---- | ----":
                so_product17_db = True
            else:
                so_product17_db = product.objects.filter(unique_product=so_unique_product17).exists()

            type_grade18 = form.cleaned_data['type_grade18']
            size18 = form.cleaned_data['size18']
            length18 = form.cleaned_data['length18']
            unique_product18 = '{0} | {1} | {2}'.format(type_grade18, size18, length18)
            order_quantity18 = form.cleaned_data['order_quantity18']
            if unique_product18 == "---- | ---- | ----":
                product18_db = True
            else:
                product18_db = product.objects.filter(unique_product=unique_product18).exists()

            so_type_grade18 = form.cleaned_data['so_type_grade18']
            so_size18 = form.cleaned_data['so_size18']
            so_length18 = form.cleaned_data['so_length18']
            so_unique_product18 = '{0} | {1} | {2}'.format(so_type_grade18, so_size18, so_length18)
            so_order_quantity18 = form.cleaned_data['so_order_quantity18']
            if so_unique_product18 == "---- | ---- | ----":
                so_product18_db = True
            else:
                so_product18_db = product.objects.filter(unique_product=so_unique_product18).exists()

            type_grade19 = form.cleaned_data['type_grade19']
            size19 = form.cleaned_data['size19']
            length19 = form.cleaned_data['length19']
            unique_product19 = '{0} | {1} | {2}'.format(type_grade19, size19, length19)
            order_quantity19 = form.cleaned_data['order_quantity19']
            if unique_product19 == "---- | ---- | ----":
                product19_db = True
            else:
                product19_db = product.objects.filter(unique_product=unique_product19).exists()

            so_type_grade19 = form.cleaned_data['so_type_grade19']
            so_size19 = form.cleaned_data['so_size19']
            so_length19 = form.cleaned_data['so_length19']
            so_unique_product19 = '{0} | {1} | {2}'.format(so_type_grade19, so_size19, so_length19)
            so_order_quantity19 = form.cleaned_data['so_order_quantity19']
            if so_unique_product19 == "---- | ---- | ----":
                so_product19_db = True
            else:
                so_product19_db = product.objects.filter(unique_product=so_unique_product19).exists()

            type_grade20 = form.cleaned_data['type_grade20']
            size20 = form.cleaned_data['size20']
            length20 = form.cleaned_data['length20']
            unique_product20 = '{0} | {1} | {2}'.format(type_grade20, size20, length20)
            order_quantity20 = form.cleaned_data['order_quantity20']
            if unique_product20 == "---- | ---- | ----":
                product20_db = True
            else:
                product20_db = product.objects.filter(unique_product=unique_product20).exists()

            so_type_grade20 = form.cleaned_data['so_type_grade20']
            so_size20 = form.cleaned_data['so_size20']
            so_length20 = form.cleaned_data['so_length20']
            so_unique_product20 = '{0} | {1} | {2}'.format(so_type_grade20, so_size20, so_length20)
            so_order_quantity20 = form.cleaned_data['so_order_quantity20']
            if so_unique_product20 == "---- | ---- | ----":
                so_product20_db = True
            else:
                so_product20_db = product.objects.filter(unique_product=so_unique_product20).exists()

            #############################################################################################################
            if (order_quantity1 > 0 and (type_grade1 == "----" or size1 == "----" or length1 == "----")) \
                or (so_order_quantity1 > 0 and (so_type_grade1 == "----" or so_size1 == "----" or so_length1 == "----")) \
                or (order_quantity1 > 0 and so_order_quantity1 == 0) or (order_quantity1 == 0 and so_order_quantity1 > 0) \
                or (order_quantity2 > 0 and (type_grade2 == "----" or size2 == "----" or length2 == "----")) \
                or (so_order_quantity2 > 0 and (so_type_grade2 == "----" or so_size2 == "----" or so_length2 == "----")) \
                or (order_quantity2 > 0 and so_order_quantity2 == 0) or (order_quantity2 == 0 and so_order_quantity2 > 0) \
                or (order_quantity3 > 0 and (type_grade3 == "----" or size3 == "----" or length3 == "----")) \
                or (so_order_quantity3 > 0 and (so_type_grade3 == "----" or so_size3 == "----" or so_length3 == "----")) \
                or (order_quantity3 > 0 and so_order_quantity3 == 0) or (order_quantity3 == 0 and so_order_quantity3 > 0) \
                or (order_quantity4 > 0 and (type_grade4 == "----" or size4 == "----" or length4 == "----")) \
                or (so_order_quantity4 > 0 and (so_type_grade4 == "----" or so_size4 == "----" or so_length4 == "----")) \
                or (order_quantity4 > 0 and so_order_quantity4 == 0) or (order_quantity4 == 0 and so_order_quantity4 > 0) \
                or (order_quantity5 > 0 and (type_grade5 == "----" or size5 == "----" or length5 == "----")) \
                or (so_order_quantity5 > 0 and (so_type_grade5 == "----" or so_size5 == "----" or so_length5 == "----")) \
                or (order_quantity5 > 0 and so_order_quantity5 == 0) or (order_quantity5 == 0 and so_order_quantity5 > 0) \
                or (order_quantity6 > 0 and (type_grade6 == "----" or size6 == "----" or length6 == "----")) \
                or (so_order_quantity6 > 0 and (so_type_grade6 == "----" or so_size6 == "----" or so_length6 == "----")) \
                or (order_quantity6 > 0 and so_order_quantity6 == 0) or (order_quantity6 == 0 and so_order_quantity6 > 0) \
                or (order_quantity7 > 0 and (type_grade7 == "----" or size7 == "----" or length7 == "----")) \
                or (so_order_quantity7 > 0 and (so_type_grade7 == "----" or so_size7 == "----" or so_length7 == "----")) \
                or (order_quantity7 > 0 and so_order_quantity7 == 0) or (order_quantity7 == 0 and so_order_quantity7 > 0) \
                or (order_quantity8 > 0 and (type_grade8 == "----" or size8 == "----" or length8 == "----")) \
                or (so_order_quantity8 > 0 and (so_type_grade8 == "----" or so_size8 == "----" or so_length8 == "----")) \
                or (order_quantity8 > 0 and so_order_quantity8 == 0) or (order_quantity8 == 0 and so_order_quantity8 > 0) \
                or (order_quantity9 > 0 and (type_grade9 == "----" or size9 == "----" or length9 == "----")) \
                or (so_order_quantity9 > 0 and (so_type_grade9 == "----" or so_size9 == "----" or so_length9 == "----")) \
                or (order_quantity9 > 0 and so_order_quantity9 == 0) or (order_quantity9 == 0 and so_order_quantity9 > 0) \
                or (order_quantity10 > 0 and (type_grade10 == "----" or size10 == "----" or length10 == "----")) \
                or (so_order_quantity10 > 0 and (so_type_grade10 == "----" or so_size10 == "----" or so_length10 == "----")) \
                or (order_quantity10 > 0 and so_order_quantity10 == 0) or (order_quantity10 == 0 and so_order_quantity10 > 0) \
                or (order_quantity11 > 0 and (type_grade11 == "----" or size11 == "----" or length11 == "----")) \
                or (so_order_quantity11 > 0 and (so_type_grade11 == "----" or so_size11 == "----" or so_length11 == "----")) \
                or (order_quantity11 > 0 and so_order_quantity11 == 0) or (order_quantity11 == 0 and so_order_quantity11 > 0) \
                or (order_quantity12 > 0 and (type_grade12 == "----" or size12 == "----" or length12 == "----")) \
                or (so_order_quantity12 > 0 and (so_type_grade12 == "----" or so_size12 == "----" or so_length12 == "----")) \
                or (order_quantity12 > 0 and so_order_quantity12 == 0) or (order_quantity12 == 0 and so_order_quantity12 > 0) \
                or (order_quantity13 > 0 and (type_grade13 == "----" or size13 == "----" or length13 == "----")) \
                or (so_order_quantity13 > 0 and (so_type_grade13 == "----" or so_size13 == "----" or so_length13 == "----")) \
                or (order_quantity13 > 0 and so_order_quantity13 == 0) or (order_quantity13 == 0 and so_order_quantity13 > 0) \
                or (order_quantity14 > 0 and (type_grade14 == "----" or size14 == "----" or length14 == "----")) \
                or (so_order_quantity14 > 0 and (so_type_grade14 == "----" or so_size14 == "----" or so_length14 == "----")) \
                or (order_quantity14 > 0 and so_order_quantity14 == 0) or (order_quantity14 == 0 and so_order_quantity14 > 0) \
                or (order_quantity15 > 0 and (type_grade15 == "----" or size15 == "----" or length15 == "----")) \
                or (so_order_quantity15 > 0 and (so_type_grade15 == "----" or so_size15 == "----" or so_length15 == "----")) \
                or (order_quantity15 > 0 and so_order_quantity15 == 0) or (order_quantity15 == 0 and so_order_quantity15 > 0) \
                or (order_quantity16 > 0 and (type_grade16 == "----" or size16 == "----" or length16 == "----")) \
                or (so_order_quantity16 > 0 and (so_type_grade16 == "----" or so_size16 == "----" or so_length16 == "----")) \
                or (order_quantity16 > 0 and so_order_quantity16 == 0) or (order_quantity16 == 0 and so_order_quantity16 > 0) \
                or (order_quantity17 > 0 and (type_grade17 == "----" or size17 == "----" or length17 == "----")) \
                or (so_order_quantity17 > 0 and (so_type_grade17 == "----" or so_size17 == "----" or so_length17 == "----")) \
                or (order_quantity17 > 0 and so_order_quantity17 == 0) or (order_quantity17 == 0 and so_order_quantity17 > 0) \
                or (order_quantity18 > 0 and (type_grade18 == "----" or size18 == "----" or length18 == "----")) \
                or (so_order_quantity18 > 0 and (so_type_grade18 == "----" or so_size18 == "----" or so_length18 == "----")) \
                or (order_quantity18 > 0 and so_order_quantity18 == 0) or (order_quantity18 == 0 and so_order_quantity18 > 0) \
                or (order_quantity19 > 0 and (type_grade19 == "----" or size19 == "----" or length19 == "----")) \
                or (so_order_quantity19 > 0 and (so_type_grade19 == "----" or so_size19 == "----" or so_length19 == "----")) \
                or (order_quantity19 > 0 and so_order_quantity19 == 0) or (order_quantity19 == 0 and so_order_quantity19 > 0) \
                or (order_quantity20 > 0 and (type_grade20 == "----" or size20 == "----" or length20 == "----")) \
                or (so_order_quantity20 > 0 and (so_type_grade20 == "----" or so_size20 == "----" or so_length20 == "----")) \
                or (order_quantity20 > 0 and so_order_quantity20 == 0) or (order_quantity20 == 0 and so_order_quantity20 > 0) :

                messages.info(request,
                              'All orders with quantity greater than 0 must be associated with a product. Also, if fulfillment quantity is greater than 0, then shipping quantity must be greater than 0, and vice versa.',
                              extra_tags="warning1")

                context = {
                    'form':form,
                }
                return render(request, 'inventory_management/sales_order.html', context)

            elif product1_db == False or so_product1_db == False or product2_db == False or so_product2_db == False or \
                    product3_db == False or so_product3_db == False or product4_db == False or so_product4_db == False or \
                    product5_db == False or so_product5_db == False or product6_db == False or so_product6_db == False or \
                    product7_db == False or so_product7_db == False or product8_db == False or so_product8_db == False or \
                    product9_db == False or so_product9_db == False or product10_db == False or so_product10_db == False or \
                    product11_db == False or so_product11_db == False or product12_db == False or so_product12_db == False or \
                    product13_db == False or so_product13_db == False or product14_db == False or so_product14_db == False or \
                    product15_db == False or so_product15_db == False or product16_db == False or so_product16_db == False or \
                    product17_db == False or so_product17_db == False or product18_db == False or so_product18_db == False or \
                    product19_db == False or so_product19_db == False or product20_db == False or so_product20_db == False:

                if product1_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product1), extra_tags='exist1')

                if so_product1_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product1), extra_tags='so_xist1')

                if product2_db == False:
                    messages.info(request,'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product2), extra_tags='exist2')

                if so_product2_db == False:
                    messages.info(request,'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product2), extra_tags='so_xist2')

                if product3_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product3), extra_tags='exist3')

                if so_product3_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product3), extra_tags='so_xist3')

                if product4_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product4), extra_tags='exist4')

                if so_product4_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product4), extra_tags='so_xist4')

                if product5_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product5), extra_tags='exist5')

                if so_product5_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product5), extra_tags='so_xist5')

                if product6_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product6), extra_tags='exist6')

                if so_product6_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product6), extra_tags='so_xist6')

                if product7_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product7), extra_tags='exist7')

                if so_product7_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product7), extra_tags='so_xist7')

                if product8_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product8), extra_tags='exist8')

                if so_product8_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product8), extra_tags='so_xist8')

                if product9_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product9), extra_tags='exist9')

                if so_product9_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product9), extra_tags='so_xist9')

                if product10_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product10), extra_tags='exist_10')

                if so_product10_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product10), extra_tags='so_xist_10')

                if product11_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product11), extra_tags='exist_11')

                if so_product11_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product11), extra_tags='so_xist_11')

                if product12_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product12), extra_tags='exist_12')

                if so_product12_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product12), extra_tags='so_xist_12')

                if product13_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product13), extra_tags='exist_13')

                if so_product13_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product13), extra_tags='so_xist_13')

                if product14_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product14), extra_tags='exist_14')

                if so_product14_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product14), extra_tags='so_xist_14')

                if product15_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product15), extra_tags='exist_15')

                if so_product15_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product15), extra_tags='so_xist_15')

                if product16_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product16), extra_tags='exist_16')

                if so_product16_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product16), extra_tags='so_xist_16')

                if product17_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product17), extra_tags='exist_17')

                if so_product17_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product17), extra_tags='so_xist_17')

                if product18_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product18), extra_tags='exist_18')

                if so_product18_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product18), extra_tags='so_xist_18')

                if product19_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product19), extra_tags='exist_19')

                if so_product19_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product19), extra_tags='so_xist_19')

                if product20_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(unique_product20), extra_tags='exist_20')

                if so_product20_db == False:
                    messages.info(request, 'Product "{0}" does not exist, Contact adminstrator to add product to inventory.'.format(so_unique_product1), extra_tags='so_xist20')

                context = {
                    'form': form,
                }
                return render(request, 'inventory_management/sales_order.html', context)

            else:
                if unique_product1 == "---- | ---- | ----" or  so_unique_product1 == "---- | ---- | ----":
                    unique_product1 = None
                    order_quantity1 = None
                    so_unique_product1 = None
                    so_order_quantity1 = None
                    total_quantity1 = None
                else:
                    total_quantity1 = product.objects.get(unique_product=unique_product1)
                    total_quantity1 = total_quantity1.total_quantity
                    total_quantity1 = total_quantity1 - order_quantity1

                if unique_product2 == "---- | ---- | ----" or  so_unique_product2 == "---- | ---- | ----":
                    unique_product2 = None
                    order_quantity2 = None
                    so_unique_product2 = None
                    so_order_quantity2 = None
                    total_quantity2 = None
                else:
                    total_quantity2 = product.objects.get(unique_product=unique_product2)
                    total_quantity2 = total_quantity2.total_quantity
                    total_quantity2 = total_quantity2 - order_quantity2

                if unique_product3 == "---- | ---- | ----" or  so_unique_product3 == "---- | ---- | ----":
                    unique_product3 = None
                    order_quantity3 = None
                    so_unique_product3 = None
                    so_order_quantity3 = None
                    total_quantity3 = None
                else:
                    total_quantity3 = product.objects.get(unique_product=unique_product3)
                    total_quantity3 = total_quantity3.total_quantity
                    total_quantity3 = total_quantity3 - order_quantity3

                if unique_product4 == "---- | ---- | ----" or  so_unique_product4 == "---- | ---- | ----":
                    unique_product4 = None
                    order_quantity4 = None
                    so_unique_product4 = None
                    so_order_quantity4 = None
                    total_quantity4 = None
                else:
                    total_quantity4 = product.objects.get(unique_product=unique_product4)
                    total_quantity4 = total_quantity4.total_quantity
                    total_quantity4 = total_quantity4 - order_quantity4

                if unique_product5 == "---- | ---- | ----" or  so_unique_product5 == "---- | ---- | ----":
                    unique_product5 = None
                    order_quantity5 = None
                    so_unique_product5 = None
                    so_order_quantity5 = None
                    total_quantity5 = None
                else:
                    total_quantity5 = product.objects.get(unique_product=unique_product5)
                    total_quantity5 = total_quantity5.total_quantity
                    total_quantity5 = total_quantity5 - order_quantity5

                if unique_product6 == "---- | ---- | ----" or  so_unique_product6 == "---- | ---- | ----":
                    unique_product6 = None
                    order_quantity6 = None
                    so_unique_product6 = None
                    so_order_quantity6 = None
                    total_quantity6 = None
                else:
                    total_quantity6 = product.objects.get(unique_product=unique_product6)
                    total_quantity6 = total_quantity6.total_quantity
                    total_quantity6 = total_quantity6 - order_quantity6

                if unique_product7 == "---- | ---- | ----" or  so_unique_product7 == "---- | ---- | ----":
                    unique_product7 = None
                    order_quantity7 = None
                    so_unique_product7 = None
                    so_order_quantity7 = None
                    total_quantity7 = None
                else:
                    total_quantity7 = product.objects.get(unique_product=unique_product7)
                    total_quantity7 = total_quantity7.total_quantity
                    total_quantity7 = total_quantity7 - order_quantity7

                if unique_product8 == "---- | ---- | ----" or  so_unique_product8 == "---- | ---- | ----":
                    unique_product8 = None
                    order_quantity8 = None
                    so_unique_product8 = None
                    so_order_quantity8 = None
                    total_quantity8 = None
                else:
                    total_quantity8 = product.objects.get(unique_product=unique_product8)
                    total_quantity8 = total_quantity8.total_quantity
                    total_quantity8 = total_quantity8 - order_quantity8

                if unique_product9 == "---- | ---- | ----" or  so_unique_product9 == "---- | ---- | ----":
                    unique_product9 = None
                    order_quantity9 = None
                    so_unique_product9 = None
                    so_order_quantity9 = None
                    total_quantity9 = None
                else:
                    total_quantity9 = product.objects.get(unique_product=unique_product9)
                    total_quantity9 = total_quantity9.total_quantity
                    total_quantity9 = total_quantity9 - order_quantity9

                if unique_product10 == "---- | ---- | ----" or  so_unique_product10 == "---- | ---- | ----":
                    unique_product10 = None
                    order_quantity10 = None
                    so_unique_product10 = None
                    so_order_quantity10 = None
                    total_quantity10 = None
                else:
                    total_quantity10 = product.objects.get(unique_product=unique_product10)
                    total_quantity10 = total_quantity10.total_quantity
                    total_quantity10 = total_quantity10 - order_quantity10

                if unique_product11 == "---- | ---- | ----" or  so_unique_product11 == "---- | ---- | ----":
                    unique_product11 = None
                    order_quantity11 = None
                    so_unique_product11 = None
                    so_order_quantity11 = None
                    total_quantity11 = None
                else:
                    total_quantity11 = product.objects.get(unique_product=unique_product11)
                    total_quantity11 = total_quantity11.total_quantity
                    total_quantity11 = total_quantity11 - order_quantity11

                if unique_product12 == "---- | ---- | ----" or  so_unique_product12 == "---- | ---- | ----":
                    unique_product12 = None
                    order_quantity12 = None
                    so_unique_product12 = None
                    so_order_quantity12 = None
                    total_quantity12 = None
                else:
                    total_quantity12 = product.objects.get(unique_product=unique_product12)
                    total_quantity12 = total_quantity12.total_quantity
                    total_quantity12 = total_quantity12 - order_quantity12

                if unique_product13 == "---- | ---- | ----" or  so_unique_product13 == "---- | ---- | ----":
                    unique_product13 = None
                    order_quantity13 = None
                    so_unique_product13 = None
                    so_order_quantity13 = None
                    total_quantity13 = None
                else:
                    total_quantity13 = product.objects.get(unique_product=unique_product13)
                    total_quantity13 = total_quantity13.total_quantity
                    total_quantity13 = total_quantity13 - order_quantity13

                if unique_product14 == "---- | ---- | ----" or  so_unique_product14 == "---- | ---- | ----":
                    unique_product14 = None
                    order_quantity14 = None
                    so_unique_product14 = None
                    so_order_quantity14 = None
                    total_quantity14 = None
                else:
                    total_quantity14 = product.objects.get(unique_product=unique_product14)
                    total_quantity14 = total_quantity14.total_quantity
                    total_quantity14 = total_quantity14 - order_quantity14

                if unique_product15 == "---- | ---- | ----" or  so_unique_product15 == "---- | ---- | ----":
                    unique_product15 = None
                    order_quantity15 = None
                    so_unique_product15 = None
                    so_order_quantity15 = None
                    total_quantity15 = None
                else:
                    total_quantity15 = product.objects.get(unique_product=unique_product15)
                    total_quantity15 = total_quantity15.total_quantity
                    total_quantity15 = total_quantity15 - order_quantity15

                if unique_product16 == "---- | ---- | ----" or  so_unique_product16 == "---- | ---- | ----":
                    unique_product16 = None
                    order_quantity16 = None
                    so_unique_product16 = None
                    so_order_quantity16 = None
                    total_quantity16 = None
                else:
                    total_quantity16 = product.objects.get(unique_product=unique_product16)
                    total_quantity16 = total_quantity16.total_quantity
                    total_quantity16 = total_quantity16 - order_quantity16

                if unique_product17 == "---- | ---- | ----" or  so_unique_product17 == "---- | ---- | ----":
                    unique_product17 = None
                    order_quantity17 = None
                    so_unique_product17 = None
                    so_order_quantity17 = None
                    total_quantity17 = None
                else:
                    total_quantity17 = product.objects.get(unique_product=unique_product17)
                    total_quantity17 = total_quantity17.total_quantity
                    total_quantity17 = total_quantity17 - order_quantity17

                if unique_product18 == "---- | ---- | ----" or  so_unique_product18 == "---- | ---- | ----":
                    unique_product18 = None
                    order_quantity18 = None
                    so_unique_product18 = None
                    so_order_quantity18 = None
                    total_quantity18 = None
                else:
                    total_quantity18 = product.objects.get(unique_product=unique_product18)
                    total_quantity18 = total_quantity18.total_quantity
                    total_quantity18 = total_quantity18 - order_quantity18

                if unique_product19 == "---- | ---- | ----" or  so_unique_product19 == "---- | ---- | ----":
                    unique_product19 = None
                    order_quantity19 = None
                    so_unique_product19 = None
                    so_order_quantity19 = None
                    total_quantity19 = None
                else:
                    total_quantity19 = product.objects.get(unique_product=unique_product19)
                    total_quantity19 = total_quantity19.total_quantity
                    total_quantity19 = total_quantity19 - order_quantity19

                if unique_product20 == "---- | ---- | ----" or  so_unique_product20 == "---- | ---- | ----":
                    unique_product20 = None
                    order_quantity20 = None
                    so_unique_product20 = None
                    so_order_quantity20 = None
                    total_quantity20 = None
                else:
                    total_quantity20 = product.objects.get(unique_product=unique_product20)
                    total_quantity20 = total_quantity20.total_quantity
                    total_quantity20 = total_quantity20 - order_quantity20

            #######################################################################
            if (total_quantity1 is None or total_quantity1 >= 0) and (total_quantity2 is None or total_quantity2 >= 0) \
                and (total_quantity3 is None or total_quantity3 >= 0) and (total_quantity4 is None or total_quantity4 >= 0) \
                and (total_quantity5 is None or total_quantity5 >= 0) and (total_quantity6 is None or total_quantity6 >= 0) \
                and (total_quantity7 is None or total_quantity7 >= 0) and (total_quantity8 is None or total_quantity8 >= 0) \
                and (total_quantity9 is None or total_quantity9 >= 0) and (total_quantity10 is None or total_quantity10 >= 0) \
                and (total_quantity11 is None or total_quantity11 >= 0) and (total_quantity12 is None or total_quantity12 >= 0) \
                and (total_quantity13 is None or total_quantity13 >= 0) and (total_quantity14 is None or total_quantity14 >= 0) \
                and (total_quantity15 is None or total_quantity15 >= 0) and (total_quantity16 is None or total_quantity16 >= 0) \
                and (total_quantity17 is None or total_quantity17 >= 0) and (total_quantity18 is None or total_quantity18 >= 0) \
                and (total_quantity19 is None or total_quantity19 >= 0) and (total_quantity20 is None or total_quantity20 >= 0) \
                or override == "Yes":

                if unique_product1 == None:
                    pass
                else:
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
                                              unique_product20=unique_product20, order_quantity20=order_quantity20,
                                              created_by=request.user.username, )
                db_insert.save()
                return redirect('inventory_management')
                ##########################################
            else:
                if total_quantity1 is None:
                    pass
                elif total_quantity1 < 0 :
                    messages.info(request, 'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product1, total_quantity1),
                                  extra_tags='unique_product1')

                if total_quantity2 is None:
                    pass
                elif total_quantity2 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product2, total_quantity2),
                                  extra_tags='unique_product2')

                if total_quantity3 is None:
                    pass
                elif total_quantity3 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product3, total_quantity3),
                                  extra_tags='unique_product3')

                if total_quantity4 is None:
                    pass
                elif total_quantity4 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product4, total_quantity4),
                                  extra_tags='unique_product4')

                if total_quantity5 is None:
                    pass
                elif total_quantity5 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product5, total_quantity5),
                                  extra_tags='unique_product5')

                if total_quantity6 is None:
                    pass
                elif total_quantity6 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product6, total_quantity6),
                                  extra_tags='unique_product6')

                if total_quantity7 is None:
                    pass
                elif total_quantity7 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product7, total_quantity7),
                                  extra_tags='unique_product7')

                if total_quantity8 is None:
                    pass
                elif total_quantity8 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product8, total_quantity8),
                                  extra_tags='unique_product8')

                if total_quantity9 is None:
                    pass
                elif total_quantity9 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product9, total_quantity9),
                                  extra_tags='unique_product9')

                if total_quantity10 is None:
                    pass
                elif total_quantity10 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product10, total_quantity10),
                                  extra_tags='unique_product_10')

                if total_quantity11 is None:
                    pass
                elif total_quantity11 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product11, total_quantity11),
                                  extra_tags='unique_product_11')

                if total_quantity12 is None:
                    pass
                elif total_quantity12 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product12, total_quantity12),
                                  extra_tags='unique_product_12')

                if total_quantity13 is None:
                    pass
                elif total_quantity13 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product13, total_quantity13),
                                  extra_tags='unique_product_13')

                if total_quantity14 is None:
                    pass
                elif total_quantity14 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product14, total_quantity14),
                                  extra_tags='unique_product_14')

                if total_quantity15 is None:
                    pass
                elif total_quantity15 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product15, total_quantity15),
                                  extra_tags='unique_product_15')

                if total_quantity16 is None:
                    pass
                elif total_quantity16 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product16, total_quantity16),
                                  extra_tags='unique_product_16')

                if total_quantity17 is None:
                    pass
                elif total_quantity17 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product17, total_quantity17),
                                  extra_tags='unique_product_17')

                if total_quantity18 is None:
                    pass
                elif total_quantity18 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product18, total_quantity18),
                                  extra_tags='unique_product_18')

                if total_quantity19 is None:
                    pass
                elif total_quantity19 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product19, total_quantity19),
                                  extra_tags='unique_product_19')

                if total_quantity20 is None:
                    pass
                elif total_quantity20 < 0:
                    messages.info(request,'Total quantity for product "{0}" will update to "{1}". Select "Yes" below to override.'.format(unique_product20, total_quantity20),
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

