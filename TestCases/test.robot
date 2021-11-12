*** Setting ***
Library    ../Scripts/PythonLandingPage.py
Library    ../Scripts/PythonDownloadsPage.py
Library    ../Scripts/utils.py

*** Test Cases ***

Last python version from downloads test
    Open Page
    Click Navigation Submenu Item    Downloads    All releases
    ${result}=    Get Data From Versions Table    0    Release version 
    Should be Equal    ${result}    3.10
    Close Browser
    
Latest release after latest version test
    Open Page
    Click Navigation Submenu Item    Downloads    All releases
    ${last_version}=    Get Latest Version
    ${version_exist_on_release}=    Find Entry In Column In Releases Table    Release number    ${last_version}
    Should be True    ${version_exist_on_release}
    ${last_version_date}=    Get Latest Version Date
    ${last_release_date}=    Get Latest Release Date
    ${date_comparison}=    Compare Date    ${last_release_date}    ${last_version_date}
    Should be Equal    ${date_comparison}    1
    
    