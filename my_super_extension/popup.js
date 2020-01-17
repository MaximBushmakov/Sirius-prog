"use strict"
 
window.onload = function () {
        function updateLabel() {
                const enabled = chrome.extension.getBackgroundPage().enabled;
                let button = document.getElementById('toggle_button');
                let text = document.getElementById('text');
                if (enabled) {button.value = "Disable"; text.innerHTML = "Enabled";}
                else {button.value = "Enabled"; text.innerHTML = "Disabled";}
        }
        document.getElementById('toggle_button').onclick = function () {
                let background = chrome.extension.getBackgroundPage();
                background.enabled = !background.enabled;
                updateLabel();
        };
        updateLabel();
}