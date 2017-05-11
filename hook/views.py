import copy, json, datetime
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests


@csrf_exempt
# @require_POST
def webhook(request):
    # jsondata = request.body
    # # print(jsondata)
    # data = json.loads(jsondata.decode())
    # # print(data)
    # orderItem=data['order']['line_items'][0]
    # orderName=orderItem['name']
    # orderPrice=orderItem['price']
    # orderQuatity=orderItem['quantity']
    # customer=data['order']['customer']
    # custAdd=customer['billing_address']
    # address=custAdd['address_1']+custAdd['address_2']
    # print('<h1>amazing</h1>')
    # text='{} {} {} {}'.format(orderQuatity,orderName, orderPrice, address)


    # #send to telegram
    # url='https://api.telegram.org/bot'
    # url+='271450263:AAHV8VK5b1HiZUGz_cLp5bmd3epalHsIz3c/'
    # sendMesUrl=url+'sendMessage?chat_id={}&text={}'
    # requests.post(sendMesUrl.format("269856018",text))
    # requests.post(sendMesUrl.format("235092071", text))
    # requests.post(sendMesUrl.format("329891854", text))
    # print(data['order']['line_items'][0]['name'])
    # print('hello')
    return HttpResponse(status=200)
    # WebhookTransaction.objects.create(
    #     date_event_generated=datetime.datetime.fromtimestamp(
    #         data['timestamp']/1000.0,
    #         tz=timezone.get_current_timezone()
    #     ),
    #     body=data,
    #     request_meta=meta
    # )






# from django.shortcuts import render
# from django.http import HttpResponse
# import json
# from django.views.decorators.csrf import csrf_exempt
# # Create your views here.
#
#
# # def index(request):
# #     print(json.loads(request.body))
# #     return HttpResponse
# # # class ProcessHookView(Csr)
#
# # import json
# #
# # from django.http import HttpResponse
# from django.views.generic import View
# #
# # from braces.views import CsrfExemptMixin
# #
# #
# class ProcessHookView(View, csrf_exempt()):
#     @csrf_exempt
#     def post(self, request, args, *kwargs):
#         print(json.loads(request.body))
#         return HttpResponse()