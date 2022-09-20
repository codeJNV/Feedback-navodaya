from flask import Flask, render_template,request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key= 'projectf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/feedback navodaya'
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50),nullable=False)
    type = db.Column(db.String(20), nullable=False)

class studentpost(db.Model):
    username = db.Column(db.String(50), nullable=False)
    sno = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    slug = db.Column(db.String(1000), nullable=True)

class Reply(db.Model):
    type= db.Column(db.String(50), nullable=False)
    adminreply = db.Column(db.String(10000), primary_key=True)
    slug = db.Column(db.String(1000), nullable=False)

class parentpost(db.Model):
    username = db.Column(db.String(50), nullable=False)
    sno = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    slug = db.Column(db.String(1000), nullable=True)

class teacherpost(db.Model):
    username = db.Column(db.String(50), nullable=False)
    sno = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    slug = db.Column(db.String(1000), nullable=True)


class adminpost(db.Model) :
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    slug = db.Column(db.String(1000), nullable=True)

class comment(db.Model) :
    username = db.Column(db.String(50),  nullable=False)
    usercomment = db.Column(db.String(300), primary_key=True)
    type = db.Column(db.String(20), nullable=True)
    sno = db.Column(db.Integer, nullable=True)


@app.route('/', methods=['GET','POST'])
def index():
    if 'user' in session and session['type'] == 'student' :
        post1 = studentpost.query.filter_by(username= session['user']).all()[::-1]
        if request.method == 'POST':
            title1 = request.form['title']
            content1 = request.form['feedback']
            post_bug = studentpost.query.filter_by(content = content1).first()
            if post_bug == None :
                if len(title1.split()) == 2:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + 'short'

                elif len(title1.split()) == 1:
                    slug1 = title1.split()[0] + '-' + 'short' + '-' + 'short'

                else:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + title1.split()[2]
                for post in post1:
                    if slug1 == post.slug:
                        slug1 = slug1 + 'n'

                post_entry = studentpost(username=session['user'], title=title1, content=content1, slug=slug1)
                db.session.add(post_entry)
                db.session.commit()

        post1 = studentpost.query.filter_by(username= session['user']).all()[::-1]
        return render_template('index.html', post=post1, username= session['user'])

    elif 'user' in session and session['type'] == 'teacher' :
        post1 = teacherpost.query.filter_by(username= session['user']).all()[::-1]
        if request.method == 'POST':
            title1 = request.form['title']
            content1 = request.form['feedback']
            post_bug = teacherpost.query.filter_by(content=content1).first()
            if post_bug == None:
                if len(title1.split()) == 2:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + 'short'

                elif len(title1.split()) == 1:
                    slug1 = title1.split()[0] + '-' + 'short' + '-' + 'short'

                else:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + title1.split()[2]
                for post in post1:
                    if slug1 == post.slug:
                        slug1 = slug1 + 'n'

                post_entry = teacherpost(username=session['user'], title=title1, content=content1, slug=slug1)
                db.session.add(post_entry)
                db.session.commit()

        post1 = teacherpost.query.filter_by(username= session['user']).all()[::-1]
        return render_template('index.html', post=post1, username= session['user'])

    elif 'user' in session and session['user'] == 'admin' :
        post1 = adminpost.query.filter_by().all()[::-1]
        return render_template("dashboard.html", post=post1)

    elif 'user' in session and session['type'] == 'parent' :
        post1 = parentpost.query.filter_by(username= session['user']).all()[::-1]
        if request.method == 'POST':
            title1 = request.form['title']
            content1 = request.form['feedback']
            post_bug = parentpost.query.filter_by(content=content1).first()
            if post_bug == None:
                if len(title1.split()) == 2:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + 'short'

                elif len(title1.split()) == 1:
                    slug1 = title1.split()[0] + '-' + 'short' + '-' + 'short'

                else:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + title1.split()[2]
                for post in post1:
                    if slug1 == post.slug:
                        slug1 = slug1 + 'n'

                post_entry = parentpost(username=session['user'], title=title1, content=content1, slug=slug1)
                db.session.add(post_entry)
                db.session.commit()

        post1 = parentpost.query.filter_by(username= session['user']).all()[::-1]
        return render_template('index.html', post=post1, username= session['user'])
    return render_template('login.html')



