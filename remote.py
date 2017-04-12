from flask import Flask, render_template, redirect, url_for, request
import pprint
import json
from roboutil import Robo, Motor

app = Flask(__name__)
robo = Robo(Motor(16, 18, 35), Motor(38, 40, 37))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/command', methods=['POST'])
def processCommand():
	print("processing post ----------------")

	data = request.data
	# decoded data: password=default&email=test%40example.com
	if not data:
		data = request.form

	command = str(data['command'])
	print ("command is - " + command)
	robo.process(command)

	return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')