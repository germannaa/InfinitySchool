/*
//Criando servidor apenas com NODEJS
const http = require('http')
const port = 3000
const server = http.createServer((req, res) => {
    res.end('Helloo World! :)')
})

server.listen(port, () => {
    console.log("Rodou!")
})
*/

//Usando express
const express = require('express')
const app = express()

app.get("/", function (req, res) {
    //res.send("Olá, pagina inicial!")
    res.sendFile(__dirname + "/index.html")
})

app.get("/teste", function(req, res) {
    //res.send("Pagina de teste")
    res.sendFile(__dirname + "/teste.html")
})

app.get("/contato", function(req, res) {
    //res.send("Pagina de teste")
    res.sendFile(__dirname + "/contato.html")

})
app.listen(3000, function(){
    console.log("RODoooU")
})