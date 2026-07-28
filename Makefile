# Makefile for Linux System Roles Quarterly Metrics
.PHONY: help collect-github collect-galaxy update-summary generate-graphs quarterly-report clean

# Auto-detect quarter and date range
CURRENT_MONTH := $(shell date +%-m)
CURRENT_YEAR := $(shell date +%Y)
CURRENT_Q := $(shell echo $$((($(CURRENT_MONTH)-1)/3+1)))
QUARTER ?= $(CURRENT_YEAR)-Q$(CURRENT_Q)
YEAR := $(shell echo $(QUARTER) | cut -d'-' -f1)
Q_NUM := $(shell echo $(QUARTER) | cut -d'Q' -f2)

ifeq ($(Q_NUM),1)
    DATE_RANGE := $(YEAR)-01-01..$(YEAR)-03-31
else ifeq ($(Q_NUM),2)
    DATE_RANGE := $(YEAR)-04-01..$(YEAR)-06-30
else ifeq ($(Q_NUM),3)
    DATE_RANGE := $(YEAR)-07-01..$(YEAR)-09-30
else ifeq ($(Q_NUM),4)
    DATE_RANGE := $(YEAR)-10-01..$(YEAR)-12-31
endif

help:
	@echo "Targets: collect-github, collect-galaxy, update-summary, generate-graphs, quarterly-report, clean"
	@echo "Current quarter: $(QUARTER) ($(DATE_RANGE))"
	@echo "Requires: GITHUB_TOKEN, optionally GALAXY_API_KEY"

collect-github:
	@test -n "$(GITHUB_TOKEN)" || (echo "ERROR: GITHUB_TOKEN not set" && exit 1)
	@QUARTER=$(QUARTER) DATE_RANGE=$(DATE_RANGE) bash scripts/collect_github_stats.sh

collect-galaxy:
	@QUARTER=$(QUARTER) python3 scripts/collect_galaxy_stats.py

update-summary:
	@QUARTER=$(QUARTER) python3 scripts/update_quarterly_summary.py

generate-graphs:
	@QUARTER=$(QUARTER) python3 scripts/generate_graphs.py

quarterly-report: collect-github collect-galaxy update-summary generate-graphs
	@echo ""
	@echo "✅ Complete for $(QUARTER)"
	@echo "To generate AI analysis with your AI agent:"
	@echo "  Use the skill defined in .claude/skills/analyze-quarterly-metrics/"
	@echo "  (For Claude Code users: /analyze-quarterly-metrics $(QUARTER))"

clean:
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
