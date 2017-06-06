from builtins import str
import re

from django.http.response import HttpResponse, JsonResponse, \
    HttpResponseRedirect
from django.shortcuts import render

from findorders.connect_db2 import *
from findorders.connect_db2 import format_args, select_table

#def home(request):
def home(request):
    return render(request, 'home.html')
def rev(request):
    list_orders=[]
    list_orders=request.GET().get('a','None')
    request.GET.get("id",'None')
def finddelivery(request):
    return render(request,'finddelivery.html')
def orderlog(request):
    return render(request,'orderlog.html')

def get_request(request):
    #list1=list(request.GET.get('textarea','None').strip())
    users=[]
    if request.method=="POST":
        list1=request.POST.get('textarea','None').strip()
        list1.strip()
        
        print("list1",list(list1.split('\r\n')))
        list2=list1.split('\r\n')
        print("list2",list2)
        #pattern=re.compile(r"(^\d*)")
        for item in list2:
            print("len",len(list2))
            print("for",item)
            obj=re.match(r'([^0-9])',item, re.M|re.I)
            print("obj",obj)
            if obj:
                print("match*************")
                list2.remove(item)
        print("list11",list1)
#         #list2=[]
#         #[list2.append(i) for i in list1 if not i in list2]
#         if '\r' in list2:
# #             for item in list2:
# #             if item=='\r':
#             list2.remove('\r')
#         elif '\n' in list2:
#                 list2.remove('\n')
#         elif '\t' in list2:
#                 list2.remove('\t')
        #list2.remove('\n')
        #list2.remove(',')
    #     list2 = []
    #     [list2.append(i) for i in list1 if not i in list2]
    #     list2.remove(',')
    #     list2.remove('\r')
    #     list2.remove('\t')
    #     list2.remove('\n')
        print("list2",list2)
        print("format_args(list2)",format_args(list2))
        sql='''
            select a.orders_id,b.ormorder,a.field2,a.field3,a.field4,a.field5 from  
            DB2INST1.xordextdata a,DB2INST1.orders b where a.orders_id=b.orders_id and a.orders_id in
            ''' +format_args(list2) % tuple(list2)
        print("sql",sql)
        global order_list
        order_list = select_table(sql)
        count=len(order_list)
        print("order_list",order_list)
    return render(request, 'finddelivery.html', { 'orders': order_list },{'count':count})

#导出xls      
def xls_mould(request):
    
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment; filename='+time.strftime('%Y%m%d',time.localtime(time.time()))+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet(u'订单')
    #1st line   
    sheet.write(0,0, '订单号')
    sheet.write(0,1, '外部订单号')
    sheet.write(0,2, '快递单号')
    sheet.write(0,3, '快递公司简称')
    #people_list=User.objects.filter(id=items)
   
    row = 1
    for item in order_list:
        sheet.write(row,0, item[0])
        sheet.write(row,1, item[1])
        sheet.write(row,2, item[2])
        sheet.write(row,3, item[5])
        row=row + 1
    wb.save(response)
    return response