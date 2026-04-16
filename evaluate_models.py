from modeller import *
from modeller.scripts import complete_pdb

log.verbose()
env = Environ()

env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

# List all models
models = [
    "spcas9_wt.B99990001.pdb",
    "spcas9_wt.B99990002.pdb",
    "spcas9_wt.B99990003.pdb",
    "spcas9_mut.B99990001.pdb",
    "spcas9_mut.B99990002.pdb",
    "spcas9_mut.B99990003.pdb"
]

print("\nDOPE SCORES\n")

for pdb in models:
    mdl = complete_pdb(env, pdb)
    s = Selection(mdl)

    score = s.assess_dope()

    print(pdb, "DOPE score:", score)