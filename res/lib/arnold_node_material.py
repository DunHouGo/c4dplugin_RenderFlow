# Copyright 2022 Autodesk, Inc.  All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk license
# agreement provided at the time of installation or download, or which
# otherwise accompanies this software in either electronic or hard copy form. 

import c4d

# Arnold Node Material is available since Cinema 4D R23
node_material_available = False
if c4d.GetC4DVersion() >= 23000:
    node_material_available = True

# material id
ARNOLD_SHADER_NETWORK = 1033991

# root port ids
ARNOLD_SHADER_PORT_ID = 537905099
ARNOLD_DISPLACEMENT_PORT_ID = 537905100
ARNOLD_VIEWPORT_PORT_ID = 537906863
ARNOLD_HISTOGRAM_PORT_ID = 537908968
ARNOLD_VCOLOR_DATATYPE_LEGACYID = 1035785
ARNOLD_VCOLOR_DATATYPE = "com.autodesk.arnold.datatype.vcolor"

C4DAI_SHADERLINK_CONTAINER = 9988000
C4DAI_SHADERLINK_TYPE = 101
C4DAI_SHADERLINK_VALUE = 102
C4DAI_SHADERLINK_TEXTURE = 103
C4DAI_SHADERLINK_MATERIAL = 104

C4DAI_GVC4DSHADER_BITMAP_COLOR_SPACE = 10101

C4DTOA_MSG_GET_NODEMATERIAL_CUSTOMDATA = 1093
C4DTOA_MSG_SET_NODEMATERIAL_CUSTOMDATA = 1094

ARNOLD_SCENE_HOOK = 1032309
# output component ids
ARNOLD_PARAMCOMP_R = 1
ARNOLD_PARAMCOMP_G = 2
ARNOLD_PARAMCOMP_B = 3
ARNOLD_PARAMCOMP_A = 4
ARNOLD_PARAMCOMP_X = 5
ARNOLD_PARAMCOMP_Y = 6
ARNOLD_PARAMCOMP_Z = 7

# message ids
C4DTOA_MSG_TYPE = 1000
C4DTOA_MSG_PARAM1 = 2001
C4DTOA_MSG_PARAM2 = 2002
C4DTOA_MSG_PARAM3 = 2003
C4DTOA_MSG_PARAM4 = 2004
C4DTOA_MSG_RESP1 = 2011
C4DTOA_MSG_RESP2 = 2012
C4DTOA_MSG_RESP3 = 2013
C4DTOA_MSG_RESP4 = 2014
C4DTOA_MSG_QUERY_SHADER_NETWORK = 1028
C4DTOA_MSG_ADD_SHADER = 1029
C4DTOA_MSG_REMOVE_SHADER = 1030
C4DTOA_MSG_ADD_CONNECTION = 1031
C4DTOA_MSG_REMOVE_CONNECTION = 1032
C4DTOA_MSG_CONNECT_ROOT_SHADER = 1033
C4DTOA_MSG_DISCONNECT_ROOT_SHADER = 1034
C4DTOA_MSG_ALIGN_NODES = 1097

# shader type ids
ARNOLD_SHADER_GV = 1033990
ARNOLD_C4D_SHADER_GV = 1034190
ARNOLD_REFERENCE_GV = 1035541
  
C4DAI_GVSHADER_TYPE = 200
C4DAI_GVC4DSHADER_TYPE = 200

# C4D shader ids
C4DAIN_C4D_BITMAP = 904247772
C4DAIN_C4D_NOISE = 218464707
C4DAIN_C4D_SUBSTANCE_SHADER = 799632067
C4DAIN_C4D_VERTEX_MAP = 1896336102
C4DShaderIdMap = {
    c4d.Xbitmap: C4DAIN_C4D_BITMAP,
    c4d.Xnoise: C4DAIN_C4D_NOISE,
    c4d.Xsubstance: C4DAIN_C4D_SUBSTANCE_SHADER,
    c4d.Xvertexmap: C4DAIN_C4D_VERTEX_MAP,
}

# Arnold shader ids
C4DAIN_BLACKBODY = 1326266352
C4DAIN_DISPLACEMENT = 1227821282
C4DAIN_LIGHT_BLOCKER = 974577342
C4DAIN_OBJECT = 301260540
C4DAIN_OSL = 193501779
C4DAIN_RAMP_FLOAT = 1343782602
C4DAIN_RAMP_RGB = 499635473
C4DAIN_RANDOM = 417623846
C4DAIN_REFERENCE = 1491778796
C4DAIN_SHADOW_MATTE = 1432373531
C4DAIN_SPACE_TRANSFORM = 778771884
C4DAIN_TRIGO = 275933738
C4DAIN_VALUE = 277698370
C4DAIN_XPARTICLES = 206657884

LIGHT_BLOCKER_SHADER_ID = 1035773
OSL_SHADER_ID = 1050718
BLACKBODY_SHADER_ID = 1034217
RAMP_FLOAT_SHADER_ID = 1034228
RAMP_RGB_SHADER_ID = 1034229
RANDOM_SHADER_ID = 1034221
SHADOW_MATTE_SHADER_ID = 1034222
SPACE_TRANSFORM_SHADER_ID = 1034223
TRIGO_SHADER_ID = 1034226
VALUE_SHADER_ID = 1054367
OBJECT_SHADER_ID = 1055077
XPARTICLES_SHADER_ID = 1051148
DISPLACEMENT_SHADER_ID = 1051169
ArnoldCustomShaderIdMap = {
    LIGHT_BLOCKER_SHADER_ID: C4DAIN_LIGHT_BLOCKER,
    OSL_SHADER_ID: C4DAIN_OSL,
    BLACKBODY_SHADER_ID: C4DAIN_BLACKBODY,
    RAMP_FLOAT_SHADER_ID: C4DAIN_RAMP_FLOAT,
    RAMP_RGB_SHADER_ID: C4DAIN_RAMP_RGB,
    RANDOM_SHADER_ID: C4DAIN_RANDOM,
    SHADOW_MATTE_SHADER_ID: C4DAIN_SHADOW_MATTE,
    SPACE_TRANSFORM_SHADER_ID: C4DAIN_SPACE_TRANSFORM,
    TRIGO_SHADER_ID: C4DAIN_TRIGO,
    VALUE_SHADER_ID: C4DAIN_VALUE,
    OBJECT_SHADER_ID: C4DAIN_OBJECT,
    XPARTICLES_SHADER_ID: C4DAIN_XPARTICLES,
    DISPLACEMENT_SHADER_ID: C4DAIN_DISPLACEMENT,    
}

