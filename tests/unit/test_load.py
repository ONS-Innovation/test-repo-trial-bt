import pandas as pd

from test_repo_trial_bt.load import save_to_destination


def test_load_data_success() -> None:
    # Sample data to load
    data = pd.DataFrame({"id": [1], "name": ["Test"]})
    destination = "test_destination.csv"

    # Assuming load_data returns True on success
    result = save_to_destination(data, destination)
    assert result is True


def test_load_data_failure() -> None:
    # Sample data with an invalid destination
    data = pd.DataFrame({"id": [1], "name": ["Test"]})
    destination = ""  # Invalid destination

    # Assuming load_data raises an exception on failure
    result = save_to_destination(data, destination)
    assert result is False
