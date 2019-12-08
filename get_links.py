import os
import waybackpack


if __name__ == '__main__':
    os.system('waybackpack --from-date 201401 --to-date 201912 --list www.bostonglobe.com >..//target_links//bostonglobe.txt')
    os.system('waybackpack --from-date 201401 --to-date 201912 --list www.wgbh.org >..//target_links//wgbh.txt')
    os.system('waybackpack --from-date 201401 --to-date 201912 --list www.wbur.org >..//target_links//wbur.txt')