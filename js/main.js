

window.onload = myApp();

function myApp() {

let active_modal;

let button_retrieve_movies = document.getElementById('get_movie_details');
// Get the modal
let modal = document.getElementsByClassName('modal')[0];

let modal_1 = document.getElementsByClassName('modal_content_ticket')[0];

let modal_2 = document.getElementsByClassName('modal_content_signin')[0];

let modal_3 = document.getElementsByClassName('modal_content_register')[0];

let button_register_modal = document.getElementById('button_register')

let button_signin_modal = document.getElementById('button_signin')

let submit_form_register = document.forms['form_register'];

submit_form_register.addEventListener('submit', func_submit_form_register);

let submit_form_signin = document.forms['form_signin'];

submit_form_signin.addEventListener('submit', func_submit_form_signin);


button_register_modal.addEventListener('click', launch_register_modal)

function launch_register_modal(){    

    modal.style.display = "block";
    active_modal = modal_3;
    modal_3.style.display = "block";

};

button_signin_modal.addEventListener('click', launch_signin_modal);

function launch_signin_modal(){

    modal.style.display = "block";
    active_modal = modal_2;
    modal_2.style.display = "block";

};



// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0]; // revert this to [0] if experiment does not work.

let close_span_signin = document.getElementById("close_signin");

let close_span_register = document.getElementById("close_register");


let button_select_no_of_seats = document.forms['form_select_no_of_seats'];

let submit_movie_selection = document.forms['movie_selection'];

button_retrieve_movies.addEventListener('click',get_movie_details_request);

get_movie_details_request();


// When the user clicks on <span> (x), close the modal - add cleanup code in this.
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

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//     if (active_modal && event.target == modal)
    
//         modal.style.display = "none";

// }


button_select_no_of_seats.addEventListener('submit',get_ticket_details);

// var form_get_user_details = document.forms['contact'];

// form_get_user_details.addEventListener('submit',book_ticket);


submit_movie_selection.addEventListener('submit',func_submit_movie_selection);

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
    }
    }
    book_ticket.send(JSON.stringify(data_to_send));
        //document.location.reload(true)
    }



function func_submit_movie_selection(event){
    if (!document.cookie.match(/session_id=[^;]+/)[0])
        
    console.info("submit button clicked");
    var movie_selection = document.getElementById('movie_selection1_select').value;
    console.info(movie_selection);
    var form_contact_movie_selection = document.forms['form_select_no_of_seats'].elements.namedItem('form_contact_movie_selection');
    form_contact_movie_selection.value = movie_selection;
    event.preventDefault();
    //console.info(movie_data[movie_selection].avail_seats);
    var get_no_of_avail_seats = new XMLHttpRequest();
    get_no_of_avail_seats.open("POST", "/no_of_seats_avail", true);
    // get_no_of_avail_seats.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    get_no_of_avail_seats.responseType = "json";
    get_no_of_avail_seats.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            validate_no_of_available_seats(get_no_of_avail_seats.response["no_of_seats"]);
            // when validated no of seats is passed to the next function, the modal is called.
            // this will be needed to be altered when checking for available seats and raising alert for letting a user know if seats are available.
            active_modal = modal_1;
            modal.style.display = "block";
            modal_1.style.display = "block";
            }
        }
    text_to_send = { "movie_name" : movie_selection} ;
    get_no_of_avail_seats.send(JSON.stringify(text_to_send));
    
    };

    function validate_no_of_available_seats(no_of_seats_in_selected_movie){
        // var data_to_send = new FormData();
        // data_to_send.append('movie_name',movie_selection);
        // console.info(data_to_send);
        console.info(no_of_seats_in_selected_movie);

        //no_of_seats_in_selected_movie  = movie_data[movie_selection].avail_seats;
        if (no_of_seats_in_selected_movie == 0){
            console.info("no seats available, choose another movie!");
        } else {
            console.info("Select the number of seats you want to book.")
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


//getting the initial details of movies
function get_movie_details_request(){
    var request_movies = new XMLHttpRequest();
    request_movies.open("GET", "/display_movie", true);
    request_movies.responseType = "json"
    request_movies.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //Typical action to be performed when the document is ready:
            //console.log(request_movies.response);
            var movie_data = request_movies.response;
            window.movie_details = movie_data;
            populate_movies(movie_data);
            // console.info(movie_data)
        }
    };
    request_movies.send();
};

// modal.onclick = function(event) {
//     if (event.target == modal)
//         active_modal.style.display = "none";
//         modal.style.display = "none";
//         active_modal = undefined;

// };

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

}

func_submit_form_signin

function func_submit_form_signin(event){
//needs to be modified. do not use yet
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

}


}


