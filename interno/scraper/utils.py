import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def scrape():
    timestamp = time.time()
    all_internships = []
    
    for i in range(1, 2):
        my_url = 'https://internshala.com/internships/work-from-home-internships/page-{}/'.format(i)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("div", {"class": "individual_internship"})
        
        for container in containers:
            internship_detail = {}

            title = container.find('h3', class_='job-internship-name')
            if title:
                internship_detail['title'] = title.text.strip()

            companyName = container.find('p', class_='company-name')
            if companyName:
                internship_detail['companyname'] = companyName.text.strip()

            location = container.find('div', class_='row-1-item locations')
            if location:
                location_text = location.span.a.text.strip()
                if 'home' in location_text.lower() or 'remote' in location_text.lower():
                    internship_detail['location'] = "remote"
                else:
                    internship_detail['location'] = location_text
            
            internship_detail['timestamp'] = timestamp

            all_internships.append(internship_detail)

    return all_internships

# t = scrape()
# print(t)
