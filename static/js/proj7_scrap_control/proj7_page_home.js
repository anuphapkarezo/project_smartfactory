function load_user() {
    $.ajax({ // search process        
        url: 'proj7_page1_login_check_user',
        type: 'post',
        data: {

        },
        success: function(ajax_proj7_page1_login_check_user) {
            console.log(ajax_proj7_page1_login_check_user);
            let full_name = '<span class="" id="user_name" style="color: white;">' + ajax_proj7_page1_login_check_user + '</span>'
            $('#user_name').html(full_name);
        }
    })
}