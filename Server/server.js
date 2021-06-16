
const express = require("express");
const app = express();
const port = 3000;
app.listen(port, ()=> {
    console.log("server läuft unter http://localhost:"+port);
})

app.use(express.static('public'));