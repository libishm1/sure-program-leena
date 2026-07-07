import time
import pandas as pd
from rtde_receive import RTDEReceiveInterface

ROBOT_IP = "192.168.1.100"          # <-- real robot IP (or URSim)
FREQUENCY_HZ = 25
INTERVAL = 1.0 / FREQUENCY_HZ
N_SAMPLES = 5

rtde_r = RTDEReceiveInterface(ROBOT_IP)   # RTDE, port 30004 (read-only, safe)
print("Connected. Collecting...")

data_list = []
try:
    for i in range(N_SAMPLES):
        x, y, z, rx, ry, rz = rtde_r.getActualTCPPose()   # metres + axis-angle
        data_list.append({
            "Timestamp": pd.Timestamp.now(),
            "X": x, "Y": y, "Z": z, "RX": rx, "RY": ry, "RZ": rz,
        })
        print(f"sample {i+1}/{N_SAMPLES} -> X {x:.3f}  Y {y:.3f}  Z {z:.3f}")
        time.sleep(INTERVAL)
finally:
    rtde_r.disconnect()

if data_list:
    df = pd.DataFrame(data_list).set_index("Timestamp")
    print("\n--- Final Time-Series DataFrame ---")
    print(df)