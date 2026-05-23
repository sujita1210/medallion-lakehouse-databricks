# Medallion Architecture ETL Pipeline — Databricks

## Overview
End-to-end lakehouse pipeline built on Databricks using PySpark 
and Delta Lake, following the Bronze → Silver → Gold medallion pattern.

## Dataset
NYC Yellow Taxi Trip Records (Jan 2023) — ~3M rows

## Architecture
Raw CSV → Bronze (raw Delta table)
         → Silver (cleaned, validated, deduped)
         → Gold (daily stats + hourly demand aggregations)

## Key Concepts Covered
- PySpark transformations and filtering
- Delta Lake ACID transactions
- Schema enforcement and evolution
- Data quality reporting
- Delta Time Travel

## Tech Stack
Databricks | PySpark | Delta Lake | Databricks SQL | DBFS
