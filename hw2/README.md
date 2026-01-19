# ESDP1 – Homework Assignment 2 (WS 2025/26)

## Objective
The goal of this homework is to design a simple, reproducible **daily data processing pipeline**
based on Earth system data.

Starting from the data that was accessed and explored in Homework 1, the focus is now on
**processing, transforming, and analysing the data in a structured and reproducible workflow**.

## Relation to Homework 1
In Homework 1, ERA5 atmospheric data was accessed via ECMWF services and inspected with respect
to structure, variables, and metadata.

This homework builds directly on the same dataset and extends the workflow from
**data access to daily processing and aggregation**.

## Dataset
- **Source:** ECMWF ERA5
- **Variable:** Specific humidity
- **Temporal resolution:** 6-hourly
- **Processing concept:** Daily aggregation and transformation

## Processing Overview
The implemented workflow follows these steps:

1. Load ERA5 data for individual days
2. Select relevant variables and levels
3. Perform daily aggregation
4. Store processed outputs in a structured format
5. Enable reproducible re-running of the pipeline

Further details are documented in the corresponding scripts and notebooks.