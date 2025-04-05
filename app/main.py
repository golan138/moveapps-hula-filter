import pandas as pd
import moveapps
import moveapps.io

LAT_MIN = 33.1
LAT_MAX = 33.3
LON_MIN = 35.55
LON_MAX = 35.65

input_file = "/data/input_data.rds"
output_file = "/data/output_data.rds"

print("Reading input MoveStack...")
df = moveapps.io.read_movestack(input_file)
print("Original data points:", len(df))

filtered_df = df[
    (df['location_lat'] >= LAT_MIN) &
    (df['location_lat'] <= LAT_MAX) &
    (df['location_long'] >= LON_MIN) &
    (df['location_long'] <= LON_MAX)
]

print("Filtered data points:", len(filtered_df))
moveapps.io.write_movestack(filtered_df, output_file)
print("Saved filtered data to:", output_file)
