APP_NAME=github-heatmap
PY_FILE=heatmap.py

SHELL := /bin/bash

.PHONY: install setup run clean

install:
	@echo "Installing dependencies (Debian/Ubuntu)..."
	sudo apt update
	sudo apt install -y \
		python3 \
		python3-gi \
		gir1.2-gtk-4.0 \
		gir1.2-gdkx11-4.0 \
		libgtk-4-1 \
		libgirepository1.0-dev \
		gobject-introspection \
		curl

setup:
	@echo "----------------------------------"
	@read -p "Enter your GitHub username: " username; \
	if [ -z "$$username" ]; then \
		echo "Username cannot be empty!"; \
		exit 1; \
	fi; \
	sed -i "s/GitHubFetcher(\"USERNAME\")/GitHubFetcher(\"$$username\")/" $(PY_FILE); \
	echo "Username updated successfully."
	@echo "----------------------------------"

run:
	@echo "Running $(APP_NAME)..."
	python3 $(PY_FILE)

clean:
	@echo "Reverting username back to placeholder..."
	sed -i 's/GitHubFetcher(".*")/GitHubFetcher("USERNAME")/' $(PY_FILE)