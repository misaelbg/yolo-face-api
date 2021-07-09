def frame(camera, detector):
    while True:
        if camera.stopped:
            camera.stop()
            break
        else:
            frame = camera.frame
            rects = detector.detect(frame)

            for xywh, conf, landmarks in rects:
                detector.draw_face_box(frame, xywh, conf, landmarks)

            frame = camera.encode_frame(frame)

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
