from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


alumni_profiles = []
student_profiles = []


@app.route('/')
def home():
    return render_template('forum.html')


@app.route('/alumni')
def display_alumni():
    return render_template('alumni.html', alumni=alumni_profiles)


@app.route('/students')
def display_students():
    return render_template('students.html', students=student_profiles)


@app.route('/create_alumni', methods=['GET','POST'])
def create_alumni():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        profession = request.form['profession']
        expertise = request.form['expertise']
        alumni_profiles.append({'name': name, 'email': email, 'phone': phone, 'profession': profession, 'expertise': expertise})
        return redirect(url_for('display_alumni'))
    else:
        return render_template('create_alumni.html')

@app.route('/create_events', methods=['GET','POST'])
def create_events():
    if request.method == 'POST':
        ename = request.form['ename']
        date = request.form['date']
        loc = request.form['loc']
        des = request.form['des']
        alumni_profiles.append({'ename': ename, 'date': date, 'loc': loc, 'des': des})
        return redirect(url_for('display_events'))
    else:
        return render_template('create_events.html')


@app.route('/message', methods=['POST'])
def message():
    sender = request.form['sender']
    receiver = request.form['receiver']
    message = request.form['message']
    # In a real-world scenario, you would implement message storage and handling here
    return redirect(url_for('home'))


# Events and workshops route
@app.route('/events')
def events():
    # This route could display upcoming events and workshops
    return render_template('events.html')

if __name__ == "__main__":
    app.run(debug=True)