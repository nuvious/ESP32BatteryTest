from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import datetime as dt

app = Flask(__name__)
api = Api(app)

class Esp32Test(Resource):
    def get(self):
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
