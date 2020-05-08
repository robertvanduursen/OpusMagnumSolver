from RulesAndActions import *

#todo: how to express for 'glCalcification': I can do this for Tin, but I need X,Y,Z

class glPrime(Glyph):
    name = 'Atom Prime'
    description = 'The regular dispenser '
    cost = 10
    area = 1
    form = 'dot'
    features = [Dispensing]

    def activate(self, atom1):
        self.dispense(atom1)

    @staticmethod
    def dispense(atom):
        mol = Molecule(atom)
        if mol:
            return mol
        return False

class glBonding(Glyph):
    name = 'Glyph of Bonding'
    description = 'Creates a bond between two atoms, after which they will move as a group'
    cost = 10
    area = 2
    form = 'bar'
    features = [Bonding]

    def activate(self, *args):
        atom1, atom2 = args[0], args[1]
        process = Bonding(atom1, atom2)
        return process.result

    @staticmethod
    def bond(*args):
        atom1, atom2 = args[0], args[1]
        bondedMolecule = Molecule()
        bondedMolecule += atom1
        bondedMolecule += atom2
        return bondedMolecule

class glMultiBonding(Glyph):
    name = 'Glyph of Multi-Bonding'
    description = '''can create up to 3 bonds at once'''
    cost = 30
    area = 4
    form = '3 star'
    features = [Bonding]

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

    @staticmethod
    def bond(*args):
        bondedMolecule = Molecule(args[0])
        return bondedMolecule

class glTriplexBonding(Glyph):
    name = 'Glyph of Triplex-Bonding'
    description = '''The Glyph of Triplex-bonding is a complex Glyph with a very specific usage.
    #It occupies a triangular are of 3 hexes, each of which acts purely on Fire atoms. 
    Each of the three pairs of hexes within the Glyph form a separate bond, in the manner of other bonding Glyphs. 
    These individual bonds are not valid for final products; when all three bonds are present between two atoms, they are considered to be Triplex Bonded.'''
    cost = 20
    area = 3
    form = 'triangle'
    features = [Bonding]

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

    @staticmethod
    def bond(*args):
        #print('Glyph of Triplex-Bonding')
        #for atom in args: print(atom.atoms)
        if all([atom == Fire for atom in args]):
            triplexBonded = Molecule(args[0])
            triplexBonded += Molecule(args[0])
            return triplexBonded
        else:
            #print('opting for this one')
            new = Molecule()
            #print('new ',new,new.weight)
            return new  # False


class glUnbonding(Glyph):
    name = 'Glyph of Unbonding'
    description = '''eliminates the bond between 2 atoms'''
    cost = 10
    area = 2
    form = 'bar'
    features = [Unbonding]

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass


    @staticmethod
    def unbond(mol):
        # if any([cardinal == atom for atom in [Air, Water]]):
        return mol
        return mol


