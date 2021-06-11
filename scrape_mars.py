import datetime as dt

def scrape_all():

    news_title = 'Testing Title'
    news_paragraph = 'Testing Paragraph'
    featured_image = 'http://peoplelovescience.com/wp-content/uploads/2017/08/21151729_1326742644090307_971208679029560636_n-2.jpg'
    mars_facts = 'Testing Facts Table'

    hemispheres_list_of_dicts = [
        {"title": "Title of Hemisphere Image",
        "img_url": 'http://peoplelovescience.com/wp-content/uploads/2017/08/21151729_1326742644090307_971208679029560636_n-2.jpg'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'http://peoplelovescience.com/wp-content/uploads/2017/08/21151729_1326742644090307_971208679029560636_n-2.jpg'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'http://peoplelovescience.com/wp-content/uploads/2017/08/21151729_1326742644090307_971208679029560636_n-2.jpg'},
        
        {"title": "Title of Hemisphere Image",
        "img_url": 'http://peoplelovescience.com/wp-content/uploads/2017/08/21151729_1326742644090307_971208679029560636_n-2.jpg'},
    ]

    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "hemispheres": hemispheres_list_of_dicts,
        "last_modified": dt.datetime.now()
    }

    return scraped_data