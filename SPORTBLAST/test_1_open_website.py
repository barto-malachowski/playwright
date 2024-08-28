import time
from playwright.sync_api import sync_playwright, expect



def test_1_open_website(playwright):

    #Create the browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)

    #Create the page
    page = browser.new_page()

    #Open the website
    page.goto('https://sportblast.pl')

    ## Expect a title "to contain" a substring.
    expect(page).to_have_title("SPORT BLAST - Hantle żeliwne, obciążenie, sztangi, gryfy ")

    time.sleep(2)

    browser.close()



