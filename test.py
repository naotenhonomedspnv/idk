from flask import Flask, request, jsonify, send_file
from random import randint as rand
from numpy import array,cos,sin, dot
from json import loads
import requests as req



app = Flask(__name__)


@app.route('/3d/rotate', methods=['POST'])
def rotate():
    coords = array([request.json.get("x"),request.json.get("y"),request.json.get("z")])
    rotation = array([request.json.get("rx") or request.json.get("pitch"),request.json.get("ry") or request.json.get("yaw"),request.json.get("rz") or request.json.get("roll")])
    
    rMatrices = {
        "x": lambda a: array([
            [1, 0, 0],
            [0, cos(a), -sin(a)],
            [0, sin(a), cos(a)]
        ]),
        "y": lambda a: array([
            [cos(a), 0, sin(a)],
            [0, 1, 0],
            [-sin(a), 0, cos(a)]
        ]),
        "z": lambda a: array([
            [cos(a), -sin(a), 0],
            [sin(a), cos(a), 0],
            [0, 0, 1]
        ])
    }
    
    result = [dot(dot(dot(coords,rMatrices['x'](rotation[0])), rMatrices['y'](rotation[1])), rMatrices['z'](rotation[2]))]
    
    return jsonify(result.tolist())

@app.route('/3d/project', methods=['POST'])
def project():
    coords = array([request.json.get("x"),request.json.get("y"),request.json.get("z")])
    z = coords[2]
    result = array([coords[0]/z,coords[1]/z])
    
    return jsonify(result.tolist())

@app.route('/ai/gemini', methods=['POST'])
def aiResponse():
    m = loads(request.json)['txt']
    key = loads(request.json)['key']
    payload = {
      "contents": [
        {"role":"user",
         "parts":[{
           "text": m}]}
      ]
    }
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="
    
    result = req.post(url+key, json=payload)
    
    return result.json()['candidates'][0]['content']['parts'][0]['text']

@app.route('/')
def none():
    return send_file('main.html')

if __name__ == '__main__':
    app.run()
