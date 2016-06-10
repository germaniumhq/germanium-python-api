from behave import *

from germanium.static import *


@step(u'I upload a file using the form from the page')
def step_impl(context):

    if get_web_driver().capabilities['browserName'] == "internet explorer":
        file_select(InputFile(),
                    r"c:\features\steps\test-data\upload_test_file.txt",
                    path_check=False)
    else:
        file_select(InputFile(),
                    'features/steps/test-data/upload_test_file.txt')

    click(Button())
    get_germanium().wait_for_page_to_load()


@step(u'the file is uploaded successfully')
def step_impl(context):
    assert Text("Uploaded 'upload_test_file.txt'.").exists()
