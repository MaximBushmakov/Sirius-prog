"use strict"
 
var enabled = true;
 
// Check on sochisirius.ru and ngs.ru
const badDomains = [
        "doubleclick.com",
        "mc.yandex.ru",
        "google-analytics.com",
        "googletagmanager.com",
        "google.com",
        "an.yandex.ru",
        "reklama.ngs.ru",
        "ads.adfox.ru",
        "www.tns-counter.com",
];
 
let leetRequestFilter = function(details) {
        if (!enabled) return {};

        let host = new URL(details.url).host;
 
        console.log("Trying to load: ", host);
        const block = badDomains.findIndex(badHost => {return host.endsWith(badHost);}) >= 0;
        if (block) {console.log("BLOCKED " + host)};

        return {cancel: block};
}
 
chrome.webRequest.onBeforeRequest.addListener(
        leetRequestFilter,
        {urls: ["http://*/*", "https://*/*"]},
        ["blocking"]  // Nothing continues until we decide to proceed.
);