from ultralytics import YOLO 

model = YOLO(r'training\runs\detect\train4\weights\best.pt')

results = model.predict(r'training\CaptchaDetection-1\CaptchaDetection-1\test\images\889120_png.rf.2dcf76e8028b43ac24b8cb31c4edbcf2.jpg')
print(results.tojson())
# Process results list
