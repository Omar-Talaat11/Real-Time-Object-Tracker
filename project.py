import cv2

def select_object(frame):
    """ Function to select the object to be tracked """
    bonding_box = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Object to Track")
    return bonding_box

camera = cv2.VideoCapture(0) # Open camera
if camera.isOpened() == False: # check if camera is opened
    print("Error: Cannot access webcam.")
    while(1):
        pass

suc, frame = camera.read() # Read first frame
if suc == False:    # Check if frame is read successfully
    print("Error: Failed to read from webcam.")
    camera.release()
    while(1):
        pass

bonding_box = select_object(frame) # Select object to be tracker
tracker = cv2.TrackerKCF_create() # Faster than CSRT
tracker.init(frame, bonding_box) # Initiate tracking the object

while True: # Loop until the user exits or code fails
    suc, frame = camera.read()  # Read frame
    if suc == False: # check if frame is read and break otherwise
        break

    success, bonding_box = tracker.update(frame) # Update the tracker to get new position
    if success: # check if updated successfully
        x, y, w, h = map(int,bonding_box) # get the bounding box coordinates and dimentions in int format
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # draw rectangle around the object
        cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2) # put text that the tracker is tracking
    else: # if the tracker not updated successfully
        cv2.putText(frame, "Lost - Press R to reselect or X to quit", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2) # tell the user to press r to reselct or x to exit
        cv2.imshow("Object Tracker", frame)
        key = cv2.waitKey(0) # Wait for user input
        
        if key == ord('r'): # if user chose to reselect
            bonding_box = select_object(frame) # select the object again
            tracker = cv2.TrackerKCF_create() # create the tracker
            tracker.init(frame, bonding_box) # initiate the tracker
            continue
        
        elif key == ord('x'): # end the loop if user pressed x
            break

    cv2.imshow("Object Tracker", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('x'): # end the loop if user pressed x
        break

camera.release()
cv2.destroyAllWindows()

