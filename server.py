# -*- coding:utf-8 -*-
from tornado.ioloop import IOLoop
from tornado.web import Application,StaticFileHandler, RequestHandler,escape
import os
from tornado.log import gen_log
import api

class App(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')



def itersubclasses(cls, _seen=None):
    """
    itersubclasses(cls)
    
    """
    
    if not isinstance(cls, type):
        raise TypeError('itersubclasses must be called with '
                        'new-style classes, not %.100r' % cls)
    if _seen is None: 
        _seen = set()
    try:
        subs = cls.__subclasses__()
    except TypeError: # fails only when cls is type
        subs = cls.__subclasses__(cls)
    for sub in subs:
        if sub not in _seen:
            _seen.add(sub)
            yield sub
            for sub in itersubclasses(sub, _seen):
                yield sub

def get_service_handlers():
    """
    get class info which must be inherite from RequestHandler and named XXXService and return array of tornado urls map
    :return [(r'/api/xxx',handler_class)]
    """
    service=[(cls.__name__,cls,cls.__module__) for cls in itersubclasses(RequestHandler) if 'Service' in cls.__name__ ]
    cls_map=map(lambda item:dict(zip(['cls_name','cls','module_name'],item)),service)
    service_urls=[]
    for item in  cls_map:
        service_pre=item.get('cls_name')[:-7]
        handler='%s.%s'%(item.get('module_name'),item.get('cls_name'))
        service_urls.append((r'/api/%s'%service_pre.lower(),item.get('cls')))
    return service_urls



if __name__ == '__main__':
    service_handlers=get_service_handlers()
   
    handlers=[
        (r'/',App),
        #(r'/(.*)',StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__),'static')))
        (r'/(.*)',StaticFileHandler,dict(path=os.path.dirname(__file__))),
    ]
    service_handlers.extend(handlers)

    app=Application(handlers=service_handlers,debug=True,
                    static_path=os.path.join(os.path.dirname(__file__),'dist'),
                    static_url_prefix="/dist/",
                    template_path=os.path.join(os.path.dirname(__file__),'src'))
    app.listen(11108)
    gen_log.info('server at localhost:11108')
    IOLoop.current().start()