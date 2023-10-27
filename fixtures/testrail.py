import logging
import typing
from collections import namedtuple

import pytest
from testrail_api import TestRailAPI

import configs

_logger = logging.getLogger(__name__)

testrail_api = None
test_run_id = None

PASS = 1
FAIL = 5
SKIPPED = 11
UNTESTED = 12

test_case = namedtuple('TestCase', ['id', 'skipped'])


@pytest.fixture(scope='session')
def init_testrail_api(request):
    if configs.testrail.RUN_NAME:
        _logger.info('TestRail API initializing')
        global testrail_api
        testrail_api = TestRailAPI(
            configs.testrail.URL,
            configs.testrail.USR,
            configs.testrail.PSW
        )
        test_cases = get_test_cases_in_session(request)
        test_run = get_test_run(configs.testrail.RUN_NAME)
        if not test_run:
            test_case_ids = list(set([tc_id.id for tc_id in test_cases]))
            test_run = create_test_run(configs.testrail.RUN_NAME, test_case_ids)

        global test_run_id
        test_run_id = test_run['id']

        for test_case in test_cases:
            if is_test_case_in_run(test_case.id):
                if test_case.skipped:
                    _update_result(test_case.id, SKIPPED, test_case.skipped)
                    _logger.info(f'Test: "{test_case.id}" marked as "Skipped"')
                else:
                    if _get_test_case_status(test_case.id) != UNTESTED:
                        _update_result(test_case.id, UNTESTED)
                        _logger.info(f'Test: "{test_case.id}" marked as "Untested"')
            else:
                _logger.info(
                    f'Report result for test case: {test_case.id} skipped, not in test run: {configs.testrail.RUN_NAME}')
    else:
        _logger.info('TestRail report skipped')


@pytest.fixture
def check_result(request):
    yield
    if configs.testrail.RUN_NAME:
        item = request.node
        test_case_ids = _find_test_case_id_markers(request)
        for test_case_id in test_case_ids:
            if is_test_case_in_run(test_case_id):
                current_test_status = _get_test_case_status(test_case_id)
                if item.rep_call.failed:
                    _update_result(test_case_id, FAIL, item.rep_call.longreprtext)
                else:
                    if current_test_status != FAIL:
                        _update_result(test_case_id, PASS, f"{request.node.name} SUCCESS")
                    else:
                        _update_comment(test_case_id, f"{request.node.name} SUCCESS")


def _update_result(test_case_id: int, result: int, comment: str = None):
    testrail_api.results.add_result_for_case(
        run_id=test_run_id,
        case_id=test_case_id,
        status_id=result,
        comment=comment or ""
    )


def _update_comment(test_case_id: int, comment: str):
    testrail_api.results.add_result_for_case(
        run_id=test_run_id,
        case_id=test_case_id,
        comment=comment
    )


def _find_test_case_id_markers(request) -> typing.List[int]:
    for marker in request.node.own_markers:
        if marker.name == 'case':
            test_case_ids = marker.args
            return test_case_ids
    return []


def _get_test_case_status(test_case_id: int) -> int:
    test_case_results = testrail_api.results.get_results_for_case(test_run_id, test_case_id)
    try:
        result = 0
        while True:
            last_test_case_status = test_case_results['results'][result]['status_id']
            if last_test_case_status is None:
                result += 1
            else:
                return last_test_case_status
    except:
        return SKIPPED


def is_test_case_in_run(test_case_id: int) -> bool:
    try:
        testrail_api.results.get_results_for_case(test_run_id, test_case_id)
    except Exception as err:
        return False
    else:
        return True


def _get_test_cases():
    results = []
    limit = 250
    chunk = 0
    while True:
        tests = testrail_api.tests.get_tests(test_run_id, offset=chunk)['tests']
        results.extend(tests)
        if len(tests) == limit:
            chunk += limit
        else:
            return results


def  get_test_cases_in_session(request) -> typing.List[test_case]:
    tests = request.session.items
    test_cases = []
    for test in tests:
        tc_ids = []
        skipped = ''
        for marker in getattr(test, 'own_markers', []):
            match getattr(marker, 'name', ''):
                case 'case':
                    tc_ids = list(marker.args)
                case 'skip':
                    skipped = f'Reason: {marker.kwargs.get("reason", "")}'
        for tc_id in tc_ids:
            test_cases.append(test_case(tc_id, skipped))
    return test_cases


def create_test_run(name: str, ids: list) -> dict:
    test_run = testrail_api.runs.add_run(
        project_id=configs.testrail.PROJECT_ID,
        name = name,
        description = f'Jenkins: {configs.testrail.CI_BUILD_URL}',
        include_all = False if list else True,
        case_ids = ids or None
    )
    return test_run


def get_test_run(name: str) -> typing.Optional[dict]:
    test_runs = testrail_api.runs.get_runs(
        project_id=configs.testrail.PROJECT_ID,
        is_completed=False
    )
    for test_run in test_runs['runs']:
        if test_run['name'] == name:
            return test_run
