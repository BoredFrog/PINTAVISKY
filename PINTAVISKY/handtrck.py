import cv2 
import mediapipe as mp


class handDetector():
    def __init__(self, mode=False,complexity=1, maxHands=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.complexity=complexity

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw =True):  #para encontrar las manos
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


    def findposition(self, img, handNo=0, draw=True): #para encontrar la posición de las manos
        lmList=[]
        if self.results.multi_hand_landmarks:
            thehand = self.results.multi_hand_landmarks[handNo]
            for lm in thehand.landmark:
                h , w , c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return lmList            

    def fingersup(self, img): #la posición de cada uno de los dedos
        pos = self.findposition(img, draw=False)
        self.upfingers = []
        if pos:
            self.upfingers.append((pos[4][1] < pos[3][1] and (pos[5][0]-pos[4][0]> 10))) #pulgar
            self.upfingers.append((pos[8][1] < pos[7][1] and pos[7][1] < pos[6][1])) #indice
            self.upfingers.append((pos[12][1] < pos[11][1] and pos[11][1] < pos[10][1])) #medio
            self.upfingers.append((pos[16][1] < pos[15][1] and pos[15][1] < pos[14][1])) #anular
            self.upfingers.append((pos[20][1] < pos[19][1] and pos[19][1] < pos[18][1])) #meñique
        return self.upfingers

    
  
  