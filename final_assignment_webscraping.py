# -*- coding: utf-8 -*-
"""Final Assignment_Webscraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18dgUJwA_TZzOIwRKxNGpBKfoBKl6kFuj

<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/Images/SN_logo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

<h1>Extracting Stock Data Using a Web Scraping</h1>

Not all stock data is available via API in this assignment; you will use web-scraping to obtain financial data. You will be quizzed on your results.\
Using beautiful soup we will extract historical share data from a web-page.

<h2>Table of Contents</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li>Downloading the Webpage Using Requests Library</li>
        <li>Parsing Webpage HTML Using BeautifulSoup</li>
        <li>Extracting Data and Building DataFrame</li>
    </ul>
<p>
    Estimated Time Needed: <strong>30 min</strong></p>
</div>

<hr>
"""

#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.6.4
#!pip install plotly==5.3.1

import pandas as pd
import requests
from bs4 import BeautifulSoup

"""## Using Webscraping to Extract Stock Data Example

First we must use the `request` library to downlaod the webpage, and extract the text. We will extract Netflix stock data <https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html>.
"""

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text

"""Next we must parse the text into html using `beautiful_soup`

"""

soup = BeautifulSoup(data, 'html5lib')

"""Now we can turn the html table into a pandas dataframe

"""

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

"""We can now print out the dataframe

"""

netflix_data.head()

"""We can also use the pandas `read_html` function using the url

"""

read_html_pandas_data = pd.read_html(url)

"""Or we can convert the BeautifulSoup object to a string

"""

read_html_pandas_data = pd.read_html(str(soup))

"""Beacause there is only one table on the page, we just take the first table in the list returned

"""

netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()

"""## Using Webscraping to Extract Stock Data Exercise

Use the `requests` library to download the webpage <https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html>. Save the text of the response as a variable named `html_data`.
"""

new_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

html_data = requests.get(new_url).text

"""Parse the html data using `beautiful_soup`.

"""

beautiful_soup=BeautifulSoup(html_data,'html5lib')

"""<b>Question 1</b> What is the content of the title attribute:

"""

soup_title=beautiful_soup.title
print("The title is:",soup_title)

"""Using beautiful soup extract the table with historical share prices and store it into a dataframe named `amazon_data`. The dataframe should have columns Date, Open, High, Low, Close, Adj Close, and Volume. Fill in each variable with the correct data from the list `col`.

"""

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

"""Print out the first five rows of the `amazon_data` dataframe you created.

"""

amazon_data.head()

"""<b>Question 2</b> What is the name of the columns of the dataframe

"""

print(amazon_data.columns)

"""<b>Question 3</b> What is the `Open` of the last row of the amazon_data dataframe?

"""

amazon_data.tail()

"""<h2>About the Authors:</h2> 

<a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork900-2022-01-01">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

Azim Hirjani

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By | Change Description |
| ----------------- | ------- | ---------- | ------------------ |

```
| 2021-06-09       | 1.2     | Lakshmi Holla|Added URL in question 3 |
```

\| 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |
\| 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |

<hr>

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>

<p>
"""