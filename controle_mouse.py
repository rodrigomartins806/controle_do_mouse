import cv2
import mediapipe as mp
import pyautogui

# Configurações do pyautogui para o tamanho da tela
screen_width, screen_height = pyautogui.size()

# Configurações do mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicialização do mediapipe
with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    # Variável para controlar o estado do clique do mouse
    is_mouse_clicked = False

    # Inicialização da webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # Leitura do frame da webcam
        ret, frame = cap.read()

        if not ret:
            break

        # Conversão do frame para RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Espelha a imagem horizontalmente para corresponder ao movimento da mão
        image = cv2.flip(image, 1)

        # Processa a imagem com o mediapipe
        results = hands.process(image)

        # Verifica se há mãos detectadas
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Obtém a bounding box da mão
                bounding_box = mp_hands.HandLandmark.WRIST

                # Calcula a posição da palma da mão usando a bounding box
                x = (hand_landmarks.landmark[bounding_box].x + hand_landmarks.landmark[
                    mp_hands.HandLandmark.THUMB_CMC].x) / 2
                y = (hand_landmarks.landmark[bounding_box].y + hand_landmarks.landmark[
                    mp_hands.HandLandmark.THUMB_CMC].y) / 2

                # Converte as coordenadas normalizadas para as coordenadas do monitor
                x_pixel = int(x * screen_width)
                y_pixel = int(y * screen_height)

                # Move o ponteiro do mouse para a posição detectada
                pyautogui.moveTo(x_pixel, y_pixel)

                # Verifica a distância entre o dedo indicador e o polegar
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

                # Verifica se os dedos indicador e polegar estão juntos para fazer o clique
                if distance < 0.05:  # Ajuste esse valor conforme necessário
                    if not is_mouse_clicked:
                        # Faz o clique do botão esquerdo do mouse
                        pyautogui.mouseDown(button='left')
                        is_mouse_clicked = True
                else:
                    if is_mouse_clicked:
                        # Libera o clique do botão esquerdo do mouse
                        pyautogui.mouseUp(button='left')
                        is_mouse_clicked = False
        # Desenha as landmarks das mãos no frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Exibe a imagem resultante
        cv2.imshow('Hand Tracking', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        # Verifica se a tecla 'q' foi pressionada para sair do loop
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Libera a captura da webcam e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()


