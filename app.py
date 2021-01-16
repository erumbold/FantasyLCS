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

if __name__ == '__main__':
    app.run(debug=True)