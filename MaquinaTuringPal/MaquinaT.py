class Maquina_Turing:

    def __init__(self,estado,cabezal,cinta_list):
        self.estado = estado
        self.cabezal = cabezal
        self.cinta_list = cinta_list

    def getEstado(self):
        return self.estado

    def getCabezal(self):
        return self.cabezal
    
    def getLista(self):
        return self.cinta_list

    # Tabla de Reglas
    def actualizarMaquina(self, caracter_list):

        # Estado Inicial
        if (self.estado == 'q1'):
            if (self.cinta_list[self.cabezal] != 0):
                #ESTADO (p)
                char_leer = self.cinta_list[self.cabezal]
                char_index = caracter_list.index(char_leer)
                self.estado = ''.join(['p',str(char_index)])
                #ESCRIBIR (cero)
                self.cinta_list[self.cabezal] = 0
                #MOVERSE A LA DERECHA
                self.cabezal += 1
            else:
                # ESTADO (qy)
                self.estado = 'qy'
                #ESCRIBIR (cero) SIN ALTERAR
                self.cinta_list[self.cabezal] = 0
                ### MOVERSE A LA DERECHA (no importa)
                self.cabezal += 1
    
        elif (self.estado.startswith('p')):
            if (self.cinta_list[self.cabezal]!=0):
                ### ESTADO (SIN CAMBIAR )
                self.estado = self.estado
                ### ESCRIBIR (SIN CAMBIAR)
                self.cinta_list[self.cabezal] = self.cinta_list[self.cabezal]
                # MOVERSE A LA DERECHA
                self.cabezal += 1
            else:
                ### ESTADO (r)
                self.estado = ''.join(['r',self.estado[1:]])
                ### ESCRIBIR CERO SIN CAMBIAR 
                self.cinta_list[self.cabezal] = 0
                # MOVERSE A LA IZQUIERDA
                self.cabezal -= 1
                    
        elif (self.estado.startswith('r')):
            char_leer = caracter_list[int(self.estado[1:])]
            if (self.cinta_list[self.cabezal] != char_leer and self.cinta_list[self.cabezal] != 0): # zero is needed for strings of odd length
                #ESTADO (qn)
                self.estado = 'qn'
                #ESCRIBIR
                self.cinta_list[self.cabezal] = self.cinta_list[self.cabezal]
                # MOVERSE A LA IZQUIERDA
                self.cabezal -= 1
            else:
                #ESTADO (q2)
                self.estado = 'q2'
                #ESCRIBIR CERO
                self.cinta_list[self.cabezal] = 0
                # MOVERSE A LA IZQUIERDA
                self.cabezal -= 1
                
        elif (self.estado == 'q2'):
            if (self.cinta_list[self.cabezal] != 0):
                #ESTADO SIN CAMBIAR
                self.estado = 'q2'
                #ESCRIBIR SIN IMPORTAR
                self.cinta_list[self.cabezal] = self.cinta_list[self.cabezal]
                #MOVERSE A LA IZQUIERDA
                self.cabezal -= 1
            else:
                #ESTADP(q1)
                self.estado = 'q1'
                #ESCRIBIR CERO
                self.cinta_list[self.cabezal] = 0
                # MOVERSE A LA DERECHA
                self.cabezal += 1