#=============================================
# Arnold Vector/Color custom gui
#=============================================

class ArnoldVColorCustomData:
    """
    A class used to represent data stored in the Arnold Vector/Color custom gui.
    """

    TYPE_COLOR = 1
    TYPE_VECTOR = 2
 
    def __init__(self, value = c4d.Vector(), guiType = TYPE_COLOR):
        self.value = value
        self.type = guiType

    def __repr__(self):
        return "%f %f %f (%s)" % (self.value.x, self.value.y, self.value.z, 
            "color" if self.type == ArnoldVColorCustomData.TYPE_COLOR else "vector")

def GetVColor(node, paramId):
    """
    Returns the value defined in the given node parameter.

    Parameters
    ----------
    node : c4d.BaseList2D or maxon.frameworks.graph.GraphNode
        Scene node (e.g. object).
    paramId : Int32
        Id of the parameter.
    """
    if node is None:
        return None

    vcolorData = ArnoldVColorCustomData()

    if node_material_available and isinstance(node, maxon.frameworks.graph.GraphNode):
        material = c4d.NodeMaterial.GetMaterial(maxon.Cast(maxon.frameworks.nodes.NodesGraphModelRef, node.GetGraph()))
        if material is None:
            return None

        # send a custom message to the Arnold Scene hook class to get the data
        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_GET_NODEMATERIAL_CUSTOMDATA)
        msg.SetLink(C4DTOA_MSG_PARAM1, material)
        msg.SetString(C4DTOA_MSG_PARAM2, node.GetPath())
        msg.SetString(C4DTOA_MSG_PARAM3, paramId)

        doc = c4d.documents.GetActiveDocument()
        arnoldSceneHook = doc.FindSceneHook(ARNOLD_SCENE_HOOK)
        if arnoldSceneHook is None:
            return none
        arnoldSceneHook.Message(c4d.MSG_BASECONTAINER, msg)

        vcolorData.value = msg.GetVector(C4DTOA_MSG_RESP1)
        vcolorData.type = msg.GetInt32(C4DTOA_MSG_RESP2)

    else:
        valueId = c4d.DescID(c4d.DescLevel(paramId), c4d.DescLevel(1))
        vcolorData.value = node.GetParameter(valueId, c4d.DESCFLAGS_GET_0)
        guiTypeId = c4d.DescID(c4d.DescLevel(paramId), c4d.DescLevel(2))
        vcolorData.type = node.GetParameter(guiTypeId, c4d.DESCFLAGS_GET_0)

    return vcolorData
 
def SetVColor(node, paramId, value):
    """
    Sets the value of the given node parameter.

    Parameters
    ----------
    node : c4d.BaseList2D or maxon.frameworks.graph.GraphNode
        Scene node (e.g. object).
    paramId : int
        Id of the parameter.
    value : ArnoldVColorCustomData, c4d.Vector, maxon.Color
        Value of the parameter to set.
    """
    if node is None:
        return None

    # check the data type of the value
    # accept ArnoldVColorCustomData, Vector and Color
    if isinstance(value, ArnoldVColorCustomData):
        vcolorData = value
    elif isinstance(value, c4d.Vector) or isinstance(value, maxon.Vector):
        vcolorData = ArnoldVColorCustomData(value, ArnoldVColorCustomData.TYPE_VECTOR)
    elif isinstance(value, maxon.Color):
        vcolorData = ArnoldVColorCustomData(c4d.Vector(value.r, value.g, value.b), ArnoldVColorCustomData.TYPE_COLOR)
    elif value is None:
        vcolorData = ArnoldVColorCustomData()
    else:
        print("[WARNING] %s.%s: invalid vcolor value, only ArnoldVColorCustomData, Vector or Color is accepted" % (node.GetId(), paramId))
        return None

    if node_material_available and isinstance(node, maxon.frameworks.graph.GraphNode):
        material = c4d.NodeMaterial.GetMaterial(maxon.Cast(maxon.frameworks.nodes.NodesGraphModelRef, node.GetGraph()))
        if material is None:
            return None

        # send a custom message to the Arnold Scene hook class to set the data
        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_SET_NODEMATERIAL_CUSTOMDATA)
        msg.SetLink(C4DTOA_MSG_PARAM1, material)
        msg.SetString(C4DTOA_MSG_PARAM2, node.GetPath())
        msg.SetString(C4DTOA_MSG_PARAM3, paramId)
        msg.SetVector(C4DTOA_MSG_PARAM4, vcolorData.value)
        msg.SetInt32(C4DTOA_MSG_PARAM5, vcolorData.type)

        doc = c4d.documents.GetActiveDocument()
        arnoldSceneHook = doc.FindSceneHook(ARNOLD_SCENE_HOOK)
        if arnoldSceneHook is None:
            return none
        arnoldSceneHook.Message(c4d.MSG_BASECONTAINER, msg)

    else:     
        valueId = c4d.DescID(c4d.DescLevel(paramId), c4d.DescLevel(1))
        node.SetParameter(valueId, vcolorData.value, c4d.DESCFLAGS_SET_0)
        guiTypeId = c4d.DescID(c4d.DescLevel(paramId), c4d.DescLevel(2))
        node.SetParameter(guiTypeId, vcolorData.type, c4d.DESCFLAGS_SET_0)

