import time
from playwright.sync_api import sync_playwright, expect


product_name = "Hantle żeliwne regulowane 2x10kg zestaw 20kg"

def test_3_add_to_cart(playwright):

    #Create the browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)

    #Create the page
    page = browser.new_page()

    #Open the website
    page.goto('https://sportblast.pl')

    ## Expect a title "to contain" a substring.
    expect(page).to_have_title("SPORT BLAST - Hantle żeliwne, obciążenie, sztangi, gryfy ")

    #Accept cookie policy
    page.get_by_role("button", name="zaakceptuj").click()
    
    #Looking for the product
    page.get_by_placeholder("Szukaj").fill(product_name)
    
    #Select product from the list
    page.locator("xpath=/html/body/div[1]/header/div[2]/div[4]/form/div[2]/div[3]/div[2]/ul/li[1]/a").click()

    #Add to cart
    page.locator("xpath=/html/body/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/form/fieldset[1]/div[2]").click()

    #Open the cart
    page.locator("xpath=/html/body/div[13]/div[3]/div/a[2]").click()

    time.sleep(2)

    browser.close()

