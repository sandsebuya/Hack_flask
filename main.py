from flask import Flask, request,jsonify, Response
import psycopg2
app = Flask(__name__)


def connect_to_db():
	try:
		conn = psycopg2.connect(dbname='nzsjlari', user='nzsjlari', password='DAKyGuo8-6zj5VI6XYOW2jEZXGVrCiTf',
		                        host='snuffleupagus.db.elephantsql.com')
	except:
		print('Can`t establish connection to database')
	cursor = conn.cursor()
	return conn, cursor
conn,cursor = connect_to_db()



@app.route("/api",methods=['GET'])
def get_api():
	#cursor.execute(f"select id,name,longitude,latitude from hackaton")
	cursor.execute(f"select longitude,latitude from hackaton")
	list_data = []
	#list_keys = ["id", "name", "longitude", "latitude"]
	list_keys = [ "latitude","longitude" ]
	responce = cursor.fetchall()
	if responce == []:
		return "error", 500
	for i in responce:
		list_data.append(dict(zip(list_keys, i)))
	return list_data, 200


@app.route("/api/id_get",methods=["POST"])
def get_data_by_id():
	longitude = request.get_json(silent=True)["longitude"]
	latitude = request.get_json(silent=True)["latitude"]
	print(longitude)
	print(latitude)

	try:
		cursor.execute(f"select name, description,url from hackaton where (longitude = '{longitude}' && latitude = '{latitude}')")
		list_data = []
		list_keys = ["name", "description", "url"]
		responce = cursor.fetchall()
		if responce == []:
			return "NO item", 500
		for i in responce:

			return dict(zip(list_keys, i)), 200
	except:
		return "error", 500




@app.route("/type",methods=['POST'])
def get_type():
	print("ffefeeffeef")
	try:
		type_=request.get_json(silent=True)["type"]
	except:
		pass
	cursor.execute(f"select id, longitude,latitude,name from hackaton where type = {type_}")
	list_data = []
	list_keys = ["id", "latitude","longitude", "name"]
	responce = cursor.fetchall()
	if responce == []:
		return "error", 500
	for i in responce:
		list_data.append(dict(zip(list_keys, i)))
	return list_data, 200


app.run(debug=True, host='10.131.57.149')

