from django.urls import path , include
from . import views

urlpatterns = [
    # Basic HTML
    path('index',views.go_index),
    path('go_form1',views.go_form1),
    path('go_class',views.go_class),
    path('go_boxinline',views.go_boxinline),
    path('go_absolute',views.go_absolute),
    path('go_Universal',views.go_Universal),
    path('go_font',views.go_font),
    path('go_width',views.go_width),
    path('go_border',views.go_border),


    # PCTT Project for P' Tukta
    path('page_master_machine_pcap',views.page_master_machine_pcap),
    path('Page_master_machine_FPC',views.Page_master_machine_FPC),
    path('Page_master_clean_scan',views.Page_master_clean_scan),
    path('Page_master_clean_query_lot',views.Page_master_clean_query_lot),
    path('Page_report_product_transfer_to_WH',views.Page_report_product_transfer_to_WH),
    path('Page_report_product_std_leadtime',views.Page_report_product_std_leadtime),
    path('Page_report_item_inventory_data',views.Page_report_item_inventory_data),
    path('Page_FPC_system_cancel_lot',views.Page_FPC_system_cancel_lot),
    path('Page_FPC_system_check_scan_MAT',views.Page_FPC_system_check_scan_MAT),
    path('Page_FPC_system_test_formulas',views.Page_FPC_system_test_formulas),
    path('Page_main_menu',views.Page_main_menu),

    

    path('Page_Login',views.Page_Login),

    # Smart scrap control
        # Go to page > Record weight
    path('go_html_record_weight',views.go_html_record_weight),

        # Function for page1
    path('proj7_read_database_product',views.proj7_read_database_product),
    path('proj_page1_delete_waste_item_master',views.proj_page1_delete_waste_item_master),

        # Function for page database_management
    path('go_html_database_management',views.go_html_database_management),
    path('proj7_page2_upload_file_waste_item_master_list',views.proj7_page2_upload_file_waste_item_master_list),
    path('proj7_page2_upload_file_waste_group_master_list',views.proj7_page2_upload_file_waste_group_master_list),
    path('proj7_page2_upload_file_waste_item_price_list',views.proj7_page2_upload_file_waste_item_price_list),
    path('proj7_page2_upload_file_waste_item_map_factory',views.proj7_page2_upload_file_waste_item_map_factory),
    
    path('proj7_page2_upload_file_company_master_list',views.proj7_page2_upload_file_company_master_list),
    path('proj7_page2_upload_file_company_contact_name_list',views.proj7_page2_upload_file_company_contact_name_list),

    # Function for page record_weight_waste_scrap
    path('go_html_record_weight_waste_scrap',views.go_html_record_weight_waste_scrap),
    path('proj7_page3_record_weight_waste_scrap',views.proj7_page3_record_weight_waste_scrap),
    path('proj7_page3_record_weight_waste_scrap_search_item',views.proj7_page3_record_weight_waste_scrap_search_item),
    path('proj7_page3_save_waste_daily_transaction',views.proj7_page3_save_waste_daily_transaction),
]