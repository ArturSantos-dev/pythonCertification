class relogioLuxuoso:
    relogiosCriados = 0
    
    def __init__(self):
        relogioLuxuoso.relogiosCriados += 1
        pass
    def engravado(self,engravado):
        self.engravado = engravado
        pass

    @classmethod
    def pegarNumeroDeRelogiosCriados(cls):
        return cls.relogiosCriados
    
    @classmethod
    def criarRelogio(cls, engravado):
        cls.__init__(cls)
        cls.engravado(cls,engravado)
        if len(engravado) <41:
            print ('Relógio criado, com o engravado: ' + engravado+', e o número de relógios criados é: '+str(cls.pegarNumeroDeRelogiosCriados()))
        else:
            print ('Relógio criado sem engravemento, pois o engravamento é muito grande. O número de relógios criados é: '+str(cls.pegarNumeroDeRelogiosCriados()))


relogio1 = relogioLuxuoso.criarRelogio('Relógio 1')