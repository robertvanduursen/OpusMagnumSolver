""" branched version of the OpusMagnum Solver """
import math

class glyph_dispenser(object):
	def __init__(self): pass

	def glBonding(atom1,atom2):
		'''Creates a bond between two atoms, after which they will move as a group '''
		cost = 10
		area = 2
		form = 'bar'
		if atom1.molecule:
			# append to current
			pass
		else:
			# make new one
			mol = Molecule()


	def glMultiBonding():
		'''can create up to 3 bonds at once'''
		cost = 30
		area = 4
		form = '3 star'
	def glTriplexBonding():
		'''A single arm and gripper'''
		cost = 20
		area = 3
		form = 'triangle'
	def glUnbonding():
		'''eliminates the bond between 2 atoms'''
		cost = 10
		area = 2
		form = 'bar'
	def glCalcification():
		'''transmutes any of the 4 cardinal elements into neutral salt'''
		transmutes = {
			'earth':'salt',
			'water':'salt',
			'fire':'salt',
			'air':'salt',
		}
		cost = 10
		area = 1
		form = 'dot'
	def glDuplication():
		'''transmutes a salt atom into 1 of 4 cardinals by imbuing it with the essence of an existing atom '''
		transmutes = {
			'salt':'vitae',
			'salt':'mors',
		}
		cost = 20
		area = 2
		form = 'bar'
	def glProjection():
		'''consumes an atom of quicksilver and promotes an atom of metal to its next higher form'''
		#'lead':'quicksilver'
		transmutes = {
			# steps, like connections in a graph, this also lists valid paths
			'lead':'tin',
			'tin':'iron',
			'iron':'copper',
			'copper':'silver',
			'silver':'gold',
			}
		cost = 20
		area = 2
		form = 'bar'
	def glPurification():
		'''transmutes 2 atoms of the same metal into a single atom of their next higher form'''
		cost = 20
		area = 3
		form = 'triangle'
	def glAnimismus():
		'''A single arm and gripper'''
		cost = 20
		area = 4
		form = 'diamond'
	def glUnification():
		'''A single arm and gripper'''
		cost = 20
		area = 5
		form = 'zigzag'
	def glDispersion():
		'''A single arm and gripper'''
		cost = 20
		area = 5
		form = 'half moon'
	def glDisposal():
		'''removes unneeded atoms from the board'''
		cost = 0
		area = 7
		form = '6 star'
	def glEquilibrium():
		'''A single arm and gripper'''
		cost = 0
		area = 1
		form = 'dot'

glyphs = {
	'Glyph of Bonding':glyph_dispenser.glBonding,
	'Glyph of Multi-Bonding':glyph_dispenser.glMultiBonding,
	'Glyph of Triplex-Bonding':glyph_dispenser.glTriplexBonding,
	'Glyph of Unbonding':glyph_dispenser.glUnbonding,
	'Glyph of Calcification':glyph_dispenser.glCalcification,
	'Glyph of Duplication':glyph_dispenser.glDuplication,
	'Glyph of Projection':glyph_dispenser.glProjection,
	'Glyph of Purification':glyph_dispenser.glPurification,
	'Glyph of Animismus':glyph_dispenser.glAnimismus,
	'Glyph of Unification':glyph_dispenser.glUnification,
	'Glyph of Dispersion':glyph_dispenser.glDispersion,
	'Glyph of Disposal':glyph_dispenser.glDisposal,
	'Glyph of Equilibrium':glyph_dispenser.glEquilibrium,
}

""" MECHANISMS ###########################################################################################################"""
class mech_dispenser(object):
	def __init__(self): pass

	def FixedArm_1():
		'''A single arm and gripper'''
		cost = 20
	def FixedArm_2():
		'''An assembly with two arms and two grippers'''
		cost = 30
	def FixedArm_3():
		'''An assembly with three arms and three grippers'''
		cost = 30
	def FixedArm_6():
		'''An assembly with six arms and six grippers'''
		cost = 30
	def PistonArm():
		'''A single arm and gripper that can extend and retract'''
		cost = 40
	def Track():
		'''Arms can be placed on tracks and instructed to move along them'''
		cost = 5
	def VanBerloWheel():
		'''By using van Berlo's wheel with the glyph of
		duplication, salt can be turned into any of the
		four cardinal elements  '''
		cost = 30

