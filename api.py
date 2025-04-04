from flask import Blueprint,request
from database import *

from keras.models import load_model
from testingpage import *
import numpy as np
import pandas as pd

api = Blueprint("api",__name__)



@api.route('/api/login/')
def login():
	data = {}
	username = request.args['username']
	password = request.args['password']
	q = "select * from login inner join consumers on login.login_id = consumers.login_id where username='%s' and password='%s'" % (username,password)
	result = select(q)
	print(result)
	if(len(result) > 0):
		data['status'] = "success"
		data['result'] = result
	else:
		data['status'] = 'failed'
	return str(data)

@api.route('/api/generate_bill/')
def generate_bill():
	data = {}
	cons_id = request.args['cons_id']
	reading = request.args['reading']
	if reading.isdigit():
		q = """SELECT MAX(reading_id) AS id, cur_reading
FROM meter_reading
WHERE reading_id = (SELECT MAX(reading_id) FROM meter_reading) AND cons_id='%s'
""" % cons_id
		res = select(q)
		print(res)

		if len(res)>0 and res[0]['id']!=None:
			current_reading = res[0]['cur_reading']
			
		else:
			current_reading = 0
		print(reading)
		print(current_reading)
		if int(reading)>int(current_reading):
			q = "insert into meter_reading(cons_id,date,time,cur_reading)values('%s',curdate(),curtime(),'%s')" % (cons_id,reading) 
			print(q)
			reading_id = insert(q)

			bill_unit = int(reading) - int(current_reading)
			print(type(bill_unit))
			if bill_unit > 500 :
				amount = bill_unit * 7.50

			elif bill_unit > 400 :
				amount = bill_unit * 6.1
			elif bill_unit > 350 :
				amount = bill_unit * 5.7
			elif bill_unit > 250 :
				amount = bill_unit * 5
			elif bill_unit > 200 :
				amount = bill_unit * 4.20	
			else:
				amount = bill_unit * 3.20
			q = "insert into bill (cons_id,`usage`,amount,reading_id,bill_date,pay_status)values('%s','%s','%s','%s',curdate(),'pending')" % (cons_id,bill_unit,amount,reading_id)
			print(q)
			insert(q)
			data = {}
			data['status'] = 'success'
			print(data['status'])
		else:
			data = {}
			data['status'] = 'Greater'
			print(data['status'])
	else:
		data = {}
		data['status'] = 'Int'
		print(data['status'])
	return str(data)

@api.route('/api/get_my_bills/')
def get_my_bills():
	cons_id = request.args['cons_id']
	q = "select * from bill where cons_id='%s' order by bill_id desc" %(cons_id)
	print(q)
	res = select(q)
	data ={}
	data['status'] = 'success'
	data['result'] = res
	return str(data)


@api.route('/api/notifications/')
def notifications():
	cons_id = request.args['cons_id']
	q = "select * from notification"
	print(q)
	res = select(q)
	data ={}
	data['status'] = 'success'
	data['result'] = res
	return str(data)

@api.route('/api/payment/')
def payment():
	cons_id = request.args['cons_id']
	bill_id = request.args['bill_id']
	amount = request.args['amount']
	q = "update bill set pay_status='Payed' where bill_id='%s'" %(bill_id)
	update(q)
	q="insert into payment values(null,'%s','%s','%s',curdate())" %(bill_id,cons_id,amount)
	insert(q)
	
	data ={}
	data['status'] = 'success'
	data['method'] = 'payment'
	
	return str(data)



@api.route('/api/addwallet/')
def addwallet():
	amount = request.args['amount']
	type = request.args['type']
	lid = request.args['cons_id']
	q="insert into wallet values(null,'%s','%s','credit',curdate())" %(lid,amount)
	insert(q)
	print(q)
	data ={}
	data['status'] = 'success'
	data['method'] = 'addwallet'

	return str(data)

@api.route('/api/viewwallet/')
def viewwallet():
	data ={}
	lid = request.args['cons_id']
	q = "select * from wallet where cons_id='%s' order by wallet_id desc" %(lid)
	res = select(q)
	if res:
		q="select sum(transaction_amount) as camount from wallet where cons_id='%s' and transaction_type='credit'" %(lid)
		res1=select(q)
		if res1[0]['camount']==None:
			camount=0
		else:
			camount=res1[0]['camount']
		q="select sum(transaction_amount) as damount from wallet where cons_id='%s' and transaction_type='debit'" %(lid)
		res2=select(q)
		if res2[0]['damount']==None:
			damount=0
		else:
			damount=res2[0]['damount']
		data['val']=int(res1[0]['camount'])-int(damount)
	else:
		data['val']=0
	
	data['status'] = 'success'
	data['data'] = res
	data['method'] = 'viewwallet'
	return str(data)


@api.route('/api/complaints/',methods=['get','post'])
def complaints():
	data={}
	consid= request.args['cons_id']
	complaint = request.args['complaint']
	q = "insert into complaints values(null,'%s','%s',curdate(),'NA')" % (consid,complaint)
	id = insert(q)
	if id>0:
		data['status'] = 'success'
		data['method']="complaints"
	else:
		data['status'] = 'failed'
		data['method']="complaints"
	return str(data)
	
