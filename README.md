# Guess The Number - Streamlit Game

## 📌 Project Overview
This is a fun and interactive "Guess The Number" game built using **Streamlit**, allowing users to guess a randomly generated number within a defined range. The game keeps track of attempts, difficulty levels, and maintains a leaderboard.

## 🚀 Features
- 🎮 Interactive number guessing game
- 🔢 Supports different difficulty levels: Easy, Medium, Hard
- 📊 Leaderboard tracking past attempts
- 📈 Data visualization with Plotly
- 🏆 Displays best score (fewest attempts)
- 🎈 Cheat code for debugging/testing
- 🎨 Clean and responsive UI

## 🛠️ Installation & Setup
Since you use `uv` for dependency management, follow these steps to set up the project:

### 1️⃣ **Clone the Repository**
```sh
 git clone https://github.com/muzaffar401/Assignment-1.git
 cd Assignment-1
```

### 2️⃣ **Initialize `uv` and Install Dependencies**
Since you're not using `requirements.txt`, install dependencies using `uv` as follows:

#### 🔹 **Step 1: Initialize `uv` (if not already initialized)**
```sh
 uv init
```
This will generate `pyproject.toml` and `uv.lock` files automatically.

#### 🔹 **Step 2: Add Dependencies**
```sh
 uv add streamlit pandas plotly
```
This command will install the required packages and update `pyproject.toml` accordingly.

### 3️⃣ **Run the Application**
```sh
 streamlit run main.py
```

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/b5f60124-22c7-49fe-9983-6a003ee54e3c)


## 🏗️ Project Structure
```
📂 Assignment-1
 ├── 📂 .venv              # Virtual environment (created by uv)
 ├── 📜 main.py            # Main Streamlit application
 ├── 📜 pyproject.toml     # Dependency management file
 ├── 📜 uv.lock            # Dependency lock file
 ├── 📜 README.md          # Project documentation
```

## 🎯 How to Play
1. Select a difficulty level (Easy, Medium, Hard).
2. Set the maximum range for the number.
3. Enter a guess and get hints whether the number is too high or too low.
4. Keep guessing until you find the correct number!
5. View your score and leaderboard.

## 🏆 Leaderboard
The game records all past attempts, showing the number of tries, difficulty level, and the selected max range.

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

