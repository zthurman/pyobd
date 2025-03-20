"""
Keep the gui things together.
"""

import wx

# Define notification event for sensor result window
EVT_RESULT_ID = 1000
EVT_GRAPH_VALUE_ID = 1036
EVT_GRAPHS_VALUE_ID = 1048
EVT_GRAPHS8_VALUE_ID = 1051
EVT_GRAPH_ID = 1035
EVT_GRAPHS_ID = 1049
EVT_GRAPHS8_ID = 1050
EVT_COMBOBOX = 1036
EVT_CLOSE_ID = 1037
EVT_BUILD_COMBOBOXGRAPH_ID = 1038
EVT_BUILD_COMBOBOXGRAPHS_ID = 1045
EVT_BUILD_COMBOBOXGRAPHS8_ID = 1102
EVT_DESTROY_COMBOBOX_ID = 1039
EVT_COMBOBOXGRAPH_GETSELECTION_ID = 1040
EVT_COMBOBOXGRAPHS_GETSELECTION_ID = 1046
EVT_COMBOBOXGRAPHS8_GETSELECTION_ID = 1100
EVT_COMBOBOXGRAPH_SETSELECTION_ID = 1044
EVT_COMBOBOXGRAPHS_SETSELECTION_ID = 1047
EVT_COMBOBOXGRAPHS8_SETSELECTION_ID = 1101
EVT_INSERT_SENSOR_ROW_ID = 1041
EVT_INSERT_FREEZEFRAME_ROW_ID = 1042
EVT_FREEZEFRAME_RESULT_ID = 1043

EVT_COMBOBOXGRAPHS8_GETSELECTION_ID = 1105
EVT_COMBOBOXGRAPHS8_SETSELECTION_ID = 1106


class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data


class FreezeframeResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_FREEZEFRAME_RESULT_ID)
        self.data = data


class InsertSensorRowEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_INSERT_SENSOR_ROW_ID)
        self.data = data


class InsertFreezeframeRowEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_INSERT_FREEZEFRAME_ROW_ID)
        self.data = data


class BuildComboBoxGraphEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_BUILD_COMBOBOXGRAPH_ID)
        self.data = data


class BuildComboBoxGraphsEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_BUILD_COMBOBOXGRAPHS_ID)
        self.data = data


class BuildComboBoxGraphs8Event(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_BUILD_COMBOBOXGRAPHS8_ID)
        self.data = data


class DestroyComboBoxEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_DESTROY_COMBOBOX_ID)
        self.data = data


class GetSelectionComboBoxGraphEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_COMBOBOXGRAPH_GETSELECTION_ID)
        self.data = data


class GetSelectionComboBoxGraphsEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_COMBOBOXGRAPHS_GETSELECTION_ID)
        self.data = data


class GetSelectionComboBoxGraphs8Event(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_COMBOBOXGRAPHS8_GETSELECTION_ID)
        self.data = data


class SetSelectionComboBoxGraphEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_COMBOBOXGRAPH_SETSELECTION_ID)
        self.data = data


class SetSelectionComboBoxGraphsEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_COMBOBOXGRAPHS_SETSELECTION_ID)
        self.data = data


class SetSelectionComboBoxGraphs8Event(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_COMBOBOXGRAPHS8_SETSELECTION_ID)
        self.data = data


class GraphValueEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_GRAPH_VALUE_ID)
        self.data = data


class GraphsValueEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_GRAPHS_VALUE_ID)
        self.data = data


class Graphs8ValueEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_GRAPHS8_VALUE_ID)
        self.data = data


class GraphEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_GRAPH_ID)
        self.data = data


class GraphsEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_GRAPHS_ID)
        self.data = data


class Graphs8Event(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_GRAPHS8_ID)
        self.data = data


# event pro aktualizaci DTC tabu
EVT_DTC_ID = 1001


class DTCEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_DTC_ID)
        self.data = data


# event pro aktualizaci status tabu
EVT_STATUS_ID = 1002


class StatusEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_STATUS_ID)
        self.data = data


class CloseEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_CLOSE_ID)
        self.data = data


# event pro aktualizaci tests tabu
EVT_TESTS_ID = 1003


class TestEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_TESTS_ID)
        self.data = data
