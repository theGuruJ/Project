
window.onload = myApp();

function myApp() {

var active_modal;

var notif_next_modal;

var login_status;

var button_retrieve_movies = document.getElementById('get_movie_details');
var modal = document.getElementsByClassName('modal')[0];
var modal_1 = document.getElementsByClassName('modal_content_ticket')[0];
var modal_2 = document.getElementsByClassName('modal_content_signin')[0];
var modal_3 = document.getElementsByClassName('modal_content_register')[0];
var modal_notif = document.getElementsByClassName('modal_notification')[0];
var button_register_modal = document.getElementById('button_register')
var button_signin_modal = document.getElementById('button_signin')
var submit_form_register = document.forms['form_register'];
var form_signin = document.forms['form_signin'];
var submit_button_signin = document.getElementById("submit_signin")
var submit_button_register = document.getElementById("submit_register")
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0]; // revert this to [0] if experiment does not work.
var close_span_signin = document.getElementById("close_signin");
var close_span_register = document.getElementById("close_register");
var close_span_notif = document.getElementById("close_notif");
var button_select_no_of_seats = document.forms['form_select_no_of_seats'];
// let submit_movie_selection = document.forms['movie_selection'];
var button_submit_movie_selection = document.getElementById("submit_movie_selection");

document.getElementById("no_of_seats_display").innerText = document.getElementById("no_of_seat_selection").value;


submit_form_register.addEventListener('submit', func_submit_form_register);
button_register_modal.addEventListener('click', launch_register_modal)
button_signin_modal.addEventListener('click', launch_signin_modal);
button_retrieve_movies.addEventListener('click',get_movie_details_request);
get_movie_details_request();

// When the user clicks on <span> (x), close the modal - add cleanup code in this.
// When the user clicks anywhere outside of the modal, close it

button_select_no_of_seats.addEventListener('submit',get_ticket_details);
button_submit_movie_selection.addEventListener('click',check_login);

modal.onclick = function(event) {
    if (event.target == modal){
        if (active_modal != modal_notif){
            active_modal.style.display = "none";
            modal.style.display = "none";
            active_modal = undefined;
        };
    };
};

submit_button_signin.addEventListener('click', func_submit_form_signin);

submit_button_register.addEventListener('click', func_submit_form_register);

// add functions after this line

function check_login(event) {
    if (!document.cookie){
        launch_signin_modal()
    } else if (document.cookie.match(/session_id=[^;]+/)[0]) {
        func_submit_movie_selection();
    }
};

function launch_register_modal(){    
    modal.style.display = "block";
    active_modal = modal_3;
    modal_3.style.display = "block";
};

function launch_signin_modal(event){
    modal.style.display = "block";
    active_modal = modal_2;
    modal_2.style.display = "block";
    console.info("this line ran... YAAY!");
};

span.onclick = function() {
    active_modal.style.display = "none";
    modal.style.display = "none";
    active_modal = undefined
}

close_span_signin.onclick = function() {
    active_modal.style.display = "none";
    modal.style.display = "none";
    active_modal = undefined
}

close_span_register.onclick = function() {
    active_modal.style.display = "none";
    modal.style.display = "none";
    active_modal = undefined
}

close_span_notif.onclick = function() {
    modal_notif.querySelector("#notif").innerHTML = "";
    active_modal.style.display = "none";
    // modal.style.display = "none";
    active_modal = notif_next_modal;
    active_modal.style.display = "block";

}

//getting the details of movies
function get_movie_details_request(){
    var request_movies = new XMLHttpRequest();
    request_movies.open("GET", "/display_movie", true);
    request_movies.responseType = "json"
    request_movies.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //Typical action to be performed when the document is ready:
            //console.log(request_movies.response);
            let movie_data = request_movies.response;
            let movie_details = movie_data;
            populate_movies(movie_data);
            // console.info(movie_data)
        }
    };
    request_movies.send();
};

function func_submit_movie_selection(event){

    console.info("movie selection submit button clicked");
    var movie_selection = document.getElementById('movie_selection1_select').value;
    console.info(movie_selection);
    var form_contact_movie_selection = document.forms['form_select_no_of_seats'].elements.namedItem('form_contact_movie_selection');
    form_contact_movie_selection.value = movie_selection;
    // event.preventDefault();
    //console.info(movie_data[movie_selection].avail_seats);
    var get_no_of_avail_seats = new XMLHttpRequest();
    get_no_of_avail_seats.open("POST", "/no_of_seats_avail", true);
    // get_no_of_avail_seats.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    get_no_of_avail_seats.responseType = "json";
    get_no_of_avail_seats.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            validate_no_of_available_seats(get_no_of_avail_seats.response["no_of_seats"]);
            active_modal = modal_1;
            modal.style.display = "block";
            modal_1.style.display = "block";
            // when validated no of seats is passed to the next function, the modal is called.
            // this will be needed to be altered when checking for available seats and raising alert for letting a user know if seats are available.
            }
        }
    text_to_send = { "movie_name" : movie_selection} ;
    get_no_of_avail_seats.send(JSON.stringify(text_to_send)); 
    
    };

