import http.client
import urllib.parse
import json

conn = http.client.HTTPSConnection("www.cheapshark.com")

# Input game to look
game = input("Game: ")

# Encode the game title for the URL
encoded_game_title = urllib.parse.quote(game)

# Adjust the endpoint to match the CheapShark API for game lookup by title
endpoint = f"/api/1.0/games?title={encoded_game_title}"

payload = ''
headers = {}
conn.request("GET", endpoint, payload, headers)
res = conn.getresponse()
data = res.read()

parsed_data = json.loads(data.decode("utf-8"))
print(json.dumps(parsed_data, indent=2))

## Game data

gameid = input(f"Game Id: ")
diff = f"/api/1.0/games?id={gameid}"

conn.request("GET", diff, payload, headers)
res = conn.getresponse()
data = res.read()

parsed_data = json.loads(data.decode("utf-8"))
print(json.dumps(parsed_data, indent=2))

## Store data

stores_data = {
    1: {
        "storeName": "Steam",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/0.png",
            "logo": "/img/stores/logos/0.png",
            "icon": "/img/stores/icons/0.png"
        }
    },
    2: {
        "storeName": "GamersGate",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/1.png",
            "logo": "/img/stores/logos/1.png",
            "icon": "/img/stores/icons/1.png"
        }
    },
    3: {
        "storeName": "GreenManGaming",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/2.png",
            "logo": "/img/stores/logos/2.png",
            "icon": "/img/stores/icons/2.png"
        }
    },
    4: {
        "storeName": "Amazon",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/3.png",
            "logo": "/img/stores/logos/3.png",
            "icon": "/img/stores/icons/3.png"
        }
    },
    5: {
        "storeName": "GameStop",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/4.png",
            "logo": "/img/stores/logos/4.png",
            "icon": "/img/stores/icons/4.png"
        }
    },
    6: {
        "storeName": "Direct2Drive",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/5.png",
            "logo": "/img/stores/logos/5.png",
            "icon": "/img/stores/icons/5.png"
        }
    },
    7: {
        "storeName": "GOG",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/6.png",
            "logo": "/img/stores/logos/6.png",
            "icon": "/img/stores/icons/6.png"
        }
    },
    8: {
        "storeName": "Origin",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/7.png",
            "logo": "/img/stores/logos/7.png",
            "icon": "/img/stores/icons/7.png"
        }
    },
    9: {
        "storeName": "Get Games",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/8.png",
            "logo": "/img/stores/logos/8.png",
            "icon": "/img/stores/icons/8.png"
        }
    },
    10: {
        "storeName": "Shiny Loot",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/9.png",
            "logo": "/img/stores/logos/9.png",
            "icon": "/img/stores/icons/9.png"
        }
    },
    11: {
        "storeName": "Humble Store",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/10.png",
            "logo": "/img/stores/logos/10.png",
            "icon": "/img/stores/icons/10.png"
        }
    },
    12: {
        "storeName": "Desura",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/11.png",
            "logo": "/img/stores/logos/11.png",
            "icon": "/img/stores/icons/11.png"
        }
    },
    13: {
        "storeName": "Uplay",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/12.png",
            "logo": "/img/stores/logos/12.png",
            "icon": "/img/stores/icons/12.png"
        }
    },
    14: {
        "storeName": "IndieGameStand",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/13.png",
            "logo": "/img/stores/logos/13.png",
            "icon": "/img/stores/icons/13.png"
        }
    },
    15: {
        "storeName": "Fanatical",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/14.png",
            "logo": "/img/stores/logos/14.png",
            "icon": "/img/stores/icons/14.png"
        }
    },
    16: {
        "storeName": "Gamesrocket",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/15.png",
            "logo": "/img/stores/logos/15.png",
            "icon": "/img/stores/icons/15.png"
        }
    },
    17: {
        "storeName": "Games Republic",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/16.png",
            "logo": "/img/stores/logos/16.png",
            "icon": "/img/stores/icons/16.png"
        }
    },
    18: {
        "storeName": "SilaGames",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/17.png",
            "logo": "/img/stores/logos/17.png",
            "icon": "/img/stores/icons/17.png"
        }
    },
    19: {
        "storeName": "Playfield",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/18.png",
            "logo": "/img/stores/logos/18.png",
            "icon": "/img/stores/icons/18.png"
        }
    },
    20: {
        "storeName": "ImperialGames",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/19.png",
            "logo": "/img/stores/logos/19.png",
            "icon": "/img/stores/icons/19.png"
        }
    },
    21: {
        "storeName": "WinGameStore",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/20.png",
            "logo": "/img/stores/logos/20.png",
            "icon": "/img/stores/icons/20.png"
        }
    },
    22: {
        "storeName": "FunStockDigital",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/21.png",
            "logo": "/img/stores/logos/21.png",
            "icon": "/img/stores/icons/21.png"
        }
    },
    23: {
        "storeName": "GameBillet",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/22.png",
            "logo": "/img/stores/logos/22.png",
            "icon": "/img/stores/icons/22.png"
        }
    },
    24: {
        "storeName": "Voidu",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/23.png",
            "logo": "/img/stores/logos/23.png",
            "icon": "/img/stores/icons/23.png"
        }
    },
    25: {
        "storeName": "Epic Games Store",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/24.png",
            "logo": "/img/stores/logos/24.png",
            "icon": "/img/stores/icons/24.png"
        }
    },
    26: {
        "storeName": "Razer Game Store",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/25.png",
            "logo": "/img/stores/logos/25.png",
            "icon": "/img/stores/icons/25.png"
        }
    },
    27: {
        "storeName": "Gamesplanet",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/26.png",
            "logo": "/img/stores/logos/26.png",
            "icon": "/img/stores/icons/26.png"
        }
    },
    28: {
        "storeName": "Gamesload",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/27.png",
            "logo": "/img/stores/logos/27.png",
            "icon": "/img/stores/icons/27.png"
        }
    },
    29: {
        "storeName": "2Game",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/28.png",
            "logo": "/img/stores/logos/28.png",
            "icon": "/img/stores/icons/28.png"
        }
    },
    30: {
        "storeName": "IndieGala",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/29.png",
            "logo": "/img/stores/logos/29.png",
            "icon": "/img/stores/icons/29.png"
        }
    },
    31: {
        "storeName": "Blizzard Shop",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/30.png",
            "logo": "/img/stores/logos/30.png",
            "icon": "/img/stores/icons/30.png"
        }
    },
    32: {
        "storeName": "AllYouPlay",
        "isActive": 0,
        "images": {
            "banner": "/img/stores/banners/31.png",
            "logo": "/img/stores/logos/31.png",
            "icon": "/img/stores/icons/31.png"
        }
    },
    33: {
        "storeName": "DLGamer",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/32.png",
            "logo": "/img/stores/logos/32.png",
            "icon": "/img/stores/icons/32.png"
        }
    },
    34: {
        "storeName": "Noctre",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/33.png",
            "logo": "/img/stores/logos/33.png",
            "icon": "/img/stores/icons/33.png"
        }
    },
    35: {
        "storeName": "DreamGame",
        "isActive": 1,
        "images": {
            "banner": "/img/stores/banners/34.png",
            "logo": "/img/stores/logos/34.png",
            "icon": "/img/stores/icons/34.png"
        }
    }
}

# Accessing information for store with input ID

storeinp = input(f"Store ID: ")
store_info = stores_data.get(int(storeinp))
if store_info:
    import json
    print(json.dumps(store_info, indent=4))
else:
    print("Store not found.")
