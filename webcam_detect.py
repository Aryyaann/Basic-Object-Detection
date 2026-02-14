import cv2
from ultralytics import YOLO

def main():
    # Nano model = fastest on CPU
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)  # 0 = default webcam
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        # Predict (stream=False is fine for single frames)
        results = model.predict(source=frame, imgsz=960, conf=0.35, verbose=False)

        # Draw detections
        annotated = results[0].plot()

        cv2.imshow("Object Detection (YOLOv8n)", annotated)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
