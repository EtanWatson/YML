import TencentYoutuyun

# YouTu初始化配置信息
class Config_YouTu:
    appid = '10131921'
    secret_id = 'AKIDX2NwSn076va4NV4EvRmvtgHhw1whFrBK'
    secret_key = '61mLjx0sZ5QbcT9ey9A0f8QPEtNhqocJ'
    userid = '1029580951'

    # 有图开放平台
    end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT

    # 初始化
    youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

    def get_you_tu(self):
        return self.youtu