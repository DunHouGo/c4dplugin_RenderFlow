# Copyright 2022 Autodesk, Inc.  All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk license
# agreement provided at the time of installation or download, or which
# otherwise accompanies this software in either electronic or hard copy form. 

import c4d

ARNOLD_SCENE_EXPORT = 1029993

SCENE_EXPORT_FORMAT_ASS = 193450604
SCENE_EXPORT_FORMAT_USD = 193472369

SCENE_EXPORT_OBJECT_MODE_ALL = 0
SCENE_EXPORT_OBJECT_MODE_SELECTED = 1
SCENE_EXPORT_OBJECT_MODE_SELECTED_INDIVIDUALLY = 2

def Export(doc, filename, fileFormat = None, compressed = False, bbox = False, binary = True, expandProcedurals = False,
    mask = 0xFFFF, startFrame = None, endFrame = None, stepFrame = 1, objectMode = SCENE_EXPORT_OBJECT_MODE_ALL, exportObjectHierarchy = True,
    replaceWithProcedural = False):
    """
    Exports the given scene to file.

    Parameters
    ----------
    doc : c4d.documents.BaseDocument
        The scene to export.
    filename : str
        Path of the output file. If None, the file is exported next to the c4d scene file.
    fileFormat : int
        Output file format. If None, the format is guessed from the filename.
    compressed : boolean
        If true the scene is exported directly to gzip-compressed files (.ass.gz).
    bbox : boolean
        If true bounding box of the scene are added to the ASS meta data.
    binary : boolean
        If true binary encoding is used.
    expandProcedurals : boolean
        If true procedurals will be expanded before exporting the scene.
    mask : int
        Specifies which Arnold node types are included in the output. See the AtNodeEntry page of the Arnold API for the available node types.
    startFrame : int
        Specifies the first frame when exporting an animation. If None, the scene's render settings will be used.
    endFrame : int
        Specifies the last frame when exporting an animation. If None, the scene's render settings will be used.
    stepFrame : int
        Specifies the increment between frames when exporting an animation. If None, the scene's render settings will be used.
    objectMode : int
        Specifies which objects are exported (all, selected, selected individually).
    exportObjectHierarchy : boolean
        If true, exports the whole hierarchy (children) in 'selected' object mode.
    replaceWithProcedural : boolean
        If true, replaces the exported objects with an Arnold Procedural pointing to the exported file.
    """
    if doc is None:
        return

    options = c4d.BaseContainer()
    if filename is not None:
        options.SetFilename(0, filename)
    options.SetBool(1, compressed)
    options.SetBool(2, bbox)
    options.SetBool(3, binary)
    options.SetBool(4, expandProcedurals)
    options.SetInt32(5, mask)
    if startFrame is not None:
        options.SetInt32(6, startFrame)
    if endFrame is not None:
        options.SetInt32(7, endFrame)
    if stepFrame is not None:
        options.SetInt32(8, stepFrame)
    options.SetInt32(11, objectMode)
    options.SetBool(12, replaceWithProcedural)
    options.SetBool(13, exportObjectHierarchy)
    if fileFormat is not None:
        options.SetInt32(14, fileFormat)
    doc.GetSettingsInstance(c4d.DOCUMENTSETTINGS_DOCUMENT).SetContainer(ARNOLD_SCENE_EXPORT, options)
 
    c4d.CallCommand(ARNOLD_SCENE_EXPORT)

