$(document).ready(function() {
    $('#txt_userName').focus()
    $('#btn_login_submit').click(function() {
        // event.preventDefault();
        // var form = this.form;
        // var data = new FormData(form);
        // var url = form.action;

        var user_login = $('#txt_userName').val()
        var pass_login = $('#txt_passWord').val()
            // console.log(user_login + ' / ' + pass_login);
        $.ajax({
            url: 'proj7_page1_login_alert', // เรียกใช้ URL
            type: 'post', // ประเภทของการส่งข้อมูล
            data: {
                'user_login_df': user_login,
                'pass_login_df': pass_login
            },
            success: function(ajax_proj7_page1_login_alert) {
                console.log(ajax_proj7_page1_login_alert);
                if (ajax_proj7_page1_login_alert != "Login Complete.") {
                    alert(ajax_proj7_page1_login_alert)
                }
            }
        })
    })
})