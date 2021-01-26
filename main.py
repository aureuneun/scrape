from jobkorea import get_jobs
from save import save_jobs
from flask import Flask, render_template, request, redirect

app = Flask("scrape")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    try:
        term = request.args.get("term")
        term = term.lower()
        fakeDB = db.get(term)
        if fakeDB:
            jobs = fakeDB
        else:
            jobs = get_jobs(term)
            db[term] = jobs
            save_jobs(jobs)
    except Exception:
        return redirect("/")
    return render_template("search.html", term=term, length=len(jobs), jobs=jobs)


app.run()
