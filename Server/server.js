let allTimeFaces = 0;
let allTimeEyes = 0;
let FacesNow;
let EyesNow;


const express = require("express");
const app = express();
const port = 3000;


app.listen(port, ()=> {
    console.log("server läuft unter http://localhost:"+port);
})

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// DATEN VOM CLIENT EMPFANGEN
app.post('/chartData', (req, res) => {
    console.log('HALLO DER REQUEST IST DA!');
    FacesNow = req.faces;
    EyesNow = req.eyes;

    if(allTimeEyes<EyesNow){
        allTimeEyes = EyesNow;
    }
    if(allTimeFaces<FacesNow){
        allTimeFaces = FacesNow;
    }
    //myData.push(data)

})

app.get('/chartData', (req, res) => {
    let myData = {'facesNow':FacesNow,'eyesNow':EyesNow,'facesHigh':allTimeFaces,'eyesHigh':allTimeEyes};
    res.send( JSON.stringify(myData) );
})

