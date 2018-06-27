console.log(document);

var button_retrieve_movies = document.getElementById('get_movie_details');

button_retrieve_movies.addEventListener('click',function(e){

    get_movie_details_request();
    });

function get_movie_details_request(){
    var request_movies = new XMLHttpRequest();
    request_movies.open("GET", "/display_movie", true);
    request_movies.responseType = "json"
    request_movies.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //Typical action to be performed when the document is ready:
            //console.log(request_movies.response);
            var movie_data = request_movies.response;
            populate_movies(movie_data);
        }
    };
    request_movies.send();   
};

function populate_movies(movie_data){
    console.info(document.getElementById("movie_list"));

    if (!document.getElementById("movie_list")){

    var movie_list = document.createElement('form');
    movie_list.name = "movie_selection";
    movie_list.id = "movie_list";
    var selectmovie = document.createElement('select');
    selectmovie.name = "movie_selection1";
   
    // console.log(typeof movie_data);
    //movie_data = movie_data.replace(/'/g,'"');
    //window.movie_data = JSON.parse(movie_data);

    movie_data;
    for (var key in movie_data) {
        if (movie_data.hasOwnProperty(key)) {
            // console.info(key);
            var element = document.createElement('option');
            element.setAttribute("name", key);
            element.innerHTML = key;
            selectmovie.appendChild(element);
        }
    }

    // console.log(movie_data);
    //console.info(movie_data);
    // console.log(movie_data[0]);
    
    var submit_selection = document.createElement('input')
    submit_selection.type = "submit";

    movie_list.appendChild(selectmovie);
    movie_list.appendChild(submit_selection);
    document.body.appendChild(movie_list);
} else {

    console.log("need to append the data to existing form");

}
    
    

};