@app.route("/issue/<string:post_slug>/", methods=['GET'])
def issue(post_slug):
    if 'user' in session :
        if 'user' in session and session['type'] == 'student':
            post1 = studentpost.query.filter_by(slug=post_slug).first()
            reply1 = Reply.query.filter_by(type='student', slug=post_slug).all()
            return render_template('issue.html', post=post1, reply=reply1)
        elif 'user' in session and session['type'] == 'teacher':
            post1 = teacherpost.query.filter_by(slug=post_slug).first()
            reply1 = Reply.query.filter_by(type='teacher', slug=post_slug).all()
            print(reply1)
            return render_template('issue.html', post=post1, reply=reply1)
        elif 'user' in session and session['type'] == 'parent':
            post1 = parentpost.query.filter_by(slug=post_slug).first()
            reply1 = Reply.query.filter_by(type='parent', slug=post_slug).all()
            return render_template('issue.html', post=post1, reply=reply1)

    return redirect(url_for('login'))



@app.route("/login/", methods=['GET','POST'])
def login():

    if request.method == "POST":
        username = request.form.get ("uname")
        userpass = request.form.get("pass")
        user = User.query.filter_by(username=username).first()
        if username == 'admin' and userpass == 'projectf':
            session['user'] = username
            session['type'] = 'admin'
            post1 = adminpost.query.filter_by().all()[::-1]
            return render_template('dashboard.html', post=post1)

        elif user.password == userpass :
            if user.type == 'student' :
                session['user'] = username
                session['type'] = user.type
                post1 = studentpost.query.filter_by().all()[::-1]
                return render_template('index.html', post=post1, username= session['user'])

            elif user.type == 'teacher' :
                session['user'] = username
                session['type'] = user.type
                post1 = teacherpost.query.filter_by().all()[::-1]
                return render_template('index.html', post=post1, username= session['user'])

            elif user.type == 'parent' :
                session['user'] = username
                session['type'] = user.type
                post1 = parentpost.query.filter_by().all()[::-1]
                return render_template('index.html', post=post1, username= session['user'])

    elif 'user' in session and session['user'] == 'admin' :
        post1 = adminpost.query.filter_by().all()[::-1]
        return render_template("dashboard.html", post=post1)

    elif 'user' in session and  session['type'] == 'teacher' :
        post1 = teacherpost.query.filter_by().all()[::-1]
        return render_template("index.html", post=post1)

    elif 'user' in session and  session['type'] == 'student' :
        post1 = studentpost.query.filter_by().all()[::-1]
        return render_template("index.html", post=post1)

    elif 'user' in session and  session['type'] == 'parent' :
        post1 = parentpost.query.filter_by().all()[::-1]
        return render_template("index.html", post=post1)


    return render_template('login.html')



@app.route("/edit/<string:srno>", methods=['GET','POST'])
def edit(srno) :
    if 'user' in session and session['user'] == 'admin':
        post1 = adminpost.query.filter_by().all()[::-1]
        if request.method == 'POST':
            if srno == '0':
                title1 = request.form['title']
                content1 = request.form['feedback']
                if len(title1.split()) == 2:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + 'short'

                elif len(title1.split()) == 1:
                    slug1 = title1.split()[0] + '-' + 'short' + '-' + 'short'

                else:
                    slug1 = title1.split()[0] + '-' + title1.split()[1] + '-' + title1.split()[2]
                for post in post1:
                    if slug1 == post.slug:
                        slug1 = slug1 + 'n'
                post_entry = adminpost(title=title1, content=content1, slug=slug1)
                db.session.add(post_entry)
                db.session.commit()
                return redirect(url_for('login'))

            else :
                post_update = adminpost.query.filter_by(sno=srno).first()
                post_update.title = request.form['title']
                post_update.content = request.form['feedback']
                try :
                    db.session.commit()
                except :
                    return 'There is a problem in updating your post'




                return redirect(url_for('login'))

        post_update = adminpost.query.filter_by(sno=srno).first()
        return render_template('edit.html',sno=srno, post=post_update)



@app.route("/delete/<string:srno>", methods=['GET', 'POST'])
def delete(srno):
    if 'user' in session and session['user'] == 'admin':
        post = adminpost.query.filter_by(sno=srno).first()
        db.session.delete(post)
        db.session.commit()
        post1 = adminpost.query.filter_by().all()[::-1]

    return redirect(url_for('login'))


@app.route("/check_issue", methods=['GET','POST'])
def check_issue() :
    return render_template('check_issue.html')

@app.route("/parentissue", methods=['GET','POST'])
def parentissue() :
    if 'user' in session and session['user'] == 'admin':
        post1 = parentpost.query.filter_by().all()[::-1]
        return render_template('display_issue.html', post=post1 , usertype= 'parent')

    return redirect(url_for('login'))


@app.route("/teacherissue", methods=['GET','POST'])
def teacherissue() :
    if 'user' in session and session['user'] == 'admin':
        post1 = teacherpost.query.filter_by().all()[::-1]
        return render_template('display_issue.html', post=post1, usertype= 'teacher')

    return redirect(url_for('login'))