#=============================================
# Arnold Shader Link custom gui
#=============================================

class ArnoldShaderLinkCustomData:
    """
    A class used to represent data stored in the Arnold Shader Link custom gui.
    """

    TYPE_CONSTANT = 1
    TYPE_TEXTURE = 2
    TYPE_MATERIAL = 3
 
    def __init__(self, guiType = TYPE_CONSTANT, value = c4d.Vector(), texture = None, material = None):
        self.type = guiType
        self.value = value
        self.texture = texture
        self.texture_color_space = "sRGB"
        self.material = material

    def __repr__(self):
        if self.type == ArnoldShaderLinkCustomData.TYPE_CONSTANT:
            if self.value is not None:
                return "%f %f %f (constant)" % (self.value.x, self.value.y, self.value.z)
            else:
                return "0 0 0 (constant)"
        elif self.type == ArnoldShaderLinkCustomData.TYPE_TEXTURE:
            return "%s [%s] (texture)" % (self.texture, self.texture_color_space)
        elif self.type == ArnoldShaderLinkCustomData.TYPE_MATERIAL:
            return "%s (material)" % (self.material.GetName() if self.material is not None else "<none>")
        return ""

def GetShaderLink(node, paramId):
    """
    Returns the value defined in the given node parameter.

    Parameters
    ----------
    node : c4d.BaseList2D
        Scene node (e.g. Arnold Light object).
    paramId : Int32
        Id of the parameter.
    """
    if node is None:
        return None

    # get the container which stores the shader link attributes
    shaderLinkMainContainer = node[C4DAI_SHADERLINK_CONTAINER]
    if shaderLinkMainContainer is None:
        return None
    shaderLinkContainer = shaderLinkMainContainer.GetContainer(paramId)
    if shaderLinkContainer is None:
        return None

    # read the shader link attributes
    shaderLinkData = ArnoldShaderLinkCustomData()
    shaderLinkData.type = shaderLinkContainer.GetInt32(C4DAI_SHADERLINK_TYPE,  ArnoldShaderLinkCustomData.TYPE_CONSTANT)
    shaderLinkData.value = node[paramId]
    shader = shaderLinkContainer.GetLink(C4DAI_SHADERLINK_TEXTURE)
    if shader is not None and shader.GetType() == c4d.Xbitmap:
        shaderLinkData.texture = shader[c4d.BITMAPSHADER_FILENAME]
        shaderLinkData.texture_color_space = shader[C4DAI_GVC4DSHADER_BITMAP_COLOR_SPACE]
    else:
        shaderLinkData.texture = None
        shaderLinkData.texture_color_space = ""
    shaderLinkData.material = shaderLinkContainer.GetLink(C4DAI_SHADERLINK_MATERIAL)

    return shaderLinkData
 
def SetShaderLink(node, paramId, value):
    """
    Sets the value of the given node parameter.

    Parameters
    ----------
    node : c4d.BaseList2D
        Scene node (e.g. Arnold Light object).
    paramId : int
        Id of the parameter.
    value : ArnoldShaderLinkCustomData, c4d.Vector, maxon.Color, str, c4d.BaseMaterial
        Value of the parameter to set.
    """
    if node is None:
        return None

    # check the data type of the value
    # accept ArnoldShaderLinkCustomData, Vector, Color, str and BaseMaterial
    if isinstance(value, ArnoldShaderLinkCustomData):
        shaderLinkData = value
    elif isinstance(value, c4d.Vector) or isinstance(value, maxon.Vector):
        shaderLinkData = ArnoldShaderLinkCustomData(ArnoldShaderLinkCustomData.TYPE_CONSTANT, value)
    elif isinstance(value, maxon.Color):
        shaderLinkData = ArnoldShaderLinkCustomData(ArnoldShaderLinkCustomData.TYPE_CONSTANT, c4d.Vector(value.r, value.g, value.b))
    elif isinstance(value, str):
        shaderLinkData = ArnoldShaderLinkCustomData(ArnoldShaderLinkCustomData.TYPE_TEXTURE, texture=value)
    elif isinstance(value, c4d.BaseMaterial):
        shaderLinkData = ArnoldShaderLinkCustomData(ArnoldShaderLinkCustomData.TYPE_MATERIAL, material=value)
    elif value is None:
        shaderLinkData = ArnoldShaderLinkCustomData()
    else:
        print("[WARNING] %s.%s: invalid shader link value, only ArnoldShaderLinkCustomData, Vector, Color, Filename, str or BaseMaterial is accepted" % (node.GetId(), paramId))
        return None

    # create a container to store the shader link attributes
    shaderLinkMainContainer = node[C4DAI_SHADERLINK_CONTAINER]
    if shaderLinkMainContainer is None:
        shaderLinkMainContainer = c4d.BaseContainer()

    shaderLinkContainer = shaderLinkMainContainer.GetContainer(paramId)
    if shaderLinkContainer is None:
        shaderLinkContainer = c4d.BaseContainer()

    # set the type
    shaderLinkContainer[C4DAI_SHADERLINK_TYPE] = shaderLinkData.type

    # set the color value
    if shaderLinkData.type == ArnoldShaderLinkCustomData.TYPE_CONSTANT:
        node[paramId] = shaderLinkData.value
        shaderLinkContainer[C4DAI_SHADERLINK_VALUE] = shaderLinkData.value
    # set the texture (Bitmap shader)
    elif shaderLinkData.type == ArnoldShaderLinkCustomData.TYPE_TEXTURE:
        shader = shaderLinkContainer.GetLink(C4DAI_SHADERLINK_TEXTURE)
        if shader is not None:
            shader.Remove()
        shader = c4d.BaseShader(c4d.Xbitmap)
        shader[c4d.BITMAPSHADER_FILENAME] = shaderLinkData.texture
        shader[C4DAI_GVC4DSHADER_BITMAP_COLOR_SPACE] = shaderLinkData.texture_color_space
        node.InsertShader(shader)
        shaderLinkContainer[C4DAI_SHADERLINK_TEXTURE] = shader
    # set the material link
    elif shaderLinkData.type == ArnoldShaderLinkCustomData.TYPE_MATERIAL:
        shaderLinkContainer[C4DAI_SHADERLINK_MATERIAL] = shaderLinkData.material

    # set the shader link to the node
    shaderLinkMainContainer.SetContainer(paramId, shaderLinkContainer)
    node[C4DAI_SHADERLINK_CONTAINER] = shaderLinkMainContainer

