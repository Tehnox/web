def hello_app(environ, start_response):
    query_string = environ.get('QUERY_STRING')
    if query_string is None:
        data = ''
    else:
        query_string = query_string.split('&')
        data = '\n'.join(query_string)

    data = data.encode()
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(data))),
    ]

    start_response(status, response_headers)

    return [data]
