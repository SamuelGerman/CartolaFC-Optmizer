import requests
import json
from Config.Config import Config

class CartolaAPI:
    @staticmethod
    def getAthletesOnMarket():
        response = requests.get(Config.ENDPOINTS_DICT["API_ATLETAS_MERCADO"])
        if response.status_code == Config.SUCCESS:
            response = response.json()
            return response["atletas"]
        else:
            return response.status_code
    
    """é necessário analisar o formato da resposta dessa requisição pelo postman quando o mercado fechar
    para saber se o atributo que eu quero da resposta é realmente 'ateltas'"""
    @staticmethod
    def getAthletesScores():
        response = requests.get(Config.ENDPOINTS_DICT["API_ATLETAS_PONTUADOS"])
        if response.status_code == Config.SUCCESS:
            response = response.json()
            return response["atletas"]
        else:
            return response.status_code
    
    @staticmethod
    def getBrasileiraoTeams():
        response = requests.get(Config.ENDPOINTS_DICT["API_ATLETAS_MERCADO"])
        if response.status_code == Config.SUCCESS:
            response = response.json()
            return response["clubes"]
        else:
            return response.status_code
        
    @staticmethod
    def getAllTeams():
        response = requests.get(Config.ENDPOINTS_DICT["API_CLUBES"])
        if response.status_code == Config.SUCCESS:
            response = response.json()
            return response
        else:
            return response.status_code
    

    @staticmethod
    def getMarketStatus():
        response = requests.get(Config.ENDPOINTS_DICT["API_MERCADO_STATUS"])
        if response.status_code == Config.SUCCESS:
            response = response.json()
            return response
        else:
            return response.status_code

    @staticmethod
    def getCurrentRound():
        response = requests.get(Config.ENDPOINTS_DICT["API_MERCADO_STATUS"])
        if response.status_code == Config.SUCCESS:
            response = response.json()
            return int(response["rodada_atual"])
        else:
            return -1


    @staticmethod
    def getNextMatches():
        response = requests.get(Config.ENDPOINTS_DICT["API_PARTIDAS"])
        if response.status_code == Config.SUCCESS:
            response = response.json()
            return response["partidas"]
        else:
            return response.status_code
    

    @staticmethod
    def getMatchesByRound(round):
        if round > 0 and round < CartolaAPI.getCurrentRound():
            response = requests.get(f"{Config.ENDPOINTS_DICT["API_PARTIDAS"]}/{round}")
            if response.status_code == Config.SUCCESS:
                response = response.json()
                return response["partidas"]
            else:
                return response.status_code
        else:
            return "Invalid round"
    


