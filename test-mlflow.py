import mlflow
from mlflow import log_metric, log_param, log_artifact
import os
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
mlflow.set_tracking_uri("http://localhost:5000")
if __name__ == "__main__":
    log_param("param1", 1)
    log_param("verbosity", "debug")
    log_metric("metric1", 2)

    