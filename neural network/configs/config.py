import os

host = "SPBWS-PRC944"
port = "5000"
host_api_db = "http://10.216.0.197"
port_api_db = "5050"

work_path = r"C:\Users\sturkin\Desktop\FaceRec\REST_API"

path_to_images = os.path.join(work_path, "images")
path_to_models = os.path.join(work_path, "models")

api_set_percent = f'{host_api_db}:{port_api_db}/database/1.0.0/set-percent/'
