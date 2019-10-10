import mechanicalsoup
import http.cookiejar

def printCookies(url):
    browser = mechanicalsoup.StatefulBrowser()
    cookie_jar = http.cookiejar.CookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    for cookie in cookie_jar:
        print(cookie)

url = 'http://www.syngress.com/'
printCookies(url)
