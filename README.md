# Controle do Mouse e Volume usando as Mãos

Este repositório contém dois exemplos de códigos para controlar o mouse e o volume do seu computador utilizando os movimentos das mãos.


<br>

<summary>Tecnologias utilizadas no projeto</summary>
<p>

---
|Descrição     | Versão  | Supported          |
| ----------   | ------- | ------------------ |
| Python       | 3.9     | :white_check_mark: |
| VScode       | 1.xx    | :white_check_mark: |
| OpenCV-python| 4.5.3   | :white_check_mark: |
| mediapipe    | 0.8.7.1 | :white_check_mark: |
| pyautogui    | 0.9.53  | :white_check_mark: |
---


</p>


### **Detalhe:**
No primeiro exemplo, temos o código controle_mouse.py, que permite controlar o mouse utilizando apenas os movimentos da mão. Quando você juntar o dedo polegar com o indicador, o código simulará um clique do mouse. Neste exemplo, utilizamos as bibliotecas Mediapipe e PyAutoGUI, que movimentam o ponteiro na tela.

No segundo exemplo de código, você será capaz de ajustar o volume apenas com o movimento do dedo indicador em relação ao polegar.


### **Executando o código para testes:**

Para executar o projeto em ambiente local, siga as boas práticas e crie um ambiente virtual separado para instalar as bibliotecas e executar o código. O processo de criação do ambiente virtual não será abordado aqui, mas você pode consultar a documentação sobre  [virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

1. Clone este diretório
```
git clone https://github.com/rodrigomartins806/controle_do_mouse.git
```
2. Crie um ambiente de desenvolvimento utilizando o venv ou virtualenv.

3. Execute o comando de instalação das dependências através do seguinte comando:
```
pip install -r requirements.txt
```
4. Para executar o código de controle do mouse, utilize o comando a seguir:
```
py controle_mouse.py
```
Se tudo ocorrer corretamente, uma janela para o controle do mouse será aberta, conforme mostrado na imagem abaixo:
<br>
<img src="https://github.com/rodrigomartins806/controle_do_mouse/blob/main/imagens/Controle%20do%20Mouse.png" width=515>

5. Para executar o segundo código, que controla o volume, utilize o comando abaixo:
```
py controle_volume_maos.py
```
Se tudo ocorrer corretamente, você será capaz de controlar o volume do seu computador utilizando os dedos indicador e polegar, como mostrado na imagem abaixo:
<br>
<img src="https://github.com/rodrigomartins806/controle_do_mouse/blob/main/imagens/Controle%20do%20Volume.png" width=515>



</p>
<p>Este é apenas um exemplo de utilização das bibliotecas OpenCV e Mediapipe, desenvolvido para fins de estudo.</p>



## Desenvolvedor

[<img src="https://avatars.githubusercontent.com/u/12385299?s=400&u=d146fdf8d2cec9e85473a80d696b1ee0f225790a&v=4" width=115><br><sub>Rodrigo Martins</sub>](https://github.com/rodrigomartins806)<br>
