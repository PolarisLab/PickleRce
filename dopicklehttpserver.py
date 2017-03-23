#coding:utf-8
__author__ = 'bit4'
import BaseHTTPServer
import urllib
import cPickle

class ServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        if "?payload" in self.path:
            query= urllib.splitquery(self.path)
            action = query[1].split('=')[1]  #这种写法是一个坑，如果参数payload的值中包含了等号，将导致不正确，pickle将报“insecure string pickle”错误。
            print action
            try:
                x = cPickle.loads(action) #string argv
                content = x
            except Exception,e:
                print e
                content = e

        else:
            content = "hello World"

        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write("<html>")
        self.wfile.write(" %s " % content)
        self.wfile.write("</html>")

if __name__ == '__main__':

    srvr = BaseHTTPServer.HTTPServer(('',8000), ServerHandler)
    print 'started  httpserver...'
    srvr.serve_forever()