from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time




# Replace 'YourWhatsAppNumber' with your actual WhatsApp phone number
whatsapp_number = '+919109208954'

# Replace 'YourImagePath' with the path to the folder where your DP images are stored
image_folder_path = 'C:\\Users\\nikola\\OneDrive\\Documents\\Coding\\Python\\projects\\whatsapp dp\\DP'

# Replace 'YourWebDriverPath' with the path to the Chrome WebDriver executable
webdriver_path = "C:\\Users\\nikola\\Downloads\\chromedriver_win32\\chromedriver.exe"

# Create a list of image file names (with their extensions) in the specified folder
image_files = ['image1.jpeg', 'image2.jpeg', 'image3.jpeg', 'image4.jpeg']

# Calculate the total number of images in the folder
total_images = len(image_files)

# Create a new Service instance using the WebDriver executable path
service = Service(webdriver_path)

# Create a new instance of the Chrome WebDriver, passing the Service object
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web in the Chrome browser
driver.get('https://web.whatsapp.com')
# Wait for the user to scan the QR code and log in
input('Please scan the QR code and press Enter to continue...')

# Locate and click on the profile picture element
profile_picture_element = driver.find_element(By.CLASS_NAME, "_11JPr")
profile_picture_element.click()


# Loop through the images and update the WhatsApp DP every minute
while True:
    for image_file in image_files:
        # Construct the full path to the current image
        image_path = image_folder_path + '/' + image_file

        # Locate the dp options button and click it
        time.sleep(2)
        # options = driver.find_element(By.CLASS_NAME, "_2pktu")
        # options.click()
        # input()

        # upload_button = driver.find_elements(By.CLASS_NAME, "jScby")
        # upload_button[2].click()
        # input()

        # Locate the file input element and send the image file path
        file_input = driver.find_element(By.CLASS_NAME, "_3xH7K").find_element(By.TAG_NAME, "input")
        file_input.send_keys(image_path)

        # Wait for the image to upload and set it as the new profile picture
        time.sleep(5)  # Adjust this delay if needed

        # Locate and click the 'Set as profile photo' button
        set_button = driver.find_element(By.CLASS_NAME, "_3oDXB")
        set_button.click()

        # Wait for the new profile picture to be set
        time.sleep(60)  # Adjust this delay if needed