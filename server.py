import json, cv2, time
from flask import Flask, request, Response
from waitress import serve

app = Flask(__name__)

def validate_args(args, dict):
    for key in dict:
        val = args.get(key)
        if not val or not getattr(val, dict[key])():
            return False
    return True

@app.route("/frame",methods=["GET"])
def send_vid_data():
    pos = 1
    if request.args and validate_args(request.args,{"pos":"isdigit"}): 
        pos = int(request.args.get('pos'))
    cap = cv2.VideoCapture('badapple.mp4')
    cap.set(1,pos)
    ret, frame = cap.read()
    if not ret: return "Failed"
    cap.release()

    img_data = cv2.resize(frame,(32,32)).tolist()
    data = {
        "size" : [32,32],
        "frame" : img_data,
    }
    return json.dumps(data)

@app.route("/all",methods=["GET"])
def send_all():
    size = (32, 32)
    if request.args and validate_args(request.args, {"w":"isdigit","h":"isdigit"}):
        size = abs(int(request.args['w'])),abs(int(request.args['h']))
    cap = cv2.VideoCapture('badapple.mp4')
    data, video = {"size" : size}, []
    while True:
        ret, frame = cap.read()
        if not ret: break
        img_data = cv2.resize(frame,size).tolist()
        for i, row in enumerate(img_data):
            img_data[i] = list(map(lambda x : x[0], row))
        video.append(img_data)
    cap.release()
    data['video'] = video
    return Response(json.dumps(data), mimetype="application/json")

if __name__ == "__main__":
    print("server running")
    serve(app,host="0.0.0.0",port="2989")
