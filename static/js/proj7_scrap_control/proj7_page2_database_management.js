$(document).ready(function() {
    // <!-- Upload waste item master list -->
    $("#btn_upload_waste_item_master_list").click(function(event) {
        event.preventDefault();
        var form = this.form;
        var data = new FormData(form);
        var url = form.action;
        let get_path_file_excel_waste_item_master_list = $('#upload_file_waste_item_master_list').val();

        if (get_path_file_excel_waste_item_master_list == "") {
            alert("Please select file waste item master list")
            $('#upload_file_waste_item_master_list').focus();
            return;
        }
        $.ajax({
            url: 'proj7_page2_upload_file_waste_item_master_list', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: data, // ข้อมูลที่จะถูกส่งไปกับ url
            processData: false,
            contentType: false,

            success: function(ajax_proj7_page2_upload_file_waste_item_master_list) {
                console.log(ajax_proj7_page2_upload_file_waste_item_master_list);
                alert(ajax_proj7_page2_upload_file_waste_item_master_list)
                $('#upload_file_waste_item_master_list').val("");
            }
        })
    })

    // <!-- Upload waste group master list -->
    $("#btn_upload_waste_group_master_list").click(function(event) {
        event.preventDefault();
        var form = this.form;
        var data = new FormData(form);
        var url = form.action;
        let get_path_file_excel_waste_group_master_list = $('#upload_file_waste_group_master_list').val();

        if (get_path_file_excel_waste_group_master_list == "") {
            alert("Please select file waste group master list")
            $('#upload_file_waste_group_master_list').focus();
            return;
        }
        $.ajax({
            url: 'proj7_page2_upload_file_waste_group_master_list', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: data, // ข้อมูลที่จะถูกส่งไปกับ url
            processData: false,
            contentType: false,

            success: function(ajax_proj7_page2_upload_file_waste_group_master_list) {
                console.log(ajax_proj7_page2_upload_file_waste_group_master_list);
                alert(ajax_proj7_page2_upload_file_waste_group_master_list)
                $('#upload_file_waste_group_master_list').val("");
            }
        })
    })

    // <!-- Upload waste item price list -->
    $("#btn_upload_waste_item_price_list").click(function(event) {
        event.preventDefault();
        var form = this.form;
        var data = new FormData(form);
        var url = form.action;
        let get_path_file_excel_waste_item_price_list = $('#upload_file_waste_item_price_list').val();

        if (get_path_file_excel_waste_item_price_list == "") {
            alert("Please select file waste item price list")
            $('#upload_file_waste_item_price_list').focus();
            return;
        }
        $.ajax({
            url: 'proj7_page2_upload_file_waste_item_price_list', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: data, // ข้อมูลที่จะถูกส่งไปกับ url
            processData: false,
            contentType: false,

            success: function(ajax_proj7_page2_upload_file_waste_item_price_list) {
                console.log(ajax_proj7_page2_upload_file_waste_item_price_list);
                alert(ajax_proj7_page2_upload_file_waste_item_price_list)
                $('#upload_file_waste_item_price_list').val("");
            }
        })
    })

    // <!-- Upload Company master list -->
    $("#btn_upload_company_master_list").click(function(event) {
        event.preventDefault();
        var form = this.form;
        var data = new FormData(form);
        var url = form.action;
        let get_path_file_excel_company_master_list = $('#upload_file_company_master_list').val();

        if (get_path_file_excel_company_master_list == "") {
            alert("Please select file Company master list")
            $('#upload_file_company_master_list').focus();
            return;
        }
        $.ajax({
            url: 'proj7_page2_upload_file_company_master_list', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: data, // ข้อมูลที่จะถูกส่งไปกับ url
            processData: false,
            contentType: false,

            success: function(ajax_proj7_page2_upload_file_company_master_list) {
                console.log(ajax_proj7_page2_upload_file_company_master_list);
                alert(ajax_proj7_page2_upload_file_company_master_list)
                $('#upload_file_company_master_list').val("");
            }
        })
    })

    // <!-- Upload Company contact name list -->
    $("#btn_upload_company_contact_name_list").click(function(event) {
        event.preventDefault();
        var form = this.form;
        var data = new FormData(form);
        var url = form.action;
        let get_path_file_excel_company_contact_name_list = $('#upload_file_company_contact_name_list').val();

        if (get_path_file_excel_company_contact_name_list == "") {
            alert("Please select file Company contact name list")
            $('#upload_file_company_contact_name_list').focus();
            return;
        }
        $.ajax({
            url: 'proj7_page2_upload_file_company_contact_name_list', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: data, // ข้อมูลที่จะถูกส่งไปกับ url
            processData: false,
            contentType: false,

            success: function(ajax_proj7_page2_upload_file_company_contact_name_list) {
                console.log(ajax_proj7_page2_upload_file_company_contact_name_list);
                alert(ajax_proj7_page2_upload_file_company_contact_name_list)
                $('#upload_file_company_contact_name_list').val("");
            }
        })
    })

    // <!-- Upload waste item map factory -->
    $("#btn_upload_waste_item_map_factory").click(function(event) {
        event.preventDefault();
        var form = this.form;
        var data = new FormData(form);
        var url = form.action;
        let get_path_file_excel_waste_item_map_factory = $('#upload_file_waste_item_map_factory').val();

        if (get_path_file_excel_waste_item_map_factory == "") {
            alert("Please select file waste item map factory")
            $('#upload_file_waste_item_map_factory').focus();
            return;
        }
        $.ajax({
            url: 'proj7_page2_upload_file_waste_item_map_factory', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: data, // ข้อมูลที่จะถูกส่งไปกับ url
            processData: false,
            contentType: false,

            success: function(ajax_proj7_page2_upload_file_waste_item_map_factory) {
                console.log(ajax_proj7_page2_upload_file_waste_item_map_factory);
                alert(ajax_proj7_page2_upload_file_waste_item_map_factory)
                $('#upload_file_waste_item_map_factory').val("");
            }
        })
    })
})