#=============================================
# Legacy Arnold Material implementation
#=============================================

class ArnoldLegacyMaterial:
    """
    A class used to represent a legacy Arnold Material.
    """

    def __init__(self, material):
        """
        Parameters
        ----------
        material : c4d.BaseMaterial
            The BaseMaterial instance from the C4D document.
        """
        self.material = material

    def Create(name):
        """
        Creates a new legacy Arnold Material.

        Parameters
        ----------
        name : str
            Name of the new material node.
        """
        material = c4d.BaseMaterial(ARNOLD_SHADER_NETWORK)
        if material is None:
            return None
        material.SetName(name)
        return ArnoldLegacyMaterial(material)

    def IsNodeBased(self):
        """
        Returns whether this is a Node Material or a legacy material.
        """
        return False

    def GetInPort(self, shader, portId):
        """
        Returns the input GvPort with the given id.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        portId : int
            Id of the input port.
        """
        for port in shader.GetInPorts():
            if port.GetMainID() == portId:
                return port
        return None
    
    def GetShaderId(self, shader):
        """
        Returns the Arnold node id of the given shader.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        """
        if shader is None:
            return None
     
        if shader.GetOperatorID() == ARNOLD_SHADER_GV:
            return shader.GetOpContainerInstance().GetInt32(C4DAI_GVSHADER_TYPE)
        if shader.GetOperatorID() == ARNOLD_C4D_SHADER_GV:
            c4dShaderId = shader.GetOpContainerInstance().GetInt32(C4DAI_GVC4DSHADER_TYPE)
            return C4DShaderIdMap.get(c4dShaderId, c4dShaderId)
        if shader.GetOperatorID() == ARNOLD_REFERENCE_GV:
            return C4DAIN_REFERENCE
        
        return ArnoldCustomShaderIdMap.get(shader.GetOperatorID(), shader.GetOperatorID())

    def GetShaderName(self, shader):
        """
        Returns the name of the given shader.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        """
        if shader is None:
            return None

        return shader.GetName()

    def GetPortName(self, shader, portId, isInput):
        """
        Returns the name of the given port.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        portId : int
            Id of the input port.
        isInput : boolean
            True if this is an input port.
        """
        if shader is None or portId is None:
            return None

        if isInput:
            port = self.GetInPort(shader, portId)
        else:
            port = shader.GetOutPort(portId)

        if port is None:
            return None
        return port.GetName(shader)

    def GetParamDataType(self, shader, paramId):
        """
        Returns the data type of the given shader parameter.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        paramId : int
            Id of the parameter.
        """
        if shader is None:
            return None

        description = shader.GetDescription(c4d.DESCFLAGS_DESC_NONE)
        for bc, param, groupid in description:
            if param[0].id == paramId:
                return param[0].dtype
        return None

    def GetShaderValue(self, shader, paramId):
        """
        Returns the value stored in the given shader parameter.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        paramId : int
            Id of the parameter.
        """
        if shader is None or paramId is None:
            return None

        # vcolor custom data type
        if self.GetParamDataType(shader, paramId) == ARNOLD_VCOLOR_DATATYPE_LEGACYID:
            return GetVColor(shader, paramId)

        # standard data type
        if shader.GetOperatorID() == ARNOLD_C4D_SHADER_GV:
            c4dShader = shader.GetFirstShader()
            if c4dShader is None:
                return None
            return c4dShader[paramId]
        
        return shader[paramId]

    def SetShaderValue(self, shader, paramId, value):
        """
        Sets the value stored in the given shader parameter.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        paramId : int
            Id of the parameter.
        value : [depends on the parameter]
            Parameter value.
        """
        if shader is None or paramId is None:
            return None

        # vcolor custom data type
        if self.GetParamDataType(shader, paramId) == ARNOLD_VCOLOR_DATATYPE_LEGACYID:
            return SetVColor(shader, paramId, value)

        # standard data type
        if shader.GetOperatorID() == ARNOLD_C4D_SHADER_GV:
            c4dShader = shader.GetFirstShader()
            if c4dShader is None:
                return None
            c4dShader[paramId] = value
        
        shader[paramId] = value

    def AlignShaders(self):
        """
        Aligns shaders in the Node Editor.
        """
        if self.material is None:
            return

        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_ALIGN_NODES)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)

    def QueryNetwork(self):
        """
        Queries the shader graph of the material.
        Returns a c4d.BaseContainer containing the shaders and connections.
        """
        if self.material is None:
            return

        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_QUERY_SHADER_NETWORK)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)
        return msg

    def GetShaders(self):
        """
        Returns the list of shaders (c4d.modules.graphview.GvNode)
        within this shader graph.
        """
        if self.material is None:
            return []

        shaders = []

        network = self.QueryNetwork()
        numShaders = network.GetInt32(C4DTOA_MSG_RESP1)
        for i in range(0, numShaders):
            shader = network.GetLink(10000+i)
            if shader is not None:
                shaders.append(shader)

        return shaders

    def GetConnections(self):
        """
        Returns the list of connections within this shader graph.
        A connection is a tuple of:
            source shader node : c4d.modules.graphview.GvNode
            source shader output port id : int
            target shader node : c4d.modules.graphview.GvNode
            target shader input port id : int
        """
        if self.material is None:
            return []

        connections = []

        network = self.QueryNetwork()
        numConnections = network.GetInt32(C4DTOA_MSG_RESP2)
        for i in range(0, numConnections):
            connection = network.GetContainer(20000+i)
            src = connection.GetLink(0)
            outPort = connection.GetInt32(1)
            dst = connection.GetLink(2)
            inPort = connection.GetInt32(3)
            connections.append((src, outPort, dst, inPort))

        return connections

    def GetRootShader(self, rootPortId):
        """
        Returns the shader (c4d.modules.graphview.GvNode)
        connected to given root port.

        Parameters
        ----------
        rootPortId : int or str
            The root port id.
        """
        if self.material is None:
            return None

        rootPortId = GetRootPortIntId(rootPortId)

        network = self.QueryNetwork()

        if rootPortId == ARNOLD_SHADER_PORT_ID:
            return network.GetLink(C4DTOA_MSG_RESP3)
        elif rootPortId == ARNOLD_DISPLACEMENT_PORT_ID:
            return network.GetLink(C4DTOA_MSG_RESP4)

        return None
    
    def GetShaderRoot(self):
        """
        Returns the shader (c4d.modules.graphview.GvNode)
        connected to 'shader' root port.
        """
        return self.GetRootShader(ARNOLD_SHADER_PORT_ID)

    def GetDisplacementRoot(self):
        """
        Returns the shader (c4d.modules.graphview.GvNode)
        connected to 'displacement' root port.
        """
        return self.GetRootShader(ARNOLD_DISPLACEMENT_PORT_ID)

    def AddShader(self, nodeId, name):
        """
        Adds a new shader to the graph.

        Parameters
        ----------
        nodeId : int
            The Arnold node id.
        name : str
            Name of the shader node.
        """
        if self.material is None:
            return None

        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_ADD_SHADER)
        msg.SetData(C4DTOA_MSG_PARAM2, nodeId)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)

        shader = msg.GetLink(C4DTOA_MSG_RESP1)
        if shader is not None:
            shader.SetName(name)

        return shader

    def RemoveShader(self, shader):
        """
        Removes the given shader from the graph.

        Parameters
        ----------
        shader : c4d.modules.graphview.GvNode
            The shader node.
        """
        if self.material is None:
            return None
        
        if shader is None:
            return None
        
        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_REMOVE_SHADER)
        msg.SetLink(C4DTOA_MSG_PARAM1, shader)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)

        return msg.GetBool(C4DTOA_MSG_RESP1)        

    def AddConnection(self, src, outPort, dst, inPort):
        """
        Connects the given shaders in the graph.

        Parameters
        ----------
        src : c4d.modules.graphview.GvNode
            The source shader node.
        outPort : int
            Output port id of the source shader node.
        dst : c4d.modules.graphview.GvNode
            The target shader node.
        inPort : int
            Input port id of the target shader node.
        """
        if self.material is None:
            return None

        if src is None or dst is None:
            return None

        if outPort is None or outPort == "":
            outPort = 0

        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_ADD_CONNECTION)
        msg.SetLink(C4DTOA_MSG_PARAM1, src)
        msg.SetData(C4DTOA_MSG_PARAM2, outPort)
        msg.SetLink(C4DTOA_MSG_PARAM3, dst)
        msg.SetData(C4DTOA_MSG_PARAM4, inPort)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)

        if msg.GetBool(C4DTOA_MSG_RESP1):
            return (src, outPort, dst, inPort)

        return None

    def RemoveConnection(self, dst, inPort):
        """
        Disconnects the given shader input.

        Parameters
        ----------
        dst : c4d.modules.graphview.GvNode
            The target shader node.
        inPort : int
            Input port id of the target shader node.
        """
        if self.material is None:
            return None
        
        if dst is None:
            return None
        
        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_REMOVE_CONNECTION)
        msg.SetLink(C4DTOA_MSG_PARAM1, dst)
        msg.SetData(C4DTOA_MSG_PARAM2, inPort)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)

        return msg.GetBool(C4DTOA_MSG_RESP1)
    
    def AddRootConnection(self, src, outPort, rootPortId):
        """
        Connects the given shader to the given root port.

        Parameters
        ----------
        src : c4d.modules.graphview.GvNode
            The source shader node.
        outPort : int
            Output port id of the source shader node.
        rootPortId : int or str
            The root port id.
        """
        if self.material is None:
            return None

        if src is None:
            return None

        if outPort is None or outPort == "":
            outPort = 0

        rootPortId = GetRootPortIntId(rootPortId)

        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_CONNECT_ROOT_SHADER)
        msg.SetLink(C4DTOA_MSG_PARAM1, src)
        msg.SetData(C4DTOA_MSG_PARAM2, outPort)
        msg.SetData(C4DTOA_MSG_PARAM3, rootPortId)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)

        return msg.GetBool(C4DTOA_MSG_RESP1)


    def RemoveRootConnection(self, rootPortId):
        """
        Disconnects the given root port.

        Parameters
        ----------
        rootPortId : int or str
            The root port id.
        """
        if self.material is None:
            return None
        
        rootPortId = GetRootPortIntId(rootPortId)
        
        msg = c4d.BaseContainer()
        msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_DISCONNECT_ROOT_SHADER )
        msg.SetInt32(C4DTOA_MSG_PARAM1, rootPortId)
        self.material.Message(c4d.MSG_BASECONTAINER, msg)

        return msg.GetBool(C4DTOA_MSG_RESP1)

