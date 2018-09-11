

window.onload = myApp();

function myApp() {
    let button_retrieve_movies_d = document.getElementById('get_movie_details');

    let submit_movie_selection_d = document.forms['movie_selection'];
    get_movie_details_request();
    submit_movie_selection_d.addEventListener('submit',load_movie_details);
    
    button_retrieve_movies_d.addEventListener('click',get_movie_details_request);

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

function load_movie_details(event){

    event.preventDefault();

};

};





