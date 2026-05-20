---
name: analyze-quarterly-metrics
description: This skill should be used when the user asks to "analyze quarterly metrics", "analyze the quarter", "generate quarterly report", "quarterly analysis", mentions a specific quarter like "2026-Q2", or discusses trends, risks, and growth opportunities for Linux System Roles metrics.
---

# Quarterly Metrics Analysis Skill

This skill analyzes quarterly metrics data and generates a comprehensive report with insights, trends, risks, and recommendations.

## What to do

1. **Determine if the quarter is complete or in-progress:**
   - Get today's date and compare to the quarter being analyzed
   - If analyzing current or future quarter: Add a disclaimer that data is PARTIAL/INCOMPLETE
   - Adjust your interpretation: low numbers may just mean "not much time has passed yet", not a crisis
   - For partial quarters: focus on trends and rates rather than absolute numbers

2. **Load the raw data** for the specified quarter:
   - Read the summary CSV files: `data/github_prs_summary.csv`, `data/github_issues_summary.csv`, `data/galaxy_legacy_summary.csv`, `data/galaxy_collections_summary.csv`
   - Extract data for the specified quarter and the previous 3-4 quarters for comparison
   - If `data/{{quarter}}/galaxy_legacy.csv` exists, read it for per-role download analysis

3. **Calculate key metrics** from the raw data:
   - **PR Merge Rate**: PRs Merged / (PRs Created - PRs Open) × 100 (excludes PRs still under review)
   - **External Acceptance Rate**: External PRs Merged / (External PRs Created - External PRs Open) × 100
   - **External Contribution %**: External PRs Created / PRs Created × 100
   - **Issue Resolution Rate**: Issues Closed / Issues Created × 100
   - **QoQ Growth rates**: Compare current quarter to previous quarter
   - **Fastest growing roles**: If per-role data exists, identify top gainers by comparing to previous quarter

4. **Analyze the data** and generate a detailed report with these sections:

   ### Executive Summary (2-3 sentences)
   - High-level overview of the quarter's performance
   - Most significant achievement or concern
   
   ### Key Metrics Overview
   - Present the main numbers (PRs, Issues, Downloads)
   - Compare to previous quarter (QoQ change)
   - Compare to same quarter last year (YoY if available)
   
   ### Trend Analysis
   - **PR Activity**: Are PRs increasing/decreasing? Merge rate trends?
   - **External Contributions**: Growing or declining? Acceptance rate healthy?
   - **Issue Management**: Resolution rate? Backlog growing?
   - **Galaxy Downloads**: Which collections/roles are trending? Growth rate sustainable?
   
   ### Highlights & Achievements
   - What went well this quarter?
   - Notable improvements in metrics
   - Fastest growing roles or areas
   
   ### Risks & Concerns
   - Declining trends that need attention
   - Bottlenecks or capacity issues
   - Quality concerns (low acceptance rates, etc.)
   - Areas falling behind
   
   ### Growth Opportunities
   - Underutilized roles with potential
   - Areas showing momentum
   - External contributor engagement opportunities
   
   ### Recommendations
   - 2-4 specific, actionable recommendations based on the data
   - Focus on addressing risks and capturing opportunities
   
5. **Be specific with numbers**: Always cite actual metrics, percentages, and comparisons. Don't use vague language like "significant" without quantifying it.

6. **Be smart about partial quarters**:
   - If the quarter is incomplete, DO NOT flag low absolute numbers as risks
   - Focus on rates (merge rate, acceptance rate) rather than volumes for partial data
   - Only flag things as concerns if they represent actual problems, not just "we're only 2 weeks into the quarter"
   - Make it clear in the Executive Summary if data is partial

7. **Automatically save the report**:
   - Save to `reports/{{quarter}}-analysis.md`
   - Create the reports directory if it doesn't exist
   - **Safe to overwrite**: If the report file already exists, overwrite it (reports are tracked in git, so previous versions are preserved)
   - Notify the user where the file was saved

8. **Output the analysis** directly to the user in Markdown format.

## Guidelines

- **Detect partial quarters**: Compare today's date to the quarter end date. If analyzing an incomplete quarter, prominently note this and adjust your analysis
- **Compare to historical data**: Always reference previous quarters for context
- **Identify patterns**: Look for multi-quarter trends, not just single-quarter changes
- **Be balanced**: Include both positive and negative findings
- **Be actionable**: Recommendations should be specific and implementable
- **Consider seasonality**: Note if quarterly patterns are typical or anomalous
- **Highlight outliers**: Call out unusual spikes or drops in any metric
- **Don't cry wolf on partial data**: For incomplete quarters, only flag true risks (bad rates, declining trends), not low volumes that are expected mid-quarter

## Example invocations

**Via skill invocation:**
User types: `/analyze-quarterly-metrics 2026-Q2`

**Via natural language:**
- "Analyze the quarterly metrics for 2026-Q2"
- "Generate a quarterly report for Q2 2026"
- "What do the metrics show for this quarter?"

You should:
1. Extract the quarter from the user's request or args (format: YYYY-QN, e.g., 2026-Q2)
2. Determine if the quarter is complete or in-progress based on today's date
3. Read all the raw metrics data from CSV files for that quarter
4. Calculate derived metrics from the raw data (merge rates, growth rates, etc.)
5. Read historical data for comparison (previous 3-4 quarters)
6. Generate the comprehensive analysis (being smart about partial data)
7. Present it in a well-formatted Markdown document
8. Automatically save to `reports/{{quarter}}-analysis.md`
9. Notify user that the report was saved

## Important

- **Always check if the quarter is complete**: Compare today's date to quarter end
  - Q1: January 1 - March 31
  - Q2: April 1 - June 30
  - Q3: July 1 - September 30
  - Q4: October 1 - December 31
- For partial quarters: add clear disclaimer in Executive Summary and adjust risk assessment
- **Always calculate metrics from CSV data** - don't rely on pre-computed derived_metrics.json
- If the quarter directory doesn't exist (like 2026-Q1), work with summary CSV data only
- For per-role analysis, check if `data/{{quarter}}/galaxy_legacy.csv` exists
- Always show your reasoning and cite specific data points
- **Automatically save** the report to `reports/{{quarter}}-analysis.md` (create directory if needed)
- Safe to overwrite existing report files - they're tracked in git
- Notify the user where the file was saved

## Metric Calculation Formulas

Use these formulas when calculating metrics from the raw CSV data:

**PR Metrics:**
- Merge Rate = (PRs Merged) / (PRs Created - PRs Open) × 100
  - Excludes PRs still under review from the calculation
- External Acceptance = (External PRs Merged) / (External PRs Created - External PRs Open) × 100  
  - Excludes external PRs still under review
- External % = (External PRs Created) / (PRs Created) × 100
- QoQ Growth = ((Current - Previous) / Previous) × 100

**Issue Metrics:**
- Resolution Rate = (Issues Closed) / (Issues Created) × 100
- External % = (External Issues Created) / (Issues Created) × 100
- QoQ Growth = ((Current - Previous) / Previous) × 100

**Galaxy Metrics:**
- Legacy QoQ Growth = ((Current Total - Previous Total) / Previous Total) × 100
- Collections QoQ Growth = ((Current Total - Previous Total) / Previous Total) × 100
