import csv


def export_jobs(jobs, name):
    with open(file=f"{name}.csv", mode="w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["company", "title", "location", "date", "link"])
        for job in jobs:
            writer.writerow(job.values())
