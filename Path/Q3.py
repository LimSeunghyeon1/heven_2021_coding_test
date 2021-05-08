'''
시작 시각 :17시
종료 시각 :17시 30분까지 하고 20시 30분 시작 21시 완료

Google Drive > 20년 화성대회 > 로깅 영상 > 정지선 인식용 영상에 업로드된 영상을 기반으로,
해당 영상에서 정지선이 인식되면 "Stop"을 출력하는 프로그램을 작성해 주세요.

이미지가 아니라 영상을 로드하셔서 처리해야 하며, 영상은 Repository에 Push하지 말아주세요.

실제 테스트 시에는 해당 Google Drive에 있는 영상 파일을 파일명 변경 없이 사용할 예정입니다.
최상 폴더에 영상을 첨부했을 때 바로 코드를 실행해서 결과물을 볼 수 있도록 작성해 주세요.
'''
## 기존 코드에서 숫자를 조금 수정했습니다
import cv2
import numpy as np

video=cv2.VideoCapture('stopline3.mp4')
white_color=(np.array([150, 150, 150],dtype='uint8'),np.array([255, 255, 255], dtype="uint8"))

while video.isOpened():
    ret,frame=video.read()
    if ret==True:

        height, width = frame.shape[:2]
        #print(height, width)
        pts1 = np.float32([(100, 400),
                           (200, 480),
                           (550, 480),
                           (500, 400),
                           ])
        #new_frame=frame[400:480,:,:]

        pts2 = np.float32([(0 * width, 0 * height),
                           (0 * width, 1 * height),
                           (1 * width, 1 * height),
                           (1 * width, 0 * height)])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        wrapped_img = cv2.warpPerspective(frame, matrix, (width, height), flags=cv2.INTER_CUBIC + cv2.INTER_LINEAR)
        cv2.imshow("wrapped_img2", wrapped_img)
        (minRange,maxRange)=white_color
        mask = cv2.inRange(wrapped_img, minRange, maxRange)
        cv2.imshow("wrapped_img", mask)
        left_high = (int(0.3 * width), int(0.93 * height))
        right_low = (int(0.85 * width), int(0.97 * height))
        area = (right_low[0] - left_high[0]) * (right_low[1] - left_high[1])
        s_img = mask[left_high[1]:right_low[1], left_high[0]:right_low[0]]
        cv2.imshow("s_img", s_img)
        nums_flatten = s_img.reshape(-1)
        num = cv2.countNonZero(nums_flatten)

        # 사각형 지역 안에 일정 비율 이상 하얀 픽셀이 존재하면 정지선으로 판단한다.
        if num > int(area * 0.9):
            print("STOP")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break