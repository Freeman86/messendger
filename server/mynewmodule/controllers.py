
from protocol import make_response


def my_new_controller(request):
    data = request.get('data')
    return make_response(request, 200, data)