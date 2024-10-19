meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "FR": "Aynı şeyi düşünmek",
            "NUH UH": "Hayır, öyle birşey yok, değil",
            "COOKED": "Birini utandırmak, yenmek etc.",
            "AGGRO": "Agresifleşmek",
            "LOCK IN": "Odaklanmak, zorlamak",
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelime daha sistemimizde bulunmamakta")
