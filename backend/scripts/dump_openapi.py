import json
import pathlib
import sys

BASE = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(BASE))

from main import app

# Generate the schema
schema = app.openapi()

# Write it out
with open("openapi.json", "w") as f:
    json.dump(schema, f, indent=2)
