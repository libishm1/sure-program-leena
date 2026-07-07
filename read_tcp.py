# pip install ur-rtde     (import name is rtde_receive / rtde_control)
import time
from rtde_receive import RTDEReceiveInterface

ROBOT_IP = "192.168.1.100"   # <-- put the REAL robot IP (pendant: Settings > Network)

rtde_r = RTDEReceiveInterface(ROBOT_IP)   # connects to RTDE on port 30004
print("Connected. Reading live values (Ctrl-C to stop)...\n")

try:
    while True:
        q   = rtde_r.getActualQ()            # 6 joint angles, radians
        tcp = rtde_r.getActualTCPPose()      # [x, y, z, rx, ry, rz]  metres + axis-angle

        q_deg = [round(a * 180.0 / 3.141592653589793, 1) for a in q]
        tcp_r = [round(v, 4) for v in tcp]
        print(f"joints(deg): {q_deg}   TCP(m,rad): {tcp_r}")

        time.sleep(0.1)                      # 10 Hz print (RTDE itself runs up to 500 Hz)

except KeyboardInterrupt:
    print("\nstopped")
finally:
    rtde_r.disconnect()
