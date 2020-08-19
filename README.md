# PyVision

#### Computer Vision projects in Python and C++ sometimes
- OpenCV
- DLib
- Machine Learning
- Deep Learning

#### Setup until now
- Install VS Code
- Install MinGW for the gcc compiler
- Install Git
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

#### Install the packages through `pip`: 
```
py -m pip install numpy
py -m pip install matplotlib
py -m pip install opencv-python
```

Setup the `tasks.json` and `launch.json` files with the PATH to the compiler `g++.exe` and debugger `gdb.exe` respectively

If the MinGW `python` is taking over the Python `py` on Code Runner, add to `settings.json`
```
    "code-runner.executorMap":{
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "python": "py -u",
    }
```