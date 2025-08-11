from mlflow import log_metric, log_param, log_artifact
import os
from random import choice
import mlflow
import time

metrics = ["metric1", "metric2", "metric3"]
percentages = [i for i in range(1, 100)]

os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
mlflow.set_tracking_uri("http://localhost:5000")

if __name__ == "__main__":
    for i in range(100):
        log_metric(choice(metrics), choice(percentages))
        time.sleep(1)
    