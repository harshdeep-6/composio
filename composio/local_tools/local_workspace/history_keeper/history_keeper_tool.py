from typing import Optional

from composio.local_tools.local_workspace.commons.get_logger import get_logger
from composio.local_tools.local_workspace.commons.history_processor import (
    HistoryProcessor,
)
from composio.local_tools.local_workspace.commons.local_docker_workspace import (
    WorkspaceManagerFactory,
)
from composio.local_tools.local_workspace.history_keeper.actions.get_workspace_history import (
    GetWorkspaceHistory,
)
from composio.local_tools.tool import Tool


logger = get_logger()


class HistoryKeeper(Tool):
    """
    local workspace tool which can maintain history across commands.
    """

    workspace_factory: Optional[WorkspaceManagerFactory] = None
    history_processor: Optional[HistoryProcessor] = None

    def actions(self) -> list:
        return [GetWorkspaceHistory]

    def triggers(self) -> list:
        return []

    def set_workspace_factory(self, workspace_factory: WorkspaceManagerFactory):
        self.workspace_factory = workspace_factory

    def get_workspace_factory(self) -> Optional[WorkspaceManagerFactory]:
        return self.workspace_factory

    def set_history_processor(self, history_processor: HistoryProcessor):
        self.history_processor = history_processor

    def get_history_processor(self) -> Optional[HistoryProcessor]:
        return self.history_processor