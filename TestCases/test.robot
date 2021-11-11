*** Setting ***
Library    ../Scripts/PythonLandingPage.py
Library    ../Scripts/PythonDownloadsPage.py

*** Test Cases ***

Last python version from downloads test
    Open Page
    Click Navigation Submenu Button    Downloads    All releases
    Get Table From Elements
    ${result}=    Get Data From Table    0    Python version 
    Should be Equal    ${result}    3.10
    Close Downloads Page
    

    