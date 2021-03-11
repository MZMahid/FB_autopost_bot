import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def fb_auto_post():

    username = input("Enter your Facebook ID: ")
    password = input("Enter your Facebook ID password: ")

    groups_link = open("group_links.txt", "r")
    groups = groups_link.readlines()
    groups_link.close()

    file = open("write_post.txt", "r")
    post = file.read()
    file.close()

    driver = webdriver.Chrome("E:\\Python\\Projects\\FB_autopost_bot\\chromedriver.exe")

    driver.implicitly_wait(15)

    driver.get("http://www.facebook.com")

    elem = driver.find_element_by_name("email")
    elem.send_keys(username)
    elem = driver.find_element_by_name("pass")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    time.sleep(10)

    for i in range(len(groups)):

        driver.get('https://m.facebook.com/groups/' + groups[i])

        try:
            post_box = driver.find_element_by_xpath(
                "//div[@class='_4g34 _6ber _78cq _7cdk _5i2i _52we']")
            driver.execute_script("arguments[0].click();", post_box)

            write_post = driver.find_element_by_xpath(
                "//textarea[@class='composerInput mentions-input']")
            write_post.send_keys(post)
            time.sleep(1)

            post_click = driver.find_element_by_xpath(
                "//button[@class='_54k8 _52jg _56bs _26vk _56b_ _56bw _56bv']")
            driver.execute_script("arguments[0].click();", post_click)
            time.sleep(5)

            alert_obj = driver.switch_to.alert
            alert_obj.dismiss()

        except:
            print("Looks like you are not joined in this group or this group is currently unavailable.")


fb_auto_post()
