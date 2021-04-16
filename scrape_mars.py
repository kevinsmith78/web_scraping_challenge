from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import requests

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    #Run Browser
    browser=init_browser()

    #Visit Red Plant News
    url_news= "https://redplanetscience.com/"
    browser.visit(url_news)

    #Start Soup
    html_news= browser.html
    soup= bs(html_news,"html.parser")

    #Get News Results
    news_title=soup.find("div",class_="content_title").text

    #Search for Paragraphs
    news_paragraph=soup.find("div", class_="article_teaser_body").text

    # Print the Latest News
    print("Red Planet News From Mars")
    print(news_title)
    print(news_paragraph)

    # Find the featured the image from Mars
    url='https://spaceimages-mars.com/'
    browser.visit(url)

    #Click for full image
    browser.links.find_by_partial_text('FULL IMAGE').click()

    #Search for Image Source
    html = browser.html
    soup=bs(html,'html.parser')
    img_url=soup.find('img', class_='fancybox-image')['src']

    #Create Featured URL link per homework assignment
    featured_image_url= url+ img_url
    featured_image_url