#!/bin/bash
rm -f "tests/results/*.xml"
pytest tests/unit --junitxml="tests/results/unittest_report.xml"
ls -R tests
# pytest tests/integration --junitxml="tests/results/integrationtest_report.xml"