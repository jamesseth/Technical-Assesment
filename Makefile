
.DEFAULT: help

help: ## Prints help for targets with comments.
	@cat $(MAKEFILE_LIST) \
		| grep -E '^[a-zA-Z_-]+:.*?## .*$$' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Create a virtual environment
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt


start: ## Run application menu
	bash -c "./menu.sh"

pytest: ## Run unittests.
	python3 -m venv .venv
	bash -c "source .venv/bin/activate \
	         && pip install -r requirements.txt \
			 && pytest \
			 && deactivate"

pre-commit: ## Run pre-commits
	bash -c "pre-commit run -a"
