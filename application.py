import flask
import csv
import smtplib
import ssl

app=flask.Flask(__name__)
@app.route("/")
def index():
	return flask.render_template("index.html")

@app.route("/contact")
def contact():
	return flask.render_template("contact.html")

@app.route("/render_register")
def render_register():
	return flask.render_template("register.html")

@app.route("/register",methods=["POST","GET"])
def register():
	if not flask.request.form.get("name") or not flask.request.form.get("age") or not flask.request.form.get("phone") or not flask.request.form.get("email"):
		return flask.render_template("failure.html")
	message=""
	if int(flask.request.form.get("age")) > 7 or int(flask.request.form.get("age")) < 3:
		return "Whoops! The age specified is greater than 7 or less than 3. Please check the age and try again."
	else:
		file=open("registrants.csv","a")
		writer=csv.writer(file)
		writer.writerow([flask.request.form.get("name"), flask.request.form.get("age"), flask.request.form.get("phone")])
		message="Congratulations! Your response has been recorded. We will be getting in touch with you shortly!"
	msg="Oh Hi.\nYour registration for Asha Rockstars dance class was successful!\nHere's What we got from you:\nName: " + flask.request.form.get("name") + ".\nYour child is " + flask.request.form.get("age") + " years old.\nYour phone number is:\n" + flask.request.form.get("phone") + ".\nHoping to see you in class soon!\nLove\nAsha_rocksters_bot"


	context=ssl.create_default_context()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("bots.asha.rockstars@gmail.com", "Ps180602")
	server.sendmail("bots.asha.rockstars@gmail.com", flask.request.form.get("email"), "Oh hi!\nCongratulations! We just got your registration for Asha Rockstars! Here's what we got from you:\nYour child's name is "+flask.request.form.get("name")+".\nYour child is "+str(flask.request.form.get("age"))+".\nYour phone number is: "+str(flask.request.form.get("phone"))+".\nWe will get in personal contact with you shortly!\nLove\nAsha_Rockstars_Bot!")
	server.sendmail("bots.asha.rockstars@gmail.com", "savlaasha75@gmail.com", "Oh hi!\nCongratulations! We just got your registration for Asha Rockstars! Here's what we got from you:\nYour child's name is "+flask.request.form.get("name")+".\nYour child is "+str(flask.request.form.get("age"))+".\nYour phone number is: "+str(flask.request.form.get("phone"))+".\nWe will get in personal contact with you shortly!\nLove\nAsha_Rockstars_Bot!")
	server.quit()
	return message
@app.route("/highlights")
def highlights():
	return flask.render_template("highlights.html")

@app.route("/render_admin")
def render_admin():
	return flask.render_template("adminform.html")

@app.route("/admin",methods=['POST','GET'])
def admin():
	if flask.request.form.get("password") != "asha_rockstars":
		return "Whoops! Incorrect password! Please use the back button of your browser to exit this page!"
	return flask.render_template("admin.html")
