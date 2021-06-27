#!/bin/bash
# mkdir walldatFiles
# mkdir datFiles

# NekMesh -m extract:surf=1,2,3,4 ../run/mesh.xml bnd_wall.xml


for i in {6..256}  #{6..1606}

do
        FieldConvert ../run/mesh.xml ../run/naca0012.xml ../solution/mesh_$i.chk $i.vtu &
done
date
echo Now following jobs are running:
jobs
wait
date

mv *.vtu vtuFiles
