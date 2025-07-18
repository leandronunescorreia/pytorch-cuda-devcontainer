# PyTorch CUDA Devcontainer

This project provides a development environment for PyTorch with CUDA support, using a Docker-based devcontainer setup. It includes code and tests for verifying CUDA availability and basic PyTorch functionality.

## Features
- **Devcontainer**: Pre-configured for VS Code Remote Containers, with CUDA 11.8, Python 3.10, and PyTorch (with torchvision and torchaudio) installed.
- **Jupyter Notebook**: Example notebook to check CUDA and PyTorch setup.
- **Source Code**: Python scripts to check CUDA availability.
- **Tests**: Simple Pytest-based tests for PyTorch tensor operations.

## Project Structure
```
jupyter/
    cuda-test.ipynb         # Jupyter notebook to test CUDA and PyTorch
src/
    __init__.py
    check_cuda_is_available.py  # Script to check CUDA availability

# Tests
/test/
    __init__.py
    test_tensor.py          # Pytest for basic tensor checks
```

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) with the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension

### Usage
1. **Open in VS Code**: Open this folder in VS Code.
2. **Reopen in Container**: When prompted, reopen in the devcontainer. This will build the Docker image and set up the environment.
3. **Run Jupyter Notebook**: Open `jupyter/cuda-test.ipynb` to verify CUDA and PyTorch setup.
4. **Run Tests**: Use the VS Code testing UI or run `pytest` in the terminal to execute tests in the `test/` folder.

### Example: Check CUDA Availability
Run the following script:
```bash
python src/check_cuda_is_available.py
```

### Example: Run Tests
```bash
pytest
```

## Customization
- The devcontainer is defined in `.devcontainer/devcontainer.json` and `.devcontainer/Dockerfile`.
- Modify these files to change Python, CUDA, or PyTorch versions as needed.

## License
MIT License
