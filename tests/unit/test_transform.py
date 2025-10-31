import pandas as pd

from test_repo_trial_bt.transform import apply_business_rules


def test_transform_data() -> None:
    # Sample input data
    input_data = pd.DataFrame(
        [
            {"id": 1, "value": 10},
            {"id": 2, "value": 20},
            {"id": 3, "value": 30},
        ]
    )

    # Expected output data after transformation
    expected_output = pd.DataFrame(
        [
            {"id": 1, "value": 10},
            {"id": 2, "value": 20},
            {"id": 3, "value": 30},
        ]
    )

    # Call the transform_data function
    output_data = apply_business_rules(input_data)

    # Assert that the output matches the expected output
    pd.testing.assert_frame_equal(output_data, expected_output)
