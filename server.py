from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('/index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            if 'submit' in data:
                del data['submit']
            write_to_txt(data)
            write_to_csv(data)
            return "I'll be in touch soon."
        except:
            return 'did not save to database'
        # return redirect('/thankyou.HTML')
    else:
        return 'something went wrong. Try again!'

def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database2:
        email=data['email']
        name=data['name']
        message=data['message']
        csv_writer=csv.writer(database2,delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

def write_to_txt(data):
    f= open("database.txt", "a")
    f.write(str(data) + "\n")
    f.close()