from src.local import *
from src.txt.desc_locais_txt import *
from src.obj.monstros import *

locais = []

locais.insert(0, Local("???? - ??" , nSei, None, None, None, None, minotauro))
locais.insert(1, Local("Floresta - L1", fl1, 3, 2, None, None))
locais.insert(2, Local("Floresta - L0" , fl0, 1, None, None, None, goblin, 1))
locais.insert(3, Local("Floresta - L2" , fl2, 4, 1, None, 5, goblin, 1))
locais.insert(4, Local("Floresta - L3" , fl3, None, 3, 7, 6))
locais.insert(5, Local("Floresta - L4" , fl4, 6, None, 3, None))
locais.insert(6, Local("Floresta - L5" , fl5, None, 5, 4, None, lobo, 2))
locais.insert(7, Local("Floresta - L6" , fl6, None, None, 8, 4, goblin))
locais.insert(8, Local("Jardim - L1" , jl1, 9, None, None, 7, None, 3))
locais.insert(9, Local("Jardim - L2" , jl2, None, 8, None, 11, zumbi, 2))
locais.insert(10, Local("Castelo - L1" , "", 14, 4, 11, 12, nobreZumbi, 1))
locais.insert(11, Local("Castelo - L2" , "", 16, None, 9, 10))
locais.insert(12, Local("Castelo - L3" , "", 13, None, 10, None))
locais.insert(13, Local("Castelo - L4" , "", None, 12, None, 14))
locais.insert(14, Local("Castelo - L5" , "", None, 11, None, None, nobreZumbi, 2))
