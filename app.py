from flask import Flask
from flask_restful import Resource, Api
import os
import datetime as dt

# Create the flask app.
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

        # If t0.txt doesn't exits.
        if not os.path.exists('t0.txt'):
            # Set target output file to t0.txt
            fname = 't0.txt'
        else:
            # Otherwise set it to t1.txt
            fname = 't1.txt'
        # Write timestamp to target file
        with open(fname, 'w') as f:
            f.write(str(dt.datetime.now()))
        # Return simple hello-world rest response.
        return {'hello': 'world'}


# Bind Esp32Test Resource to the "/" path.
api.add_resource(Esp32Test, '/')


if __name__ == "__main__":
    # Run app on default 5000 port and bind to 0.0.0.0
    app.run(host='0.0.0.0', debug=True)
