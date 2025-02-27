def verify_weather(hex_flawer, direction):
    actual_position = 1

    element = hex_flawer[actual_position - 1]
    name, severity, blk1, blk2, blk3 = element

    if direction == blk1 | blk2 | blk3:
        print("weather dosen't change")
        return

    match actual_position:        
        case 1:
            links = []
        case 2:
            links = []
        case 3:
            links = []
        case 4:
            links = []
        case 5:
            links = []
        case 6:
            links = []
        case 7:
            links = []
        case 8:
            links = []
        case 9:
            links = []
        case 10:
            links = []
        case 11:
            links = []        
        case 12:
            links = []
        case 13:
            links = []
        case 14:
            links = []
        case 15:
            links = []
        case 16:
            links = []
        case 17:
            links = []
        case 18:
            links = []
        case 19:
            links = []      

    actual_position = links[direction - 1]


summer = [
    ["chuva torrencial!", 2, 0, 0, 1],
    ["chuva forte", 1, 0, 0, 1],
    ["tempestade!", 2, 0, 0, 1],
    ["chuva morna", 0, 0, 0, 0],
    ["nublado e humido", 0, 0, 0, 0],
    ["vento forte!", 1, 0, 0, 2],
    ["sereno morno", 0, 0, 0, 0],
    ["nublado e com vento", 0, 0, 0, 0],
    ["garoa morna", 0, 0, 0, 0],
    ["tempo agradavel", 0, 0, 0, 0],
    ["parcialmente nublado e ameno", 0, 0, 0, 0],
    ["quente e abafado", 0, 0, 0, 0],
    ["nublado e morno", 0, 0, 0, 0],
    ["brisa morna", 0, 0, 0, 0],
    ["quente e abafado!", 1, 0, 0, 5],
    ["quente e seco!", 1, 0, 0, 0],
    ["tempo limpo e ameno", 0, 0, 0, 0],
    ["quente e com vento!", 1, 0, 0, 4],
    ["ensolarado e claro", 0, 0, 0, 4],
    ["ondas de calor!!", 2, 0, 0, 4]
]

winter = [
    "ensolarado e ameno",
    "nublado e ameno",
    "frio e limpo",
    "claro e com vento",
    "frio e humido",
    "nublado e frio",
    "nevoa fria",
    "garoa leve",
    "chuva fria!",
    "chuva forte!",
    "vento frio",
    "chuva de granizo!",
    "gelado e nublado",
    "nevesca!!",
    "vento e neve!",
    "nevando leve"
]

spring = [
    "chuva forte!",
    "vento e neve",
    "chuva de granizo!",
    "nevando forte!",
    "garoa morna",
    "ameno e humido",
    "nevoa fria",
    "claro e ameno",
    "nevando leve",
    "ensolarado e claro",
    "frio e seco",
    "quente e humido",
    "noblado e morno",
    "agradavelmente morno",
    "quente e seco"
]

autumn = [
    "ventos esporadicos!",
    "neblina fria",
    "agradavelmente morno",
    "ensolarado e claro",
    "nublado e congelante",
    "ventos frios",
    "ensolarado e ameno",
    "nublado e ameno",
    "nublado e humido",
    "nevoa densa!",
    "garoa",
    "chuva e vento",
    "chuva e neblina!",
    "limpo e com vento",
    "tempestade!"
]

weather = [
    "agradável"
    "ameno e úmido"
    "brisa quente"
    "chuva"
    "chuva de granizo!"
    "chuva e neblina!"
    "chuva e vento"
    "chuva forte!"
    "chuva fria!"
    "chuva forte"
    "chuva torrencial!"
    "claro e ameno"
    "claro e com vento"
    "ensolarado e ameno"
    "ensolarado e claro"
    "frio e úmido"
    "frio e claro"
    "frio e seco"
    "garoa"
    "garoa leve"
    "garoa morna"
    "gelado e nublado"
    "limpo e com vento"
    "neblina fria"
    "nevando forte!"
    "nevando leve"
    "nevasca!!"
    "nevoa densa!"
    "nublado e morno"
    "nublado e ameno"
    "nublado e com vento"
    "nublado e congelante"
    "nublado e frio"
    "nublado e úmido"
    "ondas de calor!!"
    "parcialmente nublado e ameno"
    "quente e abafado!"
    "quente e com vento!"
    "quente e úmido"
    "quente e seco!"
    "quente nublado"
    "sereno"
    "tempestade!"
    "tempestade!"
    "tempo limpo e ameno"
    "vento e neve!"
    "vento forte!"
    "vento frio"
    "ventos esporádicos!"
    "ventos frios"
    "sereno morno"
]