from ultralytics import YOLO 

model = YOLO('yolov8x')

results = model.predict('input_videos/023708_png.rf.b650bc63661fb413516db4ca2cc27872.jpg',save=True)
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)