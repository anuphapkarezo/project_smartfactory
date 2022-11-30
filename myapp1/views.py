from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Waste_item_master_list , Waste_group_master_list , Waste_item_price_list , Waste_item_map_factory , Waste_daily_transaction
from .models import Company_master_list , Company_contact_name_list

import pandas as pd
from .proj7_functions import save_waste_item_master_list , update_waste_item_master_list
from .proj7_functions import save_waste_group_master_list , update_waste_group_master_list
from .proj7_functions import save_waste_item_price_list , update_waste_item_price_list
from .proj7_functions import save_company_master_list , update_company_master_list
from .proj7_functions import save_company_contact_name_list , update_company_contact_name_list
from .proj7_functions import save_waste_item_map_factory , update_waste_item_map_factory
from .proj7_functions import save_waste_daily_transaction

import json
from json import dumps
# Create your views here.
def go_index(request):
    return  render(request,'index.html')

def go_form1(request):
    return  render(request,'ฺBasic_HTML/HTML_0_From_1.html')

def go_class(request):
    return  render(request,'ฺBasic_HTML/HTML_1_CLASS.html')

def go_boxinline(request):
    return  render(request,'ฺBasic_HTML/HTML_2_BOX_INLINE.html')

def go_absolute(request):
    return  render(request,'ฺBasic_HTML/HTML_3_Absolute.html')

def go_Universal(request):
    return  render(request,'ฺBasic_HTML/HTML_4_Universal_Selector.html')

def go_font(request):
    return  render(request,'ฺBasic_HTML/HTML_5_Font_color.html')

def go_width(request):
    return  render(request,'ฺBasic_HTML/HTML_6_Width_Height.html')

def go_border(request):
    return  render(request,'ฺBasic_HTML/HTML_7_Border.html')

def page_master_machine_pcap(request):
    return  render(request,'PCTT_project/Page_master_machine_PCAP.html')

def Page_master_machine_FPC(request):
    return  render(request,'PCTT_project/Page_master_machine_FPC.html')

def Page_master_clean_scan(request):
    return  render(request,'PCTT_project/Page_master_clean_scan.html')

def Page_master_clean_query_lot(request):
    return  render(request,'PCTT_project/Page_master_clean_query_lot.html')

def Page_report_product_transfer_to_WH(request):
    return  render(request,'PCTT_project/Page_report_product_transfer_to_WH.html')

def Page_report_product_std_leadtime(request):
    return  render(request,'PCTT_project/Page_report_product_std_leadtime.html')

def Page_report_item_inventory_data(request):
    return  render(request,'PCTT_project/Page_report_item_inventory_data.html')

def Page_FPC_system_cancel_lot(request):
    return  render(request,'PCTT_project/Page_FPC_system_cancel_lot.html')

def Page_FPC_system_check_scan_MAT(request):
    return  render(request,'PCTT_project/Page_FPC_system_check_scan_MAT.html')

def Page_FPC_system_test_formulas(request):
    return  render(request,'PCTT_project/Page_FPC_system_test_formulas.html')

def Page_main_menu(request):
    return  render(request,'PCTT_project/Page_main_menu.html')

def Page_Login(request):
    return  render(request,'Smart_scrap_management/Page_Login.html')

def go_html_record_weight(request):
    return  render(request,'proj7_scrap_control/proj7_page1_record_weight.html')

def go_html_database_management(request):
    return render(request,"proj7_scrap_control/proj7_page2_database_management.html")

def go_html_record_weight_waste_scrap(request):
    return  render(request,'proj7_scrap_control/proj7_page3_record_weight_waste_scrap.html')

