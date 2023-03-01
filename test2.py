import json
from pprint import pprint
from configparser import ConfigParser

# function for mapping
def mapping_order(test_item):
    # config = ConfigParser.RawConfigParser()
    # config.read('MASTER.ini')
    # counter = 1
    # while "order"+str(counter) in config["order"]:
    #     content = config["order"]["order"+str(counter)]
    #     pprint(content)
    #     counter +=1
    with open('MASTER.ini','r') as g:
        mapping_order = g.readlines()
        for line in mapping_order:
            if test_item in line and 'order' in line:
                order = line.split("=")
                order2 = order[1].split(",")
                #print (order2[2])
    return order2[2]
           
    
  

def parse_o01(data_order):
    #code_hclab = mapping()

   

    msh = data_order['ORM_O01']['MSH']
    pv1 = data_order['ORM_O01']['ORM_O01.PATIENT']['ORM_O01.PATIENT_VISIT']['PV1']
    pid = data_order['ORM_O01']['ORM_O01.PATIENT']['PID']

    #MSH
    message_id = str(msh['MSH.10'])
    message_dt = str(msh['MSH.7']['TS.1'])
    message_tm = str(msh['MSH.7']['TS.2'])
    receiving_app = msh['MSH.5']['HD.1']
    version = str(msh['MSH.12'])

    #OBR
    site_id = str(msh['MSH.4']['HD.1'])
    no_rm = str(pid['PID.3']['CX.1'])
    specialty = pv1['PV1.3']['PL.1']
    apid = str(pid['PID.4']['CX.1'])
    pname = pid['PID.5']['XPN.2'] +','+ pid['PID.5']['XPN.4']
    birth_dt=str(pid['PID.7']['TS.1'])
    gender = str(pid['PID.8'])
    address = pid['PID.11']['XAD.1']+'^'+pid['PID.11']['XAD.3']+'^'+pid['PID.11']['XAD.4']+'^'+str(pid['PID.11']['XAD.5'])
    ptype = pv1['PV1.2']
    grp_ono = str(pv1['PV1.19']['CX.1'])
    source= str(pv1['PV1.3']['PL.1'])
    room_no = ''
    lno =''
    clinician_code = pv1['PV1.7']['XCN.1']
    clinician_name = pv1['PV1.7']['XCN.2']
    

    for order in data_order['ORM_O01']['ORM_O01.ORDER']:
        order_control = order['ORC']['ORC.1']
        visitno = str(order['ORC']['ORC.4']['EI.1'])
        test_item = order['ORM_O01.ORDER_DETAIL']['OBR']['OBR.4']['CE.1']
        mapped_item = mapping_order(test_item)
        request_dt = str(order['ORM_O01.ORDER_DETAIL']['OBR']['OBR.7']['TS.1'])
        request_tm = str(order['ORM_O01.ORDER_DETAIL']['OBR']['OBR.7']['TS.2'])
        ono = str (order['ORM_O01.ORDER_DETAIL']['OBR']['OBR.2']['EI.1'])
        dept_code = order['ORM_O01.ORDER_DETAIL']['OBR']['OBR.19']
        comment = order['ORM_O01.ORDER_DETAIL']['OBR']['OBR.13']

        o01 = "[MSH]"+"\n"
        o01 = o01 + "message_id=O01|"+ message_id +"\n"
        o01 = o01 + "message_dt="+ message_dt + message_tm+"\n"
        o01 = o01 + "receiving_application="+ receiving_app+"\n"
        o01 = o01 + "version="+ version+"\n"
        o01 = o01 + "[OBR]"+"\n"
        o01 = o01 + "order_control="+ order_control +"\n"
        o01 = o01 + "order_action=A"+"\n"
        o01 = o01 + "visitno="+ visitno +"\n"
        o01 = o01 + "specialty=" + specialty +"\n"
        o01 = o01 + "site_id=" + site_id + "\n"
        o01 = o01 + "pid=" + no_rm + "\n"
        o01 = o01 + "apid=" + apid + "\n"
        o01 = o01 + "pname=" + pname + "\n"
        o01 = o01 + "birth_dt=" + birth_dt +"\n"
        o01 = o01 + "sex="+ gender + "\n"
        o01 = o01 + "address="+ address + "\n"
        o01 = o01 + "ptype="+ ptype + "\n"
        o01 = o01 + "grp_ono="+ grp_ono + "\n"
        o01 = o01 + "source="+source+"\n"
        o01 = o01 + "room_no="+room_no+"\n"
        o01 = o01 + "request_dt=" +request_dt + request_tm+"\n"
        o01 = o01 + "ono="+ono+"\n"
        o01 = o01 + "lno="+lno+"\n"
        o01 = o01 + "clinician="+clinician_code+"^"+clinician_name+"\n"
        o01 = o01 + "order_testid="+mapped_item+"\n"
        o01 = o01 + "dept="+dept_code+"\n"
        o01 = o01 + "comment="+comment+"\n"
        pprint(o01)
        

print(mapping_order('LABA310000'))

with open('O01.JSON','r') as f:
    data_order = json.load(f)

print(parse_o01(data_order))