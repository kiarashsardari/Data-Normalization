import Data_Normalization as dn

lst = [-10, 0, 25, 50, 75, 100, 110]
assert dn.norm([]) == []
assert dn.loc([]) is None
assert dn.scale([]) is None
assert dn.norm([10]) == [10]
assert dn.math.isclose((dn.scale(lst)**2)*7,13450)
assert dn.loc(lst) == 50