from flask import Flask, request, jsonify, render_template, Response
import os
from flask_cors import CORS, cross_origin
import sys
sys.path.append('ESRGAN/')
from ESRGAN.inference import ImageRestoration
from ESRGAN.utils.utils import decodeImage

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.image_restoration = ImageRestoration(self.filename)
        # self.image_restoration = image_restoration_pipeline(self.filename,
        #                             self.save_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        save_path = "ESRGAN/results/outputImage.jpg"
        input_path = "ESRGAN/inputImage/" + clApp.filename
        clApp.image_restoration.image_restoration_pipeline(input_path, save_path)
        result = clApp.image_restoration.decode_result(save_path)

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    port = 9500
    app.run(host='0.0.0.0', port=port)
