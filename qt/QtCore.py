# -*- coding: utf-8 -*-
"""
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
"""

import qt

from PyQt4.QtCore import *
from PyQt4.QtCore import Qt 
from PyQt4.QtCore import pyqtSignal as Signal 

Qt.ItemSelectionMode.ContainsItemShape = Qt.ContainsItemShape 
Qt.ItemSelectionMode.IntersectsItemShape = Qt.IntersectsItemShape
Qt.ItemSelectionMode.ContainsItemBoundingRect = Qt.ContainsItemBoundingRect 
Qt.ItemSelectionMode.IntersectsItemBoundingRect = Qt.IntersectsItemBoundingRect

Qt.ItemDataRole.UserRole = Qt.UserRole

Qt.ItemDataRole.BackgroundRole = Qt.BackgroundRole
Qt.ItemDataRole.DisplayRole = Qt.DisplayRole
Qt.ItemDataRole.EditRole = Qt.EditRole
Qt.ItemDataRole.UserRole = Qt.UserRole

Qt.ToolButtonStyle.ToolButtonTextUnderIcon = Qt.ToolButtonTextUnderIcon
Qt.ToolBarArea.TopToolBarArea = Qt.TopToolBarArea

Qt.ItemFlag.NoItemFlags = Qt.NoItemFlags 
Qt.ItemFlag.ItemIsEnabled = Qt.ItemIsEnabled
Qt.ItemFlag.ItemIsDragEnabled = Qt.ItemIsDragEnabled
Qt.ItemFlag.ItemIsSelectable = Qt.ItemIsSelectable
Qt.ItemFlag.ItemIsEditable = Qt.ItemIsEditable    

Qt.WindowModality.ApplicationModal = Qt.ApplicationModal

Qt.PenStyle.NoPen = Qt.NoPen    

Qt.SortOrder.AscendingOrder = Qt.AscendingOrder
Qt.KeyboardModifierMask.ControlModifier = Qt.ControlModifier    
Qt.KeyboardModifierMask.ShiftModifier = Qt.ShiftModifier
Qt.ScrollBarPolicy.ScrollBarAlwaysOff = Qt.ScrollBarAlwaysOff