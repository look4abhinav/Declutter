# DeClutter 🧹

DeClutter is a robust Python utility designed to automatically organize files in a directory based on their file extensions. It groups files into categorized folders (like `Images`, `Documents`, `Video`, etc.), making it easy to keep your workspace clean.

## 🚀 Features

- **Automatic Categorization**: Groups files into logical folders using a comprehensive list of extensions.
- **Smart Renaming**: Automatically handles filename conflicts using incremental numbering.
- **Undo Functionality**: Can revert the organization process and move files back to their original source.
- **Modern Python Stack**: Uses `pathlib` for robust path handling and `uv` for lightning-fast environment management.
- **CLI Interface**: Flexible command-line arguments to specify source and destination.

## 🛠️ Setup

### Prerequisites

- Python 3.7+
- [uv](https://github.com/astral-sh/uv) (Recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/look4abhinav/Declutter.git
   cd Declutter
   ```

2. **Create a virtual environment and install dependencies:**
   Using `uv`:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

## 📖 Usage

Run the utility from your terminal:

### Basic Declutter
Organize the current directory into a folder named `Declutter`:
```bash
declutter
```

### Specify Source Directory
Organize a specific folder:
```bash
declutter /path/to/your/messy/folder
```

### Custom Destination
Change the name of the organization folder:
```bash
declutter --dest MyOrganizedFiles
```

### Undo Changes
Move everything back to the source directory and remove the categories:
```bash
declutter --undo
```

## 🧪 Development

### Running Tests
```bash
uv pip install pytest
pytest
```

### Linting
```bash
uv pip install ruff
ruff check .
```

## 📝 License
This project is licensed under the MIT License.
