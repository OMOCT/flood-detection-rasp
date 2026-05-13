import pandas as pd
from sensors.waterFlow import read_flow_lpm
from sensors.waterLevel import get_distance
import time

data = []

for _ in range(200):
    distance = get(distance)
    time.sleep(1)
    flow_rate = read_flow_lpm()

    data.append([time.time(), distance, flow_rate])

df = pd.DataFrame(data, columns=["time", "distance", "flow"])
df.to_csv("flood_data.csv", index=False)
