import json
import subprocess
import shutil
from datetime import datetime


def battery():

    try:

        result = subprocess.check_output(
            [
                "termux-battery-status"
            ]
        )

        data = json.loads(
            result.decode()
        )

        print(
            f"Battery: {data['percentage']}%"
        )

        print(
            f"Status: {data['status']}"
        )

        print(
            f"Plugged: {data['plugged']}"
        )

        print(
            f"Temperature: {data['temperature']}°C"
        )

        print(
            f"Health: {data['health']}"
        )

    except Exception as e:

        print(
            f"Battery Error: {e}"
        )


def storage():

    try:

        total, used, free = shutil.disk_usage(
            "/storage/emulated/0"
        )

        gb = 1024 ** 3

        print(
            f"Total: {total / gb:.2f} GB"
        )

        print(
            f"Used: {used / gb:.2f} GB"
        )

        print(
            f"Free: {free / gb:.2f} GB"
        )

    except Exception as e:

        print(
            f"Storage Error: {e}"
        )


def device():

    try:

        result = subprocess.check_output(
            [
                "getprop",
                "ro.product.model"
            ]
        )

        model = result.decode().strip()

        print(
            f"Device: {model}"
        )

    except Exception as e:

        print(
            f"Device Error: {e}"
        )


def current_time():

    print(
        datetime.now().strftime(
            "%H:%M:%S"
        )
    )


def current_date():

    print(
        datetime.now().strftime(
            "%d-%m-%Y"
        )
    )


def internet():

    try:

        subprocess.check_output(
            [
                "ping",
                "-c",
                "1",
                "8.8.8.8"
            ],
            stderr=subprocess.DEVNULL
        )

        print(
            "Internet: Connected"
        )

    except Exception:

        print(
            "Internet: Not Connected"
        )


def clipboard():

    try:

        result = subprocess.check_output(
            [
                "termux-clipboard-get"
            ]
        )

        text = result.decode().strip()

        if text:

            print(
                text
            )

        else:

            print(
                "Clipboard is empty."
            )

    except Exception as e:

        print(
            f"Clipboard Error: {e}"
        )


def vibrate():

    try:

        subprocess.run(
            [
                "termux-vibrate",
                "-d",
                "300"
            ]
        )

        print(
            "Vibrated."
        )

    except Exception as e:

        print(
            f"Vibrate Error: {e}"
        )


def torch_on():

    try:

        subprocess.run(
            [
                "termux-torch",
                "on"
            ]
        )

        print(
            "Torch ON"
        )

    except Exception as e:

        print(
            f"Torch Error: {e}"
        )


def torch_off():

    try:

        subprocess.run(
            [
                "termux-torch",
                "off"
            ]
        )

        print(
            "Torch OFF"
        )

    except Exception as e:

        print(
            f"Torch Error: {e}"
        )


def location():

    try:

        result = subprocess.check_output(
            [
                "termux-location"
            ]
        )

        data = json.loads(
            result.decode()
        )

        print(
            f"Latitude: {data.get('latitude')}"
        )

        print(
            f"Longitude: {data.get('longitude')}"
        )

    except Exception as e:

        print(
            f"Location Error: {e}"
        )


def handle(command):

    lower = command.lower().strip()

    if lower == "battery":

        battery()

        return True

    if lower == "storage":

        storage()

        return True

    if lower == "device":

        device()

        return True

    if lower == "time":

        current_time()

        return True

    if lower == "date":

        current_date()

        return True

    if lower == "internet":

        internet()

        return True

    if lower == "clipboard":

        clipboard()

        return True

    if lower == "vibrate":

        vibrate()

        return True

    if lower == "torch on":

        torch_on()

        return True

    if lower == "torch off":

        torch_off()

        return True

    if lower == "location":

        location()

        return True

    return False
