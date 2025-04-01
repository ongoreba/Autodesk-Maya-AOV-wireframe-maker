import maya.cmds as cmds
import mtoa.aovs
import mtoa.ui.aoveditor
#This script will create a wireframe AOV node
#If you plug the rendered image into a post-processing
#software, it will spit out the information of all the AOVs

#We are gonna access the AOV making script in Maya
#You can also find it in this path:
#C:\Program Files\Autodesk\Arnold\maya2025\scripts\mtoa\aovs

#Call the Driver node for the AOV we are about to create
interface=mtoa.aovs.AOVInterface()
#Create the wireframe AOV
aov=interface.addAOV("wireframe",aovType="rgba")
#Check
print(aov)
print(aov.destAttr)
print(aov.node)
#Create a new aiWireframe node
newWireframe = cmds.createNode('aiWireframe')   
#Set the type to quad
cmds.setAttr(newWireframe+".edgeType", 1)
#Set the line size to 2
cmds.setAttr(newWireframe+".lineWidth", 2)
#Connect the wireframe shader to the AOV node
cmds.connectAttr(
newWireframe+".outColor", 
aov.node+".defaultValue")


#update= mtoa.ui.aoveditor.createArnoldAOVTab()
