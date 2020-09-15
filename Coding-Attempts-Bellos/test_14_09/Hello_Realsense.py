import pyrealsense2 as rs
import numpy as np
import cv2

# Διαμορφωσε τις ροές βάθους και χρώματος
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Άρχισε το  streaming
pipeline.start(config)

try:
    while True:

        # Περιμενε για το ζεύγος πλαισίων: βάθος και χρώμα
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Μετέτρεψε εικόνες σε numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Εφάρμοσε colormap στην depth image 
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Τοποθέτησε και τις 2 εικόνες οριζόντια
        images = np.hstack((color_image, depth_colormap))

        # Εμφάνησε τις εικόνες
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        key = cv2.waitKey(1)
        # Πάτα το 'q' για να κλείσει το παράθυρο αφου πρώτα το έχεις επιλέξει
        if key & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


finally:

    # Διέκοψε τη ροή
    pipeline.stop()
