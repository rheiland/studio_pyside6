# Use a Python base image with the desired Python version
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required by PySide6
RUN apt-get update && apt-get install -y \
    python3-pip \
    build-essential \
    libgl1-mesa-glx \
    libxcb-xinerama0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-render-util0 \
    libxext6 libx11-6 libgl1 libglib2.0-0 libxrender1 \
    libegl1 libxkbcommon0 libdbus-1-3 \    
    qtbase5-dev \
    python3-pyqt5 \
    python3-matplotlib \
    xvfb




# Install PySide6 using pip
RUN pip install PySide6 numpy matplotlib scipy pandas
# RUN pip install --no-cache-dir -r requirements.txtS

# Copy your application code into the container
COPY . .

# Set the command to run your application
CMD ["python", "bin/studio.py"]