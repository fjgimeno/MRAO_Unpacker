Simple python script and windows executable to unpack MRAO texture maps into it's individual maps.

Example usage:

  Linux:
    Open terminal into this project folder.
    Install requirements.txt (pip install -r ./requirements.txt)
    Execute with "python MRAO_Extractor.py ImagePath.ext (Optional)OutputPath"
    When not supplying an output path, a folder will be created where the executable is (if not, check the parent folder)

  Windows:
    Open a Command prompt window (Windows_Key + r, write CMD, press enter)
    Input the following command: ".\MRAO_Unpacker.exe ImagePath.ext (Optional)OutputPath"
    When not supplying an output path, a folder will be created where the executable is (if not, check the parent folder)


  Build from source (Windows):
    Make sure you have Pyinstaller installed (pip install pyinstaller)
    Then navigate to the *.py containing folder in CMD and execute "pyinstaller --onefile FileName.py)
