class Config:
    '''
    General configuration parent class 
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration class

    Arg:
        Config:The parent configuration clas with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class 
    Arg:
        The parent configuration class with the general comfiguration settings
    '''
    DEBURG = True