@csrf_exempt
def proj7_read_database_product(request):
    db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
    json_records = db_item_master.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)
    ajax_proj7_read_database_waste_item = dumps(data_loads)
    return HttpResponse(ajax_proj7_read_database_waste_item)

    # btn_name_sv = request.POST['btn_name']
    # month_salary = int(request.POST['salary'])
    # print("Test request server : " , btn_name_sv)

    #net_salary_years = 12 * month_salary
    #print(net_salary_years)

    #Read Excel
    # df_excel = pd.read_excel(r"C:\django_Project\project_smartfactory\static\upload\waste item master list 1.xlsx")
    # print("File Excel :" , df_excel)

    # # Read database from dBeaver and Print show

    # #check exists database ตรวจสอบข้อมูลที่มีอยู่ใน Database วิธีที่ 1
    # check_db = Waste_item_master_list.objects.all().exists() #จะได้ค่า true/false เท่านั้น
    # print(check_db)
    # if check_db == False:
    #     save_waste_item_master_list(df_excel)
    #     db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
    #     json_records = db_item_master.reset_index().to_json(orient='records')
    #     data_loads = json.loads(json_records)
    #     ajax_proj7_read_database_waste_item = dumps(data_loads)
    #     return HttpResponse(ajax_proj7_read_database_waste_item)

    # else:
    #     db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
    #     db_item_master["exists_data"] = "YES"
    #     print(db_item_master.columns)
        

    #     df_merge_data = pd.merge(df_excel,db_item_master,how="left",on=["waste_item_code"])
    #     print(df_merge_data.columns)
    #     df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
    #     print(df_merge_data[["waste_item_code" , "exists_data"]])
    #     df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
    #     df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
    #     print(df_merge_data_save)
    #     if len(df_merge_data_save) > 0 :
    #         #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
    #         df_merge_data_save.rename({"description_EN_x":"description_EN" , "description_TH_x":"description_TH" , "waste_group_code_x":"waste_group_code" },axis=1 , inplace=True)
    #         save_waste_item_master_list(df_merge_data_save)
    #         # print("df_merge_data_save")
    #     if len(df_merge_data_update) > 0 :
    #         print(df_merge_data_update.columns)
    #         update_waste_item_master_list(df_merge_data_update)
    #         #convert to Json
    #         json_records = db_item_master.reset_index().to_json(orient='records')
    #         data_loads = json.loads(json_records)
    #         ajax_proj7_read_database_waste_item = dumps(data_loads)
    #         return HttpResponse(ajax_proj7_read_database_waste_item)


# waste_item_master_list
@csrf_exempt
def proj_page1_delete_waste_item_master(request):
    waste_item_delete = request.POST['item_delete']
    print(waste_item_delete)
    Waste_item_master_list.objects.filter(waste_item_code=waste_item_delete).delete()
    ajax_proj_page1_delete_waste_item_master = waste_item_delete
    return HttpResponse(ajax_proj_page1_delete_waste_item_master)

@csrf_exempt
def proj7_page2_upload_file_waste_item_master_list(request):
    if len(request.FILES) == 0: #ถ้าไม่พบ file ให้กลับหน้าเดิม
        ajax_proj7_page2_upload_file_waste_item_master_list = "Not found file for upload"
        return HttpResponse(ajax_proj7_page2_upload_file_waste_item_master_list)
    
    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))

    db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
    check_db = Waste_item_master_list.objects.all().exists() #เช็คว่าใน database มีข้อมูลหรือยัง จะได้ค่า true/false เท่านั้น

    if check_db == False:
         save_waste_item_master_list(excel_raw_data)

         ajax_proj7_page2_upload_file_waste_item_master_list = "Upload data waste item master list successful(New)"
         return HttpResponse(ajax_proj7_page2_upload_file_waste_item_master_list)
    
    else:
        db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.all().values()))
        db_item_master["exists_data"] = "YES"

        df_merge_data = pd.merge(excel_raw_data,db_item_master,how="left",on=["waste_item_code"])
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
 
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        print(df_merge_data_save)
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"description_EN_x":"description_EN" , "description_TH_x":"description_TH" , "waste_group_code_x":"waste_group_code" , "waste_unit_x":"waste_unit" },axis=1 , inplace=True)
            save_waste_item_master_list(df_merge_data_save)

            ajax_proj7_page2_upload_file_waste_item_master_list = "Upload data waste item master list successful(New)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_item_master_list)

            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            update_waste_item_master_list(df_merge_data_update)
         
            ajax_proj7_page2_upload_file_waste_item_master_list = "Upload data waste item master list successful(Update)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_item_master_list)

