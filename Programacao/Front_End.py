# area das importações:
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel
from PyQt5.QtCore import Qt
from Programacao.Back_End import Processamento

# classe da inteface gráfica da aplciação:
class Interface(QWidget):
    # função de inicialização da classe:
    def __init__(self):
        super().__init__()

        # variaveis da tela:
        self.altura = 1
        self.largura = 1
        self.titulo = 'Face & Hand validator'

        # variavel relativa ao back-end do programa:
        self.backEnd = ""

        # QLabel do video da camera:
        self.video = QLabel(self)
        self.video.setStyleSheet('background-color: black')
        self.video.move(5, 5)

        # chama a função que calcula e posiciona o video da camera:
        self.tamanhoVideo()

        # QLabel de aguarde a valdiação:
        self.label1 = QLabel(self)
        self.label1.setText('Aguarde a validação:')
        self.label1.setStyleSheet("color: red; font-size: 32px")
        
        # chama a função que calcula e posiciona a label1:
        self.posicionaLabel1()

        # QLabel de segundos para validação:
        self.segundosValidacao = QLabel(self)
        self.segundosValidacao.setText('10s')
        self.segundosValidacao.setStyleSheet("color: red; font-size: 32px")
        
        # chama a função que calcula e posiciona o segundos da validação:
        self.posicionaSegundosValidacao()

        # QLabel de validado com sucesso:
        self.label2 = QLabel(self)
        self.label2.setText("Validado com sucesso!")
        self.label2.setStyleSheet("color: green; font-size: 28px")
        
        # chama a função que calcula e posiciona a label2:
        self.posicionaLabel2()

        # QLabel de fechando em:
        self.label3 = QLabel(self)
        self.label3.setText("Fechando em:")
        self.label3.setStyleSheet("color: green; font-size: 28px")
        
        # chama a função que calcula e posiciona a label3:
        self.posicionaLabel3()

        # QLabel de segundos para fechar:
        self.segundosFechar = QLabel(self)
        self.segundosFechar.setText('10s')
        self.segundosFechar.setStyleSheet("color: green; font-size: 32px")

        # chama a função que calcula e posiciona a label de segundos para fechar:
        self.posicionaSegundosFechar()

        # QLabel informação do que fazer:
        self.Informacao = QLabel(self)      
        self.Informacao.setText('Mostre seu rosto e uma mão na camera!')
        self.Informacao.setStyleSheet("color: black; font-size: 55px; background-color: yellow")
        self.Informacao.setAlignment(Qt.AlignHCenter)

        # chama a função que calcula e posiciona a label de informação do que fazer:
        self.posicionaInformacao()

        # instancia a classe do backEnd na variavel:
        self.backEnd = Processamento(self, self.video, self.label1, self.label2, self.label3, self.segundosValidacao, self.segundosFechar, self.Informacao)

        # chama a função que carrega a janela e suas propriedades:
        self.carregarJanela()

    # função que carrega a janela e suas propriedades:
    def carregarJanela(self):
        self.resize(self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.showFullScreen()
    
    # função que calcula e posiciona o video da camera:
    def tamanhoVideo(self):
        # obtem a geometria da tela:
        desktopGeometry = QDesktopWidget().availableGeometry() 

        # tamanho da altura da tela:
        height = desktopGeometry.height()

        # tamanho da largura da tela:
        width = desktopGeometry.width()

        # obtem a posição relativa ao eixoX do video da camera:
        eixoX = self.video.geometry().x()

        # obtem a posição relativa ao eixoY do video da camera:
        eixoY = self.video.geometry().y()

        # calcula a altura do video:
        calcHeight = int(height - eixoY - (height * 0.15)) 

        # calcula a largura do video:
        calcWidth = int((width - eixoX) * 0.75)

        # redimensiona o video da camera:
        self.video.resize(calcWidth, calcHeight)

    # função que calcula e posiciona a label1:
    def posicionaLabel1(self):
        # obtem a geometria da tela:
        desktopGeometry = QDesktopWidget().availableGeometry() 

        # tamanho da largura da tela:
        width = desktopGeometry.width()

        # tamanho da altura da tela:
        height = desktopGeometry.height()

        # obtem a largura do video da camera:
        width_video = self.video.geometry().width()

        # obtem o eixoX do video da camera:
        eixoX_video = self.video.geometry().x()

        # define a posição do eixoX da label1:
        eixoX = int(width_video + eixoX_video + (width * 0.0125))

        # define a posição do eixoY da label1:
        eixoY = int(height * 0.25)

        # move a label1:
        self.label1.move(eixoX, eixoY)

    # função que calcula e posiciona o segundos da validação:
    def posicionaSegundosValidacao(self):
        # para calcular a posição dos segundos de validação vai ser usado como base a Label1.
        
        # obtem a geometria da label1:
        label1Geometry = self.label1.geometry()

        # obtem o eixoX da label1:
        eixoX_Label1 = label1Geometry.x()
        
        # obtem o eixoY da label1:
        eixoY_Label1 = label1Geometry.y()

        # calcula eixoX da label de segundos de validação:
        eixoX = eixoX_Label1 + 130

        # calcula eixoY da label de segundos de validação:
        eixoY = eixoY_Label1 + 35

        # move a label de segundos de validação:
        self.segundosValidacao.move(eixoX, eixoY)
    
    # função que calcula e posiciona a label2:
    def posicionaLabel2(self):
        # para calcular a posição da label2 vai ser usado como base a Label1.
        
        # obtem a geometria da label1:
        label1Geometry = self.label1.geometry()

        # obtem o eixoX da label1:
        eixoX_Label1 = label1Geometry.x()
        
        # obtem o eixoY da label1:
        eixoY_Label1 = label1Geometry.y()

        # calcula eixoX da label2:
        eixoX = eixoX_Label1 + 10

        # calcula eixoY da label2:
        eixoY = eixoY_Label1 + 135

        # move a label2:
        self.label2.move(eixoX, eixoY)
    
    # função que calcula e posiciona a label3:
    def posicionaLabel3(self):
        # para calcular a posição da label3 vai ser usado como base a Label2.
        
        # obtem a geometria da label2:
        label1Geometry = self.label2.geometry()

        # obtem o eixoX da label2:
        eixoX_Label2 = label1Geometry.x()
        
        # obtem o eixoY da label2:
        eixoY_Label2 = label1Geometry.y()

        # calcula eixoX da label3:
        eixoX = eixoX_Label2 + 60

        # calcula eixoY da label3:
        eixoY = eixoY_Label2 + 35

        # move a label3:
        self.label3.move(eixoX, eixoY)

    # função que calcula e posiciona o segundos para fechar:
    def posicionaSegundosFechar(self):
        # para calcular a posição dos segundos para fechar vai ser usado como base a Label2.
        
        # obtem a geometria da label2:
        label1Geometry = self.label2.geometry()

        # obtem o eixoX da label2:
        eixoX_Label2 = label1Geometry.x()
        
        # obtem o eixoY da label2:
        eixoY_Label2 = label1Geometry.y()

        # calcula eixoX dos segundos para fechar:
        eixoX = eixoX_Label2 + 120

        # calcula eixoY dos segundos para fechar:
        eixoY = eixoY_Label2 + 70

        # move os segundos para fechar:
        self.segundosFechar.move(eixoX, eixoY)
    
    # função que calcula e posiciona a label de informação do que fazer:
    def posicionaInformacao(self):
        # obtem a geometria do video:
        videoGeometry = self.video.geometry()

        # obtem o eixoX do video:
        eixoX_video = videoGeometry.x()

        # obtem o eixoY do video:
        eixoY_video = videoGeometry.y()

        # obtem a altura do video:
        height_video = videoGeometry.height()

        # obtem a largura do video:
        width_video = videoGeometry.width()

        # calcula o eixoX da informação:
        eixoY = eixoY_video + height_video + 15

        # move a informação:
        self.Informacao.move(eixoX_video, eixoY)

        # redimensiona a informação:
        self.Informacao.resize(width_video, 75)

    # função que ve quando uma tecla é clicada:     
    def keyPressEvent(self, event):
            # verifica se a tecla clicada é o 'esc':
            if event.key() == Qt.Key_Escape:
                # fecha a tela:
                self.close()