#=============================================
# Arnold Node Material implementation
#=============================================

if node_material_available:

    import maxon
    import maxon.frameworks.nodespace
    import maxon.frameworks.nodes
    import maxon.frameworks.graph

    ARNOLD_NODESPACE = "com.autodesk.arnold.nodespace"
    ARNOLD_MATERIAL_END_NODE = "com.autodesk.arnold.material"
    ARNOLD_SHADER_PREFIX = "com.autodesk.arnold.shader."

    class ArnoldNodeMaterial:
        """
        A class used to represent an Arnold Node Material.
        """

        def __init__(self, material):
            """
            Parameters
            ----------
            material : c4d.BaseMaterial
                The BaseMaterial instance from the C4D document.
            """
            self.material = material
            self.graph = None

            if self.material is not None:
                nodeMaterial = self.material.GetNodeMaterialReference()
                self.graph = nodeMaterial.GetGraph(ARNOLD_NODESPACE)
                if self.graph is None:
                    print("[WARNING] Arnold node space is not found in Node Material: %s" % self.material.GetName())
                
        def Create(name):
            """
            Creates a new Arnold Node Material.

            Parameters
            ----------
            name : str
                Name of the new material node.
            """
            material = c4d.BaseMaterial(c4d.Mmaterial)
            if material is None:
                return None
            material.SetName(name)

            nodeMaterial = material.GetNodeMaterialReference()
            nodeMaterial.AddGraph(ARNOLD_NODESPACE)

            return ArnoldNodeMaterial(material)

        def IsNodeBased(self):
            """
            Returns whether this is a Node Material or a legacy material.
            """
            return True

        def IsPortValid(self, port):
            """
            Returns true if the given port is valid.
            """
            try:
                return port.IsValid()
            except Exception as e:
                return False

        def GetAssetId(self, shader):
            """
            Returns the asset id of the given shader.

            Parameters
            ----------
            shader : maxon.frameworks.graph.GraphNode
                The shader node.
            """
            # FIXME GetValue("net.maxon.node.attribute.assetid").GetFirst() returns an empty string
            return ("%r" % shader.GetValue("net.maxon.node.attribute.assetid"))[1:].split(",")[0]
        
        def GetShaderId(self, shader):
            """
            Returns the Arnold node id of the given shader.

            Parameters
            ----------
            shader : maxon.frameworks.graph.GraphNode
                The shader node.
            """
            if shader is None:
                return None
        
            assetId = self.GetAssetId(shader)
            if assetId.startswith(ARNOLD_SHADER_PREFIX):
                return assetId[len(ARNOLD_SHADER_PREFIX):]
        
            return ""
        
        def GetShaderName(self, shader):
            """
            Returns the name of the given shader.

            Parameters
            ----------
            shader : maxon.frameworks.graph.GraphNode
                The shader node.
            """
            if shader is None:
                return None

            return shader.GetValue("effectivename")

        def GetPortName(self, port):
            """
            Returns the name of the given port.

            Parameters
            ----------
            port : maxon.frameworks.graph.GraphNode
                The shader port.
            """
            if port is None:
                return None

            return shader.GetValue("effectivename")

        def GetParamDataType(self, shader, paramId):
            """
            Returns the data type id of the given port.

            Parameters
            ----------
            shader : maxon.frameworks.graph.GraphNode
                The shader node.
            paramId : int
                Id of the parameter.
            """
            if shader is None or paramId is None:
                return None

            port = shader.GetInputs().FindChild(paramId)
            if not self.IsPortValid(port):
                return None

            # FIXME port.GetValue("type") fails
            return port.GetDefaultValue().GetType().GetId()

        def GetShaderValue(self, shader, paramId):
            """
            Returns the value stored in the given shader parameter.

            Parameters
            ----------
            shader : maxon.frameworks.graph.GraphNode
                The shader node.
            paramId : int
                Id of the parameter.
            """
            if shader is None or paramId is None:
                return None

            # vcolor custom data type
            if self.GetParamDataType(shader, paramId) == ARNOLD_VCOLOR_DATATYPE:
                return GetVColor(shader, paramId)

            # standard data type
            port = shader.GetInputs().FindChild(paramId)
            if not self.IsPortValid(port):
                print("[WARNING] Input port '%s' is not found on shader '%r'" % (paramId, shader))
                return None

            return port.GetDefaultValue()

        def SetShaderValue(self, shader, paramId, value):
            """
            Sets the value stored in the given shader parameter.

            Parameters
            ----------
            shader : maxon.frameworks.graph.GraphNode
                The shader node.
            paramId : int
                Id of the parameter.
            value : [depends on the parameter]
                Parameter value.
            """
            if shader is None or paramId is None:
                return None

            # vcolor custom data type
            if self.GetParamDataType(shader, paramId) == ARNOLD_VCOLOR_DATATYPE:
                return SetVColor(shader, paramId, value)

            # standard data type
            port = shader.GetInputs().FindChild(paramId)
            if not self.IsPortValid(port):
                print("[WARNING] Input port '%s' is not found on shader '%r'" % (paramId, shader))
                return None
        
            port.SetDefaultValue(value)

        def _CollectShaders(self, node, shaders):
            """
            Private function to collect shaders from the graph.

            Parameters
            ----------
            node : maxon.frameworks.graph.GraphNode
                Graph node.
            shaders : list
                List of shaders.
            """
            if node.GetKind() != maxon.frameworks.graph.NODE_KIND.NODE:
                return

            if self.GetAssetId(node) == "net.maxon.node.group":
                for node in root.GetChildren():
                    self._CollectShaders(node, shaders)
                return

            shaders.append(node)

        def GetShaders(self):
            """
            Returns the list of shaders (maxon.frameworks.graph.GraphNode)
            within this shader graph.
            """
            if self.graph is None:
                return []

            shaders = []

            root = self.graph.GetRoot()
            for node in root.GetChildren():
                self._CollectShaders(node, shaders)

            return shaders

        def GetConnections(self):
            """
            Returns the list of connections within this shader graph.
            A connection is a tuple of:
                source shader node : maxon.frameworks.graph.GraphNode
                source shader output port id : str
                target shader node : maxon.frameworks.graph.GraphNode
                target shader input port id : str
            """
            if self.graph is None:
                return []

            connections = []

            for shader in self.GetShaders():
                for inPort in shader.GetInputs().GetChildren():
                    for c in inPort.GetConnections(maxon.frameworks.misc.PORT_DIR.INPUT):
                        outPort = c[0]
                        src = outPort.GetAncestor(maxon.frameworks.graph.NODE_KIND.NODE)
                        connections.append((src, outPort, shader, inPort))

            return connections

        def GetEndNode(self):
            """
            Returns the Arnold material end node.
            """
            if self.graph is None:
                return None

            for shader in self.GetShaders():
                if self.GetAssetId(shader) == ARNOLD_MATERIAL_END_NODE:
                    return shader

            return None

        def GetRootShader(self, rootPortId):
            """
            Returns the shader (maxon.frameworks.graph.GraphNode)
            connected to given root port.

            Parameters
            ----------
            rootPortId : int or str
                The root port id.
            """
            if self.graph is None:
                return None

            endNode = self.GetEndNode()
            if endNode is None:
                print("[WARNING] End node is not found in Node Material: %s" % self.material.GetName())
                return None

            rootPortId = GetRootPortStrId(rootPortId)

            root_port = endNode.GetInputs().FindChild(rootPortId)
            if root_port is None:
                print("[WARNING] End node port '%s'' is not found in Node Material: %s" % (rootPortId, self.material.GetName()))
                return None

            for c in root_port.GetConnections(maxon.frameworks.misc.PORT_DIR.INPUT):
                outPort = c[0]
                src = outPort.GetAncestor(maxon.frameworks.graph.NODE_KIND.NODE)
                return src

            return None

        def GetShaderRoot(self):
            """
            Returns the shader (maxon.frameworks.graph.GraphNode)
            connected to 'shader' root port.
            """
            return self.GetRootShader("shader")

        def GetDisplacementRoot(self):
            """
            Returns the shader (maxon.frameworks.graph.GraphNode)
            connected to 'displacement' root port.
            """
            return self.GetRootShader("displacement")

        def AddShader(self, nodeId, name):
            """
            Adds a new shader to the graph.

            Parameters
            ----------
            nodeId : str
                The Arnold node entry name.
            name : str
                Name of the shader node.
            """
            if self.graph is None:
                return None

            shader = self.graph.AddChild("", "com.autodesk.arnold.shader." + nodeId, maxon.DataDictionary())
            if shader is not None:
                shader.SetValue("effectivename", name)

            return shader

        def RemoveShader(self, shader):
            """
            Removes the given shader from the graph.

            Parameters
            ----------
            shader : maxon.frameworks.graph.GraphNode
                The shader node.
            """
            if self.graph is None:
                return

            if shader is None:
                return

            shader.Remove()

        def AddConnection(self, src, outPort, dst, inPort):
            """
            Connects the given shaders in the graph.

            Parameters
            ----------
            src : maxon.frameworks.graph.GraphNode
                The source shader node.
            outPort : str
                Output port id of the source shader node.
            dst : maxon.frameworks.graph.GraphNode
                The target shader node.
            inPort : str
                Input port id of the target shader node.
            """
            if self.graph is None:
                return None

            if src is None or dst is None:
                return None

            if outPort is None or outPort == "":
                outPort = "output"

            if isinstance(outPort, str):
                outPort_name = outPort
                outPort = src.GetOutputs().FindChild(outPort_name)
                if not self.IsPortValid(outPort):
                    print("[WARNING] Output port '%s' is not found on shader '%r'" % (outPort_name, src))
                    outPort = None

            if isinstance(inPort, str):
                inPort_name = inPort
                inPort = dst.GetInputs().FindChild(inPort_name)
                if not self.IsPortValid(inPort):
                    print("[WARNING] Input port '%s' is not found on shader '%r'" % (inPort_name, dst))
                    inPort = None

            if outPort is None or inPort is None:
                return None

            outPort.Connect(inPort)
            return (src, outPort, dst, inPort)

        def RemoveConnection(self, dst, inPort):
            """
            Disconnects the given shader input.

            Parameters
            ----------
            dst : maxon.frameworks.graph.GraphNode
                The target shader node.
            inPort : str
                Input port id of the target shader node.
            """
            if self.graph is None:
                return None

            if dst is None:
                return None

            if isinstance(inPort, str):
                inPort_name = inPort
                inPort = dst.GetInputs().FindChild(inPort_name)
                if not self.IsPortValid(inPort):
                    print("[WARNING] Input port '%s' is not found on shader '%r'" % (inPort_name, dst))
                    inPort = None

            if inPort is None:
                return None

            mask = maxon.frameworks.graph.Wires(maxon.frameworks.graph.WIRE_MODE.NORMAL)
            inPort.RemoveConnections(maxon.frameworks.misc.PORT_DIR.INPUT, mask)
        
        def AddRootConnection(self, src, outPort, rootPortId):
            """
            Connects the given shader to the given root port.

            Parameters
            ----------
            src : maxon.frameworks.graph.GraphNode
                The source shader node.
            outPort : str
                Output port id of the source shader node.
            rootPortId : int or str
                The root port id.
            """
            endNode = self.GetEndNode()
            rootPortId = GetRootPortStrId(rootPortId)
            return self.AddConnection(src, outPort, endNode, rootPortId) is not None
    
        def RemoveRootConnection(self, rootPortId):
            """
            Disconnects the given root port.

            Parameters
            ----------
            rootPortId : int or str
                The root port id.
            """
            endNode = self.GetEndNode()
            rootPortId = GetRootPortStrId(rootPortId)
            self.RemoveConnection(endNode, rootPortId)

    class ArnoldMaterialTransaction:
        """
        A class used to represent a transaction in an Arnold Node Material.
        Use it in a with statement.
        """

        def __init__(self, arnoldMaterial):
            self.arnoldMaterial = arnoldMaterial
            self.transaction = None

        def __enter__(self):
            if self.arnoldMaterial is not None and self.arnoldMaterial.graph is not None:
                self.transaction = self.arnoldMaterial.graph.BeginTransaction()
            return self

        def __exit__(self, type, value, traceback):
            if self.transaction is not None:
                self.transaction.Commit()

