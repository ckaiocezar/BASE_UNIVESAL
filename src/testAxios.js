"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var axios_1 = require("axios");
axios_1.default.get('https://jsonplaceholder.typicode.com/todos/1')
    .then(function (res) { return console.log(res.data); })
    .catch(function (err) { return console.error(err); });
