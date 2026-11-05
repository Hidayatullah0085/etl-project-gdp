# 🌍 GDP Data ETL Project

## 📌 Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline using Python to process global GDP data.

The pipeline extracts GDP data, performs data transformation, and loads the processed information into a SQLite database for storage and further analysis.

## 🎯 Project Objectives

- Understand the ETL process in practical data engineering.
- Extract GDP data from a JSON file.
- Process and transform data using Python.
- Store structured data in a SQLite database.
- Maintain execution logs for monitoring the ETL process.

## 🛠️ Technologies Used

- **Python** – ETL pipeline development
- **SQLite** – Database storage
- **JSON** – Data source format
- **Logging** – ETL execution monitoring

## 🔄 ETL Workflow

The project follows three main stages:

### 1. Extract
- Read GDP data from `Countries_by_GDP.json`.
- Load the source data into Python for processing.

### 2. Transform
- Process the extracted GDP data.
- Prepare the data for database storage.

### 3. Load
- Load the processed data into the SQLite database.
- Store the results in `World_Economies.db`.

## 📁 Project Structure

```text
etl_project-gdp/
│
├── Countries_by_GDP.json
├── World_Economies.db
├── etl_project_gdp.py
├── etl_project_log.txt
├── .gitignore
└── README.md
```

## ⚙️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/Hidayatullah0085/etl-project-gdp.git
```

### Step 2: Navigate to the Project Directory

```bash
cd etl-project-gdp
```

### Step 3: Install Dependencies

Make sure Python is installed on your system.

The project uses Python's built-in SQLite and logging modules. Install any additional third-party packages required by the script.

### Step 4: Run the ETL Pipeline

```bash
python etl_project_gdp.py
```

### Step 5: Check the Output

- Check `World_Economies.db` for the stored data.
- Check `etl_project_log.txt` for execution logs.

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Understanding the ETL pipeline architecture.
- Working with JSON data.
- Developing data processing workflows using Python.
- Storing data in SQLite databases.
- Implementing logging for ETL monitoring.

## 👨‍💻 Author

**Hidayat Ullah**

BS Data Science | Aspiring Data Engineer

[GitHub Profile](https://github.com/Hidayatullah0085)

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.