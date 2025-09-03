import cv2
from ultralytics import YOLO

# مدل آموزش‌داده‌شده
model = YOLO("best.pt")

# لیست رنگ برای هر کلاس
# فرض: 0 = with_mask , 1 = without_mask
colors = {
    0: (0, 255, 0),   # سبز برای with_mask
    1: (0, 0, 255)    # قرمز برای without_mask
}

# باز کردن وب‌کم
cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    if not ret:
        break

    # پیش‌بینی با YOLO
    results = model(frame , verbose=False)

    # پردازش نتایج
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0].item())      # کلاس
            conf = float(box.conf[0].item())  # اطمینان
            x1 , y1 , x2 , y2 = map(int , box.xyxy[0])  # مختصات باکس

            # رسم باکس
            color = colors.get(cls , (255, 255, 255))
            cv2.rectangle(frame , (x1, y1) , (x2, y2) , color , 2)
            label = f"{r.names[cls]} {conf:.2f}"
            cv2.putText(frame , label , (x1 , y1 - 10) ,
                        cv2.FONT_HERSHEY_SIMPLEX , 0.6 , color , 2)

    cv2.imshow("Mask Detection" , frame)

    # کلید q برای خروج
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
