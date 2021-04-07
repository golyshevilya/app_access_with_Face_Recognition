import ast
import json
import shutil
import subprocess

import flask
from flask import request
from waitress import serve
import configs.config as config
import configs.config_api as config_api
import base64
import os
from threading import Thread
import train


app = flask.Flask(__name__)


def to_json(data):
    return json.dumps(data, ensure_ascii=False) + "\n"


"""_______________________________________________________________
    Function need to configure output response
    Input:
        1. API status number-int
        2. The returned data-any
    Output: 
        flask.Response
    _______________________________________________________________"""


def resp(code, data):
    return flask.Response(
        status=code,
        response=data
    )


@app.route(config_api.get_model, methods=['GET'])
def get_model():
    json_data = request.get_json(force=True)

    try:
        user_id = json_data["id_user"]
        path_to_model = os.path.join(config.path_to_models, str(user_id), "model_face.h5")
        model_binary = open(path_to_model, "rb")
        # print(model_binary.read())
    except Exception as e:
        print(e)
        return resp(400, "ERROR")
    return resp(200, to_json(base64.b64encode(bytes(str(model_binary.read()), "utf-8")).decode('ascii')))


@app.route(config_api.train_model, methods=['GET'])
def train_model():
    json_data = request.get_json(force=True)
    user_id = json_data[0]
    try:
        shutil.rmtree(f"images/train/{user_id}")
    except:
        pass
    try:
        shutil.rmtree(f"images/test/{user_id}")
    except:
        pass
    try:
        shutil.rmtree(f"models/{user_id}")
    except:
        pass
    os.mkdir(f"models/{user_id}")
    os.mkdir(f"images/train/{user_id}")
    os.mkdir(f"images/test/{user_id}")
    item = 1
    for train_data in json_data[1]:
        with open(f"images/train/{user_id}/face_{user_id}_{item}.png", "wb") as f:
            f.write(ast.literal_eval(base64.b64decode(train_data).decode()))
        item += 1
    item = 1
    for test_data in json_data[2]:
        with open(f"images/test/{user_id}/face_{user_id}_{item}.png", "wb") as f:
            f.write(ast.literal_eval(base64.b64decode(test_data).decode()))
        item += 1
    # os.system("conda activate turkin")
    # subprocess.call(["python", "train.py", user_id])
    train_thread = Thread(target=train.train, args=(user_id,))
    train_thread.start()
    return resp(200, "success")


if __name__ == "__main__":
    app.debug = True
    serve(app, host=config.host, port=config.port)
