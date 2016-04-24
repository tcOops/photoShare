#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext , Context
from django.views.decorators.csrf import *
import MySQLdb
from photos.models import *
import time, subprocess, datetime
from django.core import serializers #serualizer
from django.contrib.auth import authenticate, login #用django的auth做验证
import hashlib, json
import os, sys

db_host = 'localhost'
db_user = 'root'
db_pwd = 'ROOT'
db_name = 'control'
db_charset = 'utf-8'

uploadPos = '/static/upload'
defaultPath = '/static/img/default.png'

@csrf_exempt
def login(request):
	if request.method == 'GET':
		return render_to_response('login.html')
	elif request.method == 'POST':
		alias = request.POST.get('username', '')
		password = request.POST.get('password', '')
		print alias, password
		try:
			userGet = User.objects.get(alias=alias, password=password)
		except Exception, e:
			print e
			return HttpResponseRedirect('/photos/login')
		else:
			request.session['alias'] = userGet.alias
			request.session['username'] = userGet.name
			request.session['userid'] = userGet.id
			return HttpResponseRedirect('/photos/index/')
			


@csrf_exempt
def register(request):
	if request.method == 'GET':
		return render_to_response('register.html')
	elif request.method == 'POST':
		alias = request.POST.get('alias', '')
		userName = request.POST.get('name', '')
		password = request.POST.get('password', '')
		p = User(
			alias=alias,
			name=userName,
			password=password,
			createTime=str(datetime.datetime.now()).split('.')[0],
			is_deleted=0)
		p.save()
		return HttpResponseRedirect('/photos/login')
	

@csrf_exempt
def logout(request):
	del request.session['username']  #delete session
	del request.session['userid']
   	return HttpResponseRedirect('/photos/login')


def index(request):
	userName = request.session.get('username', '')
	userId = request.session.get('userid', '')
	alias = request.session.get('alias', '')
	if not userName:
		return HttpResponseRedirect('/photos/login')
	else:
		p = PhotoSet.objects.filter(
			ownerId=userId,
			is_deleted=0,
			isPrivate=True)
		cnt = 0
		for each in p:
			each.mod = cnt
			cnt += 1
			q = Photo.objects.filter(photoSetId=each.id).order_by('-id')
			if len(q) != 0:
				each.src = q[0].filePath
			else:
				each.src = defaultPath
			if cnt >=3:
				cnt = 0

		params = {"photoSets":p}
		params['username'] = userName
		params['alias'] = alias
		params['userid'] = userId

	return render_to_response("index.html",  params, context_instance=RequestContext(request))

def public(request):
	userName = request.session.get('username', '')
	userId = request.session.get('userid', '')
	alias = request.session.get('alias', '')
	if not userName:
		return HttpResponseRedirect('/photos/login')
	else:
		p = PhotoSet.objects.filter(
			is_deleted=0,
			isPublic=True)
		for each in p:
			q = Photo.objects.filter(photoSetId=each.id).order_by('-id')
			u = User.objects.filter(id=each.ownerId)
			each.username = u[0].name
			if len(q) != 0:
				each.src = q[0].filePath
			else:
				each.src = defaultPath

		params = {"photoSets":p}
		params['username'] = userName
		params['alias'] = alias
		params['userid'] = userId

	return render_to_response("public.html",  params, context_instance=RequestContext(request))

@csrf_exempt
def addPhotoSet(request):
	name = request.POST.get('photoSetName', '')
	remark = request.POST.get('photoSetMark', '')
	setType = request.POST.get('setType', '')
	#print name, remark, setType
	isPublic, isPrivate = False, False
	if setType == 'public':
		isPublic = True;
	if setType == 'private':
		isPrivate = True

	owner = request.session.get('userid', '')
	p = PhotoSet(
		name=name,
		ownerId=owner,
		isPublic=isPublic,
		isPrivate=isPrivate,
		is_deleted=0,
		createTime=str(datetime.datetime.now()).split('.')[0],
		remark = remark)
	p.save()
	if setType == 'public':
		return HttpResponseRedirect('/photos/public')

	return HttpResponseRedirect('/photos/index')

@csrf_exempt
def addPhoto(request):
	ownerId = request.session.get('userid', '0')
	setId = request.POST.get('uploadSet', '0')
	remark = request.POST.get('photomark', '')
	type = request.POST.get('type', '')


	if 'file' in request.FILES:
		osDir = os.getcwd() + '/photos' + uploadPos
		if not os.path.exists(osDir):
			os.makedirs(osDir)

		f = request.FILES['file']
		fn = osDir + '/' + f.name
		filePath = uploadPos + '/' + f.name
		with open(fn, 'wb') as dst:
			for chunk in f.chunks():
				dst.write(chunk)

		p = Photo(
			name=f.name,
			ownerId=ownerId,
			photoSetId=setId,
			createTime=str(datetime.datetime.now()).split('.')[0],
			filePath=filePath,
			remark=remark,
			is_deleted=0)
		p.save()

	if type == 'public':
		return HttpResponseRedirect('/photos/public')
	else:
		return HttpResponseRedirect('/photos/index')


@csrf_exempt
def getPhotoSet(request):
	ownerId = request.POST.get("userId", '')
	type = request.POST.get('type', '')
	if type == 'private':
		p = PhotoSet.objects.filter(ownerId=ownerId, isPrivate=True)

	if type == 'public':
		p = PhotoSet.objects.filter(ownerId=ownerId, isPublic=True)

	response = HttpResponse()
	response['Content_Type'] = 'text/javascript'
	response.write(serializers.serialize('json', p))
	return response # return results' json

@csrf_exempt
def getPhotos(request):
	photoSetId = request.POST.get('photoSetId', '0')
	p = Photo.objects.filter(photoSetId=photoSetId).order_by('-id')
	photos, data = {}, []
	for each in p:
		data.append([each.filePath, each.name, each.createTime])

	photos["photos"] = data
	response = HttpResponse()
	response['Content_Type'] = 'text/javascript'
	response.write(json.dumps(photos))
	return response
