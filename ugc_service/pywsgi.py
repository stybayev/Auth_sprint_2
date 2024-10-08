from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from main import app

http_server = WSGIServer(('', 8084), app)
http_server.serve_forever()
