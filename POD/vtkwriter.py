
# this routine is designed for writing fluid file to vtk format

import vtk
from vtk.numpy_interface import dataset_adapter as dsa

def yzywriter(input_file_name,append_data,append_data_name,length):

    reader = vtk.vtkXMLUnstructuredGridReader()
    reader.SetFileName(input_file_name)
    #reader.ReadAllVectorsOn()
    #reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()   # set the data file that new data need to append to

    """
    calc = vtk.vtkArrayCalculator()
    calc.SetInputData(data)

    calc.SetFunction("5")
    calc.SetResultArrayName("MyResults")
    calc.Update()"""

    dataNew = dsa.WrapDataObject(data)  # dsa magic

    for i in range(length):
        
        dataNew.PointData.append(append_data[:,i], append_data_name[i])   #append new data

    print('Writing...')

    writer = vtk.vtkXMLUnstructuredGridWriter()   #write to vtu file in xml format
    #writer = vtk.vtkUnstructuredGridWriter()   #write to vtu file in legency format
    writer.SetInputData(dataNew.VTKObject)
    writer.SetFileName("VTKWriterOutput.vtu")
    writer.Write()
    print('Done!')
