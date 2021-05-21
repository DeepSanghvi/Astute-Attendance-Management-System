const express = require('express')
const mysql  =  require('mysql')

const db = mysql.createConnection({
    host: 'localhost',
    database: 'att_mng',
    user: 'pi',
    password: 'vectors'
})

db.connect(err => {
    if(err) {
        throw err
    }
    console.log('MySQL connected');
})
const app= express();


app.get('/attendance', (req, res) => {
    let sql ='SELECT * FROM attendance';
     db.query(sql, (err, results) => {
        if (err) {
          throw err;
        }
        console.log(results)
        res.send(results)
    })
})

app.listen('3000', () =>{
    console.log('Server started on port 3000')
})