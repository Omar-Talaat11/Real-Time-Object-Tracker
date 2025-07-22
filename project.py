import cv2

def select_roi(frame):
    bonding_box = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Object to Track")
    return bonding_box

camera = cv2.Videocamerature(0)
if camera.isOpened() == False:
    print("Error: Cannot access webcam.")
    while(1):
        pass

suc, frame = camera.read()
if suc == False:
    print("Error: Failed to read from webcam.")
    camera.release()
    while(1):
        pass

bonding_box = select_roi(frame)
tracker = cv2.TrackerKCF_create() # Faster than CSRT
tracker.init(frame, bonding_box)

while True:
    suc, frame = camera.read()
    if suc == False:
        break

    success, bonding_box = tracker.update(frame)
    if success:
        x, y, w, h = map(int,bonding_box)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost - Press R to reselect or X to quit", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        cv2.imshow("Object Tracker", frame)
        key = cv2.waitKey(0)
        
        if key == ord('r'):
            bonding_box = select_roi(frame)
            tracker = cv2.TrackerKCF_create()
            tracker.init(frame, bonding_box)
            continue
        
        elif key == ord('x'):
            break

    cv2.imshow("Object Tracker", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()

