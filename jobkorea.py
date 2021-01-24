import requests
from bs4 import BeautifulSoup


def get_last_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    pagination = soup.select_one("div.recruit-info span.pgTotal").get_text()

    return int(pagination)


def extract_job(post):
    company = post.select_one("div.post-list-corp a")["title"]
    title = post.select_one("div.post-list-info a")["title"]
    location = post.select_one("div.post-list-info span.long").get_text(strip=True)
    date = post.select_one("div.post-list-info span.date").get_text(strip=True)
    link = post.select_one("div.post-list-info a")["href"]

    return {
        "company": company,
        "title": title,
        "location": location,
        "date": date,
        "link": f"http://www.jobkorea.co.kr{link}",
    }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"scraping page {page+1}")
        res = requests.get(f"{url}&Page_No={page+1}")
        soup = BeautifulSoup(res.text, "html.parser")
        posts = soup.select("div.recruit-info div.post")
        for post in posts:
            job = extract_job(post)
            jobs.append(job)
    return jobs


def get_jobs(term):
    url = f"http://www.jobkorea.co.kr/Search/?stext={term}&tabType=recruit"

    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
