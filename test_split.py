#coding=utf8
import re


a = re.split(u'，|。', u'我是独生女，他们的希望都在我这里 。越是')
for one in a:
    print one

content = u'''我是独生女，他们的希望都在我这里 。越是这样想的越多，想的越多越痛苦，我快要发疯啦，我的性格本身就急躁，再加上这件事压抑着，谁都无法倾诉，更加抑郁。
　　今天，我去相亲，他看见了，我在这一年里总是挣扎着闹着说分手，但总是狠不下心，觉得他想我身体的一部分一样珍贵而难以割舍，爱他已经成为我的习惯。每次因为他没有办法陪在我身边而生气，我都很懊恼，我决心一定要离开他，发誓一定要找到一个能陪我的人，但总是遇不到。每次我闹，他都耐心哄我，我们就又在一起了，我痛恨自己对他的依赖，我自认是个自立的女孩，但这是我第一次如此深切的爱一个，我做不到。
　　今天，我说，哥哥，请你放开我的手吧，我求他给我希望，哪怕是骗我，我都会等他的，但他从来没说过，他说不能拿我的幸福开玩笑。可是，他应该知道，我的幸福就是他啊，但现实让我们不得不以地下的关系维持着这份爱。也许好多人会鄙视我，但爱是真的，就该得到尊重。今天，我在他怀里哭了，他说叫我把握好能给我幸福的人，以后有什么委屈哥哥的肩膀永远向你敞开。临分开时，我对他说，哥哥，我爱你，他说我永远爱你，我想，我们正式结束了，我回到家里大哭了一场。
　　今天，我说，哥哥，请你放开我的手吧，我求他给我希望，哪怕是骗我，我都会等他的，可是，他应该知道，我的幸福就是他啊，但现实让我们不得不以地下的关系维持着这份爱。也许好多人会鄙视我，但爱是真的，就该得到尊重。
    。今天，我在他怀里哭了，他说叫我把握好能给我幸福的人，以后有什么委屈哥哥的肩膀永远向你敞开。临分开时，我对他说，哥哥，我爱你，他说我永远爱你，我想，我们正式结束了，我回到家里大哭了一场。'''

content = u'''我是独生女，他们的希望都在我这里 。越是这样想的越多，想的越多越痛苦，我快要发疯啦，'''
b = re.split(u"，|。|；|！|？", content)
for one in b:
    if one :
        print one