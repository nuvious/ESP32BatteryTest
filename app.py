from flask import Flask
from flask_restful import Resource, Api
import os
import datetime as dt

app = Flask(__name__)
api = Api(app)


class Esp32Test(Resource):
    """
    A simple Flask-RESTful resource class to log times of initial and most
    recent rest requests to files t0.txt and t1.txt.
    """
    def get(self):
        """
        Returns a hello-world rest response and logs time of initial request
        to t0.txt and subsequent requests to t1.txt.

        Returns:
            dict: A hello-world rest response.
        """
        if not os.path.exists('t0.txt'):
            fname = 't0.txt'
        else:
            fname = 't1.txt'
        with open(fname, 'w') as f:
            f.write(str(dt.datetime.now()))
        return {'hello': 'world'}


api.add_resource(Esp32Test, '/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
