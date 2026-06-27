# 🚀 NASA Software Visualization Pipeline

An end-to-end data pipeline that ingests NASA software data from a public API, transforms it with dbt, and visualizes it in Looker Studio also build with Claude.

## 📊 Dashboard

[View Live Dashboard](https://datastudio.google.com/reporting/2f7a68b3-6026-4a36-b3ed-8d55cc397761) 

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Ingestion | [dlt](https://dlthub.com/) |
| Storage | DuckDB |
| Transformation | dbt |
| Visualization | Looker Studio |

## 🏗️ Architecture

```
NASA API → dlt → DuckDB → dbt staging → CSV → Google Sheets → Looker Studio
```

## 📁 Project Structure

```
├── rest_nasa_pipeline.py     # dlt pipeline to ingest NASA API data
├── _stg_nasa_software.sql    # dbt staging model
├── final_nasa_software.csv   # exported data for Looker Studio
```

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install dlt duckdb pandas requests
```

### 2. Run the pipeline
```bash
python rest_nasa_pipeline.py
```

This will:
- Fetch data from the NASA software API
- Clean HTML tags from text fields
- Load 80 rows into DuckDB
- Export to `final_nasa_software.csv`

### 3. Load to Looker Studio
1. Upload `final_nasa_software.csv` to Google Sheets
2. Connect Google Sheets to Looker Studio
3. Build your dashboard

## 📦 Data Source

- **API**: [NASA Technology Transfer](https://technology.nasa.gov/api/api/software/visualization)
- **Records**: 80 NASA visualization software tools
- **Fields**: title, category, license, center, description, model_code, link

## 📈 Dashboard Charts

- **Bar chart** — Software count per NASA center
- **Pie chart** — License type distribution
- **Table** — Full software catalog with links

## 🏢 NASA Centers in the Data

| Code | Center |
|---|---|
| JPL | Jet Propulsion Laboratory |
| ARC | Ames Research Center |
| LARC | Langley Research Center |
| GSFC | Goddard Space Flight Center |
| GRC | Glenn Research Center |
| MSFC | Marshall Space Flight Center |
| JSC | Johnson Space Center |