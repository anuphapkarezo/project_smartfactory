$(document).ready(function() {
    $('#opt_select_factory').focus()


    $.ajax({
        url: 'proj7_page3_record_weight_waste_scrap', // เรียกใช้ URL
        type: 'post', // ประเภทของการส่งข้อมูล
        data: { // ข้อมูลที่จะถูกส่งไปกับ url
        },
        success: function(ajax_proj7_page3_record_weight_waste_scrap) {
            // console.log(ajax_selection_values);
            let before_select = '<select name="" id="opt_select_group">'
            let default_select = '<option value="default" selected>Please select group</option>'
            let after_select = '</select>'
            var select_group;
            let row_option_value = '';

            let json_txt = JSON.parse(ajax_proj7_page3_record_weight_waste_scrap)
            let row_no = 0

            $.each(json_txt, function(key, value_db) {
                    row_no += 1;
                    row_option_value += '<option value="' + value_db.waste_group_code + '" name="' + value_db.waste_group_code + '">' + value_db.group_name + '</option>'
                })
                // console.log(row_option_value);
            select_group = before_select + default_select + row_option_value + after_select
                // console.log(select_group);
            $('#opt_select_group').html(select_group);
        }
    })
    $('#btn_search_item').click(function() {
        var today_date = new Date();
        var dd = String(today_date.getDate()).padStart(2, '0');
        var mm = String(today_date.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today_date.getFullYear();
        today_date = dd + '/' + mm + '/' + yyyy;

        var select_date = ($('#opt_select_date').val());
        if (select_date == "") {
            alert("Please select date take off")
            return
        }
        select_dt = new Date($('#opt_select_date').val());
        var select_day = select_dt.getDate();
        var select_month = select_dt.getMonth() + 1;
        var select_year = select_dt.getFullYear();
        select_date_val = select_day + '/' + select_month + '/' + select_year;

        let input_group_search = $('#opt_select_group').val();
        let input_factory = $('#opt_select_factory').val();

        if (input_group_search == "default") {
            alert("Please select group try again")
            $('#opt_select_group').focus();
            return;
        }

        $.ajax({
            url: 'proj7_page3_record_weight_waste_scrap_search_item', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: { // ข้อมูลที่จะถูกส่งไปกับ url
                'group_search': input_group_search,
                'factory_search': input_factory
            },
            success: function(ajax_proj7_page3_record_weight_waste_scrap_search_item) {
                let json_txt = JSON.parse(ajax_proj7_page3_record_weight_waste_scrap_search_item)
                let row_no = 0
                let row
                $.each(json_txt, function(key, value_db) {
                    row_no += 1;
                    row += '<tr>' +
                        '<td class="set_margin_td to_modal_factory">' + input_factory + '</td>' +
                        '<td class="set_margin_td">' + value_db.group_name + '</td>' +
                        '<td class="set_margin_td to_modal_dto">' + select_date_val + '</td>' +
                        '<td class="set_margin_td to_modal_item">' + value_db.waste_item_code + ' / ' + value_db.description_EN + '</td>' +
                        '<td class="set_textbox_td"><input type="text" class="disabled_txt" id="txt_total" value=""></td>' +
                        '<td class="set_textbox_td"><input type="text" class="disabled_txt" id="txt_detail" value=""></td>' +
                        '<td class="set_margin_td">Anupab.K</td>' +
                        '<td class="set_margin_td">' + today_date + '</td>' +
                        '<td class="set_margin_td"><input type="button" class="btn btn-sm btn-warning btn_add" id="btn_add" value="Key Weight" data-toggle="modal" data-target="#modal_key_weight"></td>' +
                        '</tr>'
                })
                $('.tbody_record_weight_waste_scrap').html(row);
                $('.disabled_txt').prop('disabled', true);
            }
        })
    })

    $(document).on('click', '.btn_add', function(e) { // click edit consumption plan
        $("#modal_txt_total").focus();

        $('#modal_txt_factory').prop('disabled', true);
        $('#modal_txt_dto').prop('disabled', true);
        $('#modal_txt_waste_item').prop('disabled', true);

        $('.item_txt').prop('disabled', true);

        var tr = $(this).closest('tr');
        let modal_factory = tr.find('.to_modal_factory').text();
        let modal_dto = tr.find('.to_modal_dto').text();
        let modal_item = tr.find('.to_modal_item').text();

        $("#modal_txt_factory").val(modal_factory);
        $("#modal_txt_dto").val(modal_dto);
        $("#modal_txt_waste_item").val(modal_item);
    });

    $(document).on('change', '.item_txt', function(e) {
        var tr = $(this).closest('tr');

        let total_w = parseFloat($('#modal_txt_total').val());
        let sum_w = parseFloat($("#modal_lbl_sum").text());
        let detail_1 = parseFloat(tr.find('.item_txt').val());
        sum_w = (sum_w + detail_1).toFixed(2)

        if (sum_w > total_w) {
            alert("Warning !!! => Weight detail more than Weight total")
            tr.find('.item_txt').val('');
            tr.find('.item_txt').focus()
            return;
        }
        if (sum_w == total_w) {
            $("#modal_lbl_sum").css("color", "green");
        }
        console.log(sum_w, '/', total_w);
        $("#modal_lbl_sum").text(sum_w);
    })

    $(document).on('change', '#modal_txt_total', function(e) {
        $('#modal_txt_total').prop('disabled', true);
        let total_val = $('#modal_txt_total').val();
        if (total_val == 0 || total_val == " ") {
            alert("Please key Total Weight")
            $('.item_txt').prop('disabled', true);
            $('#modal_txt_total').focus()
            return;
        }
        $('.item_txt').prop('disabled', false);
        $('#det_weight_1').focus()

        console.log(total_val);
    })

    $('#btn_cancel').click(function() {
        $('.item_txt').val('');
        $("#modal_txt_total").val('');
        $("#modal_lbl_sum").text(0);
        $("#modal_lbl_sum").css("color", "red");
        $('.item_txt').prop('disabled', true);
        $('#modal_txt_total').prop('disabled', false);

        $("#modal_txt_total").focus();
    })

    $('#btn_confirm').click(function() {
        let total_w = parseFloat($('#modal_txt_total').val());
        let sum_w = parseFloat($("#modal_lbl_sum").text());
        if (total_w > sum_w) {
            alert("Warning !!! => Weight detail less than Weight total")
            $('#det_weight_1').focus()
            return;
        }
        date_take_off = $('#modal_txt_dto').val()
        factory_name = $('#modal_txt_factory').val()
        alert(date_take_off)
    })
})