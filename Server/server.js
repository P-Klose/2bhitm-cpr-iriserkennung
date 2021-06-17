
const express = require("express");
const app = express();
const port = 3000;

let myData = [];

app.listen(port, ()=> {
    console.log("server läuft unter http://localhost:"+port);
})

app.use(express.static('public'));

// DATEN VOM CLIENT EMPFANGEN
app.post('/chartData', (req, res) => {
    console.log('HALLO DER REQUEST IST DA!');
    let data = req.body;
    myData.push(data)

})

app.get('/chartData', (req, res) => {
    res.send( JSON.stringify(myData) );
})

