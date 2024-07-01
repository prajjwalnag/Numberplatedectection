from simple_image_download import simple_image_download as simp

# Create an instance of the downloader
response = simp.simple_image_download

# Define the search keyword and the number of images you want to download
search_keyword = "indian car  on road with number plate"
num_images = 100  # You can adjust the number of images

# Download the images
response().download(search_keyword, num_images)

print("Download completed.")

