from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv, sys, re, math

args = sys.argv
field = args[1] if len(args)>1 else "Tech"

print(f"Looking for {field}")

# prepare csv file
with open(f'./{field}.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Intro', 'Content'])

    domain = "https://www.some.jobs"
    fields = urlopen(f"{domain}/philippines/open-roles.htm?jobfield_name_level_1={field}").read()
    soup = BeautifulSoup(fields, 'html.parser')
    vacancies = soup.find_all('div', {'class':'careers-search-result'})
    h2 = soup.find_all('h2', {})
    pages = int(h2[len(h2)-1].contents[2].text)
    pages = math.ceil(pages / 20) if math.floor(pages / 20) > 0 else 1
    start = 0
    fetched = 0
    for p in range(pages):
        print(f"{p+1}/{pages}")
        fields = urlopen(f"{domain}/philippines/open-roles.htm?jobfield_name_level_1={field}&start={start}").read()
        soup = BeautifulSoup(fields, 'html.parser')
        vacancies = soup.find_all('div', {'class':'careers-search-result'})
        start = start + 20


        for vacancy in vacancies :
            vurl = domain + vacancy.h3.a.get_attribute_list('href')[0]
            print(f"SCRAPING\n{vurl}")
            vacancy_html = urlopen(vurl).read()
            soup = BeautifulSoup(vacancy_html, 'html.parser')
            content_article = soup.find_all('div', {'class':'content-article'})
            title = content_article[0].h1.text
            intro_arr = content_article[0].find('div', {'class':'article-intro'}).text.strip().split('|')
            intro = intro_arr[len(intro_arr) - 1].strip()
            print(intro)
            content = re.sub(r'[^\x00-\x7f]',r'', content_article[0].find('div', {'class':'vacancy-content'}).get_text(separator=u"\n",strip=True))
            writer.writerow([title,intro,content])
            fetched = fetched + 1
            print(f"Page: {p+1}/{pages} Job: {fetched}")