import pygame,os,sys,easygui,pickle,re,datetime,random,hashlib

'''载入'''
#初始化
pygame.init()
screen_size = screen_width,screen_height = [1200,600]
screen = pygame.display.set_mode(screen_size)
screen.fill([255,255,255])
pygame.display.set_caption("(❁´◡`❁)  Be Your Best Self: 自律打卡器  (❁´◡`❁)")

#字体
# font1 = pygame.font.Font(r"fonts\1.TTF",200)
# font2 = pygame.font.Font(r"fonts\2.ttf",100)
# font3 = pygame.font.Font(r"fonts\3.ttf",70)
# font4 = pygame.font.Font(r"fonts\4.TTF",100)
# font5 = pygame.font.Font(r"fonts\5.ttf",100)
# font6 = pygame.font.Font(r"fonts\6.ttf",100)
font7 = pygame.font.Font(r"fonts\12.ttF",27)
# font8 = pygame.font.Font(r"fonts\1.TTF",35)
font9 = pygame.font.Font(r"fonts\12.ttf",190)
font10 = pygame.font.Font(r"fonts\12.ttf",70)
font11 = pygame.font.Font(r"fonts\12.ttf",40)
font12 = pygame.font.Font(r"fonts\12.ttf",25)
font13 = pygame.font.Font(r"fonts\11.ttf",30)
# font14 = pygame.font.Font(r"fonts\11.ttf",35)
font15 = pygame.font.Font(r"fonts\12.ttf",60)

'''文字'''
# display_state = 1
# title1 = font1.render("Daily List",True,[0,0,0])
title0 = font15.render("Be Your Best Self",True,[0,0,0])
title0_pos = [360,260]
title1 = font9.render("自律打卡器",True,[0,0,0])
title1_pos = [125,50]
title2 = font7.render("Programmed by 方乐(sanjuu)",True,[0,0,0])
title2_pos = [835,530]
title3 = font7.render("From 2024-12-06 To 2025-03-24",True,[0,0,0])
title3_pos = [805,565]
logup_str = font10.render("注册",True,[0,0,0])
logup_str_pos = [290,363]
login_str = font10.render("登录",True,[0,0,0])
login_str_pos = [762,363]
default_st_str = "养成好习惯，从每天打卡开始！"
# st_str_pos = [15,190]
# display_state = 2

'''图像'''
# display_state = 1
background_image = pygame.image.load(r"images\background.png")
diamond_frame_image = pygame.image.load(r"images\框2.png")
dframe1_pos = [185,350]
dframe2_pos = [655,350]
# display_state = 2
profile_bg_img = pygame.image.load(r"images\profileframe.png")
profile_bg_img_pos = [10,10]
default_profile_path = r"images\defaultprofile.png"
profile_img = pygame.image.load(default_profile_path)
profile_pos = [28,35]
# coins_img = pygame.image.load(r"images\coins2.png")
# coins_img_pos = [120,73]
# coins_str_pos = [164,73]
name_str_pos = [120,45]
# test_img = pygame.image.load(r"images\test.png")
# test_img_pos = [1100,100]
setting_img = pygame.image.load(r"images\settings.png")
setting_img_pos = [10,480]
home_img = pygame.image.load(r"images\home.png")
home_img_pos = [10,150]
music_img = pygame.image.load(r"images\musicsetting.png")
music_img_pos = [10,260]
record_img = pygame.image.load(r"images\record.png")
record_img_pos = [10,370]
st_frame_img = pygame.image.load(r"images\stframe.png")
st_frame_img_pos = [10,155]
list_img = pygame.image.load(r"images\notebook2.png")
list_img_pos = [325,20]
add_img = pygame.image.load(r"images\add.png")
add_imgs = [add_img for i in range(9)]
add_img_poses = [[1080,128],[1080,170],[1080,210],[1080,250],[1080,290],[1080,331],[1080,373],[1080,415],[1080,457]]
minus_img = pygame.image.load(r"images\minus.png")
minus_imgs = [minus_img for i in range(9)]
minus_img_poses = [[1115,128],[1115,170],[1115,210],[1115,250],[1115,290],[1115,331],[1115,373],[1115,415],[1115,457]]
todo_poses = [[470,128],[470,170],[470,210],[470,250],[470,290],[470,331],[470,373],[470,415],[470,457]]
num1_img = pygame.image.load(r"images\nums\1.png")
num2_img = pygame.image.load(r"images\nums\2.png")
num3_img = pygame.image.load(r"images\nums\3.png")
num4_img = pygame.image.load(r"images\nums\4.png")
num5_img = pygame.image.load(r"images\nums\5.png")
num6_img = pygame.image.load(r"images\nums\6.png")
num7_img = pygame.image.load(r"images\nums\7.png")
num8_img = pygame.image.load(r"images\nums\8.png")
num9_img = pygame.image.load(r"images\nums\9.png")
nums_imgs = [num1_img,num2_img,num3_img,num4_img,num5_img,num6_img,num7_img,num8_img,num9_img]
nums_poses = [[425,128],[425,170],[425,210],[425,250],[425,290],[425,331],[425,373],[425,415],[425,457]]
finished_img = pygame.image.load(r"images\finished_stamp.png")
unfinished_img = pygame.image.load(r"images\unfinished_stamp.png")
states_img_poses = [[1012,125],[1012,166],[1012,207],[1012,248],[1012,288],[1012,329],[1012,371],[1012,411],[1012,452]]

