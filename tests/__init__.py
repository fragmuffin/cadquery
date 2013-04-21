from cadquery import *
import unittest
import sys
FREECAD_LIB = "c:/apps/FreeCAD0.12/bin";
sys.path.append(FREECAD_LIB);
import FreeCAD

P = FreeCAD.Part
V = FreeCAD.Base.Vector

def readFileAsString(fileName):
    f= open(fileName,'r')
    s = f.read()
    f.close()
    return s

def writeStringToFile(strToWrite,fileName):
    f = open(fileName,'w')
    f.write(strToWrite)
    f.close()
	

def makeUnitSquareWire():
    return Solid.cast(P.makePolygon([V(0,0,0),V(1,0,0),V(1,1,0),V(0,1,0),V(0,0,0)]))

def makeUnitCube():
    return makeCube(1.0)

def makeCube(size):
    return Solid.makeBox(size,size,size)

def toTuple(v):
    "convert a vector or a vertex to a 3-tuple: x,y,z"
    pnt = v
    if type(v) == FreeCAD.Base.Vector:
        return (v.Point.x,v.Point.y,v.Point.z)
    elif type(v) == Vector:
        return v.toTuple()
    else:
        raise RuntimeError("dont know how to convert type %s to tuple" % str(type(v)) )


class BaseTest(unittest.TestCase):

    def assertTupleAlmostEquals(self,expected,actual,places):
        for i,j in zip(actual,expected):
            self.assertAlmostEquals(i,j,places)

__all__ = [ 'TestCadObjects','TestCadQuery','TestCQSelectors','TestWorkplanes','TestExporters','TestCQSelectors']
