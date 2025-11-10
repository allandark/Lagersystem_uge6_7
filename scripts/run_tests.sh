#!/bin/bash
pytest tests/unit --junitxml="tests/results/unittest_report.xml"
ls -R tests
# pytest tests/integration --junitxml="tests/results/integrationtest_report.xml"