run:
	python app/main.py

seed:
	python app/database/seed.py

test:
	pytest tests/test.py