class glCalcification(Glyph):
    name = 'Glyph of Calcification'
    description = '''transmutes any of the 4 cardinal elements into neutral salt'''
    transmutes = {
        'earth':'salt',
        'water':'salt',
        'fire':'salt',
        'air':'salt',
    }
    cost = 10
    area = 1
    form = 'dot'
    features = [Transmuting]

    def activate(self, cardinal, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

    @staticmethod
    def transmute(atom):
        if issubclass(atom, Cardinal):
            return Salt
        else:
            return False


class glDuplication(Glyph):
    name = 'Glyph of Duplication'
    description = '''transmutes a salt atom into 1 of 4 cardinals by imbuing it with the essence of an existing atom '''
    '''The Glyph of Calcification occupies a single hex, and converts any Cardinal Element that is placed on it into Salt. '''
    transmutes = {
        'salt':'vitae',
        'salt':'mors',
    }
    cost = 20
    area = 2
    form = 'bar'
    features = [Transmuting]

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

    #todo: how can you express that it requires 2?
    @staticmethod
    def transmute(*args):
        if args[0] == Salt:
            return args[1]
        else:
            return False


class glProjection(Glyph):
    name = 'Glyph of Projection'
    description = '''consumes an atom of quicksilver and promotes an atom of metal to its next higher form'''
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
    features = [Transmuting,Consumes]

    def activate(self, *args):
        if len(args) == 2:
            self.transmute(args)

    @staticmethod
    def transmute(*args):
        #metal, quicksilver = args[0],args[1]
        if any([isinstance(atom, Quicksilver) for atom in args]):
            return nextMetal(args[0])
        else:
            return Molecule()  # False


class glPurification(Glyph):
    name = 'Glyph of Purification'
    description = '''transmutes 2 atoms of the same metal into a single atom of their next higher form'''
    cost = 20
    area = 3
    form = 'triangle'
    features = [Transmuting]

    def activate(self, *args):
        if len(args) == 2 and args[0] == args[1]:
            self.transmute(args)

    @staticmethod
    def transmute(*args):
        if all([issubclass(mol, Metal) for mol in args]):
            return nextMetal(args[0])
        else:
            return Molecule()  # False

        pass

class glAnimismus(Glyph):
    name = 'Glyph of Animismus'
    description = '''The Glyph of Animismus occupies a 2x2, rhomboid area. 
    The two central hexes act as inputs, receiving a Salt atom each to activate the Glyph. 
    Upon activation, the Salt is consumed, and a Vitae atom and Mors atom are created in their respective output hexes.
    '''
    cost = 20
    area = 4
    form = 'diamond'
    features = [Transmuting]

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

    @staticmethod
    def transmute(*args):
        if all([isinstance(mol,Salt) for mol in args]):
            return (Molecule(Mors),Molecule(Vitae))
        else:
            return Molecule()  # False

        pass

class glUnification(Glyph):
    name = 'Glyph of Unification'
    description = ''' The glyph of unification transmutes one atom of each of the four cardinal elements into one atom of quintessence'''
    cost = 20
    area = 5
    form = 'zigzag'
    features = []

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

class glDispersion(Glyph):
    name = 'Glyph of Dispersion'
    description = ''' The glyph of dispersion transmutes one atom of quintessence into one atom of each of the four cardinal elements.'''
    cost = 20
    area = 5
    form = 'half moon'
    features = []

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

class glDisposal(Glyph):
    name = 'Glyph of Disposal'
    description = '''removes unneeded atoms from the board'''
    cost = 0
    area = 7
    form = '6 star'
    features = [Consumes]

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

class glEquilibrium(Glyph):
    name = 'Glyph of Equilibrium'
    description = '''The Glyph of Equilibrium costs nothing and does nothing, serving a purely aesthetic purpose'''
    cost = 0
    area = 1
    form = 'dot'
    features = []

    def activate(self, *args):
        #atom1, atom2 = args[0], args[1]
        #process = Bonding(atom1, atom2)
        #return process.result
        pass

glyphs = [
    glPrime,
    glBonding,
    glMultiBonding,
    glTriplexBonding,
    glUnbonding,
    glCalcification,
    glDuplication,
    glProjection,
    glPurification,
    glAnimismus,
    glUnification,
    glDispersion,
    glDisposal,
    glEquilibrium,
]

""" MECHANISMS ###########################################################################################################"""

class FixedArm_1(Manipulator):
    name = 'Fixed-length arm1'
    description = '''A single arm and gripper'''
    cost = 20
    area = 1
    features = [Moving]

    @staticmethod
    def transform():
        return False

class FixedArm_2(Manipulator):
    name = 'Fixed-length arm1'
    description = '''An assembly with two arms and two grippers'''
    cost = 30
    area = 1
    features = [Moving]

    @staticmethod
    def transform():
        return False

class FixedArm_3(Manipulator):
    name = 'Fixed-length arm1'
    description = '''An assembly with three arms and three grippers'''
    cost = 30
    area = 1
    features = [Moving]

    @staticmethod
    def transform():
        return False

class FixedArm_6(Manipulator):
    name = 'Fixed-length arm1'
    description = '''An assembly with six arms and six grippers'''
    cost = 30
    area = 1
    features = [Moving]

    @staticmethod
    def transform():
        return False

class PistonArm(Manipulator):
    name = 'Piston Arm'
    description = '''A single arm and gripper that can extend and retract'''
    cost = 40
    area = 1
    features = [Moving]

    @staticmethod
    def transform():
        return False

class Track(Manipulator):
    name = 'Track'
    description = '''Arms can be placed on tracks and instructed to move along them'''
    cost = 5
    area = 1
    features = [Moving]

    @staticmethod
    def transform():
        return False

class VanBerloWheel(Manipulator):
    name = 'Van Berlo\'s Wheel'
    description = '''By using van Berlo's wheel with the glyph of
    duplication, salt can be turned into any of the
    four cardinal elements  '''
    cost = 30
    area = 1
    features = [Moving]

    @staticmethod
    def transform():
        return False

mechanisms = [
    FixedArm_1,
    FixedArm_2,
    FixedArm_3,
    FixedArm_6,
    PistonArm,
    Track,
    VanBerloWheel,
]

""" MOVES ###########################################################################################################"""


class grabber_drop:
    name = 'grabber_drop'
    description = 'releases on to atoms '
    key = 'R'

class grabber_grab:
    name = 'grabber_grab'
    description = 'locks on to atoms '
    key = 'F'


class piston_extend:
    name = 'piston_extend'
    description = 'extends an arm'
    key = 'W'


class piston_retract:
    name = 'piston_retract'
    description = ' retracts an arm'
    key = 'S'


class pivot_ccw:
    name = 'pivot_ccw'
    description = ' rotates the molecule around the grippers axis for 1/6th to the right'
    key = 'Q'


class pivot_cw:
    name = 'pivot_cw'
    description = 'rotates the molecule around the grippers axis for 1/6th to the left'
    key = 'E'


class rotator_ccw:
    name = 'rotator_ccw'
    description = 'rotates the arm around its baxis for 1/6th to the right'
    key = 'A'


class rotator_cw:
    name = 'rotator_cw'
    description = 'rotates the arm around its baxis for 1/6th to the left'
    key = 'D'


class track_advance:
    name = 'track_advance'
    description = ' moves the arm along the track towards the + symbol '
    key = 'G'


class track_retreat:
    name = 'track_retreat'
    description = ' moves the arm along the track towards the - symbol '
    key = 'T'


class repeat:
    name = 'repeat'
    description = ' adds a series of steps to repeat all previous moves '
    key = 'V'


class reset:
    name = 'reset'
    description = 'adds a series of step to put the arm back at its original transform'
    key = 'C'


class clock:
    name = 'clock'
    description = '''
    when starting the transmutation engine, all instructions are automatically padded
    so they have the same as the longest instruction sequence in the solution,
    which ensures that all arms are kept in sync.'''

    key = 'Q'


moves = [
    clock,
    grabber_drop,
    grabber_grab,
    piston_extend,
    piston_retract,
    pivot_ccw,
    pivot_cw,
    repeat,
    reset,
    rotator_ccw,
    rotator_cw,
    track_advance,
    track_retreat,
]

""" ENTRIES ###########################################################################################################"""

pathways = {
    Gold: Silver,
    Silver: Copper,
    Copper: Iron,
    Iron: Tin,
    Tin: Lead,
    Quicksilver: Lead,

    Air: Salt,
    Water: Salt,
    Fire: Salt,
    Earth: Salt,

    Salt: Water or Air or Fire or Earth,

}

def showPathway(atom,pool):
    chain = [atom]
    while atom not in pool:
        atom = pathways[atom]
        chain.append(atom)
    return chain

def nextMetal(metal):
    paths = {
        Silver : Gold,
        Copper: Silver ,
        Iron : Copper,
        Tin : Iron ,
        Lead : Tin,
    }
    return paths[metal]