@app.route("/studentissue", methods=['GET','POST'])
def studentissue() :
    if 'user' in session and session['user'] == 'admin':
        post1 = studentpost.query.filter_by().all()[::-1]
        return render_template('display_issue.html', post=post1, usertype= 'student')

    return redirect(url_for('login'))


@app.route("/issue_adminview/<string:usertype>/<string:post_slug>/", methods=['GET'])
def issue_adminview(usertype,post_slug):
    if 'user' in session and session['user'] == 'admin':
        if usertype == 'student' :
            post1 = studentpost.query.filter_by(slug=post_slug).first()
            reply1 = Reply.query.filter_by(slug=post_slug).all()
            return render_template('issue_adminview.html', post=post1 ,usertype=usertype, reply=reply1)

        if usertype == 'teacher':
            post1 = teacherpost.query.filter_by(slug=post_slug).first()
            reply1 = Reply.query.filter_by(slug=post_slug).all()
            return render_template('issue_adminview.html', post=post1, usertype=usertype, reply=reply1)
        if usertype == 'parent':
            post1 = parentpost.query.filter_by(slug=post_slug).first()
            reply1 = Reply.query.filter_by(slug=post_slug).all()
            return render_template('issue_adminview.html', post=post1, usertype=usertype, reply=reply1)

    return redirect(url_for('login'))


@app.route("/reply/<string:usertype>/<string:post_slug>/", methods=['POST'])
def reply(usertype,post_slug):
    if 'user' in session and session['user'] == 'admin':
        if request.method == 'POST' :
            if usertype == 'student' :
                post1 = studentpost.query.filter_by(slug=post_slug).first()
                reply1 = request.form['reply']
                slug1 = post_slug
                type1 = usertype
                reply_entry = Reply(adminreply=reply1, slug=slug1, type=type1)
                db.session.add(reply_entry)
                db.session.commit()
                return redirect(url_for('studentissue'))
            if usertype == 'teacher' :
                post1 = teacherpost.query.filter_by(slug=post_slug).first()
                reply1 = request.form['reply']
                slug1 = post_slug
                type1 = usertype
                reply_entry = Reply(adminreply=reply1, slug=slug1, type=type1)
                db.session.add(reply_entry)
                db.session.commit()
                return redirect(url_for('teacherissue'))

            if usertype == 'parent' :
                post1 = parentpost.query.filter_by(slug=post_slug).first()
                reply1 = request.form['reply']
                slug1 = post_slug
                type1 = usertype
                reply_entry = Reply(adminreply=reply1, slug=slug1, type=type1)
                db.session.add(reply_entry)
                db.session.commit()
                return redirect(url_for('parentissue'))




    return redirect(url_for('login'))





@app.route("/updates", methods=['GET'])
def updates():
    if 'user' in session:
        post1 = adminpost.query.filter_by().all()[::-1]
        return render_template('updates.html', post=post1)

    return redirect(url_for('login'))



@app.route("/update/<string:srno>", methods=['GET', 'POST'])
def update(srno):
    if 'user' in session :
        if session['type'] != 'student' :
            if request.method == 'POST':
                comment1 = request.form['comment']
                username1 = session['user']
                type1 = session['type']
                comment_bug = comment.query.filter_by( usercomment = comment1 ).first()
                if comment_bug == None :
                    comment_entry = comment(usercomment=comment1, username=username1, type=type1, sno=srno)
                    db.session.add(comment_entry)
                    db.session.commit()
                    comments1 = comment.query.filter_by(sno=srno).all()[::-1]
                    post1 = adminpost.query.filter_by(sno=srno).first()
                    return render_template('update.html', post=post1, sno=srno, comments=comments1)


        comments1 = comment.query.filter_by(sno=srno).all()[::-1]
        post1 = adminpost.query.filter_by(sno=srno).first()
        return render_template('update.html', post=post1, comments=comments1, sno=srno, usertype=session['type'])

    return redirect(url_for('login'))


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/logout/")
def logout():
    session.pop('user')
    session.pop('type')
    return redirect(url_for('login'))


@app.route("/deletecomment/<string:usercomment>/<string:srno>", methods=['GET', 'POST'])
def deletecomment(usercomment,srno):
    if 'user' in session and session['user'] == 'admin':
        post = comment.query.filter_by(usercomment = usercomment).first()
        db.session.delete(post)
        db.session.commit()
        comments1 = comment.query.filter_by(sno=srno).all()[::-1]
        post1 = adminpost.query.filter_by(sno=srno).first()
        return render_template('update.html', post=post1, comments=comments1, sno=srno, usertype=session['type'])

    return redirect(url_for("login"))


app.run(debug = True)