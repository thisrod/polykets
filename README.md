A library to represent a general class of kets.  This includes a multivariate polynomial library.

Interface to multivariate polynomials
-------------------

This library represents monomials and polynomials abstractly.  The variables are anonymous atoms in a nested list, which are identified by their Dewey numbers.  Polynomials can be added if the lists of their variables have the same shape.  Any polynomials can be multiplied; variables from different factors stay distinct in the product, so the list of the product's variables is a list of the factors' variable lists.  Variables can be identified, so that different indices refer to the same variable.  The standard polynomial product is formed by multiplying two polynomials, then identifying corresponding variables in the product.  Values can be substituted for variables, and, when all variables are identified with a variable to which a value has been assigned, the polynomial can be evaluated.  Either substitution or identification can cause an inconsistent assignment of values, which raises an error.

when multiplication of variables doesn't commute, the monomials can have more variables than the polynomial does.  for example, P(a,b) could have a term in ab²a, which can not be reduced until we know how x and p commute.  the mapping from the variable list to the monomials is potentially many to many.  this is necessary to for polynomials to be added, without having to know every order in which non-commuting variables occur.  There will need to be an abstract operation, that removes variables from the list, and an expand operation, which generates the variable list necessary to explicitly show all orderings.  Once variables have been assigned values, they can be abstracted away entirely, to give a polynomial in the remaining variables.  These can preserve the original variables, using the convention that index zero is a placeholder.

There are operations to normalise the order of polynomials, assuming that some of the variables are non-commuting operators.  This requires that, despite being stored in a nested list, the variables have some order.  This is easily solved: the order of products is determined by the monomials, whose indices are integers; the order of variables in the `Multivariable`, doesn't matter any more than the number of times they appear.  The ordering operations assume that all variables that refer to the same operator have been identified.  They return a new polynomial, whose variable list starts and ends with the newly-ordered variables, and has the original polynomial's variable list in between.  The ordered variables are identified with those at the original places, but the indices of the latter have been reduced to zero.

The operations on variable lists are getting complicated.  Should the lists be a separate data type to the polynomials?  I think yes.

Operations on Multivariables
------------------

a `Multivariable` represents equivalence classes of Dewey numbers and integers.  these are used by `Polynomial`, to map abstract variables into indices in the monomials.  the term “variable” refers to a Dewey number, and “factor” to an integer that indexes into a monomial.

the constructor `Multivariable(n, va)` 

`factors` 