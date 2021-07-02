import numpy as np
import vtk
import vtk.util.numpy_support as ns
from sys import argv


def load_vtkFile(file_name):
    # The source file
    # file_name = "./vtu/"+str(time)+".vtu"   #debug usage
    
    # Read the source file.
    reader = vtk.vtkXMLUnstructuredGridReader()   # read the fucking file
    reader.SetFileName(file_name)
    reader.Update()                               # Needed because of GetScalarRange
    output = reader.GetOutput()
    
    # these three lines can read the varible names in the vtu file
    #n_arrays = reader.GetNumberOfPointArrays()
    #for i in range(n_arrays):
    #    print(reader.GetPointArrayName(i))

    # store the varible data into pd
    pd = output.GetPointData()
    p_t = pd.GetArray('Pressure')
    u_t = pd.GetArray('Velocity')
    rho_t = pd.GetArray('Density')

    # using vtk numpy support tool to convert to numpy array
    p = ns.vtk_to_numpy(p_t)
    u = ns.vtk_to_numpy(u_t)
    rho = ns.vtk_to_numpy(rho_t)
    
    # u.shape = [:][2] u.T.shape = [2][:], easier to return: u[0] = u, u[1] = v, etc...
    u = u.T
    
    return p,u[0],u[1],rho

def load_coordinate(file_name):
    # The source file
    # file_name = "./vtu/"+str(time)+".vtu"   #debug usage
    
    # Read the source file.
    reader = vtk.vtkXMLUnstructuredGridReader()   # read the fucking file
    reader.SetFileName(file_name)
    reader.Update()                               # Needed because of GetScalarRange

    # this line can get the coordinate data stored in vtk files, please notice the difference
    Point_cordinates = reader.GetOutput().GetPoints().GetData()
    
    numpy_coordinates = ns.vtk_to_numpy(Point_cordinates)
    numpy_coordinates = numpy_coordinates.T     #transpose: x = numpy_coordinates[0], y = numpy_coordinates[1] etc..
    
    return numpy_coordinates[0],numpy_coordinates[1]
