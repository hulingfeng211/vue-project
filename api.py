# -*- coding:utf-8 -*- 

from tornado.web import RequestHandler,escape


class UsersService(RequestHandler):
	def get(self,*args,**kwargs):
		users=[{'name':'name%s'%x,'age':x,'sex':'mail'} for x in range(100)]
		self.write(escape.json_encode(users))