mechanisms = {
	'Fixed-length arm1':mech_dispenser.FixedArm_1,
	'Fixed-length arm2':mech_dispenser.FixedArm_2,
	'Fixed-length arm3':mech_dispenser.FixedArm_3,
	'Fixed-length arm6':mech_dispenser.FixedArm_6,
	'Piston Arm':mech_dispenser.PistonArm,
	'Track':mech_dispenser.Track,
	'Van Berlo\'s Wheel':mech_dispenser.VanBerloWheel,
}

""" MOVES ###########################################################################################################"""
class move_dispenser(object):
	def __init__(self): pass

	def grabber_drop():
		'''releases on to atoms '''
		key='r'

	def grabber_grab():
		'''locks on to atoms '''
		key='f'

	def piston_extend():
		'''extends an arm'''
		key='w'

	def piston_retract():
		''' retracts an arm'''
		key='s'

	def pivot_ccw():
		''' rotates the molecule around the grippers axis for 1/6th to the right'''
		key='q'

	def pivot_cw():
		'''rotates the molecule around the grippers axis for 1/6th to the left'''
		key='e'

	def rotator_ccw():
		'''rotates the arm around its baxis for 1/6th to the right'''
		key='a'

	def rotator_cw():
		'''rotates the arm around its baxis for 1/6th to the left'''
		key='d'

	def track_advance():
		''' moves the arm along the track towards the + symbol '''
		key='g'

	def track_retreat():
		''' moves the arm along the track towards the - symbol '''
		key='t'

	def repeat():
		''' adds a series of steps to repeat all previous moves '''
		key='v'

	def reset():
		'''adds a series of step to put the arm back at its original transform'''
		key='c'

	def clock():
		'''
		when starting the transmutation engine, all instructions are automatically padded
		so they have the same as the longest instruction sequence in the solution, 
		which ensures that all arms are kept in sync.

		1 can exist at any given time

		'''
		key = 'q'

moves = {
	'clock':move_dispenser.clock,
	'grabber_drop':move_dispenser.grabber_drop,
	'grabber_grab':move_dispenser.grabber_grab,
	'piston_extend':move_dispenser.piston_extend,
	'piston_retract':move_dispenser.piston_retract,
	'pivot_ccw':move_dispenser.pivot_ccw,
	'pivot_cw':move_dispenser.pivot_cw,
	'repeat':move_dispenser.repeat,
	'reset':move_dispenser.reset,
	'rotator_ccw':move_dispenser.rotator_ccw,
	'rotator_cw':move_dispenser.rotator_cw,
	'track_advance':move_dispenser.track_advance,
	'track_retreat':move_dispenser.track_retreat,
}

""" ENTRIES ###########################################################################################################"""
prime = {
	'air':False,
	'fire':False,
	'salt':False,
	'water':False,
	'earth':False,
	'mors':False,
	'vitae':False,

	'lead':False,
	'quicksilver':False,
	'tin':False,
	'iron':False,
	'copper':False,
	'silver':False,
	'gold':False,

	'omni':False,
}


""" MANAGERS ###########################################################################################################"""

class Molecule(object):
	'''every atom has a molecule, but a molecule can consist of multiple atoms with bonds '''
	areaCovered = False # a series of positions
	atoms = False
	bonds = False
	def __init__(self,type=False):
		self.atoms = []
		self.links = []

	def __add__(Mol_A,Mol_B):
		return Mol_A

	def __sub__(Mol_A,Mol_B):
		return Mol_A

class TransmutationEngine(object):
	molecules = []
	mechanisms = []
	histogram = [] # the musical score
	def __init__(self):
		self.atoms = []
		self.links = []

		self.glypher = glyph_dispenser()
		self.mover = move_dispenser()
		self.mechanismer = mech_dispenser()


TE = TransmutationEngine()

