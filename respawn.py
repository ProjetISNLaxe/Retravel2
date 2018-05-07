import pygame

def respawn():
    with open("save1/map", "r") as mapactive:
        mapactive = mapactive.read()

    with open("save1/posmap/posmap"+mapactive, "w") as writer:
        writer.write("")

    with open("save1/pospeso/pospeso"+mapactive, "w") as writer:
        writer.write("")

    with open("save1/map", "w") as mapactive:
        mapactive.write("maison_2")

    with open("save1/pospeso/pospesomaison_2", "w") as writer:
        writer.write("571,237")

    with open("save1/posmap/posmapmaison_2", "w") as writer:
        writer.write("-208,-9")
    with open("save1/pospeso/pospesocapitale", "w") as writer:
        writer.write("403,208")

    with open("save1/posmap/posmapcapitale", "w") as writer:
        writer.write("-1136,-2925")