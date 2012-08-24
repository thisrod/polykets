"""Multivariate polynomials."""

class Polynomial(object):
	"""Maintains the variables and values tables.  Dispatches to subclasses to manipulate coefficients.
	
	The variables table is a metacollection, whose indices are the variables visible to the user.  These can be identified with each other, and values might have been substituted for some of them.  The entries in the vars collection are positive if they index variables in the actual term list, or negative if they index subtitutions in the vals table.
	
	What happens when we add polynomials, some of whose variables are identified or substituted?"""
	
	def __init__(self, arity):
		"Set up tables for a polynomial with arity variables."
		self.vars = range(arity)
		self.vals = [None]*arity

	# Subclasses must override either from_terms or from_coefficients.  

	@classmethod
	def from_terms(cls, terms):
		"Construct from something that generates terms, as coefficient, index tuple pairs."
		pass

	@classmethod
	def coefficients(cls, coefs):
		"Construct from a list of coefficients, which might themselves be polynomials"
		pass
		
		
class Termlist(Polynomial):
	"""A polynomial, represented as a table mapping terms to coefficients."""
	
	@classmethod
	def from_terms(cls, terms):
		n = shape(variables(terms[0][1]))
		instance = Polynomial(n)
		instance.terms = {}
		for c, expts in terms:
			expts = variables(expts)
			assert shape(expts) == n
			assert expts not in instance.terms
			if c != 0:
				instance.terms[expts] = c
		return instance
			
			
def shape(vars):
	"""Return the shape of vars, which is a collection indexed by variables in canonical form."""
	# Only do the flat case for now
	return len(vars)
	
def variables(vars):
	"""Return a collection indexed by variables in canonical form.  Its elements might be sets of exponents, for example.  If there is going to be a nested representation, there needs to be a standard way to flatten these collections."""
	# Only do the flat case for now
	return tuple(vars)
