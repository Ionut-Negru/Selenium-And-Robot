*** Setting ***
Library    ../Scripts/PythonLandingPage.py
Library    ../Scripts/PythonSearchPage.py
Library    ../Scripts/PythonPEP318Page.py

*** Test Cases ***
Number of decorator example test
    Open Page
    Search On Page    decorator
    Get Search Results
    Select Result    0
    ${number_of_examples}=    Get Number Of Examples
    Should be Equal    ${number_of_examples}    5
    Close PEP318 Page