'''音乐'''
default_music_path = r"music\灰澈-星茶会.flac"
background_music = pygame.mixer.music.load(default_music_path)
pygame.mixer.music.play(-1)
mouse_click_music = pygame.mixer.Sound(r"music\click2.mp3")
finish_music = pygame.mixer.Sound(r"music\finish.mp3")
allfinish_music = pygame.mixer.Sound(r"music\allfinish.wav")
delete_music = pygame.mixer.Sound(r"music\delete.wav")

'''零零碎碎的设定'''
display_state = 1   # 1: 开始页面,2: 主页面,3: 商店页面(商店弃用了qwq)
click_able = True   # 有效点击 作用同下
click_cnt = 0   # 用于防止鼠标过于灵敏多次点击
# display_state = 1
setting_open = False   # 是否打开了设置(是否显示设置内容)
special_set_namestr = 0   # 用户名如果超长第一次渲染会赋值为子串的尾下标并进行缩减方便后面直接打印
need_update = False   # 是否需要update(如果不用这个,那么在登录瞬间直接调用会使得display_state = 2的画面还没加载出来就easygui报告打卡进度,不太友好)
muted = False   # 音效是否关闭(静音)

'''类'''
# 鼠标类
class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img_surf = pygame.surface.Surface([1,1])
        self.image = img_surf.convert()
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
mouse = Mouse()

