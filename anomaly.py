import pandas as pd

df = pd.read_excel("support_tickets.xlsx")

def detect_anomalies():
    anomalies = []
    avg_time = df["resolution_time_hrs"].mean()
    long_resolution = df[df["resolution_time_hrs"] > avg_time * 2]
    anomalies.extend(long_resolution.to_dict("records"))

    critical_open = df[(df["priority"] == "Critical") & (df["status"] != "Resolved")]
    anomalies.extend(critical_open.to_dict("records"))
    return anomalies
