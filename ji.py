from __future__ import print_function

import logging as log
import json
import io
import jsonpickle
import os
from yolo import YOLO
from PIL import Image
import argparse


from flask import request, Flask, jsonify

app = Flask(__name__)

log.basicConfig(level=log.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument('--model_path', help='model_path')
args = parser.parse_args()


def init(path):
    """Initialize model

    Returns: model

    """
    model_pb_path = 'final_model.h5'
    yolo = YOLO(path)
    return yolo

yolo = init(args.model_path)

@app.route('/predict', methods=['POST'])
def post_Data():
    print('hh')
    f = request.files['file']
    print(f)
    print(f.stream)
    img_test = Image.open(f)
    print("read image done")
    result = yolo.detect_rects(img_test)
    print(result)
    return jsonpickle.encode(json.dumps(result)), 201


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)