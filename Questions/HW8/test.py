from hw import ComplexNumber


k1 = ComplexNumber(3,-4)
k2 = ComplexNumber(0,5)
k3 = ComplexNumber(5,2)
k4 = ComplexNumber(3,-4)

assert k1.re ==  3, "Real value is incorrectly defined"
assert k1.im == -4, "Imagine value is incorrectly defined"
assert k1.len == 5, "Length is incorrectly defined"

assert k1 != k2, "Not equal is incorrectly defined"
assert k1 == k4, "Equality is incorrectly defined"
assert k1 <  k3, "Less is incorrectly defined"
assert k1 <= k2, "Less than or equal is incorrectly defined"
assert k3 >  k4, "Greater is incorrectly defined"
assert k1 >= k2, "Greater than or equal is incorrectly defined"

k5 = ComplexNumber(2,-3)
k6 = ComplexNumber(4, 5)
k7 = ComplexNumber(6, 2)
k8 = ComplexNumber(23,-2)

assert k5 + k6 == k7, "Summation is incorrectly defined"
assert k7 - k6 == k5, "Abstarct is incorrectly defined"
assert k5 * k6 == k8, "Multiply is incorrectly defined"

k9 = ComplexNumber(2, 3)
assert k5.con == k9, "Conjugate is incorrectly defined"