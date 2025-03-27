import maya.cmds as cmds

def wireframeAOV():
    #Create the wireframe shader for Arnold renderer
    if cmds.objExists("defaultArnoldRenderOptions"):
        #Create a new aiAOV node
        newAOV = cmds.createNode('aiAOV')
        #Set AOV's AOV Attribute name
        cmds.setAttr(newAOV+".name","wireframe", type="string")
        #Rename AOV node
        renamedAOV = cmds.rename(newAOV, "aiAOV_wireframe")
        
        #Create a new aiWireframe node
        newWireframe = cmds.createNode('aiWireframe')   
        #Set the type to quad
        cmds.setAttr(newWireframe+".edgeType", 1)
        #Set the line size to 2
        cmds.setAttr(newWireframe+".lineWidth", 2)
        
        #Connect the wireframe shader to the AOV node
        cmds.connectAttr(
        newWireframe+".outColor", 
        renamedAOV+".defaultValue")
        #Connect AOV to the arnold shader
        cmds.connectAttr(
        renamedAOV+".message", 
        "defaultArnoldRenderOptions.aovList", 
        nextAvailable=True)
    else:
        cmds.warning("Arnold shader is not enabled")

wireframeAOV()