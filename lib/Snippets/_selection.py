# -*- coding: utf-8 -*-

# IMPORTS
from Autodesk.Revit.DB import *

# VARIABLES
uidoc = __revit__.ActiveUIDocument
doc   = __revit__.ActiveUIDocument.Document

#FUNCTIONS

def get_selected_elements(uidoc):
    """THis function will return elements that are currently selected in Revit UI
    :param uidoc:   uidoc where elements are selected.
    :return:        List of selected elements"""
    select_elements = []

    for elem_id in uidoc.Selection.GetElementIds():
        elem = uidoc.Document.GetElement(elem_id)
        select_elements.append(elem)

    return select_elements

