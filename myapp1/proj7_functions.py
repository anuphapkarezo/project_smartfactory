from .models import Waste_item_master_list , Waste_group_master_list , Waste_item_price_list , Waste_item_map_factory , Waste_daily_transaction
from .models import Company_master_list , Company_contact_name_list
from datetime import datetime

#Function save database > save_waste_item_master_list
def save_waste_item_master_list(df_excel):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    print(df_excel.columns)
    for i in df_excel.itertuples(index=False):
        item_code = i.waste_item_code
        desc_en = i.description_EN
        desc_th = i.description_TH
        group_code = i.waste_group_code
        unit_waste = i.waste_unit
        print(item_code, desc_en, desc_th, group_code)
        db_save = Waste_item_master_list()
        db_save.waste_item_code = item_code
        db_save.description_EN = desc_en
        db_save.description_TH = desc_th
        db_save.waste_group_code = group_code
        db_save.waste_unit = unit_waste
        db_save.update_date = datetimesave
        db_save.update_by = "Anupab.K"
        db_save.save()
        print("Save completed" , item_code , desc_en , datetimesave)

#Function update database > update_waste_item_master_list
def update_waste_item_master_list(df_update):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_update.itertuples(index=False):
        item_code = i.waste_item_code
        desc_en = i.description_EN_x
        desc_th = i.description_TH_x
        group_code = i.waste_group_code_x
        unit_waste = i.waste_unit_x
        # print("Test update")
        Waste_item_master_list.objects.filter(waste_item_code=item_code).update(
            description_EN = desc_en,
            description_TH = desc_th,
            waste_group_code = group_code,
            waste_unit = unit_waste,
            update_date = datetimesave,
            update_by = "Anupab.K"
        )

#Function save database > save_waste_group_master_list
def save_waste_group_master_list(df_excel):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    print(df_excel.columns)
    for i in df_excel.itertuples(index=False):
        waste_group_code = i.waste_group_code
        waste_group_name = i.group_name
       
        db_save = Waste_group_master_list()
        db_save.waste_group_code = waste_group_code
        db_save.group_name = waste_group_name
        db_save.update_date = datetimesave
        db_save.update_by = "Anupab.K"
        db_save.save()
        
#Function update database > update_waste_group_master_list
def update_waste_group_master_list(df_update):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_update.itertuples(index=False):
        waste_group_code = i.waste_group_code
        waste_group_name = i.group_name_x
        
        Waste_group_master_list.objects.filter(waste_group_code=waste_group_code).update(
            group_name = waste_group_name,
            update_date = datetimesave,
            update_by = "Anupab.K"
        )

#Function save database > save_waste_item_price_list  
def save_waste_item_price_list(df_excel):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    print(df_excel.columns)
    for i in df_excel.itertuples(index=False):
        item_code = i.waste_item_code
        price_waste = i.price
        price_unit = i.unit_price

        price_eff_from = i.price_effective_from
        date_code_from_get = datetime.date(price_eff_from)
        get_date_code_from = int(date_code_from_get.strftime("%Y%m%d")) 

        price_eff_to = i.price_effective_to 
        date_code_to_get = datetime.date(price_eff_to)
        get_date_code_to = int(date_code_to_get.strftime("%Y%m%d"))
        comp_code = i.company_code
       
        db_save = Waste_item_price_list()
        db_save.waste_item_code = item_code
        db_save.price = price_waste
        db_save.unit_price = price_unit
        db_save.price_effective_from = price_eff_from
        db_save.price_effective_to = price_eff_to
        db_save.date_code_from = get_date_code_from
        db_save.date_code_to = get_date_code_to
        db_save.company_code = comp_code
        db_save.update_date = datetimesave
        db_save.update_by = "Anupab.K"
        db_save.save()
        
#Function update database > update_waste_item_price_list
def update_waste_item_price_list(df_update):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_update.itertuples(index=False):
        item_code = i.waste_item_code
        price_waste = i.price_x
        price_unit = i.unit_price_x

        price_eff_from = i.price_effective_from_x
        date_code_from_get = datetime.date(price_eff_from)
        get_date_code_from = int(date_code_from_get.strftime("%Y%m%d")) 

        price_eff_to = i.price_effective_to_x
        date_code_to_get = datetime.date(price_eff_to)
        get_date_code_to = int(date_code_to_get.strftime("%Y%m%d"))

        comp_code = i.company_code_x
        
        Waste_item_price_list.objects.filter(waste_item_code=item_code).update(
            waste_item_code = item_code,
            price = price_waste,
            unit_price = price_unit,
            price_effective_from = price_eff_from,
            price_effective_to = price_eff_to,
            date_code_from = get_date_code_from,
            date_code_to = get_date_code_to,
            company_code = comp_code,
            update_date = datetimesave,
            update_by = "Anupab.K"
        )

