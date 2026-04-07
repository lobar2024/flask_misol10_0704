from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile')
def profil():
    user = {
    "name"  : "Sardor Rahimov",
    "age"   : 24,
    "city"  : "Toshkent",
    "job"   : "Python Developer",
    "email" : "sardor@gmail.com"
}
    return render_template('profile.html', user=user)


if __name__  == '__main__':
    app.run(debug=True)
