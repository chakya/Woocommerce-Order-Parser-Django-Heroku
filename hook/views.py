import copy, json, datetime
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

@csrf_exempt
@require_POST
def webhook(request):
    jsondata = request.body
    # print(jsondata)
    data = json.loads(jsondata.decode())
    # print(data)
    orderItem=data['order']['line_items']
    dishes=[]
    sideId=[]
    for item in orderItem:
        itemName=item["name"]
        if len(item['composite_children'])!=0:
            dishes.append([str(item['quantity']),[str(item['name'])]])
            sideId=item['composite_children']
        elif item['id'] in sideId:
            dishes[-1][1].append(str(item['name']))
        else:
            dishes.append([str(item['quantity']),[str(item['name'])]])
    print(dishes)

     # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open('orders').sheet1
    info=data['order']['billing_address']
    for item in dishes:
        sheet.append_row([info['first_name']+' '+info['last_name'],info['address_1']+' '+info['address_2'],info['city'],info['postcode'],info['email'],info['phone'],item[0],item[1]])
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