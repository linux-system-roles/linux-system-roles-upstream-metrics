---
name: analyze-quarterly-metrics
description: This skill should be used when the user asks to "analyze quarterly metrics", "analyze the quarter", "generate quarterly report", "quarterly analysis", mentions a specific quarter like "2026-Q2", or discusses trends, risks, and growth opportunities for Linux System Roles metrics.
---

# Quarterly Metrics Analysis Skill

This skill analyzes quarterly metrics data and generates a FOCUSED report (~400-500 words) with key metrics, highlights, top downloaded roles, concerns, and actionable recommendations.

## What to do

1. **Determine if the quarter is complete or in-progress:**
   - Get today's date and compare to the quarter being analyzed
   - If analyzing current or future quarter: Add a disclaimer that data is PARTIAL/INCOMPLETE
   - Adjust your interpretation: low numbers may just mean "not much time has passed yet", not a crisis
   - For partial quarters: focus on trends and rates rather than absolute numbers

2. **Load the raw data** for the specified quarter:
   - Read the summary CSV files: `data/github_prs_summary.csv`, `data/github_issues_summary.csv`, `data/galaxy_legacy_summary.csv`, `data/galaxy_collections_summary.csv`
   - Extract data for the specified quarter and the previous quarter for comparison
   - If `data/{{quarter}}/galaxy_legacy.csv` exists, read it for top downloaded roles and growth analysis

3. **Calculate key metrics** from the raw data:
   - **PR Merge Rate**: PRs Merged / (PRs Created - PRs Open) × 100 (excludes PRs still under review)
   - **External Acceptance Rate**: External PRs Merged / (External PRs Created - External PRs Open) × 100
   - **External Contribution %**: External PRs Created / PRs Created × 100
   - **Issue Resolution Rate**: Issues Closed / Issues Created × 100
   - **QoQ Growth rates**: Compare current quarter to previous quarter
   - **Fastest growing roles**: If per-role data exists, identify top gainers by comparing to previous quarter

4. **Fetch rejected external PR details** (if External Acceptance Rate < 100%):
   - From `data/{quarter}/prs.csv`, identify roles where: `Created non-maint - Merged non-maint - Open non-maint > 0`
   - For each role with rejections, run: `gh pr list -R {org}/{role} -S "created:{date_range} is:closed is:unmerged -author:app/" --json number,author,title,url --limit 20`
   - Parse the results to get PR numbers, authors, and titles
   - Include this information in the "Top Concerns" or "Additional Notes" section of the report
   - Format: "Rejected External PRs: role #123 (author), role #456 (author)"

5. **Analyze the data** and generate a FOCUSED report with these sections:

   ### Executive Summary (2-3 sentences)
   - High-level overview: what's the overall health? One key win, one key concern.
   - Note if data is partial (for incomplete quarters)
   
   ### Key Metrics (Table format)
   - Comparison table: Current vs Previous Quarter
   - PRs Created, Merged, Merge Rate
   - External PRs, External Acceptance Rate, External % of total
   - Issues Created, Closed, Resolution Rate
   - Galaxy Legacy Downloads (QoQ change)
   - Galaxy Collections Downloads (QoQ change)
   
   ### Highlights (2-3 bullets)
   - Notable achievements and positive changes
   - Metrics that improved
   - Balance the concerns with wins
   
   ### Top Downloaded Roles (Top 5 list)
   - List the 5 most downloaded roles with cumulative totals
   - If per-role data exists for current and previous quarter, also show fastest growing/declining roles
   
   ### Top Concerns (3-4 bullets)
   - Most critical issues requiring attention
   - Use specific numbers and percentages
   - Only urgent/high-impact issues
   
   ### Recommendations (3-4 bullets)
   - Most important actionable items
   - Be specific and brief
   - Focus on high-impact actions
   
   **TARGET LENGTH**: ~400-500 words. Scannable but informative.
   
5. **Be specific with numbers**: Always cite actual metrics, percentages, and comparisons. Don't use vague language like "significant" without quantifying it.

