name= input("hello, what is your name-->")
print('hello, welcome to the world', name)
print('kindly please answer the following question')
genre= input("what genre you are looking for (action,romance,horror): ")
if genre == 'action':
    period = input("how long the manga would be (short,medium,long): ")
    if period == 'short':
        decade = input ("which decade (2010,2020): ")
        if decade == '2010':
            print('We reccomend you, all you need is kill')
        if decade == '2020':
            print('We reccomend you, kaiju')
    if period == 'medium':
        decade= input ("which decade, (2010,2020): ")
        if decade == '2010':
            print('We reccomend you, akame ga kill')
        if decade == '2020':
            print ('We reccomend you, sakamoto days')
    if period == 'long':
        decade = input ("which decade, (2010,2020): ")
        if decade == '2010':
            print('we reccomend you attack on titan')
        if decade == '2020':
            print('we reccomend you, blue lock')
if genre == 'romance':
    period = input("how long the manga would be (short,medium,long): ")
    if period == 'short':
        decade = input ("which decade (2010,2020): ")
        if decade == '2010':
            print('We reccomend you, fruits basket another')
        if decade == '2020':
            print('We reccomend you, my girlfriend child')
    if period == 'medium':
        decade= input ("which decade, (2010,2020): ")
        if decade == '2010':
            print('We reccomend you, ao haru ride')
        if decade == '2020':
            print ('We reccomend you, the dangers in my heart')
    if period == 'long':
        decade = input ("which decade, (2010,2020): ")
        if decade == '2010':
            print('we reccomend you horimiya')
        if decade == '2020':
            print('we reccomend you, oshi no ko')
if genre == 'horror':
    period = input("how long the manga would be (short,medium,long): ")
    if period == 'short':
        decade = input ("which decade (2010,2020): ")
        if decade == '2010':
            print('We reccomend you, i am a hero: the walking dead story')
        if decade == '2020':
            print('We reccomend you, shibuya goldfish')
    if period == 'medium':
        decade= input ("which decade, (2010,2020): ")
        if decade == '2010':
            print('We reccomend you, aljin: demi-human')
        if decade == '2020':
            print ('We reccomend you, dandadan')
    if period == 'long':
        decade = input ("which decade, (2010,2020): ")
        if decade == '2010':
            print('we reccomend you, tokyo ghoul')
        if decade == '2020':
            print('we reccomend you, chainsaw man')