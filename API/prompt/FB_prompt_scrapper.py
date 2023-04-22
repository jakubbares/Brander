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
number_prompt = 30
Name_Target = "Petr Pavel"

# Set up the web driver for Chrome
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
time.sleep(2)  # Wait for the page to load
driver.get(target_FB_account)
time.sleep(1)  # Wait for the page to load


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
posts = driver.find_elements(By.CSS_SELECTOR, 'div[data-ad-preview="message"]')[:number_prompt]
public_posts = [post.text for post in posts]

print(public_posts)

# Translate the posts to English
translator = Translator()
translated_posts = []
timeout = httpx.Timeout(60.0)  # 60 seconds timeout
for post in public_posts:
    try:
        translated_post = translator.translate(post, dest='en').text
        if translated_post is not None:
            translated_posts.append(translated_post)
        else:
            print(f"Translation of '{post}' failed.")
    except Exception as e:
        print(f"Translation of '{post}' failed with error: {str(e)}.")


# Print the translated posts
print(translated_posts)

# Create a dictionary with the translated posts
key = Name_Target
posts_dict = {key: translated_posts}

# Print the dictionary
print(posts_dict)

file_path = "../data/new_FB_posts.json"

# Save the dictionary to a JSON file
if len(translated_posts) > 0:  # check if there are translated posts
    with open(file_path, "w") as file:
        json.dump(posts_dict, file)
else:
    print("No translated posts to save.")

# Close the web driver
driver.quit()
