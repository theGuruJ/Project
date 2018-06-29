var button_retrieve_movies = document.getElementById('get_movie_details');

//var no_of_seats_in_selected_movie

button_retrieve_movies.addEventListener('click',get_movie_details_request);

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
        }
    };
    request_movies.send();   
};

function populate_movies(movie_data){

    if (!document.getElementById("movie_list")){

    var movie_list = document.createElement('form');
    movie_list.name = "movie_selection";
    movie_list.id = "movie_list";
    var selectmovie = document.createElement('select');
    selectmovie.name = "movie_selection1";
    selectmovie.id = "movie_selection1_select";
   
    // console.log(typeof movie_data);
    //movie_data = movie_data.replace(/'/g,'"');
    //window.movie_data = JSON.parse(movie_data);

    for (var key in movie_data) {
        if (movie_data.hasOwnProperty(key)) {
            // console.info(key);
            //console.info(movie_data[key].avail_seats);
            var element = document.createElement('option');
            element.value = key;
            element.text = key+": "+movie_data[key].avail_seats+" seats available";
            selectmovie.add(element);
        }
    }

    // console.log(movie_data);
    //console.info(movie_data);
    // console.log(movie_data[0]);
    
    var submit_selection = document.createElement('input')
    submit_selection.type = "submit";
    submit_selection.id = "submit_movie_selection";
    submit_selection.value = "book ticket";
    submit_selection.addAttribute = ("form","movie_list");

    movie_list.appendChild(selectmovie);
    movie_list.appendChild(submit_selection);
    document.getElementById('header').appendChild(movie_list);
    // document.body.appendChild(movie_list);
    window.submit_movie_selection = document.forms['movie_selection'];
    //var book_ticket_submit = document.getElementById('submit_movie_selection');
    submit_movie_selection.addEventListener('submit',function(event){
        console.info("submit button clicked");
        var movie_selection = document.getElementById('movie_selection1_select').value;
        event.preventDefault();
        var no_of_seats_in_selected_movie
        console.info(movie_selection);
        
        console.info(movie_data[movie_selection].avail_seats);
        var get_no_of_avail_seats = new XMLHttpRequest();
        get_no_of_avail_seats.open("POST", "/no_of_seats_avail", true);
        get_no_of_avail_seats.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        get_no_of_avail_seats.responseType = "json";
        get_no_of_avail_seats.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                console.info(get_no_of_avail_seats.response);
            }
        }
        // var data_to_send = new FormData();
        // data_to_send.append('movie_name',movie_selection);
        // console.info(data_to_send);
        text_to_send = { "movie_name" : movie_selection} ;
        get_no_of_avail_seats.send(JSON.stringify(text_to_send));

        //no_of_seats_in_selected_movie  = movie_data[movie_selection].avail_seats;
        console.log(typeof no_of_seats_in_selected_movie);
        if (no_of_seats_in_selected_movie == 0){
            console.info("no seats available, choose another movie!");
        } else {

            console.info("Fill your details in the contact form below and submit it to book ticket!")
        }

    });

} else {

    var movie_list_select_element = document.getElementById("movie_selection1_select");
    window.no_of_movies = movie_list_select_element.length;
    for (option in movie_list_select_element){
        movie_list_select_element.remove(option.selectedIndex);
    };


    
    for (var key in movie_data) {
        if (movie_data.hasOwnProperty(key)) {
            // console.info(key);
            //console.info(movie_data[key].avail_seats);
            var element = document.createElement('option');
            element.value = key;
            element.text = key+": "+movie_data[key].avail_seats+" seats available";
            movie_list_select_element.appendChild(element);
        }
    }
}
};

function collect_ticket_info(event){

    event.preventDefault()
    
    console.log("this is not constructed yet");
};

function book_ticket(){

    var book_ticket = new XMLHttpRequest();
    book_ticket.open("POST", "/book_ticket", true);
    book_ticket.responseType = "json";
    book_ticket.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            
        }
}
}