import flwr as fl
from flwr.server.strategy import FedAvg

import mlcube_utils as mlcube


def main():
    strategy = FedAvg(initial_parameters=mlcube.initial_parameters())
    fl.server.start_server(
        "0.0.0.0:8080", strategy=strategy, config={"num_rounds": 3},
    )


# Start Flower server for three rounds of federated learning
if __name__ == "__main__":
    main()
