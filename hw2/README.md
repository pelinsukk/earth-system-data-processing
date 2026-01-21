# ESDP1 – Homework Assignment 2 (WS 2025/26)

## Objective
The objective of this assignment is to design a simple, reproducible **daily data processing pipeline**
based on Earth system data.

Starting from the dataset that was accessed and explored in Homework 1, the focus is now on
**processing, transforming, and aggregating the data in a structured workflow**.

## Relation to Homework 1
In Homework 1, ERA5 atmospheric data was accessed via ECMWF services and inspected with respect
to data structure, variables, dimensions, and metadata.

This homework builds directly on the same dataset and extends the workflow from
**data access to daily processing and aggregation**.

## Dataset
- **Source:** ECMWF ERA5
- **Variable:** Specific humidity
- **Temporal resolution:** 6-hourly
- **Processing concept:** Daily aggregation (mean values)

## Processing Concept
The processing workflow follows these steps:

1. Load ERA5 data for individual days
2. Select the relevant variable (specific humidity)
3. Aggregate sub-daily data to daily means
4. Store processed outputs in a structured format
5. Enable reproducible re-running of the pipeline

## Workflow Design
The processing pipeline is designed to be modular and reproducible.
Each processing step can be executed independently, allowing easy extension
to additional variables or time periods.

Intermediate and final outputs are stored in a clear directory structure,
ensuring transparency and reproducibility.

## Notes on Scalability
The workflow is designed such that it can be extended to longer time periods
or larger spatial domains by looping over days and processing data in chunks.

This approach avoids loading large datasets into memory at once and supports
scalable Earth system data processing.

Further details are documented in the corresponding scripts and notebooks.

## How to run the processing pipeline

The daily processing pipeline can be executed from the repository root.

This command is used as a sanity check to verify that the pipeline is runnable.

Example (help output):

```bash
python hw2/scripts/daily_processing.py --help

Dependencies: xarray, netCDF4, zarr (optional: cfgrib for GRIB input)

##  This homework focuses on designing a reproducible processing pipeline rather than producing large data outputs.

