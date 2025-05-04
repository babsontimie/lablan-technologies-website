
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    skills = request.form.get("skills")
    with open("registrations.txt", "a") as f:
        f.write(f"Name: {name}\nEmail: {email}\nSkills: {skills}\n---\n")
    return render_template_string("""<h2>Thank you for registering!</h2><p><a href='/index.html'>Back to Home</a></p>""")

@app.route("/")
def index():
    return redirect("/index.html")

if __name__ == "__main__":
    app.run(debug=True)
