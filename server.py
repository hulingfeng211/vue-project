# -*- coding:utf-8 -*-
from tornado.ioloop import IOLoop
from tornado.web import Application,StaticFileHandler, RequestHandler
import os
class App(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')
if __name__ == '__main__':
    handlers=[
        (r'/',App),
        #(r'/(.*)',StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__),'static')))
        (r'/(.*)',StaticFileHandler,dict(path=os.path.dirname(__file__)))
    ]

    app=Application(handlers=handlers,debug=True,
                    static_path=os.path.join(os.path.dirname(__file__),'dist'),
                    static_url_prefix="/dist/",
                    template_path=os.path.join(os.path.dirname(__file__),'src'))
    app.listen(11108)
    IOLoop.current().start()