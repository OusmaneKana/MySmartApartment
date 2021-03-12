from app import app
# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# @app.route('/welcome/<user>')
# def welcome(user):
# 	return render_template('hello.html', name= user)


# @app.route('/AboutUs/')
# def about():
# 	return render_template('aboutUs.html')

# @app.route('/grades/')
# def grading():
# 	studentGrades  = {"Ousmane": 25,
# 						"Anil": 56,
# 						"Ramazan": 99,
# 						"Nouhaila": 9,
# 	}
# 	return(render_template('Grading.html', result=studentGrades))

# if __name__ == '__main__':
# 	app.run(debug= True)