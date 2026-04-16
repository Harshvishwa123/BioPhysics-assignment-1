from modeller import *
from modeller.automodel import *

env = Environ()
a = AutoModel(env, alnfile='cas9-mult-mutant.ali',
              knowns=('7S37_PP','6IFO_AA','5F9R_BB'), sequence='spcas9_mut')
a.starting_model = 1
a.ending_model = 3
a.make()