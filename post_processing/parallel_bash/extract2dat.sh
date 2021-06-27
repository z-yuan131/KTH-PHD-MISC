#!/bin/bash
# mkdir walldatFiles
# mkdir datFiles

# NekMesh -m extract:surf=1,2,3,4 ../run/mesh.xml bnd_wall.xml


for i in {641..1606}  #{27..107}

do
        FieldConvert ../run/mesh.xml ../run/naca0012.xml ../solution/mesh_$i.chk mesh_$i.fld
        FieldConvert -m interpfield:fromxml=../run/mesh.xml:fromfld=mesh_$i.fld bnd_wall.xml bnd_wall_$i.fld
        FieldConvert bnd_wall.xml bnd_wall_$i.fld bnd_wall_$i.dat

        FieldConvert ../run/mesh.xml ../run/naca0012.xml ../solution/mesh_$i.chk $i.dat

        rm *.fld
done



mv bnd_wall_* walldatFiles
mv *.dat datFiles


