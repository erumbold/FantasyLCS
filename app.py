from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("leagueStandings.html")

@app.route('/stats')
def stats():
    return render_template("stats.html")

@app.route('/roster')
def roster():
    return render_template("roster.html")

@app.route('/matchups')
def matchups():
    return render_template("matchups.html")

@app.route('/trade')
def trade():
    return render_template("trade.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/draft')
def draft():
    return render_template('draft.html')

if __name__ == '__main__':
    app.run(debug=True)