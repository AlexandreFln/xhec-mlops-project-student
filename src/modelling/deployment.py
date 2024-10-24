import os

from prefect import serve
from training import train_model_workflow

if __name__ == "__main__":
    train_model_deployment = train_model_workflow.to_deployment(
        name="Model training Deployment",
        version="0.1.0",
        tags=["training", "model"],
        cron="0 0 * * 0/2",  # Reloads every second sunday
        parameters={
            "filepath": os.path.join("src", "data", "abalone.csv"),
            "artifacts_filepath": "src/web_service/local_objects",
        },
    )

    serve(train_model_deployment)
