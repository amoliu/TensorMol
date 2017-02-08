from TensorMol import *
import cProfile

# John's tests
if (1):
	# To read gdb9 xyz files and populate an Mset.
	# Because we use pickle to save. if you write new routines on Mol you need to re-execute this.
	if (0):
		a=MSet("gdb9")
		a.ReadGDB9Unpacked("/home/kyao/TensorMol/gdb9/")
		allowed_eles=[1, 6, 7, 8]
		a.CutSet(allowed_eles)
		a.Make_Graphs()
		a.Save()
	if (0):
                # 1 - Get molecules into memory
                a=MSet("gdb9_1_6_7_8")
                a.Load()
                a.Bonds_Between_All()
		a.Save()

	# To generate training data for all the atoms in the GDB 9
	if (0):
		# 1 - Get molecules into memory
		a=MSet("gdb9_1_6_7_8")
		a.Load()
		TreatedAtoms = a.AtomTypes()
		print "TreatedAtoms ", TreatedAtoms
		d = MolDigester(TreatedAtoms, name_="GauInv_BP", OType_="Atomization")  # Initialize a digester that apply descriptor for the fragments.
		tset = TensorMolData_BP(a,d, order_=1, num_indis_=1, type_="mol") # Initialize TensorMolData that contain the training data for the neural network for certain order of many-body expansion.
		tset.BuildTrain("gdb9_1_6_7_8")

	if (0):
		tset = TensorMolData_BP(MSet(),MolDigester([]),"gdb9_1_6_7_8_Coulomb_BP")
		manager=TFMolManage("",tset,False,"fc_sqdiff_BP") # Initialzie a manager than manage the training of neural network.
		manager.Train(maxstep=3)  # train the neural network for 500 steps, by default it trainse 10000 steps and saved in ./networks.

        # To generate training data for all the atoms in the GDB 9
        if (0):
                # 1 - Get molecules into memory
                a=MSet("gdb9_1_6_7_8")
                a.Load()
                TreatedAtoms = a.AtomTypes()
                d = MolDigester(TreatedAtoms, name_="Coulomb_Bond_BP", OType_="Atomization", bonds_=TreatedBonds)  # Initialize a digester that apply descriptor for the fragments.
                tset = TensorMolData_Bond_BP(a,d, order_=1, num_indis_=1, type_="mol") # Initialize TensorMolData that contain the training data for the neural network for certain order of many-body expansion.
                tset.BuildTrain("gdb9_1_6_7_8")

        if (0):
                tset = TensorMolData_BP(MSet(),MolDigester([]),"gdb9_1_6_7_8_Coulomb_Bond_BP")
                manager=TFMolManage("",tset,False,"fc_sqdiff_BP") # Initialzie a manager than manage the training of neural network.
                manager.Train(maxstep=200)  # train the neural network for 500 steps, by default it trainse 10000 steps and saved in ./networks.


	if (0):
		manager= TFMolManage("Mol_gdb9_1_6_7_8_Coulomb_Bond_BP_fc_sqdiff_BP_1" , None, False)
		manager.Test()


	# To generate training data for all the atoms in the GDB 9
        if (0):
                # 1 - Get molecules into memory
                a=MSet("gdb9_1_6_7_8")
                a.Load()
                TreatedAtoms = a.AtomTypes()
                print "TreatedAtoms ", TreatedAtoms
                TreatedBonds = list(a.BondTypes())
                print "TreatedBonds ", TreatedBonds
                d = MolDigester(TreatedAtoms, name_="ConnectedBond_Bond_BP", OType_="Atomization")  # Initialize a digester that apply descriptor for the fragments.
                tset = TensorMolData_Bond_BP(a,d, order_=1, num_indis_=1, type_="mol") # Initialize TensorMolData that contain the training data for the neural network for certain order of many-body expansion.
                tset.BuildTrain("gdb9_1_6_7_8")
	
	if (1):
                tset = TensorMolData_BP(MSet(),MolDigester([]),"gdb9_1_6_7_8_ConnectedBond_Bond_BP")
                manager=TFMolManage("",tset,False,"fc_sqdiff_BP") # Initialzie a manager than manage the training of neural network.
                cProfile.run('manager.Train(maxstep=200)')  # train the neural network for 500 steps, by default it trainse 10000 steps and saved in ./networks.

	if (0):
                manager= TFMolManage("Mol_gdb9_1_6_7_8_Dist_Bond_BP_fc_sqdiff_BP_1" , None, False)
                manager.Test()	

# Kun's tests.
if (0):
	if (0):
		a=MSet("C2H6")
		#a.ReadXYZ("CxHy_test")
		a.ReadGDB9Unpacked("./C2H6/")
		#a.Save()
	#	a=MSet("gdb9_NEQ")
	#	a.Load()
		#b=MSet("gdb9")
		#b.Load()
		#allowed_eles=[1, 6]
		#b.CutSet(allowed_eles)
		#print "length of bmols:", len(b.mols)
		a = a.DistortedClone(100000)
		a.Save()

	if (0):
		#a=MSet("CxHy_test_NEQ")
		#a.Load()
		a=MSet("gdb9_1_6_NEQ")
	  	#a=a.DistortedClone(1)	
		a.Load()	
		# Choose allowed atoms.
		TreatedAtoms = a.AtomTypes()
		#for mol in a.mols:
		#	mol.BuildDistanceMatrix()
		# 2 - Choose Digester
		#d = Digester(TreatedAtoms, name_="SymFunc",OType_ ="Force")
		#d.TrainDigestW(a.mols[0], 6)
		print "len of amols", len(a.mols)
		d = Digester(TreatedAtoms, name_="PGaussian",OType_ ="GoForce_old_version", SamplingType_="None")
		#d.Emb(a.mols[0],0, np.zeros((1,3)))
		#d.Emb(a.mols[0],0, a.mols[0].coords[0].reshape(1,-1))
		#4 - Generate training set samples.

	if (0):
		tset = TensorData(a,d)
		tset.BuildTrain("gdb9_1_6_NEQ",TreatedAtoms) # generates dataset numpy arrays for each atom.

	if (1):
		tset = TensorData(MSet(),Digester([]),"gdb9_1_6_NEQ_PGaussian")
		#tset_test = TensorData(MSet(),Digester([]),"CxHy_test_SymFunc") 
		#manager=TFManage("",tset,False,"fc_sqdiff", tset_test) # True indicates train all atoms.
		manager=TFManage("",tset,False,"fc_sqdiff")
		manager.TrainElement(6)
		#tset = TensorData(MSet(),Digester([]),"gdb9_1_6_NEQ_SymFunc")
		#manager = TFManage("", tset , True)
	

