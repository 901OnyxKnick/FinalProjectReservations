from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin_password"


is_admin_logged_in = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reservations/', methods=['GET', 'POST'])
def reservations():
    if not is_admin_logged_in:
        return redirect(url_for('admin_login'))

    


@app.route('/admin/login/', methods=['GET', 'POST'])
def admin_login():
    global is_admin_logged_in

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            is_admin_logged_in = True
            return redirect(url_for('reservations'))
        else:
            return render_template('admin_login.html', error="Invalid username or password")

    return render_template('admin_login.html', error=None)


@app.route('/admin/logout/')
def admin_logout():
    global is_admin_logged_in
    is_admin_logged_in = False
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
