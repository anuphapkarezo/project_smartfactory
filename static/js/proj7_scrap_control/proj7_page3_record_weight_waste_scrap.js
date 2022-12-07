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
        // $('#btn_search_item').click(function() {
        //     var today_date = new Date();
        //     var dd = String(today_date.getDate()).padStart(2, '0');
        //     var mm = String(today_date.getMonth() + 1).padStart(2, '0'); //January is 0!
        //     var yyyy = today_date.getFullYear();
        //     today_date = dd + '/' + mm + '/' + yyyy;

    //     var select_date = ($('#opt_select_date').val());
    //     if (select_date == "") {
    //         alert("Please select date take off")
    //         return
    //     }
    //     select_dt = new Date($('#opt_select_date').val());
    //     var select_day = select_dt.getDate();
    //     var select_month = select_dt.getMonth() + 1;
    //     var select_year = select_dt.getFullYear();
    //     select_date_val = select_day + '/' + select_month + '/' + select_year;

    //     let input_group_search = $('#opt_select_group').val();
    //     let input_factory = $('#opt_select_factory').val();
    //     console.log(input_factory);

    //     if (input_group_search == "default") {
    //         alert("Please select group try again")
    //         $('#opt_select_group').focus();
    //         return;
    //     }

    //     $.ajax({
    //         url: 'proj7_page3_record_weight_waste_scrap_search_item', // เรียกใช้ URL
    //         type: 'post', // ประเภทของการส่งข้อมูล
    //         data: { // ข้อมูลที่จะถูกส่งไปกับ url
    //             'group_search': input_group_search,
    //             'factory_search': input_factory
    //         },
    //         success: function(ajax_proj7_page3_record_weight_waste_scrap_search_item) {
    //             let json_txt = JSON.parse(ajax_proj7_page3_record_weight_waste_scrap_search_item)
    //             let row_no = 0
    //             let row
    //             $.each(json_txt, function(key, value_db) {
    //                 row_no += 1;
    //                 row += '<tr>' +
    //                     '<td class="set_margin_td to_modal_factory">' + input_factory + '</td>' +
    //                     '<td class="set_margin_td"> <label for="" class="to_modal_group_code" id="lbl_group_code">' + input_group_search + '</label> / ' + value_db.group_name + '</td>' +
    //                     '<td class="set_margin_td to_modal_dto">' + select_date_val + '</td>' +
    //                     '<td class="set_margin_td "> <label for="" class="to_modal_item">' + value_db.waste_item_code + '</label> / <label for="" class="to_modal_desc">' + value_db.description_EN + '</label></td>' +
    //                     '<td class="set_textbox_td"><input type="text" class="disabled_txt txt_total" id="txt_total_' + input_factory + '_' + value_db.waste_item_code + '" value="' + value_db.weight + '"></td>' +
    //                     '<td class="set_textbox_td"><input type="text" class="disabled_txt txt_detail" id="txt_detail_' + input_factory + '_' + value_db.waste_item_code + '" value="' + value_db.weight + '"></td>' +
    //                     '<td class="set_margin_td">Anupab.K</td>' +
    //                     '<td class="set_margin_td">' + today_date + '</td>' +
    //                     '<td class="set_margin_td"><input type="button" class="btn btn-sm btn-warning btn_add" id="btn_add" value="Key Weight" data-toggle="modal" data-target="#modal_key_weight"></td>' +
    //                     '</tr>'
    //             })
    //             $('.tbody_record_weight_waste_scrap').html(row);
    //             $('.disabled_txt').prop('disabled', true);
    //         }
    //     })
    // })

    $(document).on('click', '#btn_search_item', function(e) {
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
        console.log(input_factory);

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
                'factory_search': input_factory,
                'select_date_val': select_date_val
            },
            success: function(ajax_proj7_page3_record_weight_waste_scrap_search_item) {
                let json_txt = JSON.parse(ajax_proj7_page3_record_weight_waste_scrap_search_item)
                let row_no = 0
                let row
                $.each(json_txt, function(key, value_db) {
                    row_no += 1;
                    row += '<tr>' +
                        '<td class="set_margin_td to_modal_factory">' + input_factory + '</td>' +
                        '<td class="set_margin_td"> <label for="" class="to_modal_group_code" id="lbl_group_code">' + input_group_search + '</label> / ' + value_db.group_name + '</td>' +
                        '<td class="set_margin_td to_modal_dto">' + select_date_val + '</td>' +
                        '<td class="set_margin_td "> <label for="" class="to_modal_item">' + value_db.waste_item_code + '</label> / <label for="" class="to_modal_desc">' + value_db.description_EN + '</label></td>' +
                        // '<td class="set_textbox_td"><input type="text" class="disabled_txt txt_total" id="txt_total_' + input_factory + '_' + value_db.waste_item_code + '" value="' + value_db.weight + '"> <label class="label_export label_total" for="" id="label_total_' + input_factory + '_' + value_db.waste_item_code + '">' + value_db.weight + '</label></td>' +
                        '<td class="set_textbox_td"><label class="label_export label_total" for="" id="label_total_' + input_factory + '_' + value_db.waste_item_code + '">' + value_db.weight + '</label></td>' +
                        // '<td class="set_textbox_td"><input type="text" class="disabled_txt txt_detail" id="txt_detail_' + input_factory + '_' + value_db.waste_item_code + '" value="' + value_db.weight + '"> <label class="label_export label_detail" for="" id="label_detail_' + input_factory + '_' + value_db.waste_item_code + '">' + value_db.weight + '</label></td>' +
                        '<td class="set_textbox_td"><label class="label_export label_detail" for="" id="label_detail_' + input_factory + '_' + value_db.waste_item_code + '">' + value_db.weight + '</label></td>' +
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

    $(document).on('click', '.btn_add', function(e) {
        // Reset Modal
        $('.item_txt').val('');
        $("#modal_txt_total").val('');
        $("#modal_lbl_sum").text(0);
        $("#modal_lbl_sum_before").text(0);
        $("#modal_lbl_sum").css("color", "red");
        $('.item_txt').prop('disabled', true);
        $('#modal_txt_total').prop('disabled', false);

        $("#modal_txt_total").focus();


        var tr = $(this).closest('tr');

        $("#modal_txt_total").focus();
        $('.item_txt').prop('disabled', true);

        let modal_factory = tr.find('.to_modal_factory').text();
        let modal_group_code = tr.find('.to_modal_group_code').text();
        let modal_dto = tr.find('.to_modal_dto').text();
        let modal_item = tr.find('.to_modal_item').text();
        let modal_desc = tr.find('.to_modal_desc').text();

        // let tr_total = '#txt_total_' + modal_factory + '_' + modal_item
        // let tr_detail = '#txt_detail_' + modal_factory + '_' + modal_item

        let lbl_total = '#label_total_' + modal_factory + '_' + modal_item
        let lbl_detail = '#label_detail_' + modal_factory + '_' + modal_item

        let tr_total_search = tr.find(lbl_total).text();
        let tr_detail_serach = tr.find(lbl_detail).text();

        if (tr_total_search > 0) {
            $('.item_txt').prop('disabled', false);
            $.ajax({
                url: 'proj7_page3_search_waste_daily_transaction', // เรียกใช้ URL
                type: 'post', // ประเภทของการส่งข้อมูล
                data: { // ข้อมูลที่จะถูกส่งไปกับ url
                    'waste_item_code': modal_item,
                    'factory_search': modal_factory,
                    'select_date_val': modal_dto
                },
                success: function(ajax_proj7_page3_search_waste_daily_transaction) {
                    let json_txt = JSON.parse(ajax_proj7_page3_search_waste_daily_transaction)
                    let row_no = 0

                    $.each(json_txt, function(key, value_db) {
                        let sum_det = parseFloat($('#modal_lbl_sum').text())

                        let detail_no_json = value_db.detail_no
                        let weight_json = value_db.weight

                        let id_detail = "#det_weight_" + detail_no_json
                        let sum_w = ((sum_det + weight_json)).toFixed(2)

                        $(id_detail).val(weight_json);
                        $(id_detail).prop('disabled', true);

                        if (tr_total_search != sum_det) {
                            $('#modal_lbl_sum').text(sum_w);
                        }

                        if (sum_w = tr_total_search) {
                            $("#modal_lbl_sum").css("color", "green");
                        } else {
                            $("#modal_lbl_sum").css("color", "red");
                        }
                    })
                    $("#modal_txt_factory").text(modal_factory);
                    $("#modal_txt_dto").text(modal_dto);
                    $("#modal_txt_waste_item").text(modal_item);
                    $("#modal_txt_waste_desc").text(modal_desc);
                    $("#model_lbl_group_code").text(modal_group_code);
                    // $("#modal_tr_total").text(tr_total);
                    // $("#modal_tr_detail").text(tr_detail);
                    $("#modal_label_total").text(lbl_total);
                    $("#modal_label_detail").text(lbl_detail);

                    $("#modal_txt_total").val(tr_total_search);
                }
            })
        } else {
            $("#modal_txt_factory").text(modal_factory);
            $("#modal_txt_dto").text(modal_dto);
            $("#modal_txt_waste_item").text(modal_item);
            $("#modal_txt_waste_desc").text(modal_desc);
            $("#model_lbl_group_code").text(modal_group_code);
            // $("#modal_tr_total").text(tr_total);
            // $("#modal_tr_detail").text(tr_detail);
            $("#modal_label_total").text(lbl_total);
            $("#modal_label_detail").text(lbl_detail);
        }
    });

    $(document).on('change', '.item_txt', function(e) {
        var tr = $(this).closest('tr');

        let total_w = parseFloat($('#modal_txt_total').val());

        let detail_1 = parseFloat(tr.find('.item_txt').val());

        let sum_w = parseFloat($("#modal_lbl_sum").text());
        // let sum_w_before = parseFloat();
        // let sum_w_before = parseFloat($("#modal_lbl_sum_before").text());

        sum_w = ((sum_w + detail_1)).toFixed(2)
            // sum_w_before = (sum_w - detail_1).toFixed(2)

        if (detail_1 >= 0) {
            $("#modal_lbl_sum").text(sum_w);
            // $("#modal_lbl_sum_before").text(sum_w_before);
            tr.find('.item_txt').prop('disabled', true)
            $("#modal_lbl_sum_before").text('0.00');
        } else {
            alert("Please key detail weight in numbers.")
            tr.find('.item_txt').val('')
            tr.find('.item_txt').focus()
            return;
        }

        if (sum_w > total_w) {
            alert("Warning !!! => Weight detail more than Weight total")
            sum_w = ((sum_w - detail_1)).toFixed(2)
            $("#modal_lbl_sum").text(sum_w);
            tr.find('.item_txt').val('');
            tr.find('.item_txt').prop('disabled', false)
            tr.find('.item_txt').focus()
            return;
        }

        if (sum_w == total_w) {
            $("#modal_lbl_sum").css("color", "green");
        }

        if (sum_w < total_w) {
            $("#modal_lbl_sum").css("color", "red");
        }

    })

    $(document).on('click', '.item_txt', function(e) {
        var tr = $(this).closest('tr');
        // tr.find('.item_txt').prop('disabled', 'false')
        let detail_1 = parseFloat(tr.find('.item_txt').val());
        $("#modal_lbl_sum_before").text(detail_1);
    })

    $(document).on('click', '.btn_edit', function(e) {
        var tr = $(this).closest('tr');

        let total_w = parseFloat($("#modal_txt_total").val());
        let sum_w = parseFloat($("#modal_lbl_sum").text());
        let detail_w = parseFloat(tr.find('.item_txt').val())
        if (isNaN(detail_w)) {
            tr.find('.item_txt').focus()
            return;
        }

        sum_w = (sum_w - detail_w).toFixed(2)

        tr.find('.item_txt').prop('disabled', false)
        tr.find('.item_txt').focus()
        tr.find('.item_txt').val('');
        $("#modal_lbl_sum").text(sum_w)
        console.log(sum_w);



        if (total_w > sum_w) {
            $("#modal_lbl_sum").css("color", "red");

        } else {
            $("#modal_lbl_sum").css("color", "green");
        }

        $("#modal_lbl_sum_before").text(detail_w);

    })


    $(document).on('change', '#modal_txt_total', function(e) {
        let total_val = $('#modal_txt_total').val();
        let sum_val = $('#modal_lbl_sum').val();

        if (total_val >= 0) {
            $('#modal_txt_total').prop('disabled', true);
            $('.item_txt').prop('disabled', false);
            $('#det_weight_1').focus()
            if (total_val > sum_val) {
                $("#modal_lbl_sum").css("color", "red");
            }
        }

        if (total_val == 0 || total_val == NaN) {
            alert("Please key Total Weight")
            $('.item_txt').prop('disabled', true);
            $('#modal_txt_total').prop('disabled', false);
            $('#modal_txt_total').val('');
            $('#modal_txt_total').focus()
            return;
        }
    })

    $('#btn_cancel').click(function() {
        $('.item_txt').val('');
        $("#modal_txt_total").val('');
        $("#modal_lbl_sum").text(0);
        $("#modal_lbl_sum_before").text(0);
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

        if (isNaN(total_w)) {
            alert("Warning !!! => Please key data")
            $('#modal_txt_total').focus()
            return;
        }

        date_take_off = $('#modal_txt_dto').text()
        factory_name = $('#modal_txt_factory').text()
        waste_item_code = $('#modal_txt_waste_item').text()
        input_group_search = $('#model_lbl_group_code').text()
            // tr_txt_total = $('#modal_tr_total').text()
            // tr_txt_detail = $('#modal_tr_detail').text()
        tr_lbl_total = $('#modal_label_total').text()
        tr_lbl_detail = $('#modal_label_detail').text()

        // 1 > 10
        det_weight_1 = $('#det_weight_1').val()
        if (det_weight_1 > 0) {
            det_weight_1 = $('#det_weight_1').val()
        } else {
            det_weight_1 = 0
        }

        det_weight_2 = $('#det_weight_2').val()
        if (det_weight_2 > 0) {
            det_weight_2 = $('#det_weight_2').val()
        } else {
            det_weight_2 = 0
        }

        det_weight_3 = $('#det_weight_3').val()
        if (det_weight_3 > 0) {
            det_weight_3 = $('#det_weight_3').val()
        } else {
            det_weight_3 = 0
        }

        det_weight_4 = $('#det_weight_4').val()
        if (det_weight_4 > 0) {
            det_weight_4 = $('#det_weight_4').val()
        } else {
            det_weight_4 = 0
        }

        det_weight_5 = $('#det_weight_5').val()
        if (det_weight_5 > 0) {
            det_weight_5 = $('#det_weight_5').val()
        } else {
            det_weight_5 = 0
        }

        det_weight_6 = $('#det_weight_6').val()
        if (det_weight_6 > 0) {
            det_weight_6 = $('#det_weight_6').val()
        } else {
            det_weight_6 = 0
        }

        det_weight_7 = $('#det_weight_7').val()
        if (det_weight_7 > 0) {
            det_weight_7 = $('#det_weight_7').val()
        } else {
            det_weight_7 = 0
        }

        det_weight_8 = $('#det_weight_8').val()
        if (det_weight_8 > 0) {
            det_weight_8 = $('#det_weight_8').val()
        } else {
            det_weight_8 = 0
        }

        det_weight_9 = $('#det_weight_9').val()
        if (det_weight_9 > 0) {
            det_weight_9 = $('#det_weight_9').val()
        } else {
            det_weight_9 = 0
        }

        det_weight_10 = $('#det_weight_10').val()
        if (det_weight_10 > 0) {
            det_weight_10 = $('#det_weight_10').val()
        } else {
            det_weight_10 = 0
        }

        // 11 > 20
        det_weight_11 = $('#det_weight_11').val()
        if (det_weight_11 > 0) {
            det_weight_11 = $('#det_weight_11').val()
        } else {
            det_weight_11 = 0
        }

        det_weight_12 = $('#det_weight_12').val()
        if (det_weight_12 > 0) {
            det_weight_12 = $('#det_weight_12').val()
        } else {
            det_weight_12 = 0
        }

        det_weight_13 = $('#det_weight_13').val()
        if (det_weight_13 > 0) {
            det_weight_13 = $('#det_weight_13').val()
        } else {
            det_weight_13 = 0
        }

        det_weight_14 = $('#det_weight_14').val()
        if (det_weight_14 > 0) {
            det_weight_14 = $('#det_weight_14').val()
        } else {
            det_weight_14 = 0
        }

        det_weight_15 = $('#det_weight_15').val()
        if (det_weight_15 > 0) {
            det_weight_15 = $('#det_weight_15').val()
        } else {
            det_weight_15 = 0
        }

        det_weight_16 = $('#det_weight_16').val()
        if (det_weight_16 > 0) {
            det_weight_16 = $('#det_weight_16').val()
        } else {
            det_weight_16 = 0
        }

        det_weight_17 = $('#det_weight_17').val()
        if (det_weight_17 > 0) {
            det_weight_17 = $('#det_weight_17').val()
        } else {
            det_weight_17 = 0
        }

        det_weight_18 = $('#det_weight_18').val()
        if (det_weight_18 > 0) {
            det_weight_18 = $('#det_weight_18').val()
        } else {
            det_weight_18 = 0
        }

        det_weight_19 = $('#det_weight_19').val()
        if (det_weight_19 > 0) {
            det_weight_19 = $('#det_weight_19').val()
        } else {
            det_weight_19 = 0
        }

        det_weight_20 = $('#det_weight_20').val()
        if (det_weight_20 > 0) {
            det_weight_20 = $('#det_weight_20').val()
        } else {
            det_weight_20 = 0
        }


        // 21 > 30
        det_weight_21 = $('#det_weight_21').val()
        if (det_weight_21 > 0) {
            det_weight_21 = $('#det_weight_21').val()
        } else {
            det_weight_21 = 0
        }

        det_weight_22 = $('#det_weight_22').val()
        if (det_weight_22 > 0) {
            det_weight_22 = $('#det_weight_22').val()
        } else {
            det_weight_22 = 0
        }

        det_weight_23 = $('#det_weight_23').val()
        if (det_weight_23 > 0) {
            det_weight_23 = $('#det_weight_23').val()
        } else {
            det_weight_23 = 0
        }

        det_weight_24 = $('#det_weight_24').val()
        if (det_weight_24 > 0) {
            det_weight_24 = $('#det_weight_24').val()
        } else {
            det_weight_24 = 0
        }

        det_weight_25 = $('#det_weight_25').val()
        if (det_weight_25 > 0) {
            det_weight_25 = $('#det_weight_25').val()
        } else {
            det_weight_25 = 0
        }

        det_weight_26 = $('#det_weight_26').val()
        if (det_weight_26 > 0) {
            det_weight_26 = $('#det_weight_26').val()
        } else {
            det_weight_26 = 0
        }

        det_weight_27 = $('#det_weight_27').val()
        if (det_weight_27 > 0) {
            det_weight_27 = $('#det_weight_27').val()
        } else {
            det_weight_27 = 0
        }

        det_weight_28 = $('#det_weight_28').val()
        if (det_weight_28 > 0) {
            det_weight_28 = $('#det_weight_28').val()
        } else {
            det_weight_28 = 0
        }

        det_weight_29 = $('#det_weight_29').val()
        if (det_weight_29 > 0) {
            det_weight_29 = $('#det_weight_29').val()
        } else {
            det_weight_29 = 0
        }

        det_weight_30 = $('#det_weight_30').val()
        if (det_weight_30 > 0) {
            det_weight_30 = $('#det_weight_30').val()
        } else {
            det_weight_30 = 0
        }


        $.ajax({
            url: 'proj7_page3_save_waste_daily_transaction', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: { // ข้อมูลที่จะถูกส่งไปกับ url
                'date_take_off': date_take_off,
                'factory_search': factory_name,
                'waste_item_code': waste_item_code,
                'group_search': input_group_search,

                'det_weight_1': det_weight_1,
                'det_weight_2': det_weight_2,
                'det_weight_3': det_weight_3,
                'det_weight_4': det_weight_4,
                'det_weight_5': det_weight_5,
                'det_weight_6': det_weight_6,
                'det_weight_7': det_weight_7,
                'det_weight_8': det_weight_8,
                'det_weight_9': det_weight_9,
                'det_weight_10': det_weight_10,

                'det_weight_11': det_weight_11,
                'det_weight_12': det_weight_12,
                'det_weight_13': det_weight_13,
                'det_weight_14': det_weight_14,
                'det_weight_15': det_weight_15,
                'det_weight_16': det_weight_16,
                'det_weight_17': det_weight_17,
                'det_weight_18': det_weight_18,
                'det_weight_19': det_weight_19,
                'det_weight_20': det_weight_20,

                'det_weight_21': det_weight_21,
                'det_weight_22': det_weight_22,
                'det_weight_23': det_weight_23,
                'det_weight_24': det_weight_24,
                'det_weight_25': det_weight_25,
                'det_weight_26': det_weight_26,
                'det_weight_27': det_weight_27,
                'det_weight_28': det_weight_28,
                'det_weight_29': det_weight_29,
                'det_weight_30': det_weight_30,
            },
            success: function(ajax_proj7_page3_save_waste_daily_transaction) {
                alert(ajax_proj7_page3_save_waste_daily_transaction)
                $('#modal_txt_factory').val('')
                $('#modal_txt_dto').val('')
                $('#modal_txt_waste_item').val('')
                $('#modal_txt_total').val('')
                $('#modal_lbl_sum').text('0.00')
                $("#modal_lbl_sum").css("color", "red");
                $('#modal_lbl_sum_before').text('0.00')
                $('#model_lbl_group_code').text('')

                $('#modal_txt_total').prop('disabled', false);

                $('.item_txt').prop('disabled', true);
                $('.item_txt').val('')

                $('#modal_txt_total').focus()
                $('#modal_key_weight').modal('toggle');
                // $(tr_txt_total).val(total_w)
                // $(tr_txt_detail).val(sum_w)
                $(tr_lbl_total).text(total_w)
                $(tr_lbl_detail).text(sum_w)
            }
        })
    })

    $('#btn_export_excel').click(function() {
        var today_date = new Date();
        var dd = String(today_date.getDate()).padStart(2, '0');
        var mm = String(today_date.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today_date.getFullYear();

        var hh = String(today_date.getHours())
        var min = String(today_date.getMinutes())
        today_date = dd + mm + yyyy + hh + min;
        FILE_name = 'SummaryWeightDetail_' + today_date
        console.log(FILE_name);

        var rowCount = $('.tbody_record_weight_waste_scrap tr').length;
        if (rowCount > 0) {
            $('#tb_record_weight_waste_scrap').excelexportjs({
                containerid: 'tb_record_weight_waste_scrap',
                datatype: 'table'
            })
            $(this).attr('download', FILE_name) // set file name (you want to put formatted date here)
                .attr('href', uri) // data to download
                .attr('target', '_blank') // open in new window (optional)
        } else {
            alert("No data for export to excel")
            return
        }
    })
})