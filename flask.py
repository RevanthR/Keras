from flask import Flask
app=Flask(__name__)

@app.route('/bio',methods=['POST','GET'])
def bio_form():
	if request.method='POST'
		username=request.form('username')
		email=request.form('email')
		hobbies=request.form('hobbies')
		return redirect(url_for('showbio',username=username,email=email,hobbies=hobbies))
	return render_template('bio_form.html')

@app.route('/showbio')
def show():
	username=request.args.get('username')
	email=request.args.get('email')
	hobbies=request.args.get('hobbies')
	return render_template("showbio.html",username=username,email=email,hobbies=hobbies)		
if __name__=="__main__"
	app.run(debug=True,port=8080)