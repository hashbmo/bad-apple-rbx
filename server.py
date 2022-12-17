import json, cv2, time
from flask import Flask, request, Response
from waitress import serve

app = Flask(__name__)

def encode(arr):
    encoded = []
    cur, count = None, 0
    for x in arr:
        if cur != x:
            if cur != None: encoded.append((cur,count))
            cur, count = x, 1
        else:
            count += 1
    encoded.append((cur,count))
    return encoded

def validate_args(args, dict):
    for key in dict:
        val = args.get(key)
        if not val or not getattr(val, dict[key])():
            return False
    return True

def get_frame(cap,size):
    ret, frame = cap.read()
    if not ret: return False
    img_data = cv2.resize(frame,size).tolist()
    serialised = []
    for row in img_data:
        for x in row: serialised.append(x[0])
    return serialised

@app.route("/frame",methods=["GET"])
def send_vid_data():
    pos, size = 1, (32,32)
    if request.args and validate_args(request.args,{"pos":"isdigit","w":"isdigit","h":"isdigit"}): 
        pos = int(request.args.get('pos'))
        size = abs(int(request.args['w'])),abs(int(request.args['h']))

    cap = cv2.VideoCapture('badapple.mp4')
    cap.set(1,pos)
    serialized = get_frame(cap,size)
    data = {
        "size" : [32,32],
        "frame" : serialized,
    }
    return json.dumps(data)

@app.route('/all',methods=["GET"])
def send_all_v2():
    size = (32,32)
    if request.args and validate_args(request.args, {"w":"isdigit","h":"isdigit"}):
        size = abs(int(request.args['w'])),abs(int(request.args['h']))
    start = time.time()
    cap = cv2.VideoCapture('badapple.mp4')
    data, video = {"size" : size}, []
    while True:
        serialised = get_frame(cap,size)
        if not serialised: break
        video.append(encode(serialised))
    cap.release()
    data['video'] = video
    print(time.time() - start)
    return Response(json.dumps(data), mimetype="application/json")

if __name__ == "__main__":
    print("server running")
    serve(app,host="0.0.0.0",port="2989")
