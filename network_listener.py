import subprocess
import time
from decouple import config

DEVICE = config('DEVICE')
PERSON = config('PERSON')

present_flag = True


def scan_network():
    p = subprocess.Popen(f"arp-scan -l -r 3 | grep {DEVICE}", stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    _ = p.wait()

    return output


if __name__ == '__main__':
    output = scan_network()
    if output:
        print("Device present at script start")
        present_flag = True
    else:
        print("Device not present at script start")
        present_flag = False


    while True:
        time.sleep(5)

        output = scan_network()

        if output and not present_flag:
            subprocess.Popen(["say", f"{PERSON} has connected to the network"])
            present_flag = True
        elif not output and present_flag:
            subprocess.Popen(["say", f"{PERSON} has disconnected from the network"])
            present_flag = False