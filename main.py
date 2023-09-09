from flask import Flask, render_template

app = Flask(__name__)

# Sample text content
sample_text_content = """
Your provided text goes here. You can replace this placeholder with your actual content.
"""

# Route for the Python intro page
@app.route('/python_intro')
def python_intro():
    return render_template('python_intro.html', sample_text=sample_text_content)


# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for an about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for a contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
