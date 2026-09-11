#
# horus-lineage
# Copyright (C) 2026 QuietFlare
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Tests for the command and where it routes.
"""

import pytest

from horus_lineage import cli

USAGE_ERROR = 2
"""The exit code for a refused command."""


class TestRouting:
    """
    The bare command, a known command, and an unknown one.
    """

    def test_no_arguments_prints_usage(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Help, exit 0."""
        assert cli.main([]) == 0
        assert "usage:" in capsys.readouterr().out

    def test_an_unknown_command_is_refused(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Exit 2 with the usage attached."""
        assert cli.main(["frobnicate"]) == USAGE_ERROR
        assert "unknown command" in capsys.readouterr().out

    def test_conformance_is_imported_and_run(self, tmp_path: object) -> None:
        """
        A known command is imported only once chosen, then run.
        """
        assert cli.main(["conformance", str(tmp_path)]) == 1
