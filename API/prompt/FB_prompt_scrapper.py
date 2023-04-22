from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
from googletrans import Translator
import httpx

# Credentials
User_Email = "pepebotellah@gmail.com"
User_Password = "Superadmin1"
target_FB_account = "https://www.facebook.com/prezidentpavel"
number_prompt = 3

# Set up the web driver for Mozilla Firefox
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(2)  # Wait for the page to load
button = driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']")
button.click()

# Log in to Facebook
email = driver.find_element(By.ID, "email")
email.send_keys(User_Email)
password = driver.find_element(By.ID, "pass")
password.send_keys(User_Password)
password.send_keys(Keys.ENTER)


# Navigate to the user's profile page
time.sleep(3)  # Wait for the page to load
driver.get(target_FB_account)

# Scroll down the page to load more posts
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while len(driver.find_elements(By.CSS_SELECTOR, 'div[data-ad-comet-preview="message"]')) < number_prompt:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Scrape the latest number_prompt public posts
posts = driver.find_elements(By.CSS_SELECTOR, 'div[data-ad-comet-preview="message"]')[:number_prompt]
public_posts = [post.text for post in posts]

print(public_posts)

# Translate the posts to English
translator = Translator(service_urls=['translate.google.com'])
translated_posts = []
timeout = httpx.Timeout(60.0)  # 60 seconds timeout
for post in public_posts:
    try:
        translated_post = translator.translate(post, dest='en')
        if translated_post is not None and translated_post.text is not None:
            translated_posts.append(translated_post.text)
        else:
            print(f"Translation of '{post}' failed.")
    except Exception as e:
        print(f"Translation of '{post}' failed with error: {str(e)}.")

# Print the translated posts
print(translated_posts)

file_path = "../data/new_FB_posts.json"

# Save the translated posts to a JSON file
with open(file_path, "w") as file:
    json.dump(translated_posts, file)

# Close the web driver
driver.quit()
