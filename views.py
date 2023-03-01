from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fileinput import close
from datetime import datetime
import os.path
import json


# Create your views here.
def testing(request):
    return HttpResponse('Hello Testing API')

    
def testing2(request):
    return HttpResponse('Hello Testing API2')

def show_json(request):
    
    data={
        "nama" : "andrew",
        "sex"  : "laki-laki",
        "umur" : 33

    }
    return JsonResponse(data)

@csrf_exempt
def retrieve_data(request):
    data = json.loads(request.body)

    #name = request.POST['name']
    #sex = request.POST['sex']
    #age = request.POST['age']

    name = data['name']
    sex = data ['sex']
    age = data['age']

    print(name)
    print(sex)
    print(age)

    balikan ={
        "Status" : "Sukses",
        "Code" :"200"
    }
    return JsonResponse(balikan)
    #return HttpResponse("Sukses",status=200)

    
@csrf_exempt
def create_order(request):
    data_order = json.loads(request.body)

    message_id = data_order['ORM_O01']['MSH']['MSH.10']
    visitno = data_order['ORM_O01']['ORM_O01.ORDER']['ORC']['ORC.4']['EI.1']
    specialty = data_order['ORM_O01']['ORM_O01.PATIENT_VISIT']['PV1']['PV1.3']['PL.1']
    site_id = data_order['ORM_O01']['MSH']['MSH.4']['HD.1']
    pid = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.3']['CX.1']
    apid = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.4']['CX.1']
    pname = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.5']['XPN.2']
    title = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.5']['XPN.4']
    dob = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.7']['TS.1']
    sex = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.8']
    ADDR1 = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.11']['XAD.1']
    ADDR2 = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.11']['XAD.2']
    ADDR3 = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.11']['XAD.3']
    ADDR4 = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']['PID.11']['XAD.4']
    
    lno = data_order['ORM_O01']['ORM_O01.PATIENT']['ORM_O01.PATIENT_VISIT']['PV1']['PV1.19']['CX.1']
    ptype = data_order['ORM_O01']['ORM_O01.PATIENT']['ORM_O01.PATIENT_VISIT']['PV1']['PV1.2']
    grp_ono = data_order['ORM_O01']['ORM_O01.PATIENT']['ORM_O01.PATIENT_VISIT']['PV1']['PV1.19']['CX.1']
    room_no = data_order['ORM_O01']['ORM_O01.PATIENT']['ORM_O01.PATIENT_VISIT']['PV1']['PV1.3']['PL.1']

    #parameter yang harus di format
    source_code = data_order['ORM_O01']['ORM_O01.PATIENT']['ORM_O01.PATIENT_VISIT']['PV1']['PV1.3']['PL.1']
    source_name = data_order['ORM_O01']['ORM_O01.PATIENT']['ORM_O01.PATIENT_VISIT']['PV1']['PV1.3']['PL.1']
    request_dt = data_order['ORM_O01']['ORM_O01.ORDER']['ORM_O01.ORDER_DETAIL']['OBR']['OBR.7']['TS.1']
    request_tm = data_order['ORM_O01']['ORM_O01.ORDER']['ORM_O01.ORDER_DETAIL']['OBR']['OBR.7']['TS.2']
    clinician_code = data_order['ORM_O01.PATIENT_VISIT']['PV1']['PV1.7']['XCN.1']
    clinician_name = data_order['ORM_O01.PATIENT_VISIT']['PV1']['PV1.7']['XCN.2']

    #need to loops and mapping with the Master ini
    ono = data_order['ORM_O01']['ORM_O01.ORDER']['ORM_O01.ORDER_DETAIL']['OBR']['OBR.2']['EI.1']
    order_testid  = data_order['ORM_O01']['ORM_O01.ORDER']['ORM_O01.ORDER_DETAIL']['OBR']['OBR.4']['CE.1']
    order_control = data_order['ORM_O01']['ORM_O01.ORDER']['ORM_O01.ORDER_DETAIL']['OBR']['OBR.4']['CE.1']

    dept_code = data_order['ORM_O01']['ORM_O01.ORDER']['ORM_O01.ORDER_DETAIL']['OBR']['OBR.19']
    comment = data_order['ORM_O01']['ORM_O01.ORDER']['ORM_O01.ORDER_DETAIL']['OBR']['OBR.13']


    print(ono)
    print(request_dt)
    print(pname)
    print(dob)
    print(sex)
    print(source_code)
    print(source_name)
    print(clinician_code)
    print(clinician_name)
    print('~'.join(order_testid))
    orderlist = ('~'.join(order_testid))

    save_path = "C:\hcini\queue\HL7_in"
    file_name = ono
    complete_name = os.path.join(save_path,file_name+".txt")
    o01 = "[MSH]"+"\n"
    o01 = o01 + "message_id=O01|"+message_id+"\n"
    o01 = o01 + "message_dt="+datetime.today().strptime(data[4]+data[5],'%Y%m%d%H%M%S')+"\n"
    o01 = o01 + "receiving_application=HCLAB"+"\n"
    o01 = o01 + "version=2.3"+"\n"
    o01 = o01 + "[OBR]"+"\n"
    o01 = o01 + "order_control="+order_control+"\n"
    o01 = o01 + "order_action=A"+"\n"
    o01 = o01 + "visitno="+visitno+"\n"
    o01 = o01 + "specialty="+specialty+"\n"
    o01 = o01 + "site_id="+site_id+"\n"
    o01 = o01 + "pid="+pid+"\n"
    o01 = o01 + "apid="+apid+"\n"
    o01 = o01 + "pname="+pname+", "+title+"\n"
    o01 = o01 + "birth_dt="+dob+"\n"
    o01 = o01 + "sex="+sex+"\n"
    o01 = o01 + "address="+ADDR1+"^^"+ADDR2+"^"+ADDR3+"^"+ADDR4+"\n"
    o01 = o01 + "ptype="+ptype+"\n"
    o01 = o01 + "grp_ono="+grp_ono+"\n"
    o01 = o01 + "source="+source_code+"^"+source_name+"\n"
    o01 = o01 + "room_no="+room_no+"\n"
    o01 = o01 + "request_dt="+request_dt+request_tm+"\n"
    o01 = o01 + "ono="+ono+"\n"
    o01 = o01 + "lno="+lno+"\n"
    o01 = o01 + "clinician="+clinician_code+"^"+clinician_name+"\n"
    o01 = o01 + "order_testid="+order_testid+"\n"
    o01 = o01 + "dept="+dept_code+"\n"
    o01 = o01 + "comment="+comment+"\n"
    f = open(complete_name, "w")
    f.write(o01)
    f.close()
    
    print(o01)


    balikan ={
        "Status" : "Sukses Order",
        "Code" :"201"
    }
    return JsonResponse(balikan)
    #return HttpResponse("Sukses",status=200)




