from pyramid.view import view_config


@view_config(route_name='checkData', renderer='json')
def my_view(request):
    return {'health-check': 'success'}
