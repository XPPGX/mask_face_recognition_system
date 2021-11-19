import numpy as np
import cv2
import dlib

Image_size = 64

def face_catch(img,filename_f):
    detector = dlib.get_frontal_face_detector()
    error_code = -1
    right_code = 1
    face_rects,score,idx = detector.run(img,0)
    try:
        print(face_rects[0])
        for i,d in enumerate(face_rects):
            x1 = d.left()
            y1 = d.top()
            x2 = d.right()
            y2 = d.bottom()
            new_img_name =  'uploads/face_' + filename_f + '.jpg'
            print(new_img_name)
            img_save = img[y1:y2,x1:x2]
            cv2.imwrite(new_img_name,img_save)
        return right_code
    except:
        return error_code

def face_catch_api(filename):
    print(filename)
    filename_f = filename.split('\\')[-1].split('.')[0]
    img = cv2.imread(filename)
    code = face_catch(img,filename_f)
    if (code == -1):
        return 'capture_fail'
    else:
        return_name = 'face_' + filename_f + '.jpg'
        return return_name

if __name__ == '__main__':
    filename = 'test_image/other_test/022.jpg'
    filename_f = filename.split('/')[-1].split('.')[0]
    img = cv2.imread(filename)
    face_catch(filename)
    '''img_name = 'uploads/0_1632.jpg'
    img = cv2.imread(img_name)
    code = face_catch(img,'aaa')
    print(code)'''