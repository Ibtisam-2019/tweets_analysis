var express = require('express');
var app = express();
var path = require('path');

app.use(express.static(path.join(__dirname, '/'))); 




app.get('/twitter', callName);
function callName(req, res) {

    // Use child_process.spawn method from
    // child_process module and assign it
    // to variable spawn
    var spawn = require("child_process").spawn;

    // Parameters passed in spawn -
    // 1. type_of_script
    // 2. List containing Path of the script
    //    and arguments for the script

    // E.g.: http://localhost:4000/twitter=user&words=Cyber
    // So, first name = Mike and last name = Will
    var process = spawn('python',["./twitter-index.py",
                            req.query.twitter,
                            req.query.words] );

    // Takes stdout data from script which executed
    // with arguments and send this data to res object
    process.stdout.on('data', function(data) {
        res.send(data.toString());
    } )}


app.listen(5000);
console.log('Listening on port 5000');