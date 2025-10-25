import os
from dotenv import load_dotenv
from flask import Flask, render_template
import psycopg
from psycopg.rows import dict_row

load_dotenv()

app = Flask(__name__)
DB_URL = os.environ["DATABASE_URL"]

@app.route("/")
def index():
    # Call the stored function
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM get_sales_by_category();")
            results = cur.fetchall()

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
