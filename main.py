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

@app.route('/flow_of_control')
def flow_of_control():
    return render_template('flow_of_control.html')

@app.route('/Data_structure')
def Datastructure():
    return render_template('Datastructure.html')

@app.route('/class1')
def class1():
    return render_template('class1.html')

@app.route('/class2')
def class2():
    return render_template('class2.html')

@app.route('/class3')
def class3():
    return render_template('class3.html')

@app.route('/class4')
def class4():
    return render_template('class4.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
