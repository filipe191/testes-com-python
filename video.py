from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ops! Ocorreu um erro.")
    print("O download foi concluído com sucesso.")

link = input("Digite o URL do vídeo do YouTube: ")
Download(link)
#Baixa o pip install pytube sempre antes de usar