@api.route('/api/viewcomplaints/',methods=['get','post'])
def viewcomplaints():
	data={}
	consid = request.args['cons_id']
	q = "select * from complaints  WHERE cons_id='%s'" % (consid)

	res = select(q)
	print(res)
	if res:
		data['status']  = "success"
		data['method']="viewcomplaints"
		data['data'] = res
	else:
		data['status']	= 'failed'
		data['method']="viewcomplaints"
	return  str(data)

@api.route('/api/viewtariff/',methods=['get','post'])
def viewtariff():
	data={}
	q = "select * from tariff"
	res = select(q)
	print(res)
	if res:
		data['status']  = "success"
		data['method']="viewtariff"
		data['data'] = res
	else:
		data['status']	= 'failed'
		data['method']="viewtariff"
	return  str(data)



@api.route('/api/viewbalance/')
def viewbalance():
	data ={}
	lid = request.args['cons_id']
	q = "select * from wallet where cons_id='%s' order by wallet_id desc" %(lid)
	res = select(q)
	if res:
		q="select sum(transaction_amount) as camount from wallet where cons_id='%s' and transaction_type='credit'" %(lid)
		res1=select(q)
		if res1[0]['camount']==None:
			camount=0
		else:
			camount=res1[0]['camount']
		q="select sum(transaction_amount) as damount from wallet where cons_id='%s' and transaction_type='debit'" %(lid)
		res2=select(q)
		if res2[0]['damount']==None:
			damount=0
		else:
			damount=res2[0]['damount']
		data['val']=int(res1[0]['camount'])-int(damount)
	else:
		data['val']=0
	
	data['status'] = 'success'
	data['method'] = 'viewbalance'
	return str(data)





@api.route('/api/walletpayment/')
def walletpayment():
	cons_id = request.args['cons_id']
	bill_id = request.args['bill_id']
	amount = request.args['amount']
	q = "update bill set pay_status='Payed' where bill_id='%s'" %(bill_id)
	update(q)
	q="insert into payment values(null,'%s','%s','%s',curdate())" %(bill_id,cons_id,amount)
	insert(q)
	print(q)
	q="insert into wallet values(null,'%s','%s','debit',curdate())" %(cons_id,amount)
	insert(q)
	data ={}
	data['status'] = 'success'
	data['method']="walletpayment"
	return str(data)
from flask import session
@api.route('/api/Predict_the_current_bill/')
def Predict_the_current_bill():
    # Extract query parameters
    cons_id = request.args.get('cons_id')
    fan = request.args.get('fanUsage')
    refrigerator = request.args.get('refrigeratorUsage')
    airconditioner = request.args.get('acUsage')
    television = request.args.get('tvUsage')
    monitor = request.args.get('monitorUsage')
    motorpump = request.args.get('motorPumpUsage')
    temperature = request.args.get('temp')
    humidity = request.args.get('humidity')
    monthlyhours = request.args.get('monthlyHours')
    tariffrate = request.args.get('tariffRate')
	
    
    print(cons_id, fan, refrigerator, airconditioner, television, monitor, 
          motorpump, temperature, humidity, monthlyhours, tariffrate, "oo")
    
    # Create input data dictionary
    input_data = {
        'Fan': float(fan),
        'Refrigerator': float(refrigerator),
        'AirConditioner': float(airconditioner),
        'Television': float(television),
        'Monitor': float(monitor),
        'MotorPump': float(motorpump),
        'Temperature': float(temperature),
        'Humidity': float(humidity),
        'MonthlyHours': float(monthlyhours),
        'TariffRate': float(tariffrate)
    }
    
    # Get prediction
    predicted_bill = predict_bill(input_data)
    
    # Construct the SQL query
    q = """INSERT INTO bill_prediction
    		VALUES (null,'%s', '%s', '%s', '%s', '%s', '%s',
    			'%s', '%s', '%s', '%s', '%s', '%s')""" % (
    			cons_id, fan, refrigerator, airconditioner, television,
    			monitor, motorpump, temperature, humidity, monthlyhours,
    			tariffrate, predicted_bill)
	
    
    # Call the insert function
    insert(q)
    print(q,"ppp")
    
    # Response
    data = {}
    data['status'] = 'success'
    data['method'] = "Predict_the_current_bill"
    data['predicted_bill'] = f"${predicted_bill:.2f}"
    return str(data)


@api.route('/api/ViewPredictedout/')
def ViewPredictedout():
	cons_id = request.args['cons_id']
	# q = "SELECT * FROM `bill_prediction` WHERE `prediction_id`='%s'" %(cons_id)
	q="""
    SELECT * 
    FROM bill_prediction
    WHERE cons_id = '%s'
    ORDER BY prediction_id DESC
    LIMIT 1
"""%(cons_id)
	print(q)
	res = select(q)
	data ={}
	data['status'] = 'success'
	data['data'] = res
	data['method'] = "ViewPredictedout"
	return str(data)