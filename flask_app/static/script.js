var character = "man";
function toggle(){
    if(character == "man"){
        document.getElementById("yellowshirt").src = "static/img/yellowshirtw.png";
        document.getElementById("blueshirt").src = "static/img/blueshirtw.png";
        document.getElementById("redshirt").src = "static/img/redshirtw.png";
        character = "woman";
    }
    else {
        document.getElementById("yellowshirt").src = "static/img/yellowshirtm.png"
        document.getElementById("blueshirt").src = "static/img/blueshirtm.png"
        document.getElementById("redshirt").src = "static/img/redshirtm.png";
        character = "man";
    }
}

function redShirt() {
    alert("You have chosen red shirt. Are you sure you want to do this?");
}

function chooseShirt() {
    shirts = document.getElementById("shirts")
    shirts.submit();
}

function hide() {
    document.getElementById("registerForm").style.display = "none";
    document.getElementById("loginForm").style.display = "none";
}

function openregister() {
    document.getElementById("registerForm").style.display = "block";
    document.getElementById("loginForm").style.display = "none";
}

function openlogin() {
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("registerForm").style.display = "none";
}

function fetchPlanet(){
    document.getElementById("loadingplanet").innerHTML = "Loading...";
    planetList();
}

async function planetList(){
    var pagenumber = 0;
    var totalpages = 47;
    var planets = []
    while(pagenumber <= totalpages){
        var res = await fetch(`https://stapi.co/api/v1/rest/astronomicalObject/search?pageNumber=${pagenumber}`);
        var data = await res.json();
        var allplanets = data.astronomicalObjects.filter(object => object.astronomicalObjectType === 'PLANET' || object.astronomicalObjectType === 'M_CLASS_PLANET');
            for(var i=0; i < allplanets.length; i++){
                planets.push(allplanets[i]);
            }
        pagenumber++;
    }
    getRandomPlanet(planets);
}

function getRandomPlanet(arr){
    var random = arr[Math.floor(Math.random() * arr.length)];
    document.getElementById("generatedplanet").setAttribute("value", random.name);
    document.getElementById("loadingplanet").style.display = "none";
    document.getElementById("getplanet").submit()
}

function fetchEncounter(){
    document.getElementById("loadingencounter").innerHTML = "Loading...";
    encounterList();
}

async function encounterList(){
    var pagenumber = 0;
    var totalpages = 16;
    var species = []
    while(pagenumber <= totalpages){
        var res = await fetch(`https://stapi.co/api/v1/rest/species/search?pageNumber=${pagenumber}`);
        var data = await res.json();
        var allhumanoids = data.species.filter(object => object.humanoidSpecies === true);
            for(var i=0; i < allhumanoids.length; i++){
                species.push(allhumanoids[i]);
            }
        pagenumber++;
    }
    getRandomSpecies(species);
}

function getRandomSpecies(arr){
    var random = arr[Math.floor(Math.random() * arr.length)];
    document.getElementById("speciesname").setAttribute("value", random.name);
    document.getElementById("loadingencounter").style.display = "none";
    document.getElementById("getencounter").submit()
}

function fetchAstronomicalObject(){
    document.getElementById("loadingastro").innerHTML = "Loading...";
    astroList();
}

async function astroList(){
    var pagenumber = 0;
    var totalpages = 47;
    var astroObjects = []
    while(pagenumber <= totalpages){
        var res = await fetch(`https://stapi.co/api/v1/rest/astronomicalObject/search?pageNumber=${pagenumber}`);
        var data = await res.json();
        var allobjects = data.astronomicalObjects.filter(object => object.astronomicalObjectType != 'PLANET' && object.astronomicalObjectType != 'M_CLASS_PLANET' && object.astronomicalObjectType != 'BORG_SPATIAL_DESIGNATION' && object.astronomicalObjectType != 'MOON');
            for(var i=0; i < allobjects.length; i++){
                astroObjects.push(allobjects[i]);
            }
        pagenumber++;
    }
    getRandomAstroObject(astroObjects);
}

function getRandomAstroObject(arr){
    var random = arr[Math.floor(Math.random() * arr.length)];
    document.getElementById("astroname").setAttribute("value", random.name);
    document.getElementById("loadingastro").style.display = "none";
    document.getElementById("getplanet").submit();
}