import csv


def save_jobs(jobs):
    with open(file="jobs.csv", mode="w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["company", "title", "location", "date", "link"])
        for job in jobs:
            writer.writerow(job.values())