# waste_group_master_list
@csrf_exempt
def proj7_page2_upload_file_waste_group_master_list(request):
    if len(request.FILES) == 0: #ถ้าไม่พบ file ให้กลับหน้าเดิม
        ajax_proj7_page2_upload_file_waste_group_master_list = "Not found file for upload"
        return HttpResponse(ajax_proj7_page2_upload_file_waste_group_master_list)
    
    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))

    db_item_master = pd.DataFrame(list(Waste_group_master_list.objects.all().values()))
    check_db = Waste_group_master_list.objects.all().exists() #เช็คว่าใน database มีข้อมูลหรือยัง จะได้ค่า true/false เท่านั้น

    if check_db == False:
         save_waste_group_master_list(excel_raw_data)

         ajax_proj7_page2_upload_file_waste_group_master_list = "Upload data waste group master list successful(New)"
         return HttpResponse(ajax_proj7_page2_upload_file_waste_group_master_list)
    
    else:
        db_item_master = pd.DataFrame(list(Waste_group_master_list.objects.all().values()))
        db_item_master["exists_data"] = "YES"

        df_merge_data = pd.merge(excel_raw_data,db_item_master,how="left",on=["waste_group_code"])
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
 
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        print(df_merge_data_save)
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"group_name_x":"group_name" },axis=1 , inplace=True)
            save_waste_group_master_list(df_merge_data_save)

            ajax_proj7_page2_upload_file_waste_group_master_list = "Upload data waste group master list successful(New)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_group_master_list)

            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            update_waste_group_master_list(df_merge_data_update)
         
            ajax_proj7_page2_upload_file_waste_group_master_list = "Upload data waste group master list successful(Update)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_group_master_list)

# Waste_item_price_list
@csrf_exempt 
def proj7_page2_upload_file_waste_item_price_list(request):
    if len(request.FILES) == 0: #ถ้าไม่พบ file ให้กลับหน้าเดิม
        ajax_proj7_page2_upload_file_waste_item_price_list = "Not found file for upload"
        return HttpResponse(ajax_proj7_page2_upload_file_waste_item_price_list)
    
    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))

    db_item_master = pd.DataFrame(list(Waste_item_price_list.objects.all().values()))
    check_db = Waste_item_price_list.objects.all().exists() #เช็คว่าใน database มีข้อมูลหรือยัง จะได้ค่า true/false เท่านั้น

    if check_db == False:
         save_waste_item_price_list(excel_raw_data)

         ajax_proj7_page2_upload_file_waste_item_price_list = "Upload data waste item price list successful(New)"
         return HttpResponse(ajax_proj7_page2_upload_file_waste_item_price_list)
    
    else:
        db_item_master = pd.DataFrame(list(Waste_item_price_list.objects.all().values()))
        db_item_master["exists_data"] = "YES"

        df_merge_data = pd.merge(excel_raw_data,db_item_master,how="left",on=["waste_item_code"])
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
 
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        print(df_merge_data_save)
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"price_x":"price" , "unit_price_x":"unit_price" , "price_effective_from_x":"price_effective_from" ,
            "price_effective_to_x":"price_effective_to" , "company_code_x":"company_code" },axis=1 , inplace=True)
            save_waste_item_price_list(df_merge_data_save)

            ajax_proj7_page2_upload_file_waste_item_price_list = "Upload data waste item price list successful(New)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_item_price_list)

            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            update_waste_item_price_list(df_merge_data_update)
         
            ajax_proj7_page2_upload_file_waste_item_price_list = "Upload data waste item price list successful(Update)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_item_price_list)

