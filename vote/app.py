from flask import Flask, render_template, request, redirect
import redis
import os

app = Flask(__name__)
redis = redis.Redis(host="redis", port=6379, db=0)

PARTY_LIST = [
    {"code": "a", "name": "YSRCP"},
    {"code": "b", "name": "TDP"},
    {"code": "c", "name": "BJP"},
    {"code": "d", "name": "BRS"},
    {"code": "e", "name": "CONGRESS"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vote = request.form['vote']
        for party in PARTY_LIST:
            if vote == party["code"]:
                redis.incr(party["name"])
        return redirect('/')
    
    # Prepare party option/name pairs for the template
    party_options = [
        {
            "code": party["code"],
            "name": party["name"]
        } for party in PARTY_LIST
    ]
    return render_template(
        'index.html',
        parties=party_options
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

