# area das importações:
import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.HandTrackingModule import HandDetector
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import datetime

# classe da programação por trás da aplicação:
class Processamento():
    # função de inicialização da classe:
    def __init__(self, tela, video, l1, l2, l3, sValida, sFecha, informacao):
        super().__init__()

        # variaveis da classe relativas a classe anterior:
        self.tela = tela
        self.video = video
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.sValida = sValida
        self.sFecha = sFecha
        self.informacao = informacao

        # abre a camera padrão:
        self.webCam = cv2.VideoCapture(0)

        # variavel que detecta o rosto:
        self.detectorFace = FaceMeshDetector(maxFaces=1) # definindo para reconhecer apenas um rosto por vez.

        # variavel que detecta a mão:
        self.detectorHand = HandDetector(maxHands=1) # definindo para reconhecer apenas uma mão por vez.
        
        # timer que atualiza o frame do video:
        timer_video = QTimer(tela)
        timer_video.timeout.connect(self.atualizaFrame)
        timer_video.start(1)

        # variaveis que contarão os segundos que aparecem na tela:
        self.tempoSegundos = 11 # é os segundos que aparecem na tela, define 11 para na hora que aparecer na tela ele ir de 10 a 0.
        self.parte = True # aqui verifica se está na parte de validação ou na parte de fechar, sendo validação -> true e fechar -> false.
        self.segundoAux = 0 # esse é os segundos auxiliares pare verificar se houve mudança de segundo.
        
        # chama a função que faz uma ação ao inciar a validação:
        self.iniciaValidacao()
    
    # função que deixa os campos invisiveis:
    def setInvisibleCampos(self):
        self.l1.setVisible(False)
        self.l2.setVisible(False)
        self.l3.setVisible(False)    
        self.sValida.setVisible(False)
        self.sFecha.setVisible(False)
    
    # função que define os padrão os relacionados aos segundos:
    def segundosDefault(self):
        self.sValida.setText('10s')
        self.sFecha.setText('10s')
        self.tempoSegundos = 11
        self.parte = True
    
    # função que exibe os campos ta parte 1 de tempo:
    def setVisibleCamposPt1(self):
        self.l1.setVisible(True)
        self.sValida.setVisible(True)

    # função que exibe os campos ta parte 2 de tempo:
    def setVisibleCamposPt2(self):
        self.l2.setVisible(True)
        self.l3.setVisible(True)   
        self.sFecha.setVisible(True)
    
    # função que define o tamanho do video da webCam:
    def tamanhoWebCam(self, frame):
        width = self.video.geometry().width()
        height = self.video.geometry().height()
        resize = cv2.resize(frame, (width, height))
        return resize

    # função que atualiza o frame do video da camera:
    def atualizaFrame(self):
        # captura o frame da camera:
        sucesso, frame = self.webCam.read()

        # if que verifica se a camera foi aberta com sucesso:
        if sucesso:
            # redimensiona o video:
            frame = self.tamanhoWebCam(frame) # chama a função que define o tamanho do video da webCam

            # inverte a camera (não é necessário isso, podendo ser essa linha apagada ou comentada!):
            frame = cv2.flip(frame, 1)

            # detecta a face:
            # frame, faces = self.detectorFace.findFaceMesh(frame) # aqui exibe o desenho no rosto.
            frame, faces = self.detectorFace.findFaceMesh(frame, False)
            
            # detecta a mao:
            # hands, _ = self.detectorHand.findHands(frame) # aqui exibe o desenho na mão.
            hands = self.detectorHand.findHands(frame, False)

            # if que verifica se há mão e face na camera:
            if faces and hands:
                self.controlSeconds() # chama a função que ontrola os segundos do tempo:
                self.informacao.setVisible(False) # deixa a label de informação de como usar invisivel.
            else:
                self.setInvisibleCampos() # chama a função que deixa os campos invisiveis:
                self.informacao.setVisible(True) # deixa a label de informação de como usar visivel.
                self.segundosDefault() # chama a função que define os padrão os relacionados aos segundos

            # converte o frame para um formato RGB:
            rgbFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # cria o QImage do frame:
            h, w, ch = rgbFrame.shape
            image = QImage(rgbFrame.data, w, h, ch * w, QImage.Format_RGB888)

            # cria o QPixmap do QImage:
            pixmap = QPixmap.fromImage(image)

            # atualiza a label que exibira o frame do video:
            self.video.setPixmap(pixmap)
    
    # função que ontrola os segundos do tempo:
    def controlSeconds(self):
        agora = datetime.datetime.now() # obtem a data atual do sistema:
        segundos = agora.strftime("%S") # obtem o segundo da data atual
        # if que verifica se os segundo auxiliar é diferente do segundo atual:
        if self.segundoAux != segundos: 
            self.segundoAux = segundos # atualiza o segundo auxiliar para o valor do segundo autal.
            self.tempoSegundos -= 1
            # verifica em qual das partes o tempo está "mexendo":
            if self.parte:
                self.setVisibleCamposPt1() # chama a função que exibe os campos ta parte 1 de tempo.
                self.sValida.setText(f'{self.tempoSegundos}s') # define o texto do segundo na label de segundos de validação.
                # verifica se o segundos da contagem regressiva é igual a 0.
                if self.tempoSegundos == 0:
                    self.parte = False # muda a parte informando que os segundos agora "vão mexer" na parte 2 do tempo
                    self.tempoSegundos = 11 # define os segundos como 11 da cotagem
                    self.confirmaValidacao() # chama a função que faz uma ação ao confirmar a validação.
            else:
                self.setVisibleCamposPt2() # chama a função que exibe os campos ta parte 2 de tempo:
                self.sFecha.setText(f'{self.tempoSegundos}s') # define o texto do segundo na label de segundos para fechar.
                # verifica se os segundos da contagem regressiva é igual a -1:
                if self.tempoSegundos == -1:
                    self.fechaValidacao()# chama a função que faz uma ação ao fechar a validação 
                    # quando os segundos da contagem for igual a -1 o programa será fechado:
                    self.tela.close()

    # função que faz uma ação ao inciar a validação:
    def iniciaValidacao(self):
        print(f'validação iniciada: {datetime.datetime.now()}')
    
    # função que faz uma ação ao confirmar a validação:
    def confirmaValidacao(self):
        print(f'validação confirmada: {datetime.datetime.now()}')
    
    # função que faz uma ação ao fechar a validação:
    def fechaValidacao(self):
        print(f'validação fechada: {datetime.datetime.now()}')