from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Wayne Enterprises')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs.10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bengaluru, India',
        'salary': 'Rs.20,00,000'
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Bengaluru, India',
        'salary': 'Rs.30,00,000'
    },
    {
        'id': 4,
        'title': 'Software Engineer',
        'location': 'Bengaluru, India',
        'salary': 'Rs.5,00,000'
    },
]

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
