from face_detection import select_face
from face_swap import face_swap
import uuid
import cv2


class SwapperArgs:
    pass


def swap_faces(src_url, dst_img):
    src_img = cv2.imread(src_url)

    # Select src face
    src_points, src_shape, src_face = select_face(src_img)
    # Select dst face
    dst_points, dst_shape, dst_face = select_face(dst_img)

    if src_points is None or dst_points is None:
        return ''

    default_settings = SwapperArgs()
    default_settings.correct_color = False
    default_settings.warp_2d = False

    output = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, dst_img, default_settings)
    print(output.shape)

    output_file = f'static/output/{str(uuid.uuid4())}.jpg'
    cv2.imwrite(output_file, output)

    return '/' + output_file
