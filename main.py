from jobkorea import get_jobs
from export import export_jobs
from flask import Flask, render_template, request, redirect, send_file

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
        return render_template("search.html", term=term, length=len(jobs), jobs=jobs)
    except Exception:
        return redirect("/")


@app.route("/export")
def export():
    try:
        term = request.args.get("term")
        term = term.lower()
        jobs = db.get(term)
        export_jobs(jobs, term)
        return send_file(
            f"{term}.csv",
            mimetype="text/csv",
            attachment_filename=f"{term}.csv",
            as_attachment=True,
        )
    except Exception:
        return redirect("/")


app.run()
