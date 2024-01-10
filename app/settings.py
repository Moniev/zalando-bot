import hashlib
from random import randint
from app.utils import generateRandomString

USERS = {1: {'m0ni3v@gmail.com': '1488Monieev!', 'is_beeing_used': False}, 2: {}}

SALT = generateRandomString(64)

PROXY_HOST = '109.61.89.1'
PROXY_PORT = '10623'
PROXY_USER = 'm0ni3v'
PROXY_PASS = 'hCPICLqXxR'
USER_MAIL = 'm0ni3v@gmail.com'
PASSWORD = '1488Monieev!'
PATH = 'C:/Users/Robert/Documents/projects/sebaBot/chrome driver/chromedriver.exe'
DATABASE_URL = 'postgresql+asyncpg://postgres:1488@localhost:5432/seba_bot'
USERS = {}

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
