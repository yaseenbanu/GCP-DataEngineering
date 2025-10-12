# GCP Data Engineering Learning Repository

![Apache Beam](https://img.shields.io/badge/Apache%20Beam-FF6600?style=for-the-badge&logo=apache&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)

A comprehensive learning repository for **Google Cloud Platform (GCP) Data Engineering** that demonstrates modern data pipeline development using **Apache Beam**, **BigQuery**, **Pub/Sub**, and other GCP services. This project covers both Python and Java implementations with real-world examples and hands-on exercises.

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Repository Structure](#-repository-structure)
- [Apache Beam - Python](#-apache-beam---python)
- [Apache Beam - Java](#-apache-beam---java)
- [GCP Services Integration](#-gcp-services-integration)
- [Sample Datasets](#-sample-datasets)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
- [Learning Path](#-learning-path)
- [Contributing](#-contributing)

## 🎯 Project Overview

This repository serves as a **complete learning platform** for data engineering concepts, focusing on:

- **Batch and Stream Processing** with Apache Beam
- **Data Pipeline Development** in Python and Java
- **GCP Services Integration** (BigQuery, Pub/Sub, Cloud Storage)
- **Real-world Data Processing** scenarios
- **Best Practices** for scalable data engineering

## 📁 Repository Structure

```
GCP-DataEngineering/
├── 📂 Apache Beam/                    # Python-based Apache Beam examples
├── 📂 ApacheBeam-Java/               # Java-based Apache Beam examples
├── 📂 GCP BigQuery/                  # BigQuery integration examples
├── 📂 GCP PubSub/                    # Pub/Sub messaging examples
├── 📂 Datasets/                      # Sample datasets for practice
└── 📄 README.md                      # This file
```

---

## 🐍 Apache Beam - Python

**Location**: [`Apache Beam/`](./Apache%20Beam/)

### Core Files
- 🔌 [**MySQL Connection**](./Apache%20Beam/01_MYSQL_Connection.py) - Database integration with Apache Beam
- ⚡ [**Spark Runner**](./Apache%20Beam/02_SparkRunner.py) - Running Beam pipelines on Spark
- 📓 [**Apache Beam Basics Notebook**](./Apache%20Beam/Apache%20Beam%20Basics%20%5BPython%5D.ipynb) - Interactive learning guide

### Examples Directory: [`Examples/`](./Apache%20Beam/Examples/)
Progressive learning examples covering core Beam concepts:

| File | Concept | Description |
|------|---------|-------------|
| [01_Beam_create_integers.py](./Apache%20Beam/Examples/01_Beam_create_integers.py) | **Create** | Creating PCollections from integers |
| [02_Beam Create Key-Value Pairs.py](./Apache%20Beam/Examples/02_Beam%20Create%20Key-Value%20Pairs.py) | **Key-Value** | Working with key-value pair data |
| [03_Beam Create objects.py](./Apache%20Beam/Examples/03_Beam%20Create%20objects.py) | **Objects** | Creating PCollections from custom objects |
| [04_Beam Create String.py](./Apache%20Beam/Examples/04_Beam%20Create%20String.py) | **Strings** | String data processing |
| [05_Beam Filter.py](./Apache%20Beam/Examples/05_Beam%20Filter.py) | **Filter** | Filtering data based on conditions |
| [06_Beam Map Elements to Formatted String.py](./Apache%20Beam/Examples/06_Beam%20Map%20Elements%20to%20Formatted%20String.py) | **Map** | Transforming elements to formatted strings |
| [07_Beam Map Elements.py](./Apache%20Beam/Examples/07_Beam%20Map%20Elements.py) | **Map** | Basic element transformation |
| [08_Beam FlatMap.py](./Apache%20Beam/Examples/08_Beam%20FlatMap.py) | **FlatMap** | Flattening nested collections |
| [09_Beam FlatMap Elements from List to Integer.py](./Apache%20Beam/Examples/09_Beam%20FlatMap%20Elements%20from%20List%20to%20Integer.py) | **FlatMap** | Converting lists to individual integers |
| [10_Beam Group by Key and Sum.py](./Apache%20Beam/Examples/10_Beam%20Group%20by%20Key%20and%20Sum.py) | **GroupByKey** | Grouping and aggregating data |
| [11_Beam Group by Key.py](./Apache%20Beam/Examples/11_Beam%20Group%20by%20Key.py) | **GroupByKey** | Basic grouping operations |
| [12_Beam ParDo (Parallel Do).py](./Apache%20Beam/Examples/12_Beam%20ParDo%20%28Parallel%20Do%29.py) | **ParDo** | Parallel data processing |
| [13_Beam ParDo with Key-Value.py](./Apache%20Beam/Examples/13_Beam%20ParDo%20with%20Key-Value.py) | **ParDo** | ParDo with key-value pairs |
| [14_WordCount.ipynb](./Apache%20Beam/Examples/14_WordCount.ipynb) | **WordCount** | Classic word counting example |

### Main Functions Directory: [`Main Functions/`](./Apache%20Beam/Main%20Functions/)
In-depth Jupyter notebooks covering essential Beam transformations:

| Notebook | Transform | Description |
|----------|-----------|-------------|
| [01_Create.ipynb](./Apache%20Beam/Main%20Functions/01_Create.ipynb) | **Create** | Creating PCollections from various sources |
| [02_ReadTransform.ipynb](./Apache%20Beam/Main%20Functions/02_ReadTransform.ipynb) | **Read** | Reading data from files and external sources |
| [03_WriteTransform.ipynb](./Apache%20Beam/Main%20Functions/03_WriteTransform.ipynb) | **Write** | Writing data to various sinks |
| [04_FlatMap.ipynb](./Apache%20Beam/Main%20Functions/04_FlatMap.ipynb) | **FlatMap** | Advanced flattening operations |
| [05_Map.ipynb](./Apache%20Beam/Main%20Functions/05_Map.ipynb) | **Map** | Element-wise transformations |
| [06_FilterLambda.ipynb](./Apache%20Beam/Main%20Functions/06_FilterLambda.ipynb) | **Filter** | Lambda-based filtering |
| [07_Filter.ipynb](./Apache%20Beam/Main%20Functions/07_Filter.ipynb) | **Filter** | Advanced filtering techniques |
| [08_Flatten.ipynb](./Apache%20Beam/Main%20Functions/08_Flatten.ipynb) | **Flatten** | Combining multiple PCollections |
| [09_CombinePerKey.ipynb](./Apache%20Beam/Main%20Functions/09_CombinePerKey.ipynb) | **CombinePerKey** | Aggregation operations |
| [10_CountPerKey.ipynb](./Apache%20Beam/Main%20Functions/10_CountPerKey.ipynb) | **Count** | Counting elements per key |
| [11_CogroupByKey.ipynb](./Apache%20Beam/Main%20Functions/11_CogroupByKey.ipynb) | **CoGroupByKey** | Joining multiple PCollections |

### Datasets: [`datasets/`](./Apache%20Beam/datasets/)
- 📄 [flights_sample.csv](./Apache%20Beam/datasets/flights_sample.csv) - Flight data for analysis
- 📄 [Poem.txt](./Apache%20Beam/datasets/Poem.txt) - Text data for word processing
- 📄 [transactions.csv](./Apache%20Beam/datasets/transactions.csv) - Financial transaction data
- 📄 [word_count_data.txt](./Apache%20Beam/datasets/word_count_data.txt) - Sample text for word counting
- 📁 [output/](./Apache%20Beam/datasets/output/) - Pipeline output files

---

## ☕ Apache Beam - Java

**Location**: [`ApacheBeam-Java/`](./ApacheBeam-Java/)

### Project Structure
- 📄 [**pom.xml**](./ApacheBeam-Java/pom.xml) - Maven build configuration
- 📄 [**coding_guide.md**](./ApacheBeam-Java/coding_guide.md) - Java Beam coding guidelines

### Basic Examples: [`src/main/java/com/example/`](./ApacheBeam-Java/src/main/java/com/example/)

| File | Concept | Description |
|------|---------|-------------|
| [BeamExample.java](./ApacheBeam-Java/src/main/java/com/example/BeamExample.java) | **Basic Pipeline** | Simple Beam pipeline example |
| [code_01_BeamCreate_Integer.java](./ApacheBeam-Java/src/main/java/com/example/code_01_BeamCreate_Integer.java) | **Create** | Creating integer PCollections |
| [code_01_BeamCreate_KV.java](./ApacheBeam-Java/src/main/java/com/example/code_01_BeamCreate_KV.java) | **Key-Value** | Key-value pair creation |
| [code_01_BeamCreate_Objects.java](./ApacheBeam-Java/src/main/java/com/example/code_01_BeamCreate_Objects.java) | **Objects** | Custom object processing |
| [code_01_BeamCreate_String.java](./ApacheBeam-Java/src/main/java/com/example/code_01_BeamCreate_String.java) | **Strings** | String data handling |
| [code_02_BeamFilter.java](./ApacheBeam-Java/src/main/java/com/example/code_02_BeamFilter.java) | **Filter** | Data filtering operations |
| [code_03_BeamMapElements_formattedStringOutput.java](./ApacheBeam-Java/src/main/java/com/example/code_03_BeamMapElements_formattedStringOutput.java) | **Map** | Formatted string output |
| [code_04_BeamFlatMap.java](./ApacheBeam-Java/src/main/java/com/example/code_04_BeamFlatMap.java) | **FlatMap** | Collection flattening |
| [code_05_BeamGroupByKey.java](./ApacheBeam-Java/src/main/java/com/example/code_05_BeamGroupByKey.java) | **GroupByKey** | Data grouping |
| [code_05_BeamGroupByKey_Sum.java](./ApacheBeam-Java/src/main/java/com/example/code_05_BeamGroupByKey_Sum.java) | **GroupByKey** | Grouping with summation |
| [code_06_BeamParDo.java](./ApacheBeam-Java/src/main/java/com/example/code_06_BeamParDo.java) | **ParDo** | Parallel processing |
| [code_07_BeamParDo_KeyValue.java](./ApacheBeam-Java/src/main/java/com/example/code_07_BeamParDo_KeyValue.java) | **ParDo** | ParDo with key-value data |

### Complex Examples: [`src/main/java/com/complexExamples/`](./ApacheBeam-Java/src/main/java/com/complexExamples/)

| File | Concept | Description |
|------|---------|-------------|
| [code_01_BeamWindowing.java](./ApacheBeam-Java/src/main/java/com/complexExamples/code_01_BeamWindowing.java) | **Windowing** | Time-based data windowing |
| [code_01_BeamWindowing_Demo.java](./ApacheBeam-Java/src/main/java/com/complexExamples/code_01_BeamWindowing_Demo.java) | **Windowing** | Advanced windowing demo |
| [code_02_BeamSideInputs.java](./ApacheBeam-Java/src/main/java/com/complexExamples/code_02_BeamSideInputs.java) | **Side Inputs** | Data enrichment patterns |
| [code_02_BeamStatefulProcessing.java](./ApacheBeam-Java/src/main/java/com/complexExamples/code_02_BeamStatefulProcessing.java) | **Stateful** | Stateful data processing |
| [code_03_BeamPipeline.java](./ApacheBeam-Java/src/main/java/com/complexExamples/code_03_BeamPipeline.java) | **Pipeline** | Complex pipeline configurations |

### Use Cases: [`src/main/java/com/usecases/`](./ApacheBeam-Java/src/main/java/com/usecases/)

| File | Use Case | Description |
|------|----------|-------------|
| [code_01_wordcount.java](./ApacheBeam-Java/src/main/java/com/usecases/code_01_wordcount.java) | **Word Count** | Classic word counting implementation |
| [code_02_even_odd.java](./ApacheBeam-Java/src/main/java/com/usecases/code_02_even_odd.java) | **Classification** | Even/odd number classification |
| [code_03_average_numbers.java](./ApacheBeam-Java/src/main/java/com/usecases/code_03_average_numbers.java) | **Aggregation** | Numerical average calculation |
| [code_03_average_numbers_combineApproach.java](./ApacheBeam-Java/src/main/java/com/usecases/code_03_average_numbers_combineApproach.java) | **Combine** | Average using Combine transforms |

---

## ☁️ GCP Services Integration

### BigQuery Integration: [`GCP BigQuery/`](./GCP%20BigQuery/)

| Notebook | Focus | Description |
|----------|-------|-------------|
| [01_Load_from_StorageBucket.ipynb](./GCP%20BigQuery/01_Load_from_StorageBucket.ipynb) | **Data Loading** | Loading data from Cloud Storage to BigQuery |
| [02_BigQuery_Datasets_Python.ipynb](./GCP%20BigQuery/02_BigQuery_Datasets_Python.ipynb) | **Dataset Management** | Creating and managing BigQuery datasets |
| [03_BigQuery_Tables_Python.ipynb](./GCP%20BigQuery/03_BigQuery_Tables_Python.ipynb) | **Table Operations** | BigQuery table creation and manipulation |
| [04_Load_to_StorageBucket.ipynb](./GCP%20BigQuery/04_Load_to_StorageBucket.ipynb) | **Data Export** | Exporting BigQuery data to Cloud Storage |

### Pub/Sub Messaging: [`GCP PubSub/`](./GCP%20PubSub/)

| Notebook | Focus | Description |
|----------|-------|-------------|
| [01_PubSub_messaging.ipynb](./GCP%20PubSub/01_PubSub_messaging.ipynb) | **Messaging** | Complete Pub/Sub messaging implementation |

---

## 📊 Sample Datasets

**Location**: [`Datasets/`](./Datasets/)

| File | Type | Description |
|------|------|-------------|
| [employee.txt](./Datasets/employee.txt) | **Employee Data** | Sample employee records |
| [titanic_dataset.csv](./Datasets/titanic_dataset.csv) | **Historical Data** | Famous Titanic passenger dataset |

---

## 🔧 Prerequisites

### Software Requirements
- **Python 3.7+** with pip
- **Java 8+** with Maven
- **Google Cloud SDK** (gcloud CLI)
- **Git** for version control

### GCP Setup
1. **GCP Project**: Create or use existing GCP project
2. **Authentication**: Configure gcloud authentication
3. **APIs**: Enable required APIs (BigQuery, Pub/Sub, Cloud Storage)
4. **Service Account**: Create service account with appropriate permissions

### Python Dependencies
```bash
pip install apache-beam[gcp]
pip install google-cloud-bigquery
pip install google-cloud-pubsub
pip install mysql-connector-python
```

### Java Dependencies
Maven dependencies are configured in [`pom.xml`](./ApacheBeam-Java/pom.xml)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/TheDataArtisanDev/GCP-DataEngineering.git
cd GCP-DataEngineering
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv beam-env
source beam-env/bin/activate  # On Windows: beam-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt  # Create this based on imports
```

### 3. Configure GCP
```bash
# Authenticate with GCP
gcloud auth login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Create application default credentials
gcloud auth application-default login
```

### 4. Run Your First Example
```bash
# Python example
cd "Apache Beam/Examples"
python 01_Beam_create_integers.py

# Java example
cd ApacheBeam-Java
mvn compile exec:java -Dexec.mainClass="com.example.BeamExample"
```

---

## 📚 Learning Path

### Beginner Track
1. **Start with**: [Apache Beam Basics Notebook](./Apache%20Beam/Apache%20Beam%20Basics%20%5BPython%5D.ipynb)
2. **Practice**: [Python Examples](./Apache%20Beam/Examples/) (01-05)
3. **Learn**: [Main Functions](./Apache%20Beam/Main%20Functions/) (01-03)

### Intermediate Track
1. **Advanced Transforms**: [Main Functions](./Apache%20Beam/Main%20Functions/) (04-11)
2. **Java Basics**: [Java Examples](./ApacheBeam-Java/src/main/java/com/example/)
3. **GCP Integration**: [BigQuery Notebooks](./GCP%20BigQuery/)

### Advanced Track
1. **Complex Patterns**: [Java Complex Examples](./ApacheBeam-Java/src/main/java/com/complexExamples/)
2. **Real-world Use Cases**: [Java Use Cases](./ApacheBeam-Java/src/main/java/com/usecases/)
3. **Streaming**: [Pub/Sub Integration](./GCP%20PubSub/)

---

## 🎓 Key Learning Outcomes

After completing this repository, you will understand:

- ✅ **Apache Beam fundamentals** in Python and Java
- ✅ **Data pipeline design patterns** and best practices
- ✅ **GCP service integration** for end-to-end data workflows
- ✅ **Batch and stream processing** concepts
- ✅ **Scalable data transformation** techniques
- ✅ **Real-world data engineering** scenarios

---

## 🤝 Contributing

Contributions are welcome! This is a learning project, so feel free to:
- Report issues or bugs you find
- Suggest improvements to examples
- Add more use cases or examples
- Fix documentation or code issues

For major changes, please open an issue first to discuss what you would like to change.

---

##  Useful Links

- [Apache Beam Documentation](https://beam.apache.org/documentation/)
- [Google Cloud Platform Documentation](https://cloud.google.com/docs)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Pub/Sub Documentation](https://cloud.google.com/pubsub/docs)

---

**Happy Learning! 🚀**

*This repository is a comprehensive data engineering learning journey. If you find it helpful, feel free to use it for your own learning!*