import pytest


@pytest.mark.xfail(strict=True)  # Найдите там параметр, который в случае неожиданного прохождения теста,
# помеченного как xfail, отметит в отчете этот тест как упавший
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