# Company_master_list
@csrf_exempt
def proj7_page2_upload_file_company_master_list(request):
    if len(request.FILES) == 0: #ถ้าไม่พบ file ให้กลับหน้าเดิม
        ajax_proj7_page2_upload_file_company_master_list = "Not found file for upload"
        return HttpResponse(ajax_proj7_page2_upload_file_company_master_list)

    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))

    db_item_master = pd.DataFrame(list(Company_master_list.objects.all().values()))
    check_db = Company_master_list.objects.all().exists() #เช็คว่าใน database มีข้อมูลหรือยัง จะได้ค่า true/false เท่านั้น

    if check_db == False:
         save_company_master_list(excel_raw_data)

         ajax_proj7_page2_upload_file_company_master_list = "Upload data company master list successful(New)"
         return HttpResponse(ajax_proj7_page2_upload_file_company_master_list)
    
    else:
        db_item_master = pd.DataFrame(list(Waste_item_price_list.objects.all().values()))
        db_item_master["exists_data"] = "YES"

        df_merge_data = pd.merge(excel_raw_data,db_item_master,how="left",on=["company_code"])
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
 
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        print(df_merge_data_save)
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"company_name_x":"company_name" },axis=1 , inplace=True)
            save_company_master_list(df_merge_data_save)

            ajax_proj7_page2_upload_file_company_master_list = "Upload data company master list successful(New)"
            return HttpResponse(ajax_proj7_page2_upload_file_company_master_list)

            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            update_company_master_list(df_merge_data_update)
         
            ajax_proj7_page2_upload_file_company_master_list = "Upload data company master list successful(Update)"
            return HttpResponse(ajax_proj7_page2_upload_file_company_master_list)


# Company_contact_name_list
@csrf_exempt
def proj7_page2_upload_file_company_contact_name_list(request):
    if len(request.FILES) == 0: #ถ้าไม่พบ file ให้กลับหน้าเดิม
        ajax_proj7_page2_upload_file_company_contact_name_list = "Not found file for upload"
        return HttpResponse(ajax_proj7_page2_upload_file_company_contact_name_list)

    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))
    excel_raw_data['company_code'] = excel_raw_data['company_code'].astype(str) #Convert int64 to str

    db_item_master = pd.DataFrame(list(Company_contact_name_list.objects.all().values()))
    check_db = Company_contact_name_list.objects.all().exists() #เช็คว่าใน database มีข้อมูลหรือยัง จะได้ค่า true/false เท่านั้น

    if check_db == False:
         save_company_contact_name_list(excel_raw_data)

         ajax_proj7_page2_upload_file_company_contact_name_list = "Upload data company contact name list successful(New)"
         return HttpResponse(ajax_proj7_page2_upload_file_company_contact_name_list)
    
    else:
        db_item_master = pd.DataFrame(list(Company_contact_name_list.objects.all().values()))
        db_item_master["exists_data"] = "YES"

        df_merge_data = pd.merge(excel_raw_data,db_item_master,how="left",on=["company_code"])
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
 
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        print(df_merge_data_save)
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"contact_firstname_x":"contact_firstname" , "contact_lastname_x":"contact_lastname" , 
            "contact_email_x":"contact_email" , "contact_phone_x":"contact_phone" },axis=1 , inplace=True)
            save_company_contact_name_list(df_merge_data_save)

            ajax_proj7_page2_upload_file_company_contact_name_list = "Upload data company contact name list successful(New)"
            return HttpResponse(ajax_proj7_page2_upload_file_company_contact_name_list)

            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            update_company_contact_name_list(df_merge_data_update)
         
            ajax_proj7_page2_upload_file_company_contact_name_list = "Upload data company contact name list successful(Update)"
            return HttpResponse(ajax_proj7_page2_upload_file_company_contact_name_list)

