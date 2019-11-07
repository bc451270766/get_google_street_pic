# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 14:46
# @Author  : Baichen
# @File    : get_google_street_pic.py

import urllib.request

class Google_street():
    def __init__(self):
        self.key = 'AIzaSyAheAbaaiIOYFPltUA2p40JAk2ed8t2xqI'
        self.location_file_name = './location.txt'
        self.pic_dir = './google_street_pic/'

    #　一个生成器，返回经纬度
    def get_lat_lng(self):
        print(self.location_file_name)
        if self.location_file_name.split('.')[-1] == 'txt':
            fp = open(self.location_file_name, "r")
            for line in fp.readlines():
                print(line)
                lo = line.strip().split('_')
                lng = lo[0]
                lat = lo[1]
                yield lng, lat
        else:
            raise IOError('Location file must be txt.')

    def make_url(self, lng, lat):
        for pitch in [y for y in range(0, 61, 60)]:
            for heading in [x for x in range(0, 360, 360)]:
                pic_name = self.pic_dir + lng + "_" + lat + "_" + str(pitch) + "_" + str(heading) + "_" + ".JPG"
                pic_url = "https://maps.googleapis.com/maps/api/streetview?size=936x537&location=" + \
                          lng + "," + lat + "&pitch=" + str(pitch) + "&heading=" + str(heading) + \
                          "&key=" + self.key
                print(pic_url)
                yield pic_name, pic_url

    def download(self):
        for lng, lat in self.get_lat_lng():
            print(lng, lat)
            for pic_name, pic_url in self.make_url(lng, lat):
                # url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"
                # 保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
                conn = urllib.request.urlopen(pic_url)

                f = open(pic_name, 'wb')  # wb以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                f.write(conn.read())
                f.close()
                print('Pic Saved!')


if __name__ == '__main__':
    gs = Google_street()
    # gs.get_lat_lng()
    gs.download()
