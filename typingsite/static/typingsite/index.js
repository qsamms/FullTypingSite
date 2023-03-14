let gameWords = "";
let numWords = 10;
let user = document.getElementById("userinput");
let goodstanding = true;
let gameOver = false;
let game = false;
let seconds = 0;
let keystrokes = 0;
let time1 = new Date();
let time2 = new Date();
let currentidx = 0;
let mistakeidx = 0;
let time = 0;
let wpm = 0;
let accuracy = 0;
let mistakes = 0;
let characters = 0;

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

async function backendPost(){
    const requestObj = new XMLHttpRequest()
    requestObj.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            console.log(this.responseText)
        }
    }
    requestObj.open("POST", '/typingsite/post/')
    requestObj.setRequestHeader('X-CSRFToken',csrftoken)
    const formdata = new FormData()
    formdata.append('speed','90')
    formdata.append('user_id','100')
    requestObj.send(formdata)
}

async function apiCall(){
    //const endpoint = new URL('https://api.api-ninjas.com/v1/randomword');
    const endpoint = new URL('https://random-word-api.herokuapp.com/word?number=' + numWords);

    /*headers:{
        "X-Api-Key": "6Q+RVd1Ovqvme9AWyIoaJQ==s7x0uNd4gpBCse9i"
    }
    */
    const response = await fetch(endpoint, {});
    

    const data = await response.json();
    return data;
}

async function makeRequest(){
    let words = [];
    let stringWords = "";

    /*
    for(let i = 0;i<numWords;i++){
        let data = await apiCall();
        words[i] = data.word;
    }
    */
   let data = await apiCall();

    for(let i = 0;i<data.length;i++){
        stringWords = stringWords + data[i] + " ";
    }

    stringWords.trim();
    gameWords = stringWords;
    document.getElementById("text").innerHTML = stringWords;
}

async function startGame(){
    resetGame(false);
    await makeRequest();
    setEditable(document.getElementById("userinput"));
    await backendPost()
}

document.getElementById("request").addEventListener("click", startGame);

function setEditable(i){
    i.readOnly = false;
    i.value = "";
}

function displayData(){
    document.getElementById("data").style.display = "flex";
    document.getElementById("time").innerHTML = time + " Seconds";
    document.getElementById("words").innerHTML = numWords + "/" + characters;
    document.getElementById("wpm").innerHTML = wpm;
    document.getElementById("accuracy").innerHTML = accuracy + "%";
}

async function resetGame(end){
    if(end){
        calculateData();
        displayData();
        game = false;
    }else{
        document.getElementById("data").style.display = "none";
        game = true;
    }
    time = 0;
    wpm = 0;
    accuracy = 0;
    correct = 0;
    mistakes = 0;
    mistakeidx = 0;
    currentidx = 0;
    keystrokes = 0;
    seconds = 0;
    gameWords = "";
    pointer = 0;
    goodstanding = true;
    gameOver = false;
    user.style.background = "white"; 
    console.log("hello")
}

function calculateData(){
    time = parseInt(Math.abs(time2 - time1) / 1000);
    let minutes = time / 60;
    characters = gameWords.trim().length;
    let cpm = parseInt(characters / minutes);
    wpm = parseInt(cpm / 4.7);
    accuracy = parseInt((characters-mistakes)/characters * 100);
}

function selector(){
    document.getElementById("time10").style.color = "black";
    document.getElementById("time25").style.color = "black";
    document.getElementById("time50").style.color = "black";
    this.style.color = "red";
    var num = parseInt(this.innerHTML);
    numWords = num;
    //console.log(numWords);
}

document.getElementById("time10").addEventListener("click", selector);
document.getElementById("time10").style.color = "red";
document.getElementById("time25").addEventListener("click", selector);
document.getElementById("time50").addEventListener("click", selector);

function displayCursor(idx){
    var str = gameWords.replace("|","");
    var newstring = "<span>" + str.substring(0,idx) + "</span>|" + str.substring(idx);
    
    document.getElementById("text").innerHTML = newstring;
}

function getLength(idx){
    var letter = gameWords[idx];
    var length = 0;

    if(gameWords[idx] == " "){
        return getLength(idx-1);
    }else{
        while(letter != " " && idx >= 0){
            length++;
            idx--;
            letter = gameWords[idx];
        }
        //console.log("getLength length:" + length);
        return length;
    }
}

function myKeyDown(e){
    if(e.code != "Backspace" || !game){
        return;
    }

    if(currentidx > 0 && gameWords[currentidx-1] != " " && goodstanding){
        currentidx--;
    }

    if(!goodstanding){
        //console.log("user.value.length: " + user.value.trimStart().length);
        if(gameWords[mistakeidx] == " "){
            if(user.value.trimStart().length == getLength(mistakeidx) + 1){
                goodstanding = true;
                user.style.background = "white";
            }
        }else{
            if(user.value.trimStart().length == getLength(mistakeidx)){
                goodstanding = true;
                user.style.background = "white";
            }
        }
        
    }

    if(game){
        displayCursor(currentidx);
    }

    //console.log("Next Letter: " + gameWords[currentidx]);
}

function myKeyPress(e){
    if(!game){
        return;
    }

    if(user.value.trim().length == 0 && e.code == "Space"){
        user.value = "";
        return;
    }

    var letter = e.key;
    var correctLetter = gameWords[currentidx];

    //star timer on first keypress
    if(keystrokes == 0){
        //console.log('timer started');
        time1 = new Date();
        keystrokes++;
    }

    if(goodstanding){
        if(e.key == correctLetter && goodstanding){
            //end game
            if(currentidx == gameWords.length-1){
                user.value = "";
                time2 = new Date();
                resetGame(true);
                return;
            }
            goodstanding = true;
            user.style.background = "white";
            if(e.code == "Space"){
                user.value = "";
            }
            currentidx++;
        }else{
            mistakes++;
            mistakeidx = currentidx;
            user.style.background = "rgba(255,0,0,.5)";
            goodstanding = false;
        } 
    }   

    
    displayCursor(currentidx);
    //console.log("Next Letter: " + gameWords[currentidx]); 
}