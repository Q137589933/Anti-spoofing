# -------------------------------------- profile_detection ---------------------------------------
detect_frontal_face = 'profile_detection/haarcascades/haarcascade_frontalface_alt.xml'
detect_perfil_face = 'profile_detection/haarcascades/haarcascade_profileface.xml'

# -------------------------------------- emotion_detection ---------------------------------------
# modelo de deteccion de emociones
path_hopenet = 'hopenet_alpha1.pkl'
# Parametros del modelo, la imagen se debe convertir a una de tamaño 48x48 en escala de grises
w, h = 48, 48
rgb = False
labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
FRAME_LIMIT = 150  # 如果连续150帧没有改变状态(没有通过验证项目) 则验证失败
# definir la relacion de aspecto del ojo EAT
# definir el numero de frames consecutivos que debe estar por debajo del umbral
EYE_AR_THRESH = 0.23  # baseline
EYE_AR_CONSEC_FRAMES = 1
EYE_AR_TOTAL_THRESH = 1

MOUTH_OPEN_TOTAL_THRESH=1
# eye landmarks
landmarks = "shape_predictor_68_face_landmarks.dat"
device='cpu'