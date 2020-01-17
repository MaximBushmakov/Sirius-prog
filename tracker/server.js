// import { createServer } from "http";
let http_module = require("http");
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

    let reqParamsArr = request.url.split('&');
    reqParamsArr[0] = reqParamsArr[0].split('?')[1];

    let reqParamsDict = {};
    const reqLen = reqParamsArr.length;
    for (let i = 0; i < reqLen; ++i) {
        let reqParamParts = reqParamsArr[i].split('=');
        reqParamsDict[reqParamParts[0]] = reqParamParts[1];
    }

    return reqParamsDict;
}


// Tracking and responding of image
function trackByImg(request, response) {

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

    const requestParams = getRequestParams(request);
    console.log("url: " + requestParams["url"]);

    const trackImg = new Buffer.from('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7', 'base64');
    response.end(trackImg);

    // let reader = new FileReader();
    // reader.onload = () => {response.end(reader.result);}
    // reader.readAsArrayBuffer("c:/users/user/desktop/vscode/prog/tracker/icon.jpg");
}


function respondeJavascript(response) {
    
    response.writeHead(200, {
        "Content-type": "text/javascript",
        "charset": "utf-8",
    });

    let script = `
    console.log('script loaded');
    `;
    response.end(script);
}


function Router(request, response) {

    const reqPath = request.url.split('?')[0].slice(1);
    console.log(reqPath);

    if (reqPath == "img") {
        trackByImg(request, response);

    } else if (reqPath == "script") {
        respondeJavascript(response);

    } else {response.writeHead(404, {});}
}


server = http_module.createServer(Router);
victimId = 0;
server.listen(port, () => {console.log("Server is working.")});