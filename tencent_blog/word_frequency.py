# -*- coding:utf-8 -*-

word_frequency = {'刘星杰': 27, '跟不上': 27, 'wyw': 26, '李志国': 25, '追风少年Wq': 24, '邵晶晶': 24, '非凡': 24, '天爱LOVE': 24, '薛进财': 23,
                  '-----筱悠': 23, '魏': 23, '景承萱': 22, 'hanjingjing': 22, '冯兴浩': 21, 'Ps暗夜精灵': 21, '陈晓': 19, '谢星': 18, '刘宛蓉': 18,
                  'LUO4444': 18, '槐米': 17, '刘克楠': 17, '邓克繁': 16, '王辉': 16, '陈乐': 16, '时光吹老了少年的梦': 15, '刘寰清': 15, '财哥': 15, '冷残影': 15,
                  '微博精灵': 15, '张憬': 15, '陈科东': 14, '蓝枫': 14, '郁义': 14, '扬': 14, '王玉娇': 14, '于建恒': 14, '天上掉下来的小傻瓜': 13, '张文瑞': 13,
                  'kaikei': 13, '陶维东': 13, '兽兽姐': 13, '尚永旺': 13, '刘昊民': 13, '简爱ing': 13, '思念': 12, '茄子': 12, '哑缺': 12, '孙靖': 12,
                  '暗香': 12, '泛滥小青年': 12, '张晓雪': 11, 'Monica': 11, '赵帅奇': 11, '杨新宇': 11, '高国强': 11, '受伤后的坚强': 11, '笨': 11, '王飚': 11,
                  '路小雪': 10, '杨勇': 10, '吴映利': 10, '夏钰翔': 10, '石祯珍': 10, '凯凯': 10, 'XWB': 10, '张天福': 10, '雷双瑜': 10, '繁华落幕丶写不完的温柔': 9,
                  '高': 9, '李艳绒': 9, '差等生L': 9, '宋鹏': 9, '逍遥': 9, '莫言': 9, '扯不清的暧昧': 9, '李文瑞': 9, '刘兴武': 9, '宋颖颖': 9, '曹璐': 9, '魏哲': 9,
                  '心月': 9, '-璇子': 9, '7': 9, '释': 9, '徐志淑': 9, '鳞': 9, '张力': 9, '李航': 8, '王诗奇': 8, '张有鹏': 8, '虎志信': 8, '潘玉': 8,
                  '王稷尧': 8, '晴': 8, '玮': 8, '周晓': 8, '康熙后裔': 8, '任学舜': 8, '阳光': 8, '含泪的微笑': 8, '昊昊': 8, '张东莉': 8, '赵彤祝华晨宇生日快乐': 8,
                  '黄耀娥': 8, '苏晋安': 8, '方朕文婧': 8, '奋斗': 8, '李东岳': 7, '爱吃小布丁': 7, '裴艳文': 7, '黄玉琛': 7, '郭懿': 7, '丶小新没蜡笔': 7, '相言': 7,
                  '自怨自艾': 7, '姜思劼': 7, '花瞳迷离': 7, '月神夜': 7, '丁宝': 7, '834394774': 7, '徐鹏': 7, '死掉发动': 7, '贺富鹏': 7, '王哲': 7, '亁道夫': 7,
                  'QQ音乐': 7, '金小玉': 7, 'Sun': 7, '崔敬文': 7, '放肆': 7, '王世琪': 7, '流水简单': 7, '韦应鹏': 7, '苏墨白': 7, '张春苗': 7, 'rxd': 7,
                  '方丈': 7, '末上光': 7, 'kiss': 7, '安小白BZJ': 7, '刘志炜': 6, '舒皖清': 6, '樱花上的蝶': 6, '蹲街-式寂寞': 6, '胡富珺': 6, '徐明明': 6, '胡福东': 6,
                  '小不着调的vR3': 6, '累可以不爱': 6, 'StarKids': 6, 'CoColovec': 6, '王萌': 6, '沈仪': 6, '刘文凯': 6, '董昊': 6, 'zqj': 6, '紫金零': 6,
                  'NewDivide': 6, 'Candy未待续': 6, '杨哲': 6, '刘翔': 6, '去无的止境': 6, '白瑞': 6, '付磊': 6, '张俊楠': 6, '007': 6, '王明威': 6, '李欣': 6,
                  '王桉': 6, 'love劼儿宝贝': 6, '王嘉路': 6, '张振平': 6, '张程程': 6, '赵通通': 6, '123456qwe': 6, '守望你-永远的-萌宠': 6, '一粒砂': 6, '王鹏程': 6,
                  '田精忠': 6, '抱抱': 6, '张裕沁': 6, '魏文菁': 6, '强': 6, '宋娜': 6, '侯雨轩': 6, '谈继魁': 6, '莫紫爱': 6, '李映辉': 6, '关文武': 6, '张程飞': 6,
                  '唐春莉': 6, '白箐儿': 5, '赵凌霄': 5, '袁鹏涛': 5, '田甜': 5, '李波': 5, 'canbb': 5, '徐志刚': 5, '王立': 5, '陈天丁': 5, '1-2-3': 5,
                  '贝坚强': 5, '黑': 5, '司航': 5, '甘璐': 5, '鬼鬼': 5, '小晓清': 5, '吴斌': 5, '守望那片天': 5, '芃芃': 5, '张奋德': 5, '君子乾乾': 5, '贾玉涵': 5,
                  '猫猫': 5, '夕亦残潋若丶': 5, '薛巍巍': 5, '朱晋': 5, '哲哲': 5, '艹尼玛': 5, '包捷': 5, '劉先森': 5, '卢凯': 5, '小磊': 5, '阳日直狮': 5, '张国鑫': 5,
                  '嫣': 5, 'QQ农牧场': 5, '张杰': 5, '夏洛': 5, '阳阳': 5, '李客': 5, '李强': 5, '谁是人间未归客': 5, '李朔': 5, 'kkkk': 5, '王鸿鈺': 5,
                  '慕容紫英': 5, '杨淑琴': 5, '李诗豪': 5, '李世强': 5, 'nuan': 5, '南国旧梦': 5, '贺国琪': 5, '陈洁': 5, '帆帆': 5, '赤那张宝元': 5, 'Gentle-X': 5,
                  '陈凯': 5, '蔡振科': 5, '王斌斌': 5, '听我听你': 5, '李珍': 5, '陌北城': 5, '张天宇': 5, '高清宇': 4, '乱-': 4, '龙': 4, '张雅': 4, '吕国玲': 4,
                  '骗子': 4, '胖大海': 4, 'CC': 4, '何招靖': 4, '雅': 4, '腾讯微博Android版': 4, '康辉': 4, '非凡业务': 4, '简': 4, '石云太': 4, '李': 4,
                  '李娇': 4, '冯昱才': 4, '牛彦翔': 4, '陈博': 4, '浮若年华': 4, '戴菲菲': 4, '古傲狂生': 4, '苏苏': 4, '丁慧': 4, '张宇伟': 4, '涛涛': 4, '谢娜': 4,
                  '听说我们不曾落泪': 4, 'momoG': 4, 'BiNsMaRt': 4, '未央': 4, '王兴斌': 4, '她比烟花寂寞': 4, '刘国民': 4, '-果果-': 4, '琪': 4, '秦瑶瑶': 4,
                  '高菲': 4, '郭洁': 4, '高文扬': 4, '邵芮': 4, '武双': 4, '南宫破域': 4, '申婉儒': 4, '找不到合适的伞我宁可淋雨': 4, '李凯': 4, '王陆虎': 4,
                  '13-水工八班王天健': 4, '装逼有罪': 4, '刘玮': 4, '马耀乾': 4, '如果不曾遇见你': 4, '赵': 4, '我的左手边是你的右手': 4, '陌颜残殇': 4, '白少': 4, '王璇': 4,
                  '岳潇煜': 4, '王菲': 4, '高海澎': 4, '祁君彦': 4, '苏珊Zhangyuron': 4, '马耀远': 4, '韩小娜': 4, '安分守己': 4, 'leo': 4, '兰儿': 4, '武伟': 4,
                  '肖涛涛': 4, 'MENG浩': 4, '高永忠': 4, '天黑请闭眼': 4, '盼': 4, '张仲源': 4, '疯子': 4, '我就是我': 4, '李睿豪': 4, '焦婉滢': 4, '高振宇': 4,
                  '海Hi': 4, '新颜': 4, '孙斌': 4, '会': 4, '路国中': 4, '靳昕': 4, '王昭荣': 4, '段樱玲': 4, 'feel厮守': 4, '高燕': 4, '帝国': 4, '王振': 4,
                  '如果深情是死罪我愿意': 4, '丁丁': 4}
