import re
import dlt
from dlt.sources.helpers import requests
import duckdb

def clean_html(value):
    if isinstance(value, str):
        return re.sub(r"<[^>]+>", "", value).strip()
    return value

def load_api_data() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_nasa_pipeline",
        destination="duckdb",
        dataset_name="nasa"
    )

    response = requests.get("https://technology.nasa.gov/api/api/software/visualization")
    response.raise_for_status()
    raw = response.json()
    data = raw["results"]

    # Map list positions to column names
    COLUMNS = [
        "id", "code", "title", "description",
        "code2", "category", "license",
        "field7", "field8", "center",
        "field10", "field11", "score"
    ]

    # Convert each list record to dict + clean HTML
    cleaned = []
    for record in data:
        row = dict(zip(COLUMNS, record))
        row = {k: clean_html(v) for k, v in row.items()}
        cleaned.append(row)

    # Preview before loading
    print(cleaned[0])

    load_info = pipeline.run(
        cleaned,
        table_name="visualization",
        write_disposition="replace"
    )
    print(load_info)

def to_csv() -> None :
    conn = duckdb.connect("rest_nasa_pipeline.duckdb")
    
    df = conn.execute("select * from _stg_nasa_software").df()

    df.to_csv("final_nasa_software.csv", index=False)
    conn.close()

    print(f"Exported to csv {len(df)} row")


if __name__ == "__main__":
    load_api_data()
    to_csv()