import Leap
import time
import subprocess

class GestureListener(Leap.Listener):
    def on_connect(self, controller):
        print("Connected to Leap Motion")

    def on_frame(self, controller):
        frame = controller.frame()
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)
                if swipe.direction.x > 0:
                    print("Swipe right detected")
                    # Execute a command or trigger an action for right swipe
                    subprocess.run(["say", "Right swipe detected"])
                else:
                    print("Swipe left detected")
                    # Execute a command or trigger an action for left swipe
                    subprocess.run(["say", "Left swipe detected"])

def main():
    listener = GestureListener()
    controller = Leap.Controller()

    controller.add_listener(listener)
    print("Press Enter to quit...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()