#=============================================
# Generic Arnold Material implementation
#=============================================

# map between integer and string root port ids
ArnoldMaterialRootPortMap = {
    "shader": ARNOLD_SHADER_PORT_ID,
    "displacement": ARNOLD_DISPLACEMENT_PORT_ID,
    "viewport": ARNOLD_VIEWPORT_PORT_ID,
}

def GetRootPortStrId(rootPortId):
    """
    Converts the given integer root port id to a string id.
    """
    if isinstance(rootPortId, int):
        for strId, intId in ArnoldMaterialRootPortMap.items():
            if intId == rootPortId:
                return strId
    return rootPortId

def GetRootPortIntId(rootPortId):
    """
    Converts the given string root port id to an integer id.
    """
    if isinstance(rootPortId, str):
        return ArnoldMaterialRootPortMap.get(rootPortId, 0)
    return rootPortId

def ArnoldMaterial(material):
    """
    Creates an Arnold Material instance based on the type of the given BaseMaterial.

    Parameters
    ----------
    material : c4d.BaseMaterial
        BaseMaterial instance from the C4D document.
    """
    if material is None:
        return None

    if node_material_available and material.IsNodeBased():
        return ArnoldNodeMaterial(material)
    elif material.GetType() == ARNOLD_SHADER_NETWORK:
        return ArnoldLegacyMaterial(material)

    print("[WARNING] Material '%s' is not an Arnold Material" % material.GetName())
    return None

