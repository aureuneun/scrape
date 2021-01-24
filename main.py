from jobkorea import get_jobs
from save import save_jobs
from flask import Flask, render_template, request, redirect

app = Flask("scrape")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    term = request.args.get("term")
    if term:
        term = term.lower()
        jobkorea_jobs = get_jobs(term)
        save_jobs(jobkorea_jobs)
    else:
        return redirect("/")
    return render_template("search.html", term=term)


app.run()
