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

    reqParamsArr = request.url.split('&');
    reqParamsArr[0] = reqParamsArr[0].split('?')[1];

    reqParamsDict = {};
    reqLen = reqParamsArr.length;
    for (let i = 0; i < reqLen; ++i) {
        reqParamParts = reqParamsArr[i].split('=');
        reqParamsDict[reqParamParts[0]] = reqParamParts[1];
    }
    
    return reqParamsDict;
}

function HandleRequest(request, response) {

    response.writeHead(200, {
        "Content-type": "text/html",
        "charset": "utf-8",
    });

    let cookies = parseCookies(request);
    if (!("id" in cookies)) {
        victimId++;
        response.writeHead(200, {"Set-Cookie": "id=" + victimId});
        console.log("id: " + victimId);
    } else console.log("id: " + cookies["id"]);

    requestParams = getRequestParams(request);
    console.log("url: " + requestParams["url"]);

    const trackImg = new Buffer.from('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7', 'base64');
    response.end(trackImg);
}


// server = createServer(HandleRequest);
server = http_module.createServer(HandleRequest);
victimId = 0;
server.listen(port, () => {console.log("Server is working.")});