6. **Be smart about partial quarters**:
   - If the quarter is incomplete, DO NOT flag low absolute numbers as risks
   - Focus on rates (merge rate, acceptance rate) rather than volumes for partial data
   - Only flag things as concerns if they represent actual problems, not just "we're only 2 weeks into the quarter"
   - Make it clear in the Executive Summary if data is partial

7. **Validate the report for accuracy**:
   - Re-read all numeric claims in your draft
   - For each number: verify it matches the correct CSV column/row
   - For each comparison: verify the direction (higher/lower) matches the math
   - Check for contradictions: "up from X, but below X" is impossible
   - If you find errors, fix them before saving

8. **Automatically save the report**:
   - Save to `reports/{{quarter}}-analysis.md`
   - Create the reports directory if it doesn't exist
   - **Safe to overwrite**: If the report file already exists, overwrite it (reports are tracked in git, so previous versions are preserved)
   - Show the user a brief summary and notify where the full file was saved

## Guidelines

- **Balanced and scannable**: Target ~400-500 words, readable in 2-3 minutes
- **Detect partial quarters**: Note if data is incomplete in the Executive Summary
- **Compare to previous quarter**: QoQ changes only, skip historical deep-dives
- **Balance concerns with wins**: Include both Highlights and Top Concerns sections
- **Show what matters**: Top downloaded roles help prioritize work
- **Only critical issues**: If it's not urgent or high-impact, skip it from concerns
- **Be actionable**: Every recommendation must be specific and implementable
- **Don't cry wolf on partial data**: For incomplete quarters, only flag true risks (bad rates, declining trends), not low volumes
- **Use numbers**: Always cite specific metrics, no vague language

### Data Accuracy and Validation

**CRITICAL: Verify all numbers before making claims**

1. **Use correct data sources**:
   - When discussing a specific collection (e.g., fedora.linux_system_roles), use that collection's column, NOT the Total Downloads column
   - When discussing totals, clearly state "total across all collections"
   - Double-check: Does the number in your sentence match the CSV cell you're referencing?

2. **Verify comparison direction**:
   - If A > B: use "higher than", "above", "exceeds", "increased from"
   - If A < B: use "lower than", "below", "decreased from", "down from"
   - If A ≈ B: use "similar to", "comparable to", "roughly equal to"
   - **NEVER** say "A is well below B" when A > B or vice versa

3. **Validate calculations**:
   - QoQ growth = ((Current - Previous) / Previous) × 100
   - If growth is positive, use "increased" or "up"; if negative, use "decreased" or "down"
   - Check sign: positive growth means increase, negative growth means decrease

4. **Before finalizing the report**:
   - Re-read each numeric claim
   - Verify the number matches the data source (correct CSV column/row)
   - Verify the comparison direction matches the math (higher/lower/equal)
   - Check for internal contradictions (e.g., "up from X, but well below X")

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
3. Read the raw metrics data from CSV files for that quarter and previous quarter
4. Read per-role Galaxy data if available for top downloaded roles analysis
5. Calculate derived metrics (merge rates, growth rates, etc.)
6. Generate a focused report (~400-500 words): Executive Summary, Key Metrics, Highlights, Top Downloaded Roles, Top Concerns, Recommendations
7. Validate: verify all numbers match data sources
8. Save to `reports/{{quarter}}-analysis.md`
9. Show the full report to user and notify where file was saved

## Important

- **Check if quarter is complete**: Compare today's date to quarter end (Q1: Jan-Mar, Q2: Apr-Jun, Q3: Jul-Sep, Q4: Oct-Dec)
- For partial quarters: add disclaimer in Executive Summary
- **Calculate metrics from CSV data** - don't rely on pre-computed files
- **Read per-role data** if `data/{{quarter}}/galaxy_legacy.csv` exists for top downloaded roles
- **Balanced report**: ~400-500 words, 6 sections (Summary, Metrics, Highlights, Top Roles, Concerns, Recommendations)
- **Auto-save** to `reports/{{quarter}}-analysis.md` (safe to overwrite, tracked in git)
- Show full report to user and file location

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
