from behave import *

from germanium.static import *


@step(u'I upload a file using the form from the page')
def step_impl(context):

    ie_path = r"c:\features\steps\test-data\upload_test_file.txt"
    normal_path = r"'features/steps/test-data/upload_test_file.txt'"

    if get_web_driver().capabilities['browserName'] == "internet explorer":
        path = ie_path
    else:
        path = normal_path

    file_select(InputFile(),
                path,
                path_check=False)
    click(Button())
    get_germanium().wait_for_page_to_load()


@step(u'the file is uploaded successfully')
def step_impl(context):
    assert Text("Uploaded 'upload_test_file.txt'.").exists()
