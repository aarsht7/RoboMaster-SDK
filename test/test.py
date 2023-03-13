
import robomaster
from robomaster import robot
import time
import cv2
import apriltag


# TP-Link_A1F8
# 28591108
if __name__ == '__main__':
    robomaster.config.LOCAL_IP_STR = "192.168.10.2"
    tl_drone = robot.Drone()
    tl_drone.initialize()

    SSID = tl_drone.get_ssid()
    SN = tl_drone.get_sn()
    print("drone sn: {0}".format(SN))
    print("drone ssid: {0}".format(SSID))
    print("drone battery {0}%".format(tl_drone.battery.get_battery()))

    tl_camera = tl_drone.camera
    #tl_camera.start_video_stream(display=True)
    #time.sleep(10)
    #tl_camera.stop_video_stream()

    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)



    while True:
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        img = tl_camera.read_cv2_image()
        image = img
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        options = apriltag.DetectorOptions(families="tag36h11")
        detector = apriltag.Detector(options)
        results = detector.detect(gray)
        print("[INFO] {} total AprilTags detected".format(len(results)))


        # loop over the AprilTag detection results
        for r in results:
            # extract the bounding box (x, y)-coordinates for the AprilTag
            # and convert each of the (x, y)-coordinate pairs to integers
            (ptA, ptB, ptC, ptD) = r.corners
            ptB = (int(ptB[0]), int(ptB[1]))
            ptC = (int(ptC[0]), int(ptC[1]))
            ptD = (int(ptD[0]), int(ptD[1]))
            ptA = (int(ptA[0]), int(ptA[1]))
            # draw the bounding box of the AprilTag detection
            cv2.line(image, ptA, ptB, (0, 255, 0), 2)
            cv2.line(image, ptB, ptC, (0, 255, 0), 2)
            cv2.line(image, ptC, ptD, (0, 255, 0), 2)
            cv2.line(image, ptD, ptA, (0, 255, 0), 2)
            # draw the center (x, y)-coordinates of the AprilTag
            (cX, cY) = (int(r.center[0]), int(r.center[1]))
            cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
            # draw the tag family on the image
            tagFamily = r.tag_family.decode("utf-8")
            cv2.putText(image, tagFamily, (ptA[0], ptA[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print("[INFO] tag family: {}".format(tagFamily))
        # show the output image after AprilTag detection
        cv2.imshow("Image", image)

        #cv2.waitKey(1)
    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()
    
    tl_led = tl_drone.led
    tl_led.set_led(r=0, g=0, b=0)
    
    rgb_list = [(100, 100, 100), (255, 255, 255), (255, 0, 0), (0, 0, 255),
                (0, 255, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    for rgb_info in rgb_list:
        tl_led.set_led(r=rgb_info[0], g=rgb_info[1], b=rgb_info[2])
        time.sleep(0.5)

    #tl_drone.config_sta(ssid="AarshWifi", password="$$$$$$$$")
    
    #print("Connection changed")

    tl_drone.close()
