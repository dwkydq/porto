from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.secret_key = 'secret123'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'porto'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users LIMIT 1")
    user = cur.fetchone()

    if user and isinstance(user[5], bytes):
        user = list(user)
        user[5] = user[5].decode('utf-8')

    cur.execute("SELECT * FROM skills")
    skills = cur.fetchall()

    cur.execute("SELECT * FROM projects")
    projects = cur.fetchall()

    return render_template('index.html', user=user, skills=skills, projects=projects)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'inpUsername' in request.form and 'inpPass' in request.form:
        username = request.form['inpUsername']
        passwd = request.form['inpPass']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, passwd))
        result = cur.fetchone()
        cur.close()

        if result:
            session['loggedin'] = True
            session['id'] = result[0]
            session['username'] = result[1]
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="Username atau password salah.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Berhasil logout!', 'info')
    return redirect(url_for('index'))


@app.route('/admin')
def admin():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users LIMIT 1")
    user = cur.fetchone()
    cur.execute("SELECT * FROM skills")
    skills = cur.fetchall()
    cur.execute("SELECT * FROM projects")
    projects = cur.fetchall()
    return render_template('admin.html', user=user, skills=skills, projects=projects)


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users LIMIT 1")
    user = cur.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        bio = request.form['bio']

        photo = request.files['photo']
        filename = user[5]  # kolom ke-6 = photo

        if photo:
            filename = photo.filename
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cur.execute("UPDATE users SET name=%s, bio=%s, photo=%s WHERE id=%s",
                    (name, bio, filename, user[0]))
        mysql.connection.commit()
        flash('Profil berhasil diperbarui!', 'success')
        return redirect(url_for('admin'))

    return render_template('edit_profile.html', user=user)


@app.route('/add_skill', methods=['POST'])
def add_skill():
    name = request.form['name']
    level = request.form['level']
    icon = request.form['icon']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO skills (name, level, icon) VALUES (%s,%s,%s)", (name, level, icon))
    mysql.connection.commit()
    flash('Skill ditambahkan!', 'success')
    return redirect(url_for('admin'))

@app.route('/update_skill/<int:id>', methods=['POST'])
def update_skill(id):
    name = request.form['name']
    level = request.form['level']
    icon = request.form.get('icon', '')

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE skills 
        SET name = %s, level = %s, icon = %s 
        WHERE id = %s
    """, (name, level, icon, id))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('admin'))

@app.route('/delete_skill/<int:id>')
def delete_skill(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM skills WHERE id=%s", [id])
    mysql.connection.commit()
    flash('Skill dihapus!', 'info')
    return redirect(url_for('admin'))


@app.route('/add_project', methods=['POST'])
def add_project():
    title = request.form['title']
    description = request.form['description']
    link = request.form['link']
    image = request.files['image']

    filename = image.filename
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO projects (title, description, image, link) VALUES (%s,%s,%s,%s)",
                (title, description, filename, link))
    mysql.connection.commit()
    flash('Project ditambahkan!', 'success')
    return redirect(url_for('admin'))


@app.route('/update_project/<int:id>', methods=['POST'])
def update_project(id):
    title = request.form['title']
    description = request.form['description']
    link = request.form['link']
    image = request.files['image']

    cur = mysql.connection.cursor()
    if image and image.filename != "":
        filename = image.filename
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cur.execute("UPDATE projects SET title=%s, description=%s, link=%s, image=%s WHERE id=%s",
                    (title, description, link, filename, id))
    else:
        cur.execute("UPDATE projects SET title=%s, description=%s, link=%s WHERE id=%s",
                    (title, description, link, id))
    mysql.connection.commit()
    flash('Project berhasil diperbarui!', 'success')
    return redirect(url_for('admin'))

@app.route('/delete_project/<int:id>')
def delete_project(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM projects WHERE id=%s", [id])
    mysql.connection.commit()
    flash('Project dihapus!', 'info')
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)
