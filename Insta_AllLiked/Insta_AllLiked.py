import getpass
from time                                    import sleep
from selenium                                import webdriver
from selenium.webdriver.common.keys          import Keys
from selenium.webdriver.common.action_chains import ActionChains

def like_it(browser): 
    sleep(5)
    print("Like that shit")
    like_it = browser.find_element_by_class_name('_9AhH0')
    actions = ActionChains(browser)
    actions.double_click(like_it).perform()

def next_picture(browser): 
    sleep(2) 
    # finds the button which gives the next picture 
    nex = browser.find_element_by_xpath("//a[text()='Next']")

    #nex = browser.find_element_by_class_name("HBoOv")   
    sleep(1) 
    return nex 

def continue_liking(browser): 
    while(True): 
        next_element = next_picture(browser) 

        # if next button is there then 
        if next_element != False:   
  
            # click the next button 
            next_element.click()    
            sleep(2) 
  
            # like the picture 
            like_it(browser)     
            sleep(2)             
        else: 
            print("not found") 
            print("Closing Browser") 
            browser.close()
            break

def insta_likethatshit(username, password, TargetAccount):
    browser = webdriver.Firefox()
    browser.implicitly_wait(20)
    browser.get('https://www.instagram.com/')

    element = browser.find_element_by_name("username")
    element.send_keys(username)
    sleep(5)
    element = browser.find_element_by_name("password")
    element.send_keys(password)

    sleep(5)
    print("Logging in")
    login_link = browser.find_element_by_xpath("//div[text()='Log In']")
    login_link.click()

    sleep(2)
    print("Notifications? Absolutely Not")
    login_remember = browser.find_element_by_xpath("//button[text()='Not Now']")
    login_remember.click()

    sleep(10)
    print("Another Not Now")
    another_remember = browser.find_element_by_xpath("//button[text()='Not Now']")
    another_remember.click()

    print("Searching", TargetAccount)
    search_bar = browser.find_element_by_xpath("//input[@placeholder='Search']")
    search_bar.send_keys(TargetAccount)

    sleep(5)
    print("First Enter")
    search_bar.send_keys(Keys.ENTER)
    print("Second Enter")
    search_bar.send_keys(Keys.ENTER)

    sleep(5)
    print("Open Latest Post")
    pic = browser.find_element_by_class_name("_9AhH0")    
    pic.click()#clicks on the first picture 
    
    like_it(browser) 
    continue_liking(browser) 

    print("Finished")
    print("Close Browser")
    browser.close()

username = input("Enter username: ")
password = getpass.getpass('Enter password: ')
target = input("Who to like: ")
insta_likethatshit(username, password, target)
