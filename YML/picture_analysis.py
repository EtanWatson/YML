
from YML.config import Config_YouTu

from YML.settings import BASE_DIR


# 初始化
youtu = you_tu = Config_YouTu().get_you_tu();


# 人脸检索 1:N 找到最相似的N张图片
def multi_face_identify(image_path):
    response = you_tu.MultiFaceIdentify(group_id='group_0', group_ids='group_0',
                                   image_path= BASE_DIR+image_path)

    return response;

# 解析相似的N个人脸的图片名称，返回一个数组
def parse_multi_res(image_path):
    res = multi_face_identify(image_path).get('results')[0].get('candidates')
    return res



if __name__ == '__main__':
    res = multi_face_identify()
    print(res)