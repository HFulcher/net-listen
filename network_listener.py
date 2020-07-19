import subprocess
import time
from decouple import config

DEVICE = config('DEVICE')
PERSON = config('PERSON')
DEFAULT_STRIKES = 20

connected_flag = True
strikes = 0


def scan_network():
    p = subprocess.Popen(f"arp-scan -l | grep {DEVICE}", stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    _ = p.wait()

    return output


if __name__ == '__main__':
    output = scan_network()
    if output:
        print("Device present at script start")
        connected_flag = True
        strikes = DEFAULT_STRIKES
    else:
        print("Device not present at script start")
        connected_flag = False
        strikes = 0


    while True:
        time.sleep(10)

        output = scan_network()

        if output and not connected_flag:
            subprocess.Popen(["say", f"{PERSON} has connected to the network"])
            connected_flag = True
            strikes = DEFAULT_STRIKES
        elif not output and connected_flag and (strikes > 0):
            strikes -= 1
        elif output and connected_flag:
            strikes = DEFAULT_STRIKES
        elif not output and connected_flag and (strikes == 0):
            subprocess.Popen(["say", f"{PERSON} has disonnected from the network"])
            connected_flag = False