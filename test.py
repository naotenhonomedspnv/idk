from flask import Flask, request, jsonify, send_file
from json import loads
import requests as req
app = Flask(__name__)
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
if __name__ == '__main__':
    app.run()
