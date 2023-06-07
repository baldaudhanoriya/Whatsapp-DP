from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont

# Define the image dimensions
image_width = 600
image_height = 600

# Define the font properties
font_size = 60
font_color = (255, 255, 255)  # White color

# Generate clock images for all possible minutes of the day
start_time = datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0)
end_time = start_time + timedelta(days=1)

current_time = start_time
while current_time < end_time:
    # Create a blank image with the specified dimensions
    image = Image.new("RGB", (image_width, image_height), (0, 0, 0))  # Black background

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Get the current time as a string in the 12-hour format with AM/PM
    time_string = current_time.strftime("%I:%M %p")

    # Calculate the text position to center it in the image
    text_width, text_height = draw.textsize(time_string, font=font)
    text_x = (image_width - text_width) // 2
    text_y = (image_height - text_height) // 2

    # Draw the time on the image
    draw.text((text_x, text_y), time_string, font=font, fill=font_color)

    # Save the image with a filename based on the current time
    image_filename = current_time.strftime("%I%M%p") + ".png"
    image.save("clock images/12 hours format/" + image_filename)

    # Increment to the next minute
    current_time += timedelta(minutes=1)