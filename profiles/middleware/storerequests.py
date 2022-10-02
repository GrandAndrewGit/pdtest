import time
import json
import logging

logging.basicConfig(filename="requests.log", format='%(message)s',level=logging.INFO)


class AllRequestLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        method = request.method
        request_url = request.get_full_path()

        response = self.get_response(request)

        execution_time = round(time.time() - start_time, 4)
        logging.info('Method: ' + method + '  ---  ' + 'Url: ' + request_url + '  ---  ' + ' Exctime ' + str(execution_time))

        return response