#Function save database > save_company_master_list  
def save_company_master_list(df_excel):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_excel.itertuples(index=False):
        comp_code = i.company_code
        comp_name = i.company_name

        db_save = Company_master_list()
        db_save.company_code = comp_code
        db_save.company_name = comp_name
        db_save.update_date = datetimesave
        db_save.update_by = "Anupab.K"
        db_save.save()
        
#Function update database > update_company_master_list
def update_company_master_list(df_update):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_update.itertuples(index=False):
        comp_code = i.company_code
        comp_name = i.company_name_x
        
        Company_master_list.objects.filter(company_code=comp_code).update(
            company_code = comp_code,
            company_name = comp_name,
            update_date = datetimesave,
            update_by = "Anupab.K"
        )

#Function save database > save_company_contact_name_list  
def save_company_contact_name_list(df_excel):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    print(df_excel.columns)
    for i in df_excel.itertuples(index=False):
        comp_code = i.company_code
        cont_firstname = i.contact_firstname
        cont_lastname = i.contact_lastname
        cont_email = i.contact_email
        cont_phone = i.contact_phone

        db_save = Company_contact_name_list()
        db_save.company_code = comp_code
        db_save.contact_firstname = cont_firstname
        db_save.contact_lastname = cont_lastname
        db_save.contact_email = cont_email
        db_save.contact_phone =cont_phone
        db_save.update_date = datetimesave
        db_save.update_by = "Anupab.K"
        db_save.save()
        
#Function update database > update_company_master_list
def update_company_contact_name_list(df_update):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_update.itertuples(index=False):
        comp_code = i.company_code
        cont_firstname = i.contact_firstname_x
        cont_lastname = i.contact_lastname_x
        cont_email = i.contact_email_x
        cont_phone = i.contact_phone_x
        
        Waste_item_price_list.objects.filter(company_code=comp_code).update(
            company_code = comp_code,
            contact_firstname = cont_firstname,
            contact_lastname = cont_lastname,
            contact_email = cont_email,
            contact_phone = cont_phone,
            update_date = datetimesave,
            update_by = "Anupab.K"
        )

#Function save database > save_waste_item_map_factory  
def save_waste_item_map_factory(df_excel):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    print(df_excel.columns)
    for i in df_excel.itertuples(index=False):
        db_waste_item_code = i.waste_item_code
        db_factory_name = i.factory_name

        db_save = Waste_item_map_factory()
        db_save.waste_item_code = db_waste_item_code
        db_save.factory_name = db_factory_name
        db_save.update_date = datetimesave
        db_save.update_by = "Anupab.K"
        db_save.save()

#Function update database > update_waste_item_map_factory
def update_waste_item_map_factory(df_update):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    for i in df_update.itertuples(index=False):
        db_waste_item_code = i.waste_item_code
        db_factory_name = i.factory_name_x
        
        Waste_item_map_factory.objects.filter(waste_item_code=db_waste_item_code).update(
            waste_item_code = db_waste_item_code,
            factory_name = db_factory_name,
            update_date = datetimesave,
            update_by = "Anupab.K"
        )

#Function save database > save_waste_daily_transaction
def save_waste_daily_transaction(date_take_off , factory_search , waste_item_code , group_search , detail_no_1 , detail_weight):
    datetime_save = datetime.now()
    date_save = datetime_save.date()
    time_save = datetime_save.time()
    datesave = date_save.strftime("%d/%m/%y")
    timesave = time_save.strftime("%H:%M")
    datetimesave = str(datesave) + " " + str(timesave)

    db_save = Waste_daily_transaction()
    db_save.date_take_off = date_take_off
    db_save.factory_name = factory_search
    db_save.waste_item_code = waste_item_code
    db_save.waste_group_code = group_search
    db_save.detail_no = detail_no_1
    db_save.weight = detail_weight
    db_save.update_date = datetimesave
    db_save.update_by = "Anupab.K"
    db_save.save()