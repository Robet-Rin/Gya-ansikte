import threading
import camera
import servologic

threading.Thread(target=servologic.servo_loop, daemon=True).start()
camera.camera_loop()