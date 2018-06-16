##########################################
#
# what it does: pone/modifica prefijos, sufijos
# explanation:  I use this in game development, since I need to Batch change prefixes and suffixes 
# for game assets that need to compply with my local NAMING CONVENTION
# author: Homar Orozco Apaza
##########################################

import os
import re
import tkinter
from pathlib import Path

tipoFile = ".tga"

#Poner prefijo sufijo
def ponerPreSuf(prefijoNEW, sufijoNEW, direccion):    
    for raiz, dirs, files in os.walk(direccion, topdown=False):    
        for nombreF in files:
            filename = Path(nombreF)
            nombreF = filename.stem
            extension = filename.suffix
            if extension == tipoFile:                            
                temporal = prefijoNEW + nombreF + sufijoNEW             #Nuevo nombre                
                os.rename( os.path.join(raiz,nombreF+extension) , os.path.join(raiz, temporal+extension)  )
                print(raiz,filename)

#Cambiar prefijo sufijo
def cmbiaPreSuf(prefijoNEW, prefijoOLD, sufijoOLD, sufijoNEW, direccion):
    for raiz, dirs, files in os.walk(direccion, topdown=False):    
        for nombreF in files:
            filename = Path(nombreF)
            nombreF = filename.stem
            extension = filename.suffix
            if extension == tipoFile:                
                temporal = nombreF.replace(prefijoOLD, prefijoNEW)      #Nuevo nombre
                temporal = temporal.replace(sufijoOLD, sufijoNEW)

                os.rename( os.path.join(raiz,nombreF+extension) , os.path.join(raiz, temporal+extension)  )
                print(raiz,filename)

def main():
    print("---------------------------------nones-------------------------------")    
    base = tkinter.Tk()
    base.title("Prefijos/Sufijos Poner/Cambiar")    
            
    tkinter.Label(base, text="prefijoNEW").grid(row=0,column=0)        #print(os.path.join(raiz,nombreF2))
    tkinter.Label(base, text="prefijoOLD").grid(row=0,column=1)
    tkinter.Label(base, text="sufijoOLD" ).grid(row=0,column=2)
    tkinter.Label(base, text="sufijoNEW" ).grid(row=0,column=3)
    tkinter.Label(base, text="direccionEnDisco").grid(row=4,column=0)

    texto1 = tkinter.Entry(base)
    texto1.grid(row=1,column=0)
    texto2 = tkinter.Entry(base)
    texto2.grid(row=2,column=1)
    texto3 = tkinter.Entry(base)
    texto3.grid(row=2,column=2)
    texto4 = tkinter.Entry(base)
    texto4.grid(row=1,column=3)
    texto5 = tkinter.Entry(base, width=50)                                        # direccion en disco
    texto5.grid(row=4,column=1,columnspan=3)
    
    boton1 = tkinter.Button(base, text="ponerPreSuf", command=lambda: ponerPreSuf( texto1.get(), texto4.get(), texto5.get() )).grid(row=3,column=1)
    boton2 = tkinter.Button(base, text="cmbiaPreSuf", command=lambda: cmbiaPreSuf( texto1.get(), texto2.get(), texto3.get(), texto4.get(), texto5.get() )).grid(row=3,column=2)

    

    base.mainloop()

if __name__ == "__main__": main()

    
