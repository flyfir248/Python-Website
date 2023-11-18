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

@app.route('/class5')
def class5():
    return render_template('class5.html')



@app.route('/class6')
def class6():
    return render_template('class6.html')

@app.route('/class7')
def class7():
    return render_template('class7.html')

@app.route('/class8')
def class8():
    return render_template('class8.html')


@app.route('/class9')
def class9():
    return render_template('class9.html')

@app.route('/class10')
def class10():
    return render_template('class10.html')

@app.route('/class11')
def class11():
    return render_template('class11.html')

@app.route('/class12')
def class12():
    return render_template('class12.html')

@app.route('/class13')
def class13():
    return render_template('class13.html')

@app.route('/class14')
def class14():
    return render_template('class14.html')

@app.route('/class15')
def class15():
    return render_template('class15.html')

@app.route('/Exercise')
def Exercise():
    return render_template('Exercise.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
