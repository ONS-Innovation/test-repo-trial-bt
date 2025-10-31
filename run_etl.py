"""Example script demonstrating how to use the ETL pipeline."""

import logging

from test_repo_trial_bt import (
    DataExtractor,
    DataLoader,
    DataTransformer,
    ETLPipeline,
    run_etl,
)


def main() -> None:
    """Main function to demonstrate ETL pipeline usage."""
    # Define file paths
    source_file = "example_data.csv"
    output_file = "outputs/processed_data.csv"

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Method 1: Using the convenience function
    logger.info("1. Running ETL using convenience function...")
    success = run_etl(
        source_path=source_file,
        output_path=output_file,
        source_type="csv",
        output_format="csv",
        apply_transforms=True,
    )

    if success:
        logger.info("ETL pipeline completed successfully!")
    else:
        logger.error("ETL pipeline failed!")
        return

    # Method 2: Using the ETLPipeline class for more control
    logger.info("2. Running ETL using ETLPipeline class...")

    pipeline = ETLPipeline()

    # Apply some filters
    filters = {
        "quantity": {"min": 1},  # Only products with quantity >= 1
        "category": ["Electronics", "Furniture"],  # Only these categories
    }

    success = pipeline.run_pipeline(
        source_path=source_file,
        output_path="outputs/filtered_data.csv",
        source_type="csv",
        output_format="csv",
        apply_transforms=True,
        filters=filters,
    )

    if success:
        logger.info("Filtered ETL pipeline completed successfully!")

        # Get pipeline summary
        summary = pipeline.get_pipeline_summary()
        logger.info("Pipeline Summary:")
        logger.info(f"- Rows extracted: {summary['extract']['rows_extracted']}")
        logger.info(f"- Final rows after transform: {summary['transform']['final_rows']}")
        logger.info(
            f"- Transformations applied: {len(summary['transform']['transformations_applied'])}"
        )
        logger.info(f"- Output file: {summary['load']['output_path']}")
    else:
        logger.error("Filtered ETL pipeline failed!")

    # Method 3: Using individual components
    logger.info("3. Using individual ETL components...")

    # Extract
    extractor = DataExtractor()
    df = extractor.extract_csv(source_file)
    logger.info(f"Extracted {len(df)} rows")

    # Transform
    transformer = DataTransformer()
    df_cleaned = transformer.clean_data(df)
    df_enhanced = transformer.add_calculated_columns(df_cleaned)
    logger.info(f"Transformed data, final shape: {df_enhanced.shape}")

    # Load
    loader = DataLoader()
    success = loader.load_to_csv(df_enhanced, "outputs/manual_etl_output.csv")

    if success:
        logger.info("Manual ETL process completed successfully!")
    else:
        logger.error("Manual ETL process failed!")


if __name__ == "__main__":
    main()
