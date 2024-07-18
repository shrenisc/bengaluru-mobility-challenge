from ultralytics import YOLO

model = YOLO('yolov8m.pt')  
data_path = 'data.yaml'


# model.train(
#     data=data_path,  
#     epochs=50,      
#     batch=16,        
#     imgsz=640,      
#     weights='yolov8m.pt',  
#     resume=False    
# )