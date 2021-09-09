import ase.build
import ase.io
import os
from ase.calculators.gulp import GULP, Conditions
pos=ase.io.read('data.si',format='lammps-data',style='atomic')
pos.set_chemical_symbols('Si8')
ase.io.write('data.vasp',pos,format='vasp',vasp5=True)
#GULP
#evaluate thermal conductivity using AF for all modes
c = Conditions(pos)
calc = GULP(keywords='isotropic conv opti prop phonon thermal',
                options=['output xyz gulp.xyz',
                         'broaden scale 5.0',
                         'omega_af rads 0.0 2.76 3615.0',
                         'temperature 300',
                         'species   1',
                         'Si     core    0.000000  '],
                library='stillinger_weber', conditions=c, atoms=pos)
opt = calc.get_optimizer(pos)
calc.atoms=pos
calc.write_input(pos)