# waste_item_map_factory
@csrf_exempt
def proj7_page2_upload_file_waste_item_map_factory(request):
    if len(request.FILES) == 0: #ถ้าไม่พบ file ให้กลับหน้าเดิม
        ajax_proj7_page2_upload_file_waste_item_map_factory = "Not found file for upload"
        return HttpResponse(ajax_proj7_page2_upload_file_waste_item_map_factory)

    excel_raw_data = pd.read_excel(request.FILES.get('excel_data'))
    excel_raw_data['waste_item_code'] = excel_raw_data['waste_item_code'].astype(str) #Convert int64 to str

    db_item_master = pd.DataFrame(list(Waste_item_map_factory.objects.all().values()))
    check_db = Waste_item_map_factory.objects.all().exists() #เช็คว่าใน database มีข้อมูลหรือยัง จะได้ค่า true/false เท่านั้น

    if check_db == False:
         save_waste_item_map_factory(excel_raw_data)

         ajax_proj7_page2_upload_file_waste_item_map_factory = "Upload data waste item map factory successful(New)"
         return HttpResponse(ajax_proj7_page2_upload_file_waste_item_map_factory)
    
    else:
        db_item_master = pd.DataFrame(list(Waste_item_map_factory.objects.all().values()))
        db_item_master["exists_data"] = "YES"

        df_merge_data = pd.merge(excel_raw_data,db_item_master,how="left",on=["waste_item_code"])
        df_merge_data.fillna("NO",inplace=True) #แทนค่าจาก Nan > NO
 
        df_merge_data_save = df_merge_data[df_merge_data['exists_data']=="NO"] #Data ที่มีการเพิ่มเข้ามาใหม่
        df_merge_data_update = df_merge_data[df_merge_data['exists_data']=="YES"] #Data ที่มีอยู่แล้ว และมีการ Update
        print(df_merge_data_save)
        if len(df_merge_data_save) > 0 :
            #เปลี่ยนชื่อ Field ที่ทำการ Merge ไว้ ให้กลับมาเป็นชื่อเดิม
            df_merge_data_save.rename({"factory_name_x":"factory_name"},axis=1 , inplace=True)
            save_waste_item_map_factory(df_merge_data_save)

            ajax_proj7_page2_upload_file_waste_item_map_factory = "Upload data waste item map factory successful(New)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_item_map_factory)

            # print("df_merge_data_save")
        if len(df_merge_data_update) > 0 :
            update_waste_item_map_factory(df_merge_data_update)
         
            ajax_proj7_page2_upload_file_waste_item_map_factory = "Upload data waste item map factory successful(Update)"
            return HttpResponse(ajax_proj7_page2_upload_file_waste_item_map_factory)

@csrf_exempt
def proj7_page3_record_weight_waste_scrap(request):
    db_item_master = pd.DataFrame(list(Waste_group_master_list.objects.all().values()))
    json_records = db_item_master.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)

    ajax_proj7_page3_record_weight_waste_scrap = dumps(data_loads)
    return HttpResponse(ajax_proj7_page3_record_weight_waste_scrap)

@csrf_exempt
def proj7_page3_record_weight_waste_scrap_search_item(request):
    # df_data_result = pd.DataFrame(list(Waste_item_master_list.objects.filter(waste_group_code=group_search_post).values()))
    group_search_post = request.POST['group_search']
    factory_search_post = request.POST['factory_search']
    select_date_val_post  = request.POST['select_date_val']
    # db_item_map_factory = pd.DataFrame(list(Waste_item_map_factory.objects.filter(factory_name=factory_search_post).values()))
    
    # df_merge_data_map = pd.merge(db_item_master,db_item_master,how="inner",on=["waste_item_code"])
    # print(db_item_map_factory)
    # print(db_item_master)
    # print(df_merge_data_map)

    db_item_master = pd.DataFrame(list(Waste_item_master_list.objects.filter(waste_group_code=group_search_post).values()))
    db_item_group = pd.DataFrame(list(Waste_group_master_list.objects.all().values()))
    df_merge_data = pd.merge(db_item_master,db_item_group,how="inner",on=["waste_group_code"])
    # print(df_merge_data)

    # print('/////////////////////////////////////////')
    db_item_map_factory = pd.DataFrame(list(Waste_item_map_factory.objects.filter(factory_name=factory_search_post).values()))
    # print(db_item_map_factory)
    # print('/////////////////////////////////////////')
    df_merge_data_map = pd.merge(df_merge_data,db_item_map_factory,how="inner",on=["waste_item_code"])

    df_daily_transaction = Waste_daily_transaction.objects.filter(date_take_off=select_date_val_post , factory_name = factory_search_post , waste_group_code = group_search_post).exists()
    if df_daily_transaction == True :
        df_daily_transaction_val = pd.DataFrame(list(Waste_daily_transaction.objects.filter(date_take_off=select_date_val_post , factory_name = factory_search_post , waste_group_code = group_search_post).values()))
        df_daily_transaction_val['weight'] = df_daily_transaction_val['weight'].astype(float)
        df_daily_transaction_val = df_daily_transaction_val.groupby(['waste_item_code'  , 'factory_name' , 'waste_group_code'],as_index=False)['weight'].sum()
        df_daily_transaction_val.fillna('Other',inplace=True)

        df_merge_data_map = pd.merge(df_merge_data_map,df_daily_transaction_val,how="left",on=['waste_item_code'  , 'factory_name' , 'waste_group_code'])
        df_merge_data_map.fillna(0,inplace=True)
    else:
        df_merge_data_map['weight'] = 0

    json_records = df_merge_data_map.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)
    ajax_proj7_page3_record_weight_waste_scrap_search_item = dumps(data_loads)

    return HttpResponse(ajax_proj7_page3_record_weight_waste_scrap_search_item)

