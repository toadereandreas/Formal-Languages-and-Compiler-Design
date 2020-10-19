from HashTable import HashTable
from SymbolTable import SymbolTable

size = 15
st = SymbolTable(size)
st.position("andreas")
st.position("marius")
st.position("vrajeala")
st.position("gunoi")
st.position("ipad")
st.position("evomag")
st.position("prajeala")
st.position("2")
st.position("14")
print(st)
print(st.position("evomag"))

print(st.position("gunoi"))
print(st.position("evomag"))
