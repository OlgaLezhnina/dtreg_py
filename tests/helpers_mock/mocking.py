def mocked_request_dtr(route):
    mocked_info = None
    if route == "https://orkg.org/api/templates/R758315":
        mocked_info = info_template_1
    elif route == "https://orkg.org/api/templates/R758316":
        mocked_info = info_template_2
    elif route == "https://orkg.org/api/templates/?target_class=C102007":
        mocked_info = info_via_class
    else:
        print("Please check the URL for mocking")
    return mocked_info


info_template_1 = {'id': 'R758315',
                   'label': 'dtreg_test_template1',
                   'target_class': {'id': 'C102006'},
                   'properties': [{
                       'min_count': 0,
                       'max_count': None,
                       'path': {'id': 'P160020', 'label': 'property1'},
                       'datatype': {'id': 'String'}},
                       {'min_count': 0,
                        'max_count': None,
                        'path': {'id': 'P160021', 'label': 'property2'},
                        'class': {'id': 'C102007'}}]}

info_template_2 = {'id': 'R758316',
                   'label': 'dtreg_test_template2',
                   'target_class': {'id': 'C102007'},
                   'properties': [{
                       'min_count': 0,
                       'max_count': None,
                       'path': {'id': 'P160024', 'label': 'property3'},
                       'datatype': {'id': 'Integer'}}]}

info_via_class = {'content': [{'id': 'R758316',
                               'label': 'dtreg_test_template2'}]}
