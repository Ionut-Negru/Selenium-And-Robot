*** Setting ***
Library    ../Scripts/PythonLandingPage.py
Library    ../Scripts/PythonDownloadsPage.py
Library    ../Scripts/utils.py

*** Test Cases ***

Last python version from downloads test
    Open Page
    Click Navigation Submenu Item    Downloads    All releases
    Get Versions Table
    ${result}=    Get Latest Version
    Should be Equal    ${result}    3.10
    Close Browser
    
Latest release after latest version test
    Open Page
    Click Navigation Submenu Item    Downloads    All releases
    Get Versions Table
    Get Releases Table
    ${last_version}=    Get Latest Version
    ${last_version_exist_on_release}=    Has Entry Inside Releases Table Column    Release version    ${last_version}
    Should be True    ${last_version_exist_on_release} 
    ${last_version_date}=    Get Latest Version Date
    ${last_release_date}=    Get Latest Release Date
    ${date_comparison}=    Compare Date    ${last_release_date}    ${last_version_date}
    Should be Equal    ${date_comparison}    1
    Close Browser
    
    