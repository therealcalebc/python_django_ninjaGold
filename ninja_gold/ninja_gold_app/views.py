from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

def index(request):
	if not ('ninjaGold' in request.session and 'places' in request.session and 'activities' in request.session):
		# print("***redirecting to /start")
		return redirect('/start')
	context = {
		'title': 'Ninja Gold',
		'ninjaGold': request.session['ninjaGold'],
		'activities': request.session['activities']
	}
	context['activities'].reverse()
	# return render(request, 'index.html', context)
	return render(request, 'index2.html', context)

def process_money(request):
	# print(f"request = {request}")
	# print(f"request.POST = {request.POST}")
	place = request.POST['place']
	found = {}
	for p in request.session['places']:
		if place == p['name']:
			found = p
			break
	if found:
		earned = 0
		while earned == 0:
			earned = randint(found['minGold'], found['maxGold'])
		request.session['ninjaGold'] += earned
		temp = { 'color': '', 'message': ''}
		if found['name'] == 'Casino':
			if earned > 0:
				temp['color'] = 'success'
				temp['message'] = f"Won {earned} gold at the Casino!"
			elif earned < 0:
				temp['color'] = 'danger'
				temp['message'] = f"Lost {abs(earned)} gold at the Casino... Ouch..."
			else:
				temp['color'] = 'dark'
				temp['message'] = f"Broke even at the Casino"
		else:
			temp['color'] = 'success'
			temp['message'] = f"Found {earned} gold at the {found['name']}!"
		temp['message'] += f" ({datetime.now().strftime('%Y/%m/%d %I:%M %p')})"
		# print(f"temp = {temp}")
		request.session['activities'].append(temp)
	# print("***redirecting back to /")
	return redirect('/')

def process_money_place(request, place):
	# print(f"request = {request}")
	found = {}
	for p in request.session['places']:
		if place == p['name']:
			found = p
			break
	if found:
		earned = 0
		while earned == 0:
			earned = randint(found['minGold'], found['maxGold'])
		request.session['ninjaGold'] += earned
		temp = { 'color': '', 'message': ''}
		if found['name'] == 'Casino':
			if earned > 0:
				temp['color'] = 'success'
				temp['message'] = f"Won {earned} gold at the Casino!"
			elif earned < 0:
				temp['color'] = 'danger'
				temp['message'] = f"Lost {abs(earned)} gold at the Casino... Ouch..."
			else:
				temp['color'] = 'dark'
				temp['message'] = f"Broke even at the Casino"
		else:
			temp['color'] = 'success'
			temp['message'] = f"Found {earned} gold at the {found['name']}!"
		temp['message'] += f" ({datetime.now().strftime('%Y/%m/%d %I:%M %p')})"
		# print(f"temp = {temp}")
		request.session['activities'].append(temp)
	# print("***redirecting back to /")
	return redirect('/')

def start(request):
	request.session['ninjaGold'] = 0
	request.session['places'] = [
		{ 'name': 'Farm', 'minGold': 10, 'maxGold': 20 },
		{ 'name': 'Cave', 'minGold': 5, 'maxGold': 10 },
		{ 'name': 'House', 'minGold': 2, 'maxGold': 5 },
		{ 'name': 'Casino', 'minGold': -50, 'maxGold': 50 }
	]
	request.session['activities'] = []
	# print("***redirecting back to /")
	return redirect('/')

def reset(request):
	request.session.flush()
	# print("***redirecting to /start")
	return redirect('/start')