import pytest
from unittest.mock import mock_open, patch
from systemreporter import SystemReporter
import json

# Test data
def read_test_data(filename):
    with open(f"tests/test_data/{filename}", "r") as f:
        return f.read()


CPUINFO_VALID = read_test_data("cpuinfo_valid")
CPUINFO_INVALID = read_test_data("cpuinfo_invalid")


# Tests
class TestSystemReporter:

    # read_cpuinfo
    @patch("builtins.open")
    def test_read_cpuinfo_positive(self, mock_file):
        reporter = SystemReporter()
        reporter.read_info("/proc/cpuinfo")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_cpuinfo_file_not_found(self, mock_file):
        reporter = SystemReporter()
        with pytest.raises(FileNotFoundError, match="cpuinfo file not found"):
            reporter.read_info("path/not/exists")


    # get_cpu_model
    @patch("builtins.open", new_callable=mock_open, read_data=CPUINFO_VALID)
    def test_get_cpu_model_positive(self, mock_file):
        reporter = SystemReporter()
        reporter.get_cpu_model()
        assert reporter.cpu_info["model"] == "Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz"

    @patch("builtins.open", new_callable=mock_open, read_data=CPUINFO_INVALID)
    def test_get_cpu_model_negative(self, mock_file):
        reporter = SystemReporter()
        with pytest.raises(ValueError, match="CPU model information not found"):
            reporter.get_cpu_model()


    # get_cpu_cores
    @patch("builtins.open", new_callable=mock_open, read_data=CPUINFO_VALID)
    def test_get_cpu_cores_positive(self, mock_file):
        reporter = SystemReporter()
        reporter.get_cpu_cores()
        assert reporter.cpu_info["cores"] == 2

    @patch("builtins.open", new_callable=mock_open, read_data=CPUINFO_INVALID)
    def test_get_cpu_cores_negative(self, mock_file):
        reporter = SystemReporter()
        with pytest.raises(ValueError, match="CPU cores information not found"):
            reporter.get_cpu_cores()


    # get_cpu_threads
    @patch("builtins.open", new_callable=mock_open, read_data=CPUINFO_VALID)
    def test_get_cpu_threads_positive(self, mock_file):
        reporter = SystemReporter()
        reporter.get_cpu_threads()
        assert reporter.cpu_info["threads"] == 6

    @patch("builtins.open", new_callable=mock_open, read_data=CPUINFO_INVALID)
    def test_get_cpu_threads_negative(self, mock_file):
        reporter = SystemReporter()
        with pytest.raises(ValueError, match="CPU threads information not found"):
            reporter.get_cpu_threads()
