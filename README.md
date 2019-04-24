# Projeto para medir as dimensoes de objetos em uma imagem.
Trabalho da disciplina Sistemas Ubíquos (ESP203) do curso de Programa de Pós-Graduação em Engenharia de Sistemas e Produtos - IFBA

Este projeto tem o intuito de verificar as dimensões de um ou mais objetos em uma imagem.

* [Quais ferramentas foram usadas](#quais-ferramentas-foram-usadas-e-configuracoes)
* [Comandos](#comandos)
* [Configurações de execução do projeto](#configuracoes-de-execucao-do-projeto)

## Quais ferramentas foram usadas e configurações

Para atingir o objetivo do projeto foi utilizado raspberry pi 3b+, uma webcam logitech c510 e um sensor ultrassônico conectado ao Raspberry pi.

Está em anexo na pasta /media fotos retiradas dos objetos e do esquema montado para capturar imagem e distância.

Para poder trabalhar com o opencv foram instaladas algumas bibliotecas e ferramentas. Está abaixo a lista de comandos utilizados para ajudar na instalação das depedências do projeto.

* sudo apt-get -y install libjpeg8-dev libjasper-dev libpng12-dev
* sudo apt-get -y install libtiff5-dev libtiff-dev
* sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
* sudo apt-get -y install libxine2-dev libv4l-dev
* sudo apt-get -y install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
* sudo apt-get -y install libgtk2.0-dev libtbb-dev qt5-default
* sudo apt-get -y install libatlas-base-dev
* sudo apt-get -y install libmp3lame-dev libtheora-dev
* sudo apt-get -y install libvorbis-dev libxvidcore-dev libx264-dev
* sudo apt-get -y install libopencore-amrnb-dev libopencore-amrwb-dev
* sudo apt-get -y install libavresample-dev
* sudo apt-get -y install python3-pip
* sudo apt-get install libgtk-3-dev
* sudo apt-get install libcanberra-gtk*
* sudo apt-get install libcanberra-gtk3*
* sudo apt-get install libatlas-base-dev gfortran
* pip3 install opencv-python
* sudo -H pip3 install -U pip numpy
* sudo apt-get install python3-tk
* sudo apt-get install python-imaging-tk
* pip3 install imutils
* sudo apt-get install python3-pil python3-pil.imagetk

| Ferramentas/bibliotecas|
|------------|
| opencv 3.4.4 | 

## Comandos 

Para rodar o projeto basta executar o comando:

				python3 startProjeto.py -o /home/pi/object_size_opencv_python/

Onde o argumento -o refere-se ao diretório aonde deseja armazenar a imagem capturada e as imagens processadas.

## Configurações de execução do projeto

Além das bibliotecas citadas no tópico das ferramentar usadas acima eu tive que definir portas e valores estáticos para que seja possível o uso do sensor e aplicar a fórmula  do cálculo das dimensões do objeto.

Para este projeto foi utilizado sensor ultrassônico (HC-SR04) para medição da distância dos objetos eu utilizei as respectivas entradas e saídas do Raspberry Pi.

1. GPIO 18 como porta de conexão com a interface trigger do sensor
2. GPIO 27 como porta de conexão com a interface echo do sensor

Também como forma de parâmetro e execução do projeto  foi utilizado uma webcam plug-and-play com tais configurações

1. comprimento do foco: 4.00 mm
2. Tamanho do sensor: 3.58x2.02 mm (wxh)

Foi utilizada a função [Pinhole camera model](https://en.wikipedia.org/wiki/Pinhole_camera_model) sendo assim está algumas características da camera no código para poder fazer a conversão de pixels para milímetros.
Caso tenha curiosidade na fórmula aplicada para achar a altura e a largura do objeto, está abaixo a fórmula utilizada.
```
{Distance to object(mm)} = f(mm) x {real height(mm)} x {image height(pixels)} / {object height(pixels)} x {sensor height(mm)}
```

1. Distance to object(mm) é a distância obtida pelo sensor ultrassônico
2. f(mm) é o comprimento do foco da camera.
3. image height(pixels) é a altura da imagem em pixels.
4. real height(mm) é o que nós queremos identificar.
5. object height(pixels) é a altura do objeto em pixels

Caso ainda haja dúvidas sobre a abordagem selecionada esnte link no [StackOverflow](https://photo.stackexchange.com/questions/12434/how-do-i-calculate-the-distance-of-an-object-in-a-photo) pode auxiliar.
