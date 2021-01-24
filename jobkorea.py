import requests
from bs4 import BeautifulSoup

JOBKOREA_URL = "http://www.jobkorea.co.kr/Search/?stext=파이썬&tabType=recruit"


def get_last_page():
    res = requests.get(JOBKOREA_URL)
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


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"scraping page {page+1}")
        res = requests.get(f"{JOBKOREA_URL}&Page_No={page+1}")
        soup = BeautifulSoup(res.text, "html.parser")
        posts = soup.select("div.recruit-info div.post")
        for post in posts:
            job = extract_job(post)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
