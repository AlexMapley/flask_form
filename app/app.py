from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# Class Definitions
class ReusableForm(Form):
    languages = TextField('Languages:', validators=[validators.required()])
    concepts = TextField('Concepts:', validators=[validators.required()])
    software = TextField('Software:', validators=[validators.required()])
    environments = TextField('Environments:', validators=[validators.required()])




# Routes
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/resume_form", methods=['GET', 'POST'])
def resume_form():
    form = ReusableForm(request.form)
    print form.errors
    if request.method == 'POST':
        languages=request.form['languages']
        concepts=request.form['concepts']
        software=request.form['software']
        environments=request.form['environments']

        if form.validate():
            # Flash diplaying entered fields
            flash('Languages ' + languages)
            flash('Concepts ' + concepts)
            flash('Software ' + software)
            flash('Environments ' + environments)
        else:
            flash('All the form fields are required. ')

    return render_template('resume_form.html', form=form)

@app.route("/page2")
def page2():
    return render_template('page2.html')



if __name__ == "__main__":
    app.run()
