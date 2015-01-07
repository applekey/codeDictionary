from bottle import route, run, template,static_file,get,post,request,BaseResponse
import os,sys
from threading import Thread
import time
import webbrowser
import json
import re
import cherrypy
##some imports to make pyinstaller work





@route('/viewer')
def hello():
  return  static_file('viewer.html',root='static')


@route(':path#.+#', name='static')
def static(path):
      return static_file(path, root='static')

    


run(server='cherrypy',host='localhost', quiet=True,port=1234,debug=False)





