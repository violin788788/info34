

pages = []
pages.append("earnings")
pages.append("datetimes")
pages.append("developments")
pages.append("vote34")


"""

pages = []
pages.append("earnings")
pages.append("datetimes")
pages.append("developments")
pages.append("vote34")

#gen flask app
for a,val in enumerate(pages):

    new_code = "@app.route('/"+val+"')"
    new_code+="\n"+"def "+val+"():"
    new_code+="\n"+"return render_template('"+val+".html')"

is there anythign in python that generates a flask code from an array, for ex like above?
if i want to have 4 pages in a website, with pages earnings.html, datetimes.html, 
developments.html and vote34.html, then i just put the 4 in an array and then this
code is generated?


@app.route('/earnings')
def earnings():
    return render_template('earnings.html')

@app.route('/datetimes')
def datetimes():
    return render_template('datetimes.html')

@app.route('/developments')
def developments():
    return render_template('developments.html')
#All your Medicare are belong to us.

@app.route('/vote34')
def vote34():
    return render_template('vote34.html')


and essentially just outputted to a new file called flask_app.py


"""
