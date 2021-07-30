from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')
        
    slide_elem.find('div', class_='content_title')

    # Use the parent element to find the first a tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    df = pd.read_html('https://galaxyfacts-mars.com')[0]

    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    mars_facts=df.to_html()

    # 1. Use browser to visit the URL 
    url='https://marshemispheres.com/'
    # url = 'https://astrogeology.usgs.gov/'

    browser.visit(url)

    html_hemispheres = browser.html
    hemispheres_bs=soup(html_hemispheres,'html.parser')

    results=hemispheres_bs.find('div', class_='result-list')
    hemispheres=results.find_all('div',{'class':'item'})

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls=[]
    hemisphere={}

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    for hemisphere in hemispheres:
    # hemisphere=hemispheres[0]
        title = hemisphere.find("h3").text
        end_link = hemisphere.find("a")["href"]
        hemisphere_link = "https://marshemispheres.com/" + end_link    
        browser.visit(hemisphere_link)

        hemisphere_html = browser.html
        hemisphere_soup=soup(hemisphere_html, "html.parser")
        hemisphere_image_link = hemisphere_soup.find("img",{"class":"wide-image"})["src"]
        hemisphere_wide_image_link = "https://marshemispheres.com/" + hemisphere_image_link
        hemisphere_dict={
            "title":title,
            "image_url":hemisphere_wide_image_link
            }
        hemisphere_image_urls.append(hemisphere_dict)
        
        # 5. Quit the browser
    browser.quit()
    

    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": img_url,
        "facts": mars_facts,
        "hemispheres": hemisphere_image_urls,
        "last_modified": dt.datetime.now()
    }

    return scraped_data