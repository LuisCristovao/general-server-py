# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:12:02 2019

@author: Luis Cristóvão
"""

import flask as fl


app = fl.Flask(__name__, static_url_path='')

map = {
    "my_key": "333"
}

@app.route('/')
def index_route():
    return fl.render_template('index.html')

@app.route('/getKey/<key>')
def getKey(key):
	
	resp = fl.Response(map[key])
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

@app.route('/setKey/<key>/<data>')
def setKey(key,data):
	map[key]=data
	resp = fl.Response("Key {0}:{1} inserted!".format(key,data))
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

@app.route('/getKey',methods=["POST"])
def getKeyPost():
	received_values=fl.request.data.decode("ascii")
	resp = fl.Response(map[received_values])
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp
    
@app.route('/setKey/<key>',methods=["POST"])
def setKeyPost(key):
	received_values=fl.request.data.decode("ascii")
	map[key]=received_values
	resp = fl.Response("Key {0}:{1} inserted!".format(key,received_values))
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp
     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)