from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle():
    return handle_agent(SampleAgent, request)

def handle_agent(cls, request):
    """Helper that routes 'method calls' to a real agent object."""
    content = request.json
    method = content['method']
    params = content.get('params')
    response = None

    if method == 'register':
        response = cls.register()
    elif method == 'check':
        response = cls(params).check()
    elif method == 'receive':
        response = cls(params).receive(params['message'])
    else:
        response = {}

    return jsonify(response)


class SampleAgent:
    """This is the agent itself"""

    def __init__(self, params):
        """Set some convenience variables.

        Oject is created from scratch on each method invocation"""
        self.options = params['options']
        self.memory = params['memory'] or {}
        self.credentials = params['credentials']

    def register():
        """Register our metadata"""
        return {
                'result': {
                    'name': 'PythonTestAgent',
                    'display_name': 'Python Test Agent',
                    'description': 'Agent Description',
                    'default_options': { 'a': 'b' }
                    }
                }

    def check(self):
        """This is run on schedule. Do something useful."""
        messages = []
        if self.memory.get('last_message'):
            messages.append(self.memory['last_message'])
        return {
                'result': {
                    'logs': ['Check done'],
                    'errors': ['Sample error'],
                    'messages': messages
                    }
                }

    def receive(self, message):
        """Process message and do something with it."""
        self.memory['last_message'] = message['payload']
        return {
                'result': {
                    'logs': ['New message received'],
                    'errors': [],
                    'messages': [],
                    'memory': self.memory
                    }
                }


if __name__ == '__main__':
    app.run()
