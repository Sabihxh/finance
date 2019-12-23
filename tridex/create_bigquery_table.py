from google.cloud import bigquery as bq

schema = [
	bq.SchemaField("date", "Date", mode="REQUIRED"),
	bq.SchemaField("High", "FLOAT", mode="NULLABLE"),
	bq.SchemaField("Low", "FLOAT", mode="NULLABLE"),
	bq.SchemaField("Open", "FLOAT", mode="NULLABLE"),
	bq.SchemaField("Close", "FLOAT", mode="NULLABLE"),
	bq.SchemaField("Volume", "INTEGER", mode="NULLABLE"),
	bq.SchemaField("Adj_Close", "FLOAT", mode="NULLABLE"),
]

# TODO(developer): Construct a BigQuery client object.
client = bq.Client()

# TODO(developer): Set table_id to the ID of the table to create
table_id = "tridex.aapl.stocks_historical_prices"

table = bq.Table(table_id, schema=schema)
table = client.create_table(table)  # API request
print(
	"Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)