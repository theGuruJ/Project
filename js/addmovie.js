
window.onload = myApp();

function myApp() {

const formToJSON = elements => [].reduce.call(elements, (data, element) => {
  
    data[element.name] = element.value;
    return data;
  
  }, {});
  

const handleFormSubmit = event => {

    event.preventDefault();

    const data = formToJSON(movie_form.elements);

    const dataContainer = document.getElementsByClassName('results__display')[0];

    dataContainer.textContent = JSON.stringify(data, null, "  ");

    var submit_movie_data = new XMLHttpRequest();
    submit_movie_data.open("POST", '/movies', true);
    submit_movie_data.responseType = "json";
    submit_movie_data.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.info(submit_movie_data.response);
            result_of_post = submit_movie_data.response;
            dataContainer.textContent += "\n data submitted to server. Key reveived: " + result_of_post.Key_ID;
        }
    };
    submit_movie_data.send(JSON.stringify(data));


} 

movie_form = document.forms[0];

movie_form.addEventListener('submit', handleFormSubmit);


}; //closing myApp()



