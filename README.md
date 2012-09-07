A library to represent a general class of kets.  This includes a multivariate polynomial library.

Interface to multivariate polynomials
-------------------

This library represents monomials and polynomials abstractly.  The variables are anonymous atoms in a nested list, which are identified by their Dewey numbers.  Polynomials can be added if the lists of their variables have the same shape.  Any polynomials can be multiplied; variables from different factors stay distinct in the product, so the list of the product's variables is a list of the factors' variable lists.  Variables can be identified, so that different indices refer to the same variable.  The standard polynomial product is formed by multiplying two polynomials, then identifying corresponding variables in the product.  Values can be substituted for variables, and, when all variables are identified with a variable to which a value has been assigned, the polynomial can be evaluated.  Either substitution or identification can cause an inconsistent assignment of values, which raises an error.

when multiplication of variables doesn't commute, the monomials can have more variables than the polynomial does.  for example, P(a,b) could have a term in ab²a, which can not be reduced until we know how x and p commute.  the mapping from the variable list to the monomials is potentially many to many.  this is necessary to for polynomials to be added, without having to know every order in which non-commuting variables occur.  There will need to be an abstract operation, that removes variables from the list, and an expand operation, which generates the variable list necessary to explicitly show all orderings.  Once variables have been assigned values, they can be abstracted away entirely, to give a polynomial in the remaining variables.  These can preserve the original variables, using the convention that index zero is a placeholder.

There are operations to normalise the order of polynomials, assuming that some of the variables are non-commuting operators.  This requires that, despite being stored in a nested list, the variables have some order.  This is easily solved: the order of products is determined by the monomials, whose indices are integers; the order of variables in the `Multivariable`, doesn't matter any more than the number of times they appear.  The ordering operations assume that all variables that refer to the same operator have been identified.  They return a new polynomial, whose variable list starts and ends with the newly-ordered variables, and has the original polynomial's variable list in between.  The ordered variables are identified with those at the original places, but the indices of the latter have been reduced to zero.

The operations on variable lists are getting complicated.  Should the lists be a separate data type to the polynomials?  I think yes.

Operations on Multivariables
------------------

a `Multivariable` represents equivalence classes of Dewey numbers and integers.  these are used by `Polynomial`, to map abstract variables into indices in the monomials.  the term “variable” refers to a Dewey number, represented as a tuple of integers; “factor” refers to an integer that indexes into a monomial.  an equivalence class might not contain any factors—the polynomial is constant in that variable.

the constructor `Multivariable(n)` returns an instance, representing the equivalence relation (i)~i for 0≤i<n.

adding an integer to a multivariable adds it to all the factors.

multiplying two multivariables returns one whose variable list is `(cons l r)`, where `l` and `r` are the variable lists of the arguments.  if two resulting equivalence classes contain identical factors, they are joined.  (what variables are in the resulting class?)  it is an error if two classes have overlapping but unequal sets of factors.

the method `identify(variable₁,…)` merges the equivalence classes of the given variables.

the method `abstract(variable₁,…,variable_n)` returns a multivariable with variables (1) through (n).  its equivalence classes are constructed by removing all variables from the classes of the receiver, then adding (1) to the class that had variable₁, and so on.

the method `concrete(variable₁,…)` returns a multivariable with variables (0 n) and (1 a), where n is between the greatest and least factor recorded in the receiver, and a is a variable of the receiver.  the equivalence classes are copied from the receiver, with (1 a) in place of a, and (0 n)~n.

Operations on Polynomials
-------------------

monomials are represented by tuples of exponents.

the methods of multivariables can be applied to polynomials, and act on the variables of the polynomial.  it must not be possible to construct references to factors outside the range of the monomials this way: monomial methods must never add factors that weren't there before.  it is an error if variables are identified after different values are substituted for them.

the equivalence classes of variables in a polynomial never include consecutive factors.  if consecutive factors are identified, the second is removed from the monomials and the term table, and its exponent added to that of the first.  the factors in the multivariable are renumbered accordingly.

the constructor `Polynomial(monomial₁,…)` constructs a polynomial with variables corresponding to the factors of the monomials.  it is an error if the monomials have different numbers of factors.

the method `substitute(variable, value)` enters the value in the substitution table.  it is an error if a different value has previously been substituted for an identical factor.

the method `evaluate()` calculates the value of the polynomial, with the substitutions.

two polynomials can be added if they have the same sets of variables, and the same equivalence relations when restricted to variables.  the monomials of the result are the products of a monomial from one term with a monomial the size of the other term, with zero exponents.

a polynomial can identify when identical factors are compactable, and does so.  (e.g. a⁰b⁰a + ab⁰a⁰ reduces to 2a.)

there will be code generation methods for Numpy, Pycuda and so on.