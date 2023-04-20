from ..models.productsModel import Telescopes
from .. import dataBase
from sqlalchemy import text

def getAllTelescopes():
<<<<<<< Updated upstream
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
=======
    return dataBase.session.execute(text('SELECT * FROM telescopes'))


def filterTelesopes(price, focal_distance, aperture, brands, lens, mounts):

    query = f'SELECT * FROM telescopes WHERE price BETWEEN {price[0]} and {price[1]} and \
                focal_distance BETWEEN {focal_distance[0]} and {focal_distance[1]} and \
                aperture BETWEEN {aperture[0]} and {aperture[1]}'
    return dataBase.session.execute(text(query))


def getAllBrands():
    return dataBase.session.execute(text('SELECT DISTINCT brand FROM telescopes')).fetchall()


def getAllLensType():
    return dataBase.session.execute(text('SELECT DISTINCT lens FROM telescopes')).fetchall()


def getAllMounts():
    return dataBase.session.execute(text('SELECT DISTINCT mount FROM telescopes')).fetchall()


def getMinFocalDistance():
    return dataBase.session.execute(text('SELECT MIN(focal_distance) FROM telescopes')).fetchone()


def getMaxFocalDistance():
    return dataBase.session.execute(text('SELECT MAX(focal_distance) FROM telescopes')).fetchone()


def getMinAperture():
    return dataBase.session.execute(text('SELECT MIN(aperture) FROM telescopes')).fetchone()


def getMaxAperture():
    return dataBase.session.execute(text('SELECT MAX(aperture) FROM telescopes')).fetchone()


def getMinPrice():
    return dataBase.session.execute(text('SELECT MIN(price) FROM telescopes')).fetchone()


def getMaxPrice():
    return dataBase.session.execute(text('SELECT MAX(price) FROM telescopes')).fetchone()


def getTelescopeById(id):
    return Telescopes.query.filter_by(id=id).first()
>>>>>>> Stashed changes
