""" Rules and actions of Opus Magnum """
# THIS IS THE CONTEXT -> The Semantics

''''
BASICS: you start with the Reagents and you have to produce the Product in order to solve the puzzle

there are Alchemical Primes (atoms) that can Transmute, the Cardinals and the Metals 

'''

#todo: Full disclaimer: we're trying Functional Composition -> is this compounding the all the data?

# features that we can add to pieces, so that we can solve with them
class Metal: pass
class Cardinal: pass

class Air(Cardinal):
    def __repr__(self):
        return 'Air'

class Fire(Cardinal):
    def __repr__(self):
        return 'Fire'

class Water(Cardinal):
    def __repr__(self):
        return 'Water'

class Earth(Cardinal):
    def __repr__(self):
        return 'Earth'

class Salt:
    """ neutral salt """
    def __repr__(self):
        return 'Salt'

class Mors:
    def __repr__(self):
        return 'Mors'

class Vitae:
    def __repr__(self):
        return 'Vitae'

class Lead(Metal):
    def __repr__(self):
        return 'Lead'

class Quicksilver(Metal):
    def __repr__(self):
        return 'Quicksilver'

class Tin(Metal):
    def __repr__(self):
        return 'Tin'

class Iron(Metal):
    def __repr__(self):
        return 'Iron'

class Copper(Metal):
    def __repr__(self):
        return 'Copper'

class Silver(Metal):
    def __repr__(self):
        return 'Silver'

class Gold(Metal):
    def __repr__(self):
        return 'Gold'

class Omni:
    """ Quintessence """
    def __repr__(self):
        return 'Omni'


atoms = [ Air, Fire, Water, Earth, Salt, Mors, Vitae,
    Lead, Quicksilver, Tin, Iron, Copper, Silver, Gold, Omni
]

class Molecule(object):
    ''' every atom has a molecule, but a molecule can consist of multiple atoms with bonds '''
    areaCovered = False # a series of positions
    atoms = False
    bonds = False
    links = []
    coordinates = []
    def __init__(self, Atom=False):
        if Atom:
            if Atom in atoms:
                self.atoms = [Atom]
            else:
                self.atoms = []
        else:
            self.atoms = []
    def __add__(Mol_A, Mol_B):
        Mol_A.atoms += Mol_B.atoms
        return Mol_A

    def __sub__(Mol_A, Mol_B):
        return Mol_A

    def distance(Mol_A, Mol_B):
        """ simplified distance metric """
        return Mol_A.weight - Mol_B.weight

    @property
    def weight(self):
        return len(self.atoms)

    @property
    def bonds(self):
        return len(self.links)

    def recipe(self):
        singles = set(self.atoms)
        for atom in singles:
            print('\t%sx %s' % (self.atoms.count(atom), atom.__name__))

class Cost:
    """ the cost attribute """
    pass

class Area:
    """ the area attribute"""
    pass

class Form:
    """ the form attribute """
    # this one is due to the lack of having an Editor
    pass

class Glyph:
    """ a template for a Glyph """
    # a passive component
    name = 'none'
    description = 'none'

    coord = (0,0)
    def __init__(self):
        pass

    def activate(self, *args):
        # ability
        return True


class Manipulator:
    """ a template for a arms and grippers """
    # an active component

    def doAction(self):
        pass


class Dispensing:
    """ adds an atom to the board """
    verb = 'Dispense'
    pass

class Consumes:
    """ removes a atom from the board """
    verb = 'Consume'
    pass

class Bonding:
    """ always needs 2 atoms to create a bond between """
    verb = 'Bond'
    result = None
    def __init__(self):
        result = Molecule() # new molecule with the combined traits
        pass

class Unbonding:
    """ always needs 2 atoms to remove a bond between """
    verb = 'Unbond'
    pass

class Transmuting:
    """ takes one or more atoms and produces one or more atoms """
    verb = 'Transmute'
    pass

class Moving:
    """ moves a molecule from one hex to another """
    verb = 'Move'
    pass


moves = [
    'clock',
    'grabber_drop',
    'grabber_grab',
    'piston_extend',
    'piston_retract',
    'pivot_ccw',
    'pivot_cw',
    'repeat',
    'reset',
    'rotator_ccw',
    'rotator_cw',
    'track_advance',
    'track_retreat',
]

rules = [
    'cant overlap objects',
    'cant block / collide mechanisms',
    'must be able to repeat cycle X times',
]
