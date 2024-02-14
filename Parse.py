import os

import requests
from bs4 import BeautifulSoup
import urllib.request

URL = 'https://hard.rozetka.com.ua/ua/videocards/c80087'

response = requests.get(URL)
print(response)

URL = 'https://ru.wallpaper.mob.org/gallery/tag=priroda/'
response = requests.get(URL)
print(response)
print(response.url)
print(response.status_code)
print(response.content)
print(response.headers['content_type'])
print(response.encoding)

bs = BeautifulSoup(response.text, 'lxml') # 'html.parser'
print(bs)
###################
# text parsing
temp = bs.find('div', 'tag-mini-widget__title-wrap')
print(temp)
print(temp.text.strip())

titles = bs.find_all('div', 'tag-mini-widget__title-wrap')

for title in titles:
	print(title.text.strip())

###################
# image parsing
images = bs.findAll('img', 'image-gallery-image__image')

image_links = []
for image in images:
	image_links.append(image.get("src"))

print(image_links)

current_file = 1

for link in image_links:
	print(f"Downloading {current_file} from {len(image_links)}...")
	folder_name = "nature_images/"
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)
	file_name = link[link.rfind('/') + 1:]
	response = requests.get(link, allow_redirects=True)
	open(folder_name + file_name, 'wb').write(response.content)
	current_file += 1


#########################
URL = 'https://hard.rozetka.com.ua/ua/videocards/c80087'

request = urllib.request.Request(URL, headers={'User-Agent': 'XYZ/3.0'})
webpage = urllib.request.urlopen(request, timeout=10).read()
print(webpage)

###################
# video parsing
SITE_URL = 'htpps://mixkit.co'

def get_video_links():
	request = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urllib.request.urlopen(request, timeout=10).read()
	# print(webpage)
	soup = BeautifulSoup(webpage, "html.parser")
	rows = soup.find_all(class_="item-grid-video-player__overlay-link")

	links_to_video_pages = []

	for row in rows:
		links_to_video_pages.append(SITE_URL[:-1] + row.get("href"))

	print(f"Started processing...")
	counter = 0
	result_video_links = []

	for link in links_to_video_pages:
		counter += 1
		print(f"Processing {counter} from {len(links_to_video_pages)}...")
		request = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urllib.request.urlopen(request, timeout=10).read()
		soup = BeautifulSoup(webpage, "html.parser")
		rows = soup.find_all(class_="video-player__viewer")

		for row in rows:
			result_video_links.append(row.get("src"))

	return result_video_links

def download_videos(links, path_to_save):
	if not os.path.exists(path_to_save):
		os.makedirs(path_to_save)
	
	counter = 0
	for link in links:
		counter += 1
		print(f"Downloading file {counter} from {len(video_links)}...")
		file_name = str(counter) + "_" + link.split("/")[-1]
		response = request.get(link, stream=True)
		with open(path_to_save + file_name, "wb") as video_file:
			for chunk in response.iter_content(chunk_size=1024 * 1024):
				if chunk:
					video_file.write(chunk)
		print(f"Downloading file {counter} finished!")
	
	print("All done!")


if __name__ == "__main__":
	video_links = get_video_links()
	download_videos(video_links, "videos/")
	