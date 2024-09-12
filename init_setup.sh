#To create env and install requirements


echo [$(date)]: "START"
echo [$(date)]: "Creating virtual environment with python"
python -m venv env  # Create a virtual environment named 'env'
echo [$(date)]: "Activating environment"
source env/bin/activate  # Activate the virtual environment
echo [$(date)]: "Installing development requirements"
pip install -r requirements_dev.txt  # Install requirements
echo [$(date)]: "END"