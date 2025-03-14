# TODO: BUILD_DIR will accumulate all application specific files (src/program?.py)

MAKEFLAGS += --no-builtin-rules --no-builtin-variables
COMMON_MODULES := src/module1.py src/module2.py

BUILD_DIR := build
BUILD_STAMP := $(BUILD_DIR)/.stamp

.PHONY: all
all: check-venv program1.pyz program2.pyz

program1.pyz: src/program1.py $(BUILD_STAMP)
	cp $< $(BUILD_DIR)
	python -m zipapp -m program1:main -o $@ $(BUILD_DIR)

program2.pyz: src/program2.py $(BUILD_STAMP)
	cp $< $(BUILD_DIR)
	python -m zipapp -m program2:main -o $@ $(BUILD_DIR)

$(BUILD_STAMP): $(COMMON_MODULES) requirements.txt
	rm -rf $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)
	cp $(COMMON_MODULES) $(BUILD_DIR)
	pip install -r requirements.txt --target $(BUILD_DIR)/
	touch $@

.PHONY: check-venv
check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "ERROR: virtual environment not activated"; \
		echo "ERROR: run 'source .venv/bin/activate' first"; \
		exit 1; \
	fi

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR) program1.pyz program2.pyz