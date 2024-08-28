import time
from playwright.sync_api import sync_playwright, expect


product_name = "Hantle żeliwne regulowane 2x10kg zestaw 20kg"
e_mail = "mail@mail.com"
name = "Jan"
surname = "Kowalski"
phone = "123123123"
street = "Radosna 1"
postal_code = "10-100"
city = "Warszawa"

def test_add_to_cart_and_order(playwright):

    #Create the browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)

    #Create the page
    page = browser.new_page()

    #Open the website
    page.goto('https://sportblast.pl')

    ## Expect a title "to contain" a substring.
    expect(page).to_have_title("SPORT BLAST - Hantle żeliwne, obciążenie, sztangi, gryfy")

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

    #Make order - button
    page.locator("xpath=/html/body/div[1]/div[4]/div/div/div[2]/div/div[2]/form/div/div[4]/span[2]/button").click()

    #Order without registration - button
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/form/button").click()

    #Fill customer data fields
    page.get_by_label("E-mail:").fill(e_mail)
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/input").fill(name)
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[3]/td[2]/div/input").fill(surname)
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[4]/td[2]/div/input").click()
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[4]/td[2]/div/input").fill(phone)
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/div/input").fill(street)
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/input").click()
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/input").fill(postal_code)
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[2]/div/input").fill(city)

    #Assert the checked state
    expect(page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[2]/span/input")).to_be_checked()
    expect(page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[2]/span/input")).to_be_checked()

    # Click summary button
    page.locator("xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div/div/div[2]/button[1]").click()

    time.sleep(2)
    
    browser.close()

