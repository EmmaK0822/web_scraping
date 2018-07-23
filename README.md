# Mission to Mars

![mission_to_mars](Images/mission_to_mars.jpg)

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

## Scraping web pages.

* `mission_to_mars.ipynb`: initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter

1. NASA Mars News

2. JPL Mars Space Images - Featured Image

3. Mars Weather

4. Mars Facts

5. Mars Hemispheres

## MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* `scrape_mars.py`: Python script calls with a function called `scrape`
* `insert_data.py`: Python script inserts a first dataset we obtained through web-scraping into local MongoDB
* `app.py`: Flask application

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

