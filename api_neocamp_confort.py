from flask import Flask
from flask import jsonify
from flask import request
import json
import functions_api as f

app = Flask("__main__")

@app.route("/a", methods = ["POST"])
def all_sensors():
	print("hello world")

#API POST to return rate comfort of all sensors combined
@app.route("/a", methods = ["POST"])
def all_sensors():
	print(request.data)
	data = json.loads(request.data)
	if "luminosity" not in data:
		return "Property missing : luminosity",400
	if "humidity" not in data:
		return "Property missing : humidity",400
	if "co2" not in data:
		return "Property missing : co2",400
	if "temperature" not in data:
		return "Property missing : temperature",400

	return jsonify({"value":f.annotationCapteur(data["temperature"],data["luminosity"],data["co2"],data["humidity"])})

#API POST to return the luminosity rate comfort
@app.route("/luminosity", methods = ["POST"])
def lumin():
	print(request.data)
	data = json.loads(request.data)
	if "luminosity" not in data:
		return "Property missing : luminosity",400

	return jsonify({"value":f.luminosite(data["luminosity"])})

#API POST to return the humidity rate comfort
@app.route("/humidity", methods = ["POST"])
def humid():
	print(request.data)
	data = json.loads(request.data)
	if "humidity" not in data:
		return "Property missing : humidity",400

	return jsonify({"value":f.humidite(data["humidity"])})

#API POST to return the CO2 rate comfort
@app.route("/co2", methods = ["POST"])
def co2():
	print(request.data)
	data = json.loads(request.data)
	if "co2" not in data:
		return "Property missing : co2",400

	return jsonify({"value":f.co2(data["co2"])})

#API POST to return the temperature rate comfort
@app.route("/temperature", methods = ["POST"])
def temperat():
	print(request.data)
	data = json.loads(request.data)
	if "temperature" not in data:
		return "Property missing : temperature",400

	return jsonify({"value":f.temperature(data["temperature"])})

if __name__ == '__main__':
	app.run(debug=True)