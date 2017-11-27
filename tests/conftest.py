# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of fixtures to be used across the tests."""

import pytest

@pytest.fixture(scope="function")
def test_fixture(request):
    """Create a test fixture."""

    myvar = 5

    def tear_down():
        # clean up here
        pass
    request.addfinalizer(tear_down)

    return myvar