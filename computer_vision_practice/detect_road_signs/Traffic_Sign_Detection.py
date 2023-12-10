import cv2 
all_classes=['Roadworks','Parking','Noentry','Pedestriancrossing', 'Movementprohibition',  'Artificialroughness','Giveway','Stop'] 
CONFIDENCE_THRESHOLD=0.4 
NMS_THRESHOLD=0.2 

def load_model():
    net=cv2.dnn.readNetFromDarknet('yolo.cfg','yolo.weights') 
    model=cv2.dnn_DetectionModel(net) 
    model.setInputParams(scale=1/255,size=(416,416),swapRB=True)
    
    return model

def detect_road_signs(image,model) -> list:
    result=[] 
    classes,scores,boxes=model.detect(image,CONFIDENCE_THRESHOLD, NMS_THRESHOLD) 
    for cls,score,box in zip(classes,scores,boxes): 
        if cls==0: 
            continue 
        x,y,w,h=box 
        result.append([all_classes[cls-1],(x,y,x+w,y+h)]) 
    return result


