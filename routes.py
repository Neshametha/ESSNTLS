from Major_Project_Flask import app, forms
from flask import request, render_template


@app.route('/')
@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = forms.project_location(request.form)
    if request.method == 'POST':
        location = request.form['location']
        print(location)
        address = forms.yelp_pass(location)
        print(address)

        return render_template("results.html", form=search_form, result=address, location=location, title= location)

    return render_template("search.html", form=search_form)













