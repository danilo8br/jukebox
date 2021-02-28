import pygame

def jukebox():
    print("               Jukebox Donato 8000")
    print("=-" * 25)
    moedas = int(input('Quantas fichas você deseja? '))
    print(f"Você comprou {moedas} fichas, você pode escolher {moedas} musicas.\n")
    while moedas != 0:
        print("-=" * 25)
        print("""               Lista de Musicas\n
            1 - Blink_182 - I miss you" 
            2 - The Offspring - The Kids Aren't Alright"
            3 - Bon Jovi - Livin' On A Prayer"
            4 - Green Day - Holiday"
            5 - Led Zeppelin - Stairway to Heaven"
            6 - David Bowie - Heroes
            7 - Red Hot Chili Peppers - Under the Bridge
            8 - Zebrahead - All My Friends Are Nobodies
            9 - Chris Isaak - Wicked Game
            10 - Interpol - Untitled""")
        print("-=" * 25)
        escolhida = int(input('Qual musica deseja ouvir? (Digite o número da musica) '))
        if escolhida == 1:
            pygame.mixer.init()
            pygame.mixer.music.load("blink-182 - I Miss You (Official Video)_50k.mp3")
            pygame.mixer.music.play()
            print('Tocando: Blink-182 - I miss you')
        elif escolhida == 2:
            pygame.mixer.init()
            pygame.mixer.music.load("The Offspring - The Kids Aren t Alright (Official Music Video)_50k.mp3")
            pygame.mixer.music.play()
            print("Tocando: The Offspring - The Kids Aren't alright")
        elif escolhida == 3:
            pygame.mixer.init()
            pygame.mixer.music.load("Bon Jovi - Livin' On A Prayer (Official Music Video).mp3")
            pygame.mixer.music.play()
            print("Tocando: Bon Jovi - Livin' On A Prayer")
        elif escolhida == 4:
            pygame.mixer.init()
            pygame.mixer.music.load("Green Day_ Holiday - Official Video _50k.mp3")
            pygame.mixer.music.play()
            print("Tocando: Green Day - Holiday")
        elif escolhida == 5:
            pygame.mixer.init()
            pygame.mixer.music.load("Led Zeppelin - Stairway To Heaven (Official Audio)_50k.mp3")
            pygame.mixer.music.play()
            print("Tocando: Led Zeppelin - Stairway To Heaven")
        elif escolhida == 6:
            pygame.mixer.init()
            pygame.mixer.music.load("David Bowie - Heroes (Official Video)_50k.mp3")
            pygame.mixer.music.play()
            print("Tocando: David Bowie - Heroes")
        elif escolhida == 7:
            pygame.mixer.init()
            pygame.mixer.music.load("Red Hot Chili Peppers - Under The Bridge Official Music Video _50k.mp3")
            pygame.mixer.music.play()
            print("Tocando: Red Hot Chili Pepper - Under the Bridge")
        elif escolhida == 8:
            pygame.mixer.init()
            pygame.mixer.music.load("Zebrahead All My Friends Are Nobodies.mp3")
            pygame.mixer.music.play()
            print("Tocando: Zebrahead - All My Friends Are Nobodies")
        elif escolhida == 9:
            pygame.mixer.init()
            pygame.mixer.music.load("Wicked Game_50k.mp3")
            pygame.mixer.music.play()
            print("Tocando: Chris Isaak - Wicked Game")
        elif escolhida == 10:
            pygame.mixer.init()
            pygame.mixer.music.load("Untitled_50k.mp3")
            pygame.mixer.music.play()
            print("Tocando: Interpol - Untitled")
        else:
            print("Por favor, selecione  musicas de 1 a 10.")
        trocar = str(input('Deseja trocar de musica? ')).upper()
        if trocar == "SIM":
            moedas -= 1
            print(f"Restam {moedas} fichas.")     
        else:
            print("♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪")
        print("Obrigado por utilizar o Jukebox Donato 8000, volte sempre!")

jukebox()