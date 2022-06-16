from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/pricing')
def pricing():
    pricings = [
        {'name': 'Free', 'price': '$0', 'benefits': ['10 users included', '2 GB of storage', 'Email support', 'Help center access']},
        {'name': 'Pro', 'price': '$15', 'benefits': ['20 users included', '10 GB of storage', 'Priority email support','Help center access']},
        {'name': 'Enterprise', 'price': '$25', 'benefits': ['30 users included', '15 GB of storage', 'Phone and email support', 'Help center access']}]
    return render_template('pricing.html', pricings=pricings)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)