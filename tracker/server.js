// import { createServer } from "http";
http_module = require("http");
let port = 8080;

function parseCookies(request) {
    var list = {},
        rc = request.headers.cookie;
    rc && rc.split(';').forEach(function( cookie ) {
        var parts = cookie.split('=');
        list[parts.shift().trim()] = decodeURI(parts.join('='));
    });

    return list;
}

function getRequestParams(request) {
    req_params_arr = request.url.split('&');
    req_params_arr[0] = req_params_arr[0].split('?')[1];
    req_params_dict = {};
    req_len = req_params_arr.length;
    for (let i = 0; i < req_len; ++i) {
        req_param_parts = req_params_arr[i].split('=');
        req_params_dict[req_param_parts[0]] = req_param_parts[1];
    }
    return req_params_dict;
}

function HandleRequest(request, response) {

    response.writeHead(200, {
        "Content-type": "text/html",
        "charset": "utf-8",
    });

    let cookies = parseCookies(request);
    if (!("id" in cookies)) {
        id++;
        response.writeHead(200, {
            "Set-Cookie": "id=" + id,
        });
        console.log("id: " + id);
    }
    else console.log("id: " + cookies["id"]);

    request_params = getRequestParams(request);
    console.log("url: " + request_params["url"]);

    const trackImg = new Buffer.from('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7', 'base64');
    response.end(trackImg);
}

function OnListen() {
    console.log("Listening");
}

server = http_module.createServer(HandleRequest);
id = 0;
server.listen(port, OnListen);