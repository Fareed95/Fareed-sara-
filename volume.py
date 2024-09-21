import os

def increase_volume():
    # Increase the volume by 10%
    os.system("pactl set-sink-volume @DEFAULT_SINK@ +10%")
    print("Volume increased by 10%")

def decrease_volume():
    # Decrease the volume by 10%
    os.system("pactl set-sink-volume @DEFAULT_SINK@ -10%")
    print("Volume decreased by 10%")

if __name__ == "__main__":
    # Increase the volume
    increase_volume()
    # decrease_volume()

    # Decrease the volume
    # decrease_volume()
