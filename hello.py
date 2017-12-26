def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    #qs = parse_qs(environ['QUERY_STRING'])
    #return ['%s=%s<br>' % (k, qs[k][0]) for k in qs]
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body
