
# source_install: pip3 install pymongo
import pymongo
from pprint import pprint

HOST = "127.0.0.1"
PORT = 27017

client = pymongo.MongoClient( host=HOST, port=PORT )
db = client.movie_company

def create_movie(   p_name,
                    p_genre,
                    p_directors_name,
                    p_franchise,
                    p_country,
                    p_year,
                    p_duration,
                    p_company,
                    p_actors ):
    post = {
        "name" : p_name,
        "genre" : p_genre,
        "directors_name" : p_directors_name,
        "franchise" : p_franchise,
        "country" : p_country,
        "year" : p_year,
        "duration" : p_duration,
        "company" : p_company,
        "actors" : p_actors
    }
    for i in post:
        if( post[i] == "" ):
            if( i == "franchise" ):
                pass
            else:
                return 1

    db.movies.insert_one(post)
    return 0

def show_movies():
    lst = db.movies.find({})
    return lst

def update_movie( pname, pfield, pdata):
    filter_post = {
        "name" : pname
    }
    action_post = {
        '$set' : {
            pfield : pdata
        }
    }
    db.movies.update_one(filter_post, action_post)
    return 0

def delete_movie( pname ):
    filter_post = {
        "name" : pname
    }
    print(db.movies.delete_one(filter_post))
    return 0

def create_company(     p_name,
                        p_fundation_year,
                        p_web ):
    post = {
        "name" : p_name,
        "fundation_year" : p_fundation_year,
        "web_address" : p_web
    }
    for i in post:
        if( post[i] == "" ):
            return 1

    db.company.insert_one(post)
    return 0

def show_companies():
    lst = db.company.find({})
    return lst

def update_company( pname, pfield, pdata):
    print("here")
    filter_post = {
        "name" : pname
    }
    action_post = {
        '$set' : {
            pfield : pdata
        }
    }
    print(db.company.update_one(filter_post, action_post))
    return 0

def delete_company( pname ):
    filter_post = {
        "name" : pname
    }
    print(db.company.delete_one(filter_post))
    return 0
