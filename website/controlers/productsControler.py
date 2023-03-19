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
    new_Telescope = Telescopes(name = 'Travel Scope',
                               brand = 'Celestron',
                               description = 'Celestron telescope',
                               lens = 'Refractor',
                               mount = 'Altazimut',
                               aperture = 70,
                               focal_distance = 400,
                               image_name = 'TravelScope.png',
                               stock = 5,
                               state = True,
                               price = 86,
                               cost = 86)
    dataBase.session.add(new_Telescope)
    dataBase.session.commit()