# MBTI Test Automation (Excel + VBA)

An automated, self-service MBTI assessment tool built in Microsoft Excel using VBA. Designed for educational settings, it allows students to sit at a computer, answer the MBTI questionnaire, submit their data with a single click, and instantly see aggregated results in a management dashboard .(unified in one file to be put in the repo)

> **Created in 2018** – This repository showcases the original project with a sample snapshot of real (anonymized) + python-generated usage data.

## Features

- **Student-friendly form** – Clear layout for personal details and translated all MBTI questions.
- **One-click submission** – A VBA-powered button validates, saves, clears the form, and prepares it for the next person.
- **data storage** – Responses are logged in a sheet with timestamps.
- **Live management dashboard** – Another sheet automatically summarizes personality type distribution, total submissions, and other key metrics.
- **Kiosk / sequential use** – No manual intervention needed between users.
- **No dependencies** – Runs entirely inside Excel (2016 or later recommended); no external database or add-ins required.

## How It Works

1. Open the macro-enabled workbook (`.xlsm`).
2. The student fills in their name, class, gender, and answers the MBTI questions in the **Questions** sheet.
3. Clicking on the **Concat** sheet to see personal results.
4. Clicking **Submit** triggers a VBA macro that:
   - Validates all required fields
   - Saves the entry to the **Data** sheet
   - Clears the form
   - Readies the file for the next student
5. The **Data**, **Pivot** & **Chart** sheet (hidden/protected from students in operation) updates automatically using formulas and VBA to show:
   - Total participants with **Heatmap** coloring for one by one inspectin
   - Heatmap pivot tables for class averages and grand total
   - Bar charts and trend charts for analysing and making insights

## Repository Contents

- `MBTI_97_macro.xlsm` – The main workbook containing the form, data log, and dashboard.
- `Screenshots/` (optional) – Images of the interface and sample dashboard output.
- `Sample_Data/` – An anonymized snapshot of the dashboard and a small excerpt of the log to demonstrate the output without enabling macros.

## Getting Started

1. Download `MBTI_Automation.xlsm`.
2. **Enable macros** when prompted, or adjust your Trust Center settings.
3. Use the form as a student would, or press `Alt+F11` to explore the VBA code.
4. Check the dashboard sheet (may be hidden – unhide via VBA or Excel’s unhide command if needed) to view the summary.

## Use Case

Ideal for career counseling centers, school psychology workshops, or any group setting where you need to:

- Quickly administer the MBTI to multiple students
- Eliminate paper forms and manual data entry
- Provide instant aggregate feedback to facilitators or administrators

## Screenshots

`Questions.png`
`Concat.png`
`Data.png`
`Pivot.png`
`Chart.png`

## About the Project

I originally built this tool in 2018 to simplify MBTI test administration and data compilation. This repository serves as a portfolio piece that demonstrates:

- Advanced Excel VBA automation
- Clean user interface design inside a spreadsheet
- Automated, formula-driven dashboards
- Practical, real-world solution thinking

The included data is a **small, anonymized slice** of actual results, shared solely to illustrate the dashboard’s output.