# 图片精灵类
class Img_sprite(pygame.sprite.Sprite):
    def __init__(self,img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = self.pos
    # 鼠标点击到
    def iscollide(self):
        if pygame.sprite.collide_mask(self,mouse):
            return True
        else:
            return False
logupsprite = Img_sprite(diamond_frame_image,dframe1_pos)
loginsprite = Img_sprite(diamond_frame_image,dframe2_pos)
settingsprite = Img_sprite(setting_img,setting_img_pos)
homesprite = Img_sprite(home_img,home_img_pos)
musicsettingsprite = Img_sprite(music_img,music_img_pos)
recordsprite = Img_sprite(record_img,record_img_pos)
st_fram_sprite = Img_sprite(st_frame_img,st_frame_img_pos)
add_sprites = [Img_sprite(add_img,i) for i in add_img_poses]
minus_sprites = [Img_sprite(minus_img,i) for i in minus_img_poses]
states_sprites = [Img_sprite(unfinished_img,i) for i in states_img_poses]
profile_sprite = Img_sprite(profile_img,profile_pos)

# 打卡任务项类
class Item:
    def __init__(self,content="None",days=0,last_finish_day=None,buqiancnt=1,state=False):
        self.content,self.days,self.last_finish_day,self.buqiancnt,self.state = content,days,last_finish_day,buqiancnt,state
    def add_content(self):   # 添加内容
        if self.content == "None":
            s = easygui.enterbox(msg="请输入打卡任务内容：(10字以内)",title="任务内容",strip=True)
        else:
            s = easygui.enterbox(msg="(请注意更改内容后打卡进度会清零)\n请输入打卡任务内容：(10字以内)",title="任务内容",strip=True,default=self.content)
        if s != None:
            if len(s) <= 10:
                self.content,self.days,self.last_finish_day,self.buqiancnt,self.state = s,0,None,1,False
            else:
                easygui.msgbox(msg="超过字数限制，请重新输入。",ok_button="我知道了")
    def del_content(self):   # 删除内容 项置空
        if self.content != "None":
            s = easygui.buttonbox(msg="请确认是否删除该项清单内容？请注意该项的打卡进度会清零。",title="删除清单内容",choices=["是","否"])
            if s != None and s == "是":
                delete_music.play()
                self.content,self.days,self.last_finish_day,self.buqiancnt,self.state = "None",0,None,1,False
                now_user.ifallfinish()
        else:
            easygui.msgbox(msg="内容为空无法删除。",ok_button="我知道了")
    def finish(self):   # 打卡
        global now_user
        if self.content != "None":
            if not self.state:
                finish_music.play()
                st = "养成好习惯，从每天打卡开始！"
                try:
                    with open(r"st\sts.txt","r",encoding="utf-8") as f:
                        sts = f.readlines()
                        st = sts[random.randint(0,len(sts)-1)]
                except:
                    pass
                self.days,self.last_finish_day,self.state = self.days+1,datetime.date.today(),True
                easygui.msgbox(msg=f"打卡第{self.days}天！\n\n\n{st}",ok_button="加油！(●'◡'●)")
                now_user.ifallfinish()
                if self.days == 21:
                    now_user.achievements.append(self.content)
                    allfinish_music.play()
                    easygui.buttonbox(msg=f"恭喜完成21天养成好习惯的打卡任务！ψ(｀∇´)ψ\n你太棒啦！(❁´◡`❁)\n请再接再厉喔！！！(●'◡'●)",choices=["好的(❁´◡`❁)"])
        else:
            easygui.msgbox(msg="内容为空无法确认完成打卡。",ok_button="我知道了")


# 账号类
class Account:
    def __init__(self,username="",password="",imgpath="",st=default_st_str,todo=[Item() for i in range(9)],musicpath=r"music\灰澈-星茶会.flac",last_login_day=datetime.date.today(),achievements=[]):
        self.username = username
        self.password = password
        self.imgpath = imgpath
        if imgpath != "":
            self.image = pygame.image.load(imgpath)
        else:
            self.imgpath = r"images\defaultprofile.png"
            self.image = pygame.image.load(self.imgpath)
        self.st = st   # 给自己的寄语
        self.todo = todo   # 清单事项
        self.musicpath = musicpath
        self.last_login_day = last_login_day
        self.achievements = achievements
    def datastore(self):
        with open("accounts\\"+self.username+".pkl","wb") as f:
            # print("store musci path: ",self.musicpath)
            self.last_login_day = datetime.date.today()
            pickle.dump([self.username,self.password,self.imgpath,self.st,self.todo,self.musicpath,self.last_login_day,self.achievements],f)
    def getdata(self,path):
        try:
            with open(path,"rb") as f:
                data = pickle.load(f)
                self.username,self.password,self.imgpath,self.st,self.todo,self.musicpath,self.last_login_day,self.achievements = data
                # print("musicpath: ",self.musicpath)
                try:
                    self.image = pygame.image.load(self.imgpath)
                except:
                    easygui.msgbox(msg="头像获取失败！请确认头像图片路径是否变更，并尝试再次上传。",ok_button="我知道了")
                    self.imgpath = default_profile_path
                    self.image = pygame.image.load(self.imgpath)
                if self.musicpath != r"music\灰澈-星茶会.flac":
                    try:
                        # print("try: ",self.musicpath)
                        pygame.mixer.music.load(self.musicpath)
                        pygame.mixer.music.play(-1)
                    except:
                        easygui.msgbox("加载自定义背景音乐错误！\n请确认上次上传的背景音乐路径是否发生变化，以及尝试再次上传。",ok_button="我知道了")
                        self.musicpath = r"music\灰澈-星茶会.flac"
        except:
            pass
    def a_new_day(self):   # 在线且过零点时调用
        finishcnt = 0
        string = ""
        now = datetime.date.today()
        delta = datetime.timedelta(days=1)
        for i in self.todo:
            if i.content != "None":
                i.state = False
                if i.last_finish_day != None:
                    if i.last_finish_day+delta == now:
                        i.state = False
                        finishcnt += 1
                    elif i.last_finish_day+delta+delta == now:
                        if i.buqiancnt:
                            i.buqiancnt -= 1
                            i.last_finish_day = now-delta
                            string += '"'+i.content+'"'+"漏签一天，已自动补签，剩余补签次数：0。\n"
                        else:
                            i.days,i.last_finish_day,i.buqiancnt = 0,None,1
                            string += '"'+i.content+'"'+"漏签一天，补签次数不足，打卡进度已清零。\n请再接再厉！"
                    else:
                        i.days,i.last_finish_day,i.buqiancnt = 0,None,1
                        string += '"'+i.content+'"'+"漏签多天，补签次数不足，打卡进度已清零。\n请再接再厉！"
        easygui.msgbox(msg=f"昨日成功打卡{finishcnt}个任务(ง •_•)ง今天继续加油！\n{string}",title="昨日总结",ok_button="好的(ง •_•)ง")
    def is_update(self):   # 登录时调用
        last = self.last_login_day
        now = datetime.date.today()
        delta = datetime.timedelta(days=1)
        if last != now:
            if last+delta == now:   # 昨天有登录
                self.a_new_day()
            elif last+delta+delta == now:   # 上一次登录在前天
                string = ""
                for i in self.todo:
                    if i.content != "None":
                        i.state = False
                        if i.last_finish_day != None:
                            if i.last_finish_day+delta+delta == now:
                                if i.buqiancnt:
                                    i.buqiancnt -= 1
                                    i.last_finish_day = now-delta
                                    string += '"'+i.content+'"'+"漏签一天，已自动补签，剩余补签次数：0。\n"
                                else:
                                    i.days,i.last_finish_day,i.buqiancnt = 0,None,1
                                    string += '"'+i.content+'"'+"漏签一天，补签次数不足，打卡进度已清零。\n"
                            else:
                                string += '"'+i.content+'"'+"超过两天未打卡，打卡进度已清零。\n"
                easygui.msgbox(msg=f"昨天未登录,各任务若有剩余补签次数已自动补签。\n{string}")
            else:   # 有再多补签也不顶用了
                for i in self.todo:
                    i.days,i.last_finish_day,i.buqiancnt,i.state = 0,None,1,False
                easygui.msgbox(msg="超过两天未上线打卡,所有打卡任务进度已清零(っ °Д °;)っ\n请再接再厉！(ง •_•)ง",title="进度清零",ok_button="我知道了")
    def ifallfinish(self):
        yes = True
        enter = False
        for i in range(9):
            if self.todo[i].content != "None":
                enter = True
                if not self.todo[i].state:
                    yes = False
        if yes and enter:
            allfinish_music.play()
            easygui.buttonbox("今日打卡任务已全部完成！ψ(｀∇´)ψ\n\n\n明天也要继续加油喔！(❁´◡`❁)\n\n\n",image=r"images\thumb_up2.png",choices=["好！(●ˇ∀ˇ●)"])

now_user = Account()


'''函数'''
# 检测鼠标按下
def isclick():
    if pygame.mouse.get_pressed()[0]:
        return True
    else:
        return False

# 检测账号用户名是否只包含英文字母、汉字和数字
def name_is_valid(s):
    for i in s:
        if i.isalpha() or i.isdigit():
            continue
        else:
            return False
    return True

# 账号注册
def logup():
    global display_state,now_user
    info = easygui.multenterbox(msg="注册新账号：\n用户名仅可包含英文字母、汉字和数字，不可使用其它特殊字符；\n且长度应不大于10个字符。",title="注册",fields=["用户名：","密码："])
    if info != None:
        if info[0] != "" and info[1] != "":
            if name_is_valid(info[0]) and len(info[0]) <= 10:
                if os.path.exists("accounts\\"+info[0]+".pkl"):
                    easygui.msgbox("注册失败，用户已存在！",ok_button="我知道了")
                else:
                    psw = info[1].encode("utf-8")
                    sha256 = hashlib.new("sha256")
                    sha256.update(psw)
                    now_user = Account(info[0],str(sha256.hexdigest()))
                    now_user.last_login_day = datetime.datetime.now()
                    easygui.msgbox(msg="注册成功！已登录。",ok_button="好的")
                    if display_state == 1:
                        display_state = 2
            else:
                easygui.msgbox("注册失败，用户名超出限制长度或者包含不合法字符。",ok_button="我知道了")
        else:
            easygui.msgbox("注册失败，请填写完整。",ok_button="我知道了")

# 账号登录
def login():
    global display_state,now_user
    info = easygui.multpasswordbox(msg="请输入用户名和密码：",title="登录",fields=["用户名：","密码："])
    if info != None:
        if info[0] != "" and info[1] != "":
            filename = "accounts\\"+info[0]+".pkl"
            if os.path.exists(filename):
                now_user.getdata(filename)
                sha256 = hashlib.new("sha256")
                psw = info[1].encode("utf-8")
                sha256.update(psw)
                if str(sha256.hexdigest()) == now_user.password:
                    easygui.msgbox("登录成功！",ok_button="好的")
                    now_user.is_update()
                    if display_state == 1:
                        display_state = 2
                else:
                    now_user = Account()
                    easygui.msgbox("登录失败，密码不正确！",ok_button="我知道了")
            else:
                easygui.msgbox("登录失败，该用户不存在！",ok_button="我知道了")
        else:
            easygui.msgbox("登录失败，请填写完整。",ok_button="我知道了")

# 打印寄语
def print_st():
    global now_user
    zhPattern = re.compile(u'[a-zA-Z]+')
    x0,y0 = [30,292]
    for i in now_user.st:
        st_str = font12.render(i,True,[0,0,0])
        screen.blit(st_str,[x0,y0])
        match = zhPattern.search(i)
        if match:
            x0 += 17
        else:
            if i.isdigit():
                x0 += 15
            else:
                x0 += 25
        if (x0 >= 275):
            y0 += 27
            x0 = 25

# 渲染
def show():
    global display_state,now_user,setting_open,special_set_namestr
    screen.fill([255,255,255])
    if display_state == 1:
        images1 = [background_image,title0,title1,title2,title3,diamond_frame_image,diamond_frame_image,logup_str,login_str]
        pos1 = [[0,0],title0_pos,title1_pos,title2_pos,title3_pos,dframe1_pos,dframe2_pos,logup_str_pos,login_str_pos]
        for i in range(len(images1)):
            screen.blit(images1[i],pos1[i])
    elif display_state == 2:
        # 背景
        screen.blit(background_image,[0,0])
        # pygame.draw.rect(screen,[255,255,255],pygame.Rect([10,10,295,110]),0,15)
        # 用户名
        if not special_set_namestr:
            name_str = font11.render(now_user.username,True,[0,0,0])
            # print(name_str.get_width())
            special_set_namestr = len(now_user.username)
            while name_str.get_width() > 160:
                special_set_namestr -= 1
                name_str = font11.render(now_user.username[0:special_set_namestr],True,[0,0,0])
        else:
            name_str = font11.render(now_user.username[0:special_set_namestr],True,[0,0,0])
        # print(special_set_namestr)
        # 批量渲染
        images2 = [list_img,setting_img,profile_bg_img,now_user.image,name_str,st_frame_img,add_imgs,minus_imgs,nums_imgs]
        pos2 = [list_img_pos,setting_img_pos,profile_bg_img_pos,profile_pos,name_str_pos,st_frame_img_pos,add_img_poses,minus_img_poses,nums_poses]
        for i in range(len(images2)):
            if (type(images2[i]) == list):
                for j in range(len(images2[i])):
                    screen.blit(images2[i][j],pos2[i][j])
            else:
                screen.blit(images2[i],pos2[i])
        # 寄语
        print_st()
        # 设置中内容
        if setting_open:
            simages = [home_img,music_img,record_img]
            spos = [home_img_pos,music_img_pos,record_img_pos]
            for i in range(len(simages)):
                screen.blit(simages[i],spos[i])
        # 清单内容和各项状态
        for i in range(9):
            screen.blit(font13.render(f"{now_user.todo[i].content}(已成功打卡{str(now_user.todo[i].days)}天)",True,[0,0,0]),todo_poses[i])
            if now_user.todo[i].state:
                screen.blit(finished_img,states_img_poses[i])
            else:
                screen.blit(unfinished_img,states_img_poses[i])

    pygame.display.flip()

# 检测事件并作出回应
def check_events():
    global display_state,setting_open,click_able,need_update,muted,special_set_namestr
    if isclick() and click_able:
        if display_state == 1:
            if logupsprite.iscollide():
                logup()
            elif loginsprite.iscollide():
                login()
        elif display_state == 2:
            if need_update:
                now_user.a_new_day()
                need_update = False
            if setting_open:
                if homesprite.iscollide():
                    get = easygui.buttonbox(msg="请确认是否退出账号登录：",title="回到主页",choices=["是","否"])
                    if get != None:
                        if get == "是":
                            now_user.datastore()
                            setting_open = False
                            muted = False
                            display_state = 1
                            special_set_namestr = 0
                            pygame.mixer.music.load(default_music_path)
                            pygame.mixer.music.play(-1)
                elif musicsettingsprite.iscollide():
                    get = easygui.choicebox(msg="请选择要进行的操作：",title="音效设置",choices=["打开/关闭音效","打开/关闭背景音乐","上传并更改背景音乐","恢复默认背景音乐"])
                    if get != None:
                        if get == "打开/关闭音效":
                            if not muted:
                                muted = True
                                mouse_click_music.set_volume(0)
                                delete_music.set_volume(0)
                                finish_music.set_volume(0)
                                allfinish_music.set_volume(0)
                            else:
                                muted = False
                                mouse_click_music.set_volume(100)
                                delete_music.set_volume(100)
                                finish_music.set_volume(100)
                                allfinish_music.set_volume(100)
                        elif get == "打开/关闭背景音乐":
                            if pygame.mixer.music.get_volume() != 0:
                                pygame.mixer.music.set_volume(0)
                            else:
                                # pygame.mixer.music.load(now_user.musicpath)
                                pygame.mixer.music.play(-1)
                                pygame.mixer.music.set_volume(100)
                        elif get == "上传并更改背景音乐":
                            fn = easygui.fileopenbox(msg="请选择要上传的背景音乐：",title="上传背景音乐",filetypes=["*.mp3","*.flac",".wav"])
                            # print("f: ",fn)   # 确认过了,是完整路径:D 设置里面的代码写了好长一段直接运行居然没报错嘿嘿~~
                            if fn != None:
                                try:
                                    # 还没试过先"关闭"背景音乐再上传会不会有影响
                                    pygame.mixer.music.load(fn)
                                    pygame.mixer.music.play(-1)
                                    now_user.musicpath = fn
                                    easygui.msgbox("背景音乐更改成功！",ok_button="好的")
                                except:
                                    easygui.msgbox("啊哦，好像出了点小差错，请检查上传文件类型是否是mp3、flac或wav。",ok_button="我知道了")
                        else:
                            if (now_user.musicpath != default_music_path):
                                pygame.mixer.music.set_volume(100)
                                pygame.mixer.music.load(default_music_path)
                                pygame.mixer.music.play(-1)
                                now_user.musicpath = default_music_path
                elif recordsprite.iscollide():
                    achi = ""
                    if now_user.achievements != []:
                        achi = "\n\n".join([f"{i+1}、{now_user.achievements[i]}" for i in range(len(now_user.achievements))])
                        easygui.buttonbox(msg=f"以下是你所有成功坚持了21天打卡养成习惯的内容: \n{achi}",title="纪念馆",image=r"images\bang.png",choices=["已阅！ψ(｀∇´)ψ"])
                    else:
                        easygui.buttonbox(msg="还没有过21天坚持打卡养成习惯的内容呢，请再接再厉！\n养成好习惯，从每天打卡开始！",title="纪念馆",image=r"images\xvyaonuli.png",choices=["好的我会努力的(ง •_•)ง"])
            if settingsprite.iscollide():
                if not setting_open:
                    setting_open = True
                    click_able = False
                else:
                    if click_able:
                        setting_open = False
                        click_able = False
            # if click_able and setting_open and isclick():
            #     setting_open = False
            elif not setting_open and display_state == 2 and st_fram_sprite.iscollide():
                tmpstr = easygui.enterbox(msg="请输入要写给自己的寄语（不超过四十个字）：",title="写给自己的寄语",default=now_user.st)
                if tmpstr != None and tmpstr != "":
                    now_user.st = tmpstr[0:min(len(tmpstr),41)]
            elif profile_sprite.iscollide():
                a = easygui.integerbox(msg="请选择新头像的序号,输入0则为默认头像。",image=r"images\profiles\tot.png",title="选择新头像序号",default=0,lowerbound=0,upperbound=9)
                if a != None:
                    if a:
                        now_user.imgpath = f"images\\profiles\\{a}.png"
                        now_user.image = pygame.image.load(now_user.imgpath)
                    else:
                        now_user.imgpath = default_profile_path
                        now_user.image = pygame.image.load(now_user.imgpath)
            else:
                for i in range(9):
                    if (add_sprites[i].iscollide()):
                        now_user.todo[i].add_content()
                    if (minus_sprites[i].iscollide()):
                        now_user.todo[i].del_content()
                    if (states_sprites[i].iscollide()):
                        now_user.todo[i].finish()
                

# 检测鼠标所在屏幕坐标
def check():
    if isclick():
        print(pygame.mouse.get_pos())


'''主循环'''
running = True
clock = pygame.time.Clock()
zero = "00:00:00"
zerocnt = 0
while running:
    t = str(datetime.datetime.now().time().replace(microsecond=0))
    if not zerocnt:
        # print(t)
        if t == zero:
            if now_user.username != "":
                need_update = True
                zerocnt = 1000
    else:
        zerocnt -= 1
    if not click_able:
        click_cnt += 1
        if click_cnt > 13:
            click_cnt = 0
            click_able = True
    clock.tick(60)
    mouse.update()

    # 渲染
    show()
    # 检测事件
    check_events()
    # 确认屏幕位置
    # check()

    # pygame事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if now_user.username != "":
                now_user.datastore()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_music.play()

sys.exit()