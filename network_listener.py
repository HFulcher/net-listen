import subprocess
import time
from decouple import config
from klaxon import klaxon


DEVICE = config('DEVICE')
PERSON = config('PERSON')
DEFAULT_STRIKES = 20

connected_flag = True
strikes = 0


def scan_network():
    p = subprocess.Popen(
        f"arp-scan -l | grep {DEVICE}", stdout=subprocess.PIPE, shell=True)
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

        # Newly connected
        if output and not connected_flag:
            klaxon(
                title='Network Listener',
                message=f"{PERSON} has connected to the network"
            )
            connected_flag = True
            strikes = DEFAULT_STRIKES
        # Not on network but still in grace period, deduct strike
        elif not output and connected_flag and (strikes > 0):
            strikes -= 1
        # Connected now and before, resets strikes
        elif output and connected_flag:
            strikes = DEFAULT_STRIKES
        # Not connected and out of strikes. Setting to disconnected
        elif not output and connected_flag and (strikes == 0):
            klaxon(
                title='Network Listener',
                message=f"{PERSON} has disonnected from the network"
            )
            connected_flag = False