def ConvertLegacyArnoldMaterial(arnoldMaterial, copy = True):
    """
    Converts the given legacy Arnold Material to a Node Material.

    Parameters
    ----------
    arnoldMaterial : ArnoldLegacyMaterial
        Legacy Arnold Material node.
    copy : boolean
        If true, the Node Material is created next to the original material (copy & convert).
        If false, the Node Material replaces the original material.
    """
    if arnoldMaterial is None or arnoldMaterial.material is None:
        return

    material = arnoldMaterial.material
    if material.GetType() != ARNOLD_SHADER_NETWORK:
        return

    nextBeforeConvert = material.GetNext()

    # select the material
    doc = c4d.documents.GetActiveDocument()
    doc.SetActiveMaterial(material)
    # run the conversion
    if copy:
        c4d.CallCommand(1058943)
    else:
        c4d.CallCommand(1058942)

    # check if the conversion succeeded
    if material.GetNext() == nextBeforeConvert:
        raise Exception("Failed to convert legacy Arnold Material '%s'" % material.GetName())

    # return the Node Material
    return ArnoldMaterial(material.GetNext())

# 创建Standard Surface
def CreateStandardSurface(name):
    """
    Creates a new Arnold Starndard Surface Material with a NAME.

    Args:
        name (str): Name of the Material

    Returns:
        Material: Arnold Material instance
    """    
    arnoldMaterial = ArnoldNodeMaterial.Create(name)
    if arnoldMaterial is None or arnoldMaterial.material is None:
        raise Exception("Failed to create Arnold Standard Surface Material")

    with ArnoldMaterialTransaction(arnoldMaterial) as transaction:
        standard_surface = arnoldMaterial.AddShader("standard_surface", "Standard_Surface")
        arnoldMaterial.AddRootConnection(standard_surface, None, "shader")
        
        # specular color white
        # NOTE color is in linear sRGB space       
        arnoldMaterial.SetShaderValue(standard_surface, "specular_color", maxon.Color(1.0, 1.0, 1.0))
        # set standard surface specular roughness
        arnoldMaterial.SetShaderValue(standard_surface, "specular_roughness", 0.2)
        
    return arnoldMaterial.material

