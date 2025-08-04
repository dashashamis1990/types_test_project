gen-openapi-types:
	# 1. dump FastAPI schema (writes ./openapi.json)
	python3 backend/scripts/dump_openapi.py
	# 2. generate TS types into your React app
	npx openapi-typescript openapi.json \
	  -o frontend/src/api/openapi-types.ts