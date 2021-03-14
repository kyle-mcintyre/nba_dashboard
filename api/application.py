import sys
import flask
from flask import Flask, escape, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import requests
import json
import players_stats
import jsonPopulate


application = Flask(__name__)
application.config['SECRET_KEY'] = "<< SECRET KEY >>"
cors = CORS(application)

@application.route('/')
def baseUrl():
    return "<h1> Hello World </h1>"

@application.route('/updatePlayers')
def updatePlayers():
    message = jsonPopulate.playerIdsToJson()
    return message

@application.route('/updateGames')
def updateGames():
    message = jsonPopulate.validGameIDsToJson()
    return message

@application.route('/getPlayers')
def getPlayers():
    players = players_stats.getPlayerNames()
    return jsonify(players)


@application.route('/get_player_info/<string:playerName>')
def get_player_info(playerName):
    info = players_stats.getPlayerInfo(playerName)
    return jsonify(info)
    
@application.route('/get_player_stats/<string:playerName>')
def get_player_points(playerName):
    points, rebounds, assists, ft, labels, totalP, totalA, totalR, totalFT = players_stats.getPlayerStats(playerName)
    return jsonify({'points':points, 'ft':ft, 'reb':rebounds, 'assists':assists, 'labels':labels,
                    'totalPoints': totalP, 'totalRebounds':totalR, 'totalAssists':totalA, 'totalFT':totalFT})
                

if __name__ == '__main__':
      application.run()