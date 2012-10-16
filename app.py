from flask import Flask, render_template, url_for
import routes

app = Flask(__name__)

@app.route('/')
def root():
    return routes.Home().index()

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')

if __name__ == '__main__':
    app.run(debug=True)
