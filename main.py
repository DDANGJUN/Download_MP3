from pytube import YouTube
import time
import numpy

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 콘솔로그 출력 안하게
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 제어 메시지 제거
options.add_experimental_option("useAutomationExtension", False)  # 자동화 확장기능 비활성화
options.add_argument('--disable-blink-features=AutomationControlled')  # 자동화 탐지 회피
service = Service()
options.add_argument("headless")
driver = webdriver.Chrome(service=service, options=options)

#===========================================================================================

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        downloadDir = 'D:\Vscode\DownloadMp3Bot\music'
        yt.streams.filter(only_audio=True).first().download()
        print('Downloaded! {}'.format(cnt))
    except:
        print('Error! {}'.format(cnt))
        pass
        
print('Start!')
files = open('MusicList.txt', 'r', encoding='utf-8')

cnt = 1

for i in files:
    driver.get("https://www.youtube.com/")
    time.sleep(2)
    
    searchKeyword = i + '가사'
    searchKeyword = searchKeyword.replace("\n", "")
    driver.find_element(By.NAME, 'search_query').send_keys(searchKeyword)
    driver.find_element(By.ID, 'search-icon-legacy').click()
    time.sleep(2)

    mainDiv = driver.find_element(By.ID, 'dismissible')
    subDiv = mainDiv.find_element(By.XPATH, '//*[@id="dismissible"]/ytd-thumbnail')
    musicLink = subDiv.find_element(By.ID, 'thumbnail').get_property('href')
    download_video(musicLink)

    cnt += 1

files.close()
print('Done!')
driver.quit()