import cv2
import dlib

# Carregar a imagem
imagem = cv2.imread('/content/people2.jpg')

# Inicializar o detector de rosto do dlib
detector_face = dlib.get_frontal_face_detector()

# Detectar rostos na imagem
deteccoes = detector_face(imagem)

# Desenhar retângulos ao redor de cada rosto detectado
for face in deteccoes:
    l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(imagem, (l, t), (r, b), (0, 255, 255), 2)

# Mostrar a imagem com os retângulos desenhados
cv2.imshow('Rostos Detectados', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
