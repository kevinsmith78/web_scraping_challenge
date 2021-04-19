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
    browser = init_browser()

    #Visit Red Plant News
    url_news= "https://redplanetscience.com/"
    browser.visit(url_news)

    # Identify and Parse 
    html_news= browser.html
    soup= bs(html_news,"html.parser")

    # Scrape the latest News
    news_title=soup.find("div",class_="content_title").text
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

    url_info = "https://galaxyfacts-mars.com/"
    browser.visit(url_info)

    #Read the data from the site
    mars_info=pd.read_html(url_info)
    mars_info

    #Create the DataFrame
    info_df=mars_info[0]

    #Create the Data Step #2
    info_df.columns = ["Category", "Mars","Value-Earth"]

    #Set index
    info_df

    # Modify Table
    mod_info_df=info_df.drop('Value-Earth', axis=1)
    mod_info_df

    # Clean up Table
    clean_mars=mod_info_df.drop(0)
    clean_mars

    #Save table to html
    html_table=clean_mars.to_html()

    #Save to folder
    clean_mars.to_html("Mars_facts_data.html")

    #Get Url
    hemisphere_url = "https://marshemispheres.com/"
    browser.visit(hemisphere_url)

    # HTML object using soup
    html_hemisphere = browser.html
    soup= bs(html_hemisphere, "html.parser")

    #Scrape, Scrape, Scrape
    hemispheres = soup.find_all("div", class_="item")

    # Create list
    hemi_info = []
    # Assign url 
    hemispheres_url = "https://marshemispheres.com/"

    # Loop through the list of all hemispheres
    for x in hemispheres:
        title = x.find("h3").text
        hemispheres_img = x.find("a",class_="itemLink product-item")["href"]
        # Visit link  
        browser.visit(hemispheres_url + hemispheres_img)
        # Develop image url
        image_html=browser.html
        web_info=bs(image_html,"html.parser")
        #Complete URL
        img_url = hemispheres_url + web_info.find("img",class_="wide-image")["src"]
        hemi_info.append({"title":title,"img_url":img_url})
        # Display titles 
        print("")
        print(title)
        print(img_url)

    # Part 2 Return scraping as dictionary
    mars_dict={'news_title': news_title,
         'news_paragraph':news_paragraph,
         'featured_image_url': featured_image_url,
         'mars_info': clean_mars(),
         'hemisphere_image_urls':hemi_info}

browser.quit()
return mars_dict