let lon;
let lat;
let temperature = document.querySelector(".temp")
let summary = document.querySelector(".summary")
let loc = document.querySelector(".location")
let icon = document.querySelector(".icon")
const kelvin = 273.15

window.addEventListener("load",() => {
    
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition((position) =>{
            
            console.log(position);
            lon = position.coords.longitude;
            lat = position.coords.latitude;
        
        //ID API
        const api_id = "27eca82d3607a7e50dab2c5ba31984dd";

        const url_base = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${api_id}`;

        fetch(url_base)
        .then((response) =>{

            console.log("RESPUESTA JSON");
            
            return response.json();
        })

        .then((data) => {
            console.log("ESTA ES LA DATA")
            console.log(data);

            temperature.textContent = 
             Math.floor(data.main.temp - kelvin) + "°C";
            summary.textContent = data.weather[0].description;
            loc.textContent = data.name + "," + data.sys.country;
        });

    });
        
    }
});