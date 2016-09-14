from jinja2 import Environment, FileSystemLoader
from os.path import dirname
from bottle import route, run, request, error

JINJA_ENV = Environment(
    loader=FileSystemLoader(dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'])


@route('/own_board.html')
def own_board():
    """
    Displays our board

    :rtype: str
    :return: Html string
    """
    return 'my own board'


@route('/opponent_board.html')
def opponent_board():
    """
    Displays the opponents board

    :rtype: str
    :return: Html string
    """
    return 'their board yo'


def respond(template_file, params):
    """
    Responds with the template file

    :param template_file: template file to respond with
    :type template_file: str
    :param params: dictionary of attributes to pass
    :type params: dict
    :rtype: str
    :return: The file rendered as a string
    """
    tpl = JINJA_ENV.get_template(template_file)
    return tpl.render(**params)


@route('/', method='POST')
def handle_fire():
    """
    Receives fire request from the opponent and handles it accordingly
        - Sends a response to the opponent

    :rtype: str
    :return: "Value is x, y"
    """
    postdata = request.body.read()
    print postdata  # this goes to log file only, not to client
    x = request.forms.get('x')
    y = request.forms.get('y')
    return 'Value is {}, {}'.format(x, y)


@error(404)
def handle_404():
    print '404'


@error(410)
def handle_410():
    print '410'


@error(400)
def handle_400():
    print '400'


if __name__ == '__main__':
    run(host='localhost', port=5000, debug=True)