def ExposeUsefulPorts(material : c4d.BaseMaterial):
    #doc = c4d.documents.GetActiveDocument()
    #c4d.CallCommand(300001026) # Deselect All
    #c4d.CallCommand(1038508) # standard_surface 


    # Retrieve the graph of the current NodeSpace
    nodespaceId = c4d.GetActiveNodeSpaceId()
    nimbusRef = material.GetNimbusRef(nodespaceId)
    if nimbusRef is None:
        raise ValueError("can't retrieve the nimbus ref for that node space")
    graph = nimbusRef.GetGraph()
    if graph is None:
        raise ValueError("can't retrieve the graph of this nimbus ref")
    
    # expose port callback
    def ExposeHidePorts(node):
        specular_color = node.GetInputs().FindChild("specular_color")
        specular_roughness = node.GetInputs().FindChild("specular_roughness")
        specular_IOR = node.GetInputs().FindChild("specular_IOR")
        transmission = node.GetInputs().FindChild("transmission")
        transmission_color = node.GetInputs().FindChild("transmission_color")
        emission = node.GetInputs().FindChild("emission")
        emission_color = node.GetInputs().FindChild("emission_color")
        normal = node.GetInputs().FindChild("normal")
        # Display the port in the node editor
        with graph.BeginTransaction() as tr:
            specular_color.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            specular_roughness.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            specular_IOR.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            transmission.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            transmission_color.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            emission.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            emission_color.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            normal.SetValue(maxon.NODE.ATTRIBUTE.HIDEPORTINNODEGRAPH, maxon.Bool(False))
            tr.Commit()
        return True
    # Do Expose defined ports on standard_surface
    maxon.GraphModelHelper.FindNodesByAssetId(graph, "com.autodesk.arnold.shader.standard_surface", False, ExposeHidePorts)
    c4d.EventAdd()
    return material