# ajax_proj7_page3_save_waste_daily_transaction
@csrf_exempt
def proj7_page3_save_waste_daily_transaction(request):
    det_weight_1 = int(request.POST['det_weight_1'])
    det_weight_2 = int(request.POST['det_weight_2'])
    det_weight_3 = int(request.POST['det_weight_3'])
    det_weight_4 = int(request.POST['det_weight_4'])
    det_weight_5 = int(request.POST['det_weight_5'])
    det_weight_6 = int(request.POST['det_weight_6'])
    det_weight_7 = int(request.POST['det_weight_7'])
    det_weight_8 = int(request.POST['det_weight_8'])
    det_weight_9 = int(request.POST['det_weight_9'])
    det_weight_10 = int(request.POST['det_weight_10'])

    det_weight_11 = int(request.POST['det_weight_11'])
    det_weight_12 = int(request.POST['det_weight_12'])
    det_weight_13 = int(request.POST['det_weight_13'])
    det_weight_14 = int(request.POST['det_weight_14'])
    det_weight_15 = int(request.POST['det_weight_15'])
    det_weight_16 = int(request.POST['det_weight_16'])
    det_weight_17 = int(request.POST['det_weight_17'])
    det_weight_18 = int(request.POST['det_weight_18'])
    det_weight_19 = int(request.POST['det_weight_19'])
    det_weight_20 = int(request.POST['det_weight_20'])

    det_weight_21 = int(request.POST['det_weight_21'])
    det_weight_22 = int(request.POST['det_weight_22'])
    det_weight_23 = int(request.POST['det_weight_23'])
    det_weight_24 = int(request.POST['det_weight_24'])
    det_weight_25 = int(request.POST['det_weight_25'])
    det_weight_26 = int(request.POST['det_weight_26'])
    det_weight_27 = int(request.POST['det_weight_27'])
    det_weight_28 = int(request.POST['det_weight_28'])
    det_weight_29 = int(request.POST['det_weight_29'])
    det_weight_30 = int(request.POST['det_weight_30'])

    date_take_off = request.POST['date_take_off']
    factory_search = request.POST['factory_search']
    waste_item_code = request.POST['waste_item_code']
    group_search = request.POST['group_search']

    df_daily_transaction_val = Waste_daily_transaction.objects.filter(date_take_off=date_take_off , factory_name = factory_search , waste_item_code = waste_item_code).exists()
    if df_daily_transaction_val == True :
        df_daily_transaction_val = Waste_daily_transaction.objects.filter(date_take_off=date_take_off , factory_name = factory_search , waste_item_code = waste_item_code).delete()

    if det_weight_1 > 0:
        detail_no_1 = "1"
        detail_weight = det_weight_1
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_1 , detail_weight)
    
    if det_weight_2 > 0:
        detail_no_2 = "2"
        detail_weight = det_weight_2
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_2 , detail_weight)
    
    if det_weight_3 > 0:
        detail_no_3 = "3"
        detail_weight = det_weight_3
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_3 , detail_weight)

    if det_weight_4 > 0:
        detail_no_4 = "4"
        detail_weight = det_weight_4
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_4 , detail_weight)

    if det_weight_5 > 0:
        detail_no_5 = "5"
        detail_weight = det_weight_5
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_5 , detail_weight)
    
    if det_weight_6 > 0:
        detail_no_6 = "6"
        detail_weight = det_weight_6
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_6 , detail_weight)

    if det_weight_7 > 0:
        detail_no_7 = "7"
        detail_weight = det_weight_7
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_7 , detail_weight)
 
    if det_weight_8 > 0:
        detail_no_8 = "8"
        detail_weight = det_weight_8
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_8 , detail_weight)

    if det_weight_9 > 0:
        detail_no_9 = "9"
        detail_weight = det_weight_9
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_9 , detail_weight)

    if det_weight_10 > 0:
        detail_no_10 = "10"
        detail_weight = det_weight_10
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_10 , detail_weight)

    if det_weight_11 > 0:
        detail_no_11 = "11"
        detail_weight = det_weight_11
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_11 , detail_weight)

    if det_weight_12 > 0:
        detail_no_12 = "12"
        detail_weight = det_weight_12
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_12 , detail_weight)

    if det_weight_13 > 0:
        detail_no_13 = "13"
        detail_weight = det_weight_13
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_13 , detail_weight)

    if det_weight_14 > 0:
        detail_no_14 = "14"
        detail_weight = det_weight_14
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_14 , detail_weight)

    if det_weight_15 > 0:
        detail_no_15 = "15"
        detail_weight = det_weight_15
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_15 , detail_weight)

    if det_weight_16 > 0:
        detail_no_16 = "16"
        detail_weight = det_weight_16
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_16 , detail_weight)
    
    if det_weight_17 > 0:
        detail_no_17 = "17"
        detail_weight = det_weight_17
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_17 , detail_weight)

    if det_weight_18 > 0:
        detail_no_18 = "18"
        detail_weight = det_weight_18
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_18 , detail_weight)

    if det_weight_19 > 0:
        detail_no_19 = "19"
        detail_weight = det_weight_19
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_19 , detail_weight)

    if det_weight_20 > 0:
        detail_no_20 = "20"
        detail_weight = det_weight_20
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_20 , detail_weight)

    if det_weight_21 > 0:
        detail_no_21 = "21"
        detail_weight = det_weight_21
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_21 , detail_weight)

    if det_weight_22 > 0:
        detail_no_22 = "22"
        detail_weight = det_weight_22
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_22 , detail_weight) 

    if det_weight_23 > 0:
        detail_no_23 = "23"
        detail_weight = det_weight_23
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_23 , detail_weight)  

    if det_weight_24 > 0:
        detail_no_24 = "24"
        detail_weight = det_weight_24
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_24 , detail_weight)

    if det_weight_25 > 0:
        detail_no_25 = "25"
        detail_weight = det_weight_25
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_25 , detail_weight)

    if det_weight_26 > 0:
        detail_no_26 = "26"
        detail_weight = det_weight_26
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_26 , detail_weight)

    if det_weight_27 > 0:
        detail_no_27 = "27"
        detail_weight = det_weight_27
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_27 , detail_weight)

    if det_weight_28 > 0:
        detail_no_28 = "28"
        detail_weight = det_weight_28
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_28 , detail_weight)

    if det_weight_29 > 0:
        detail_no_29 = "29"
        detail_weight = det_weight_29
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_29 , detail_weight)

    if det_weight_30 > 0:
        detail_no_30 = "30"
        detail_weight = det_weight_30
        save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_30 , detail_weight)

    ajax_proj7_page3_save_waste_daily_transaction = "save data daily record successful"
    return HttpResponse(ajax_proj7_page3_save_waste_daily_transaction)

# db_item_master = Waste_item_master_list.objects.filter(waste_group_code=group_search_post).exists()
@csrf_exempt
def proj7_page3_search_waste_daily_transaction(request):
    group_search_post = request.POST['group_search']
    factory_search_post = request.POST['factory_search']
    select_date_val_post  = request.POST['select_date_val']
    print(group_search_post)
    print(factory_search_post)
    print(select_date_val_post)

    df_daily_transaction_val = pd.DataFrame(list(Waste_daily_transaction.objects.filter(date_take_off=select_date_val_post , factory_name = factory_search_post , waste_group_code = group_search_post).values()))
    df_daily_transaction_val['weight'] = df_daily_transaction_val['weight'].astype(float)
    print(df_daily_transaction_val)

    json_records = df_daily_transaction_val.reset_index().to_json(orient='records')
    data_loads = json.loads(json_records)
    ajax_proj7_page3_search_daily_transaction = dumps(data_loads)

    return HttpResponse(ajax_proj7_page3_search_daily_transaction)
    