function get_ticket_details(event){
    var selected_no_of_seats = document.getElementById('no_of_seat_selection').value;
    // var form_contact_no_of_seats = document.forms['contact'].elements.namedItem('no_of_seats');
    // form_contact_no_of_seats.value = selected_no_of_seats;
    console.info(selected_no_of_seats);
    console.info("being implemented now!")
    var form_get_user_details = document.forms['form_select_no_of_seats'];
    data_to_send = {
        movie_name : form_get_user_details.elements.namedItem('form_contact_movie_selection').value,
        name : form_get_user_details.elements.namedItem('bname').value,
        noOfSeats: form_get_user_details.elements.namedItem('seats').value,
        phoneNumber : form_get_user_details.elements.namedItem('phonenumber').value,
        email : form_get_user_details.elements.namedItem('email').value
    };
    console.info(form_get_user_details.elements.namedItem('bname').value)
    event.preventDefault();
    console.info(data_to_send);
    var book_ticket = new XMLHttpRequest();
    book_ticket.open("POST", "/book_ticket", true);
    book_ticket.responseType = "json";
    book_ticket.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        window.response_from_server = book_ticket.response;
    };
    };
    book_ticket.send(JSON.stringify(data_to_send));
        //document.location.reload(true)
    };

function validate_no_of_available_seats(no_of_seats_in_selected_movie){
    // var data_to_send = new FormData();
    // data_to_send.append('movie_name',movie_selection);
    // console.info(data_to_send);
    console.info(no_of_seats_in_selected_movie);
    //no_of_seats_in_selected_movie  = movie_data[movie_selection].avail_seats;
    if (no_of_seats_in_selected_movie == 0){
        console.info("no seats available, choose another movie!"); //use notif here.
    } else {
        console.info("Select the number of seats you want to book.") //use notif here.
        let seat_selection = document.getElementById("no_of_seat_selection");
        max_no_of_seats_allowed = Math.min(6,no_of_seats_in_selected_movie);
        seat_selection.max = max_no_of_seats_allowed;
        seat_selection.placeholder = "Max no. of seats :"+max_no_of_seats_allowed;
    }
    };


function populate_movies(movie_data){
    console.info(movie_data);
    console.info("this happened");
    var movie_list_select_element = document.getElementById("movie_selection1_select");
    
    for (option in movie_list_select_element.children){
        movie_list_select_element.remove(option);
    };

    for (var key in movie_data) {
        if (movie_data.hasOwnProperty(key)) {
            var element = document.createElement('option');
            element.value = key;
            element.text = movie_data[key].name+": "+movie_data[key].avail_seats+" seats available";
            movie_list_select_element.appendChild(element);
        }
    }
};

function func_submit_form_register(event){
    event.preventDefault();
    data_to_send = {
        email_address : submit_form_register.children.name_customer_email.value,
        password : submit_form_register.children.name_cx_password.value,
        customer_name : submit_form_register.children.name_customer_name.value,
        phone_number : submit_form_register.children.name_cx_phone_number.value
    }
    var register_new_cx = new XMLHttpRequest();
    register_new_cx.open("POST", "/register", true);
    register_new_cx.responseType = "json";
    register_new_cx.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let registration_status = register_new_cx.response;
            }
        }
    register_new_cx.send(JSON.stringify(data_to_send));

    };

function func_submit_form_signin(event){
    //needs to be modified. do not use yet
        // form_signin
        event.preventDefault();
        data_to_send = {
            email_address : form_signin.children.user_name.value,
            password : form_signin.children.password.value,
        }
    
        var signin_cx = new XMLHttpRequest();
        signin_cx.open("POST", "/login", true);
        signin_cx.responseType = "json";
        signin_cx.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                let login_status = signin_cx.response;
                notif_next_modal = modal_1
                notification(login_status['status'],notif_next_modal);

                }
            }
        signin_cx.send(JSON.stringify(data_to_send));    
        };

function notification(message, notif_next_modal) {

    modal_notif.querySelector("#notif").innerHTML = message
    modal.style.display = "block";
    active_modal.style.display = "none"
    active_modal = modal_notif;
    active_modal.style.display = "block"
    }
     
    
}