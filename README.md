# PyVision

#### Computer Vision and Data Science projects in Python
- OpenCV
- DLib
- Machine Learning
- Data Analysis

#### Setup on Windows
- Install VS Code
- Install Git
- Install MinGW for the gcc compiler
- Install Python 3.x

#### Add to PATH
```
C:\{path-to}\VSCode\bin\
C:\{path-to}\MinGW\mingw32\bin\
C:\{path-to}\Git\cmd\
C:\{path-to}\Python\Python38-32\Scripts\
C:\{path-to}\Python\Python38-32\
C:\{path-to}\Python\Launcher\
```

#### Install VS Code Extensions:
- C/C++
- C/C++ Intellisense
- Python
- Code Runner (quality of life change)

#### Setup git user
```
git config --global user.name "Your Name"
git config --global user.email "yourname@email.com"
```

#### Install the packages through `pip`: 
```
py -m pip install --upgrade pip
py -m pip install numpy
py -m pip install matplotlib
py -m pip install opencv-python
py -m pip install imutils
py -m pip install cmake
py -m pip install dlib
py -m pip install face_recognition
py -m pip install scipy
py -m pip install -U scikit-image
py -m pip install skimage
```

#### To use Cuda acceleration on dlib, build from source, need Visual Studio(clang) installed:

Add to PATH
```
C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\ClangC2\14.10.25903\bin\HostX86
C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\ClangC2\14.10.25903\bin\HostX64
```
Run on cmd
```
py -m pip install cmake
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build
cd build
cmake .. -DUSE_AVX_INSTRUCTIONS=1
cmake --build .
cd ..
python setup.py install --yes USE_AVX_INSTRUCTIONS
```

#### Setup the `tasks.json` and `launch.json` files with the PATH to the compiler `g++.exe` and debugger `gdb.exe` respectively

If the MinGW `python` is taking over the Python installation, use the Launcher `py` on Code Runner, adding to `settings.json`:
```
    "code-runner.executorMap":{
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "python": "py -u",
    },
    "python.pythonPath": "C:\\Python\\Python38-32\\python.exe",
```

Fixing intellisense and linter for opencv on `settings.json`:
```
    "python.autoComplete.extraPaths": [
        "C:\\Python\\Python38-32\\Lib\\site-packages"
    ],
    "python.linting.pylintArgs": [
        "--extension-pkg-whitelist=cv2"
    ]
```

Or disable:
```
    "python.linting.enabled": false
```
