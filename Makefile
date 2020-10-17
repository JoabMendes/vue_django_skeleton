APP_COMMAND = python manage.py
FIX_LOC=seeds/
TEST_SETTINGS = 'app.settings.local'
PYTEST_CMD = py.test domain app api -v -x -n auto
PYTEST_STDOUT_CMD = py.test domain app api -s -v -x

clean:
	@rm -rf docs/build/
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "*.hot-update.*" -exec rm -rf {} \;

run-clean:
	@find . -name "*.hot-update.*" -exec rm -rf {} \;
	@find . -name "*.pyc" -exec rm -rf {} \;

run-backend: run-clean
	$(APP_COMMAND) runserver

run-frontend:
	npm run dev

seed:
	# Makes migrations
	# $(APP_COMMAND) makemigrations (ONLY IN DEV ENV)

	# Migrates database
	yes | $(APP_COMMAND) migrate

	echo "Cleanning pyc"
	@find . -name "*.pyc" -exec rm -rf {} \;

seed-dev:
	# Load the fixtures datas into the database
	# Delete local databse if exists
	rm *.sqlite*

	# Makes migrations
	$(APP_COMMAND) makemigrations

	# Migrates database
	yes | $(APP_COMMAND) migrate

	$(APP_COMMAND) loaddata $(FIX_LOC)auth

	@echo "Cleanning pyc"
	@find . -name "*.pyc" -exec rm -rf {} \;

install:
	pip install -r requirements.txt
	npm install

setup-dev: install seed-dev

setup-travis: install
	yes | $(APP_COMMAND) collectstatic

collectstatic:
	$(APP_COMMAND) collectstatic

lint:
	flake8 domain app api --exclude=*/migrations,*settings

test:
	flake8 domain app api --exclude=*/migrations,*settings
	$(PYTEST_CMD)

test-matching:
	$(PYTEST_CMD) -rs -k $(Q)

test-matching-stdout:
	$(PYTEST_STDOUT_CMD) -rs -k $(Q)

migrations:
	$(APP_COMMAND) makemigrations

make migrate:
	$(APP_COMMAND) migrate

build-frontend:
	npm run build
