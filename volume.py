from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

def increase_volume():
    # Get the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get the current volume level
    current_volume = volume.GetMasterVolumeLevelScalar()

    # Increase the volume by 10%
    new_volume = min(current_volume + 0.1, 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)

    print(f"Volume increased to {new_volume * 100}%")


def decrease_volume():
    # Get the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get the current volume level
    current_volume = volume.GetMasterVolumeLevelScalar()

    # Decrease the volume by 10%
    new_volume = max(current_volume - 0.1, 0.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)

    print(f"Volume decreased to {new_volume * 100}%")


if __name__ == "__main__":
    # Increase the volume
    # increase_volume()

    # Decrease the volume
    decrease_volume()
