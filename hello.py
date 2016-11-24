from flask import Flask, jsonify,request,abort
import os
import psycopg2
import json
import binascii
app = Flask(__name__)
port = int(os.getenv("PORT", 64781))
from twilio.rest import TwilioRestClient


'''
################### GET request to get all user info  ##########################
'''

@app.route('/get', methods=['GET'])
def GetAllUseInfo():
	ACCOUNT_SID = 'ACe4f8a304ab7204bd3adb16decbf35e28'
	AUTH_TOKEN = '7eaaeaac35ee2382a51906c6684a03a0'
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	client.messages.create(to = '+971504224291',from_ = '+16305900043',body = 'Emergency alert',)
	return "sucessfull"

@app.route('/post', methods=['POST'])
def post():
	if not request.json or not 'phone' in request.json:
		abort
	phone = request.json['phone']
	ACCOUNT_SID = 'ACe4f8a304ab7204bd3adb16decbf35e28'
	AUTH_TOKEN = '7eaaeaac35ee2382a51906c6684a03a0'
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	client.messages.create(to = phone ,from_ = '+16305900043',body = 'Emergency alert, Evacuate!!',)
	return "sucessfull"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
