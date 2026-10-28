"""Check the Python model against the original spreadsheet."""

from pathlib import Path

import pytest

from cre_underwriting import BASE_CASE
from cre_underwriting.excel import load_assumptions

WORKBOOK = Path(__file__).parent / "fixtures" / "CRE_Acquisition_Model.xlsx"


def test_reads_inputs_from_workbook():
    assert load_assumptions(WORKBOOK) == BASE_CASE


def test_missing_sheet_raises():
    with pytest.raises(KeyError):
        load_assumptions(WORKBOOK, sheet="Nope")
