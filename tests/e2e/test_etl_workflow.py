from test_repo_trial_bt.extract import extract_from_source
from test_repo_trial_bt.load import save_to_destination
from test_repo_trial_bt.transform import apply_business_rules

raw_data = extract_from_source("example_data.csv")
transformed_data = apply_business_rules(raw_data)


def test_extract_data() -> None:
    assert raw_data is not None
    assert len(raw_data) > 0


def test_transform_data() -> None:
    assert transformed_data is not None
    assert len(transformed_data) > 0
    # Add more assertions based on expected transformations


def test_load_data() -> None:
    result = save_to_destination(transformed_data, "test_destination.csv")
    assert result is True


def test_etl_workflow() -> None:
    raw_data = extract_from_source("example_data.csv")
    transformed_data = apply_business_rules(raw_data)
    result = save_to_destination(transformed_data, "test_destination.csv")
    assert result is True
