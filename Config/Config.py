from Models.FormationSchema import FormationSchema
from Models.Position import Position
class Config:
    SUCCESS = 200

    SCOUTS_SCORES_DICT = {
        "GOL" : 8,
        "ASSISTENCIA": 5,
        "FINALIZACAO TRAVE": 3,
        "FINALIZACAO DEFENDIDA": 1.2,
        "FINALIZACAO FORA": 0.8,
        "FALTA SOFRIDA": 0.5,
        "PENALTI SOFRIDO": 1,
        "PENALTI PERDIDO": -4,
        "IMPEDIMENTO": -0.1,
        "PENALTI DEFENDIDO": 7, 
        "CLEAN SHEET": 5, #DEFENDERS ONLY
        "DEFESA": 1, #GOALKEEPER ONLY
        "DESARME": 1.2, 
        "GOL CONTRA":-3,
        "CARTAO VERMELHO": -3,
        "CARTAO AMARELO": -1,
        "GOL SOFRIDO": -1, #DEFENDERS ONLY
        "FALTA COMETIDA":-0.3,
        "PENALTI COMETIDO":-1,
        "VITORIA":1, #MANAGER ONLY
    }

    FORMATIONS_DICT = {
        "3-4-3" : FormationSchema(3,0,4,3),
        "3-5-2" : FormationSchema(3,0,5,2),
        "4-3-3" : FormationSchema(2,2,3,3),
        "4-4-2" : FormationSchema(2,2,4,2),
        "4-5-1" : FormationSchema(2,2,5,1),
        "5-3-2" : FormationSchema(3,2,3,2),
        "5-4-1" : FormationSchema(3,2,4,1),
    }

    """dicionario de clubes e seus respectivos id: criar uma função que extraira 
    essas informações da API do cartola"""

    POSITION_DICT = {
        1 : Position(1, "GOALKEEPER"),
        2 : Position(2, "SIDE BACK"),
        3 : Position(3, "CENTER BACK"),
        4 : Position(4, "MIDFIELDER"),
        5 : Position(5, "FOWARD"),
        6 : Position(6,"MANAGER"),
    }

    STATUS_DICT = {
            2: "Dúvida",
            3: "Suspenso",
            5: "Contundido",
            6: "Nulo",
            7: "Provável",
        }

    ENDPOINTS_DICT = {
            "API_MERCADO_STATUS":'https://api.cartolafc.globo.com/mercado/status',
            "API_ATLETAS_MERCADO": 'https://api.cartolafc.globo.com/atletas/mercado',
            "API_ATLETAS_PONTUADOS": 'https://api.cartolafc.globo.com/atletas/pontuados',
            "API_PARTIDAS": 'https://api.cartolafc.globo.com/partidas',
            "API_CLUBES": 'https://api.cartolafc.globo.com/clubes',
        }