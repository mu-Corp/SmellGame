#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
from collections import defaultdict
import random

from SmellGuess.models   import *
from SmellGift.models    import *
from fctMaths         import *
from fctBoxPlot       import *
from fctGetDataHisto  import *
from fctGetDataPie    import *

################################################################
#####################   FCT PieGraphs   ########################
################################################################


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
