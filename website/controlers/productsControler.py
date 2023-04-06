from ..models.productsModel import Telescopes
from .. import dataBase
from sqlalchemy import text

def getAllTelescopes():
    return dataBase.session.execute(text('SELECT * FROM Telescopes'))

def getAllBrands():
    return dataBase.session.execute(text('SELECT DISTINCT brand FROM Telescopes'))

def getAllLensType():
    return dataBase.session.execute(text('SELECT DISTINCT lens FROM Telescopes'))

def TestData():
    new_Telescope = Telescopes(name = 'Skyscanner 10012',
                               brand = 'Orion',
                               description = 'Orion telescope',
                               lens = 'Reflector',
                               mount = 'Altazimut',
                               aperture = 100,
                               focal_distance = 400,
                               image_name = 'Skyscanner.jpg',
                               stock = 2,
                               state = True,
                               price = 130,
                               cost = 130)
    dataBase.session.add(new_Telescope